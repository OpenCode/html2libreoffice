# -*- coding: utf-8 -*-
# © 2016 Francesco Apruzzese <cescoap@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def page_number():
    return '<sdfield type=PAGE subtype=RANDOM format=PAGE>0</sdfield>'


def page_count():
    return '<sdfield type=DOCSTAT subtype=PAGE format=PAGE>0</sdfield>'


def new_page():
    return '<p style="page-break-before: always" />'
