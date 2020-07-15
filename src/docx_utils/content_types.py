# coding: utf-8
"""
Content-Type table
==================

Store the Default and Override content types.
"""
import collections
import mimetypes
import os

from lxml import etree


class ContentTypes(object):
    """
    ContentTypes contained in a "[Content_Types].xml" file.
    """

    NS = {"ct": u"http://schemas.openxmlformats.org/package/2006/content-types"}

    def __init__(self):
        self._defaults = collections.OrderedDict()
        self._overrides = collections.OrderedDict()

    def parse_xml_data(self, data):
        tree = etree.fromstring(data)  # type: etree._Element
        self._defaults = {
            n.attrib[u"Extension"]: n.attrib[u"ContentType"]
            for n in tree.xpath(u"//ct:Default", namespaces=self.NS)
        }
        self._overrides = {
            n.attrib[u"PartName"]: n.attrib[u"ContentType"]
            for n in tree.xpath(u"//ct:Override", namespaces=self.NS)
        }

    def resolve(self, part_name):
        basename = os.path.basename(part_name)
        ext = basename.rsplit(".", 1)[1]
        content_type = self._overrides.get(part_name) or self._defaults.get(ext)
        return content_type or mimetypes.guess_type(part_name, strict=True)[0]

    def register_part(self, part_name, content_type):
        part_name = part_name if part_name.startswith("/") else "/" + part_name
        if content_type == "application/vnd.openxmlformats-package.relationships+xml":
            self._defaults["rels"] = content_type
        elif content_type.startswith("application/vnd.openxmlformats-package"):
            self._overrides[part_name] = content_type
        else:
            ext = os.path.splitext(part_name)[1]
            self._defaults[ext] = content_type

    def create_xml_data(self):
        tree = etree.XML('<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>')
        for ext, content_type in self._defaults.items():
            etree.SubElement(tree, "Default", attrib={"Extension": ext, "ContentType": content_type})
        for part_name, content_type in self._overrides.items():
            etree.SubElement(tree, "Override", attrib={"PartName": part_name, "ContentType": content_type})
        return tree
