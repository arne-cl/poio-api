# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2013 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE.TXT

import os

import sys
import getopt

import poioapi.annotationgraph
import poioapi.io.graf


def main(argv):
    inputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('typecraft2graf.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('typecraft2graf.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--ofile'):
            outputfile = arg

    if inputfile == "" or outputfile == "":
        print('typecraft2graf.py -i <inputfile> -o <outputfile>')
        sys.exit()

    # Create the data structure
    data_hierarchy = None

    # Initialize the annotation graph
    annotation_graph = poioapi.annotationgraph.AnnotationGraph(data_hierarchy)

    # Create a graph from an typecraft file
    annotation_graph.from_typecraft(inputfile)

    graf_graph = annotation_graph.graf
    tier_hierarchies = annotation_graph.tier_hierarchies
    meta_information = annotation_graph.meta_information
    primary_data = annotation_graph.primary_data

    writer = poioapi.io.graf.Writer()

    # Set some values for the document header
    writer.standoffheader.filedesc.titlestmt = "Typecraft Example"
    writer.standoffheader.profiledesc.catRef = "EN"
    writer.standoffheader.filedesc.subdomain = "Sub domain"

    writer.write(outputfile, graf_graph, tier_hierarchies, primary_data, meta_information)

    print('Finished')


if __name__ == "__main__":
    main(sys.argv[1:])