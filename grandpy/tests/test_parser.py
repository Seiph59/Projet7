import pytest
import sys
from ..appli import question_parser

def test_delete_spaces():
    parsing = question_parser.Parser()
    assert parsing.delete_spaces("   je suis   ") == "je suis"
    #assert parsing.delete_spaces() == "je suis"

def test_sentence_parsed():
    sentence = "je cherche l'église de Lille"
    parsing = question_parser.Parser()
    assert parsing.sentence_parsed(sentence) == "l'église Lille"

def test_parser_empty():
    empty_sentence = ""
    with pytest.raises(AssertionError):
        parsing = question_parser.Parser()
        parsing.sentence_parsed(empty_sentence)