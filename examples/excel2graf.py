# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2013 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE.TXT

import sys, getopt

import poioapi.io.excel

def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('excel2graf.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('excel2graf.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg

    if inputfile == "" or outputfile == "":
        print('excel2graf.py -i <inputfile> -o <outputfile>')
        sys.exit()

    parser = poioapi.io.excel.Parser(inputfile)

    converter = poioapi.io.graf.GrAFConverter(parser)
    converter.convert()

    tiers_hierarchies = converter.tiers_hierarchy

    graf = converter.graph

    print('Finished')

if __name__ == "__main__":
    main(sys.argv[1:])