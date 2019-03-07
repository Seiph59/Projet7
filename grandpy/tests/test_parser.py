import pytest
import sys

from grandpy.appli.question_parser import Parser

def test_delete_spaces():
    parsing = Parser()
    assert parsing.delete_spaces("   je suis   ") == "je suis"
    #assert parsing.delete_spaces() == "je suis"

def test_sentence_parsed():
    sentence = "je cherche l'église de Lille"
    parsing = Parser()
    assert parsing.sentence_parsed(sentence) == "l'église Lille"

def test_parser_empty():
    empty_sentence = ""
    with pytest.raises(AssertionError):
        parsing = Parser()
        parsing.sentence_parsed(empty_sentence)