# coding: utf-8
u"""
Docx to flat XML converter
==========================

This converter is inspired from Eric White’s article: `Transforming Open XML Documents to Flat OPC Format
<https://blogs.msdn.microsoft.com/ericwhite/2008/09/29/transforming-open-xml-documents-to-flat-opc-format/>`_.

    This post describes the process of conversion of an Open XML (OPC) document
    into a Flat OPC document, and presents the C# function, OpcToFlat.

The function :func:`~docx_utils.flatten.opc_to_flat_opc` is used to convert
an Open XML document (.docx, .xlsx, .pptx) into a flat OPC format (.xml).
"""
import base64
import collections
import io
import itertools
import os
import zipfile

import six.moves.urllib.request
from lxml import etree


class ContentTypes(object):
    """
    ContentTypes contained in a "[Content_Types].xml" file.
    """
    NS = {'ct': u"http://schemas.openxmlformats.org/package/2006/content-types"}

    def __init__(self):
        self._defaults = {}
        self._overrides = {}

    def parse_xml_data(self, data):
        tree = etree.fromstring(data)  # type: etree._Element
        self._defaults = {n.attrib[u'Extension']: n.attrib[u'ContentType']
                          for n in tree.xpath(u'//ct:Default', namespaces=self.NS)}
        self._overrides = {n.attrib[u'PartName']: n.attrib[u'ContentType']
                           for n in tree.xpath(u'//ct:Override', namespaces=self.NS)}

    def resolve(self, part_name):
        basename = os.path.basename(part_name)
        ext = basename.rsplit(".", 1)[1]
        content_type = self._overrides.get(part_name) or self._defaults.get(ext)
        return content_type


PackagePart = collections.namedtuple('PackagePart', ['uri', 'content_type', 'data'])


def iter_package(opc_path):
    """
    Iterate a Open XML document and yield the package parts.

    :param str opc_path: Microsoft Office document to read (.docx, .xlsx, .pptx)
    :return: Iterator which yield package parts
    """
    content_types = ContentTypes()
    with zipfile.ZipFile(opc_path, mode="r") as f:
        for name in f.namelist():
            if name == "[Content_Types].xml":
                content_types.parse_xml_data(f.read(name))
            else:
                uri = six.text_type("/" + six.moves.urllib.request.pathname2url(name))
                content_type = content_types.resolve(uri)
                data = f.read(name)
                yield PackagePart(uri, content_type, data)


def opc_to_flat_opc(src_path, dst_path):
    """
    Convert an Open XML document into a flat OPC format.

    :param str src_path: Microsoft Office document to convert (.docx, .xlsx, .pptx)
    :param str dst_path: Microsoft Office document converted into flat OPC format (.xml)
    """
    pkg = u"http://schemas.microsoft.com/office/2006/xmlPackage"

    ext = os.path.splitext(src_path)[1].lower()
    progid = {'.docx': u"Word.Document",
              '.xlsx': u"Excel.Sheet",
              '.pptx': u"PowerPoint.Show"}[ext]

    content = (u'<?mso-application progid="{progid}"?>'
               u'<pkg:package xmlns:pkg="{pkg}"/>').format(progid=progid, pkg=pkg)

    document = etree.parse(io.StringIO(content))  # type: etree._ElementTree
    root = document.getroot()

    ns = {'pkg': pkg}

    for part in iter_package(src_path):
        node = etree.SubElement(root, u"{{{pkg}}}part".format(pkg=pkg), nsmap=ns)
        node.attrib[u"{{{pkg}}}name".format(pkg=pkg)] = part.uri
        node.attrib[u"{{{pkg}}}contentType".format(pkg=pkg)] = part.content_type
        if part.content_type.endswith("xml"):
            data = etree.SubElement(node, u"{{{pkg}}}xmlData".format(pkg=pkg), nsmap=ns)
            data.append(etree.fromstring(part.data))
        else:
            node.attrib[u"{{{pkg}}}compression".format(pkg=pkg)] = "store"
            data = etree.SubElement(node, u"{{{pkg}}}binaryData".format(pkg=pkg), nsmap=ns)
            encoded = base64.b64encode(part.data).decode()  # bytes -> str
            iterable = iter(encoded)
            chunks = list(iter(lambda: list(itertools.islice(iterable, 76)), []))
            chunks = u"\n".join(u"".join(chunk) for chunk in chunks)
            data.text = chunks

    content = etree.tostring(document,
                             xml_declaration=True,
                             encoding='UTF-8',
                             pretty_print=False,
                             with_tail=False,
                             standalone=True)
    with io.open(dst_path, mode="wb") as f:
        f.write(content)
