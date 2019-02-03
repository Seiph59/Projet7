import json
import os

test ="   la phrase qu'on teste est un vrai défi  "

def delete_spaces(test):
    input_without_spaces = test.strip()
    return input_without_spaces

def list_parsed(list):
    if len(list) == 0:
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