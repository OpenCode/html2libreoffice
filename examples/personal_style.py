from html2libreoffice import Document, Head, Header, Footer, Body, Style, \
                             page_number, page_count, new_page

doc = Document()
head = Head(title='Example', author='John Doe')
doc.head = head
header = Header('<p style="margin-bottom: 0.5cm; line-height: 100%">'
                'Header. Page {p_num} of {p_count}'
                '</p>'.format(p_num=page_number(), p_count=page_count(), ))
doc.header = header
footer = Footer('Simple Footer')
doc.footer = footer
body = Body('<p>Page 1</p>'
            '{new_page}'
            '<p>Page 2</p>'
            '{new_page}'
            '<p>Page 3</p>'
            '{new_page}'
            '<p>Page 4</p>'.format(new_page=new_page())
            )
doc.body = body
style = Style('''
@page { margin: 4cm }
p { margin-bottom: 0.30cm; color: #000; line-height: 120% }
''')
doc.style = style
doc.save('./tmp/example.html')
