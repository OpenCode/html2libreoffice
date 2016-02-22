from getpass import getuser
from html2libreoffice import BASE_TEMPLATE, HEAD_TEMPLATE, DEFAULT_STYLE


class Document:

    def __init__(self):
        # ----- Instance sections
        self._style = False
        self._head = False
        self._header = False
        self._body = False
        self._footer = False
        self._complete_document = ''

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style=False):
        self._style = style

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head=False):
        self._head = head
        return head

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header=False):
        self._header = header
        return header

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body=False):
        self._body = body
        return body

    @property
    def footer(self):
        return self._footer

    @footer.setter
    def footer(self, footer=False):
        self._footer = footer
        return footer

    def generate(self):
        # ----- Fill css style in the head
        head = ''
        if self.head:
            if self.style:
                style = self.style.content
            else:
                style = DEFAULT_STYLE
            head = self.head.complete_content.replace('{{style}}', style)
        # ----- Fill header and footer in the body
        body = ''
        if self.body:
            body = self.body.complete_content
            if self.header:
                header = self.header.complete_content
            else:
                header = ''
            body = body.replace('{{header}}', header)
            if self.footer:
                footer = self.footer.complete_content
            else:
                footer = ''
            body = body.replace('{{footer}}', footer)
        # ----- Create the complete document content
        complete_document = BASE_TEMPLATE
        complete_document = complete_document.replace(
            '{{head}}', head)
        complete_document = complete_document.replace(
            '{{body}}', body)
        self._complete_document = complete_document
        return complete_document

    def save(self, filepath=''):
        # ----- Generate complete file content
        self.generate()
        # ----- Savefile content on disk
        document_file = open(filepath, 'w')
        document_file.write(self._complete_document)
        document_file.close()
        return True
