# -*- coding: utf-8 -*-
# © 2016 Francesco Apruzzese <cescoap@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

BASE_TEMPLATE = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
    {{head}}
    {{body}}
</html>
'''

HEAD_TEMPLATE = '''
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>{{title}}</title>
    <meta name="generator" content="HTML2LibreOffice"/>
    <meta name="author" content="{{author}}"/>
    <meta name="created" content="{{created}}"/>
    <meta name="changedby" content="{{author}}"/>
    <meta name="changed" content="{{created}}"/>
    <style type="text/css">
        {{style}}
    </style>
</head>
'''

BODY_TEMPLATE = '''
<body lang="it-IT" text="#000000" dir="ltr" style="background: transparent">
    {{header}}
    {{content}}
    {{footer}}
</body>
'''

HEADER_TEMPLATE = '''
<div title="header">
    {{content}}
</div>
'''

FOOTER_TEMPLATE = '''
<div title="footer">
    {{content}}
</div>
'''
