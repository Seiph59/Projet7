"""
File used for the parser's unit test
"""
import pytest
from ..appli import question_parser


def test_delete_spaces():
    """
    Check if the method which remove empty spaces is working
    """
    parsing = question_parser.Parser()
    assert parsing.delete_spaces("   je suis   ") == "je suis"


def test_sentence_parsed():
    """
    Check if the method which parsed the sentence is working
    """
    sentence = "je cherche l'église de Lille"
    parsing = question_parser.Parser()
    assert parsing.sentence_parsed(sentence) == "l'église Lille"


def test_parser_empty():
    """
    Check if the parser generate and error if the sentence is empty
    """
    empty_sentence = ""
    with pytest.raises(AssertionError):
        parsing = question_parser.Parser()
        parsing.sentence_parsed(empty_sentence)
