from getpass import getuser
from html2libreoffice import BODY_TEMPLATE, FOOTER_TEMPLATE, HEAD_TEMPLATE,\
                             HEADER_TEMPLATE,\
                             DEFAULT_STYLE


class Section:

    def __init__(self, content=''):
        self._content = content

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content=''):
        self._content = content


class Head:

    def __init__(self, title='', author=''):
        self._title = title
        if not author:
            author = getuser()
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def complete_content(self):
        complete_content = HEAD_TEMPLATE
        complete_content = complete_content.replace(
            '{{title}}', self.title)
        complete_content = complete_content.replace(
            '{{author}}', self.author)
        complete_content = complete_content.replace(
            '{{created}}', '00:00:00')
        return complete_content


class Style(Section):

    def __init__(self, content=''):
        Section.__init__(self, content)
        if not content:
            content = DEFAULT_STYLE
        self._content = content


class Header(Section):

    @property
    def complete_content(self):
        if not self.content:
            return ''
        complete_content = HEADER_TEMPLATE
        complete_content = complete_content.replace(
            '{{content}}', self.content)
        return complete_content


class Body(Section):

    @property
    def complete_content(self):
        if not self.content:
            return ''
        complete_content = BODY_TEMPLATE
        complete_content = complete_content.replace(
            '{{content}}', self.content)
        return complete_content


class Footer(Section):

    @property
    def complete_content(self):
        if not self.content:
            return ''
        complete_content = FOOTER_TEMPLATE
        complete_content = complete_content.replace(
            '{{content}}', self.content)
        return complete_content
