import json
import os
import sys

class Parser():
    """ Class which will receive the text from
    the web application, then split, and keep only key words,
    to send to the API """

    def delete_spaces(self, sentence):
        input_without_spaces = sentence.strip()
        return input_without_spaces

    def sentence_parsed(self, sentence):
        list = sentence.split(" ")
        if len(list) <= 1:
            raise AssertionError()
        path_parser = os.path.dirname(__file__)
        fpath = os.path.join(path_parser, '..', 'ressources', 'stop_words.json')
        with open(fpath, 'r', 1, 'utf-8') as f:
            data = json.load(f)

        valid_words = ""
        for word in list:
            if word not in data:
                valid_words += word + " "
            else:
                pass
        return valid_words.strip()

    def formated_question(self, input_data):
        clean_sentence = self.delete_spaces(input_data)
        formated_sentence = self.sentence_parsed(clean_sentence)
        return formated_sentence