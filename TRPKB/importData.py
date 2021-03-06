#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PROGRAM : importData
# AUTHOR  : codeunsolved@gmail.com
# CREATED : July 5 2017
# VERSION : v0.0.1

import os
import re

import xlrd


def read_xls(path_xls, kb):
    def read_table(tab_name):
        tab_data = []

        sheet = wb.sheet_by_name(tab_name)
        nrows = sheet.nrows

        for i in range(nrows):
            if i == 0:
                continue
            tab_data.append(sheet.row_values(i))
        return tab_data

    data = {}
    wb = xlrd.open_workbook(path_xls)

    if kb == 'snp':
        tab_list = tab_snp
    elif kb == 'exp':
        tab_list = tab_exp

    for key in tab_list:
        data[key] = read_table(key)

    return data

tab_snp = ['research', 'tumor', 'gene', 'variant', 'prognosis', 'subgroup', 'association']
tab_exp = ['research', 'tumor', 'gene', 'prognosis', 'subgroup', 'association']
