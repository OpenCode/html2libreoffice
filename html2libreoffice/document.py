from os import sep
from getpass import getuser
from html2libreoffice import BASE_TEMPLATE, BODY_TEMPLATE, FOOTER_TEMPLATE,\
                             HEAD_TEMPLATE, HEADER_TEMPLATE, DEFAULT_STYLE


class Document:

    def __init__(self):
        # ----- Instance sections
        self._style = ''
        self._head = ''
        self._header = ''
        self._body = ''
        self._footer = ''
        self._complete_document = ''

    def set_style(self, style):
        self._style = style

    def set_head(self, title='', author='', created='', changedby='',
                 changed=''):
        head = HEAD_TEMPLATE
        head = head.replace('{{title}}', title)
        if not author:
            author = getuser()
        head = head.replace('{{author}}', author)
        head = head.replace('{{created}}', created)
        if not changedby:
            changedby = getuser()
        head = head.replace('{{changedby}}', changedby)
        head = head.replace('{{changed}}', changed)
        self._head = head
        return head

    def set_header(self, content=''):
        header = HEADER_TEMPLATE.replace(
            '{{content}}', content)
        self._header = header
        return header

    def set_body(self, content=''):
        body = BODY_TEMPLATE.replace(
            '{{content}}', content)
        self._body = body
        return body

    def set_footer(self, content=''):
        footer = FOOTER_TEMPLATE.replace(
            '{{content}}', content)
        self._footer = footer
        return footer

    def generate(self):
        # ----- Fill css style in the head
        head = self._head
        head = head.replace('{{style}}', self._style or DEFAULT_STYLE)
        # ----- Fill header and footer in the body
        body = self._body
        body = body.replace('{{header}}', self._header)
        body = body.replace('{{footer}}', self._footer)
        # ----- Create the complete document content
        complete_document = BASE_TEMPLATE
        complete_document = complete_document.replace(
            '{{head}}', head)
        complete_document = complete_document.replace(
            '{{body}}', body)
        self._complete_document = complete_document
        return complete_document

    def save(self, filepath=''):
        document_file = open(filepath, 'w')
        document_file.write(self._complete_document)
        document_file.close()
        return True
