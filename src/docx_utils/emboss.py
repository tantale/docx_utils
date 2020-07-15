# coding: utf-8
u"""
Flat OPC to Open Office XML converter
=====================================

The function :func:`~docx_utils.emboss.flat_opc_to_office` is used to convert
a flat OPC format (.xml) into a Open XML document (.docx, .xlsx, .pptx).
"""
import base64
import io
import os
import zipfile

import six
from lxml import etree

from docx_utils.content_types import ContentTypes

try:
    # noinspection PyPackageRequirements
    from backports import tempfile
except ImportError:
    import tempfile


def flat_opc_to_office(src_path, dst_path):
    """
    Convert a flat OPC format (.xml) into a Open XML document (.docx, .xlsx, .pptx).

    :param src_path: Flat OPC file to convert into Open XML document (.xml)
    :param dst_path: Microsoft Office document (.docx, .xlsx, .pptx)
    """

    pkg = u"http://schemas.microsoft.com/office/2006/xmlPackage"
    ns = {"pkg": pkg}

    # Create a temporary directory used to store all the XML / binary parts
    work_dir, basename = os.path.split(dst_path)
    name = os.path.splitext(basename)[0]
    with tempfile.TemporaryDirectory(dir=work_dir, prefix="~" + name) as temp_dir:

        # prepare a content_type object
        content_types = ContentTypes()

        # Parse each part of the the XML file
        tree = etree.parse(src_path)
        for node in tree.xpath("//pkg:part", namespaces=ns):  # type: etree._Element
            # decode the URI to create a file
            uri = node.attrib[u"{{{pkg}}}name".format(pkg=pkg)]
            parsed = six.moves.urllib.parse.urlparse(uri)
            part_name = six.moves.urllib.parse.unquote(parsed.path)
            part_path = os.path.join(temp_dir, part_name)
            parent_dir = os.path.dirname(part_path)
            if not os.path.exists(parent_dir):
                os.makedirs(parent_dir)

            # check the content-type
            content_type = node.attrib[u"{{{pkg}}}contentType".format(pkg=pkg)]
            if content_type.endswith("xml"):
                data = node.find(u"{{{pkg}}}xmlData/*".format(pkg=pkg), namespaces=ns)
                content = etree.tostring(
                    data,
                    xml_declaration=True,
                    encoding="UTF-8",
                    pretty_print=False,
                    with_tail=False,
                    standalone=True,
                )
                with io.open(part_path, mode="wb") as fd:
                    fd.write(content)

                # todo: guess the right content type (Override content-type)
                #  it is based on the XML content (root element).
                #  We need a translation table for that.
                #  Need to look in the official documentation of Open Office XML (dot net).
                content_types.register_part(part_name, content_type)

            else:
                data = node.find(u"{{{pkg}}}binaryData".format(pkg=pkg), namespaces=ns)
                base64_text = data.text  # type: str
                base64_text = "".join(base64_text.splitlines())
                content = base64.decodebytes(base64_text.encode("ascii"))
                with io.open(part_path, mode="wb") as fd:
                    fd.write(content)
                content_types.register_part(part_name, content_type)

        # Create the target ZIP file
        with zipfile.ZipFile(
            dst_path, mode="w", compression=zipfile.ZIP_DEFLATED, allowZip64=True
        ) as zf:

            # -- first add the "[Content_Types].xml" file
            content = etree.tostring(
                content_types.create_xml_data(),
                xml_declaration=True,
                encoding="UTF-8",
                pretty_print=False,
                with_tail=False,
                standalone=True,
            )
            zf.writestr("[Content_Types].xml", content)

            # -- then add the regular files
            for root_dir, _, file_names in os.walk(temp_dir):
                for name in file_names:
                    full_path = os.path.join(root_dir, name)
                    arch_path = os.path.relpath(full_path, temp_dir).replace("\\", "/")
                    zf.write(full_path, arch_path)
