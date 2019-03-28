from flask import Flask, render_template, request
import json
from .appli.question_parser import Parser
from .appli import googlemaps
from .appli import api_wikisearch
from config import SECRET_KEY

app = Flask(__name__)

app.config.from_object('config')

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user_question', methods=['POST'])
def test_ajax():
    tata = request.get_json()
    parse = Parser()
    question_for_api = parse.formated_question(tata['data'])
    coordinates_returned = googlemaps.api_request(question_for_api)
    #print(coordinates_returned)
    result_wiki = api_wikisearch.research_page(coordinates_returned)
    #print(result_wiki)
    return json.dumps(result_wiki).encode('utf8')


if __name__ == "__main__":
    app.run()