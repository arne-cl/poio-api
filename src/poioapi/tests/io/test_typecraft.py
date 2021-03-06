# -*- coding: utf-8 -*-
#
# Poio Tools for Linguists
#
# Copyright (C) 2009-2013 Poio Project
# Author: António Lopes <alopes@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE.TXT

import os
import re

import xml.etree.ElementTree as ET

import poioapi.io.typecraft
import poioapi.io.graf

class TestTypecraft:
    """
    This class contain the test methods to the
    class io.typecraft.py.

    """

    def setup(self):
        self.filename = os.path.join(os.path.dirname(__file__), "..", "sample_files",
            "typecraft_graf", "typecraft_example.xml")

        self.basedirname = os.path.dirname(self.filename)

        self.parser = poioapi.io.typecraft.Parser(self.filename)

        self.converter = poioapi.io.graf.GrAFConverter(self.parser)
        self.converter.parse()

        self.graph = self.converter.graf

        tree = ET.parse(self.filename)
        self.root = tree.getroot()

        self.xml_namespace = re.search('\{(.*)\}', self.root.tag).group()

    def test_phrase_nodes(self):
        nodes_number = len(self.root.findall(self.xml_namespace+"phrase")) - 1

        expected_nodes_number = 0

        for nodes in self.graph.nodes:
            if "phrase" in nodes.id:
                expected_nodes_number+=1

        assert(nodes_number == expected_nodes_number)

    def test_phrase_annotation_features(self):
        node_phrase = self.root.find(self.xml_namespace+"phrase")

        expected_features_number = len(node_phrase.attrib) - 3

        for elements in node_phrase:
            key = str(elements.tag).split(self.xml_namespace)
            if key[1] != "word" and key[1] != "globaltags":
                expected_features_number+=1

        node = self.graph.nodes["phrase..n9764"]

        node_annotations = node.annotations._elements

        features_number = len(node_annotations[0].features)

        assert(features_number == expected_features_number)

    def test_get_root_tiers(self):
        root_tiers = self.parser.get_root_tiers()

        assert len(root_tiers) == 1

    def test_get_child_tiers_for_tier(self):
        root_tiers = self.parser.get_root_tiers()

        tier = root_tiers[0]

        child_tier = self.parser.get_child_tiers_for_tier(tier)

        assert len(child_tier) == 3

    def test_get_annotations_for_tier(self):
        root_tiers = self.parser.get_root_tiers()
        child_tier_annotations = self.parser.get_annotations_for_tier(root_tiers[0])

        assert len(child_tier_annotations) == 10