# coding: utf-8
"""
Exceptions
==========

Exception hierarchy for the docx-utils package.
"""


class DocxUtilsException(Exception):
    """
    Base exception of the docx-utils package.
    """


class UnknownContentTypeError(DocxUtilsException):
    """
    Exception raised during Microsoft Office document parsing
    when a part can't be resolved.
    """
    fmt = (
        "Cannot parse the Microsoft Office document '{opc_path}':"
        " the content-type of the part '{uri}' is unknown"
    )

    def __init__(self, opc_path, uri):
        """
        Initialize the exception.

        :param str opc_path: Microsoft Office document to read (.docx, .xlsx, .pptx)
        :param str uri: URI of the part about to be parsed.
        """
        super(UnknownContentTypeError, self).__init__(opc_path, uri)

    @property
    def opc_path(self):
        return self.args[0]

    @property
    def uri(self):
        return self.args[1]

    def __str__(self):
        return self.fmt.format(opc_path=self.opc_path, uri=self.uri)
