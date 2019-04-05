from flask import Flask, render_template, request, jsonify
from config import SECRET_KEY
from .appli.question_parser import Parser
from .appli import googlemaps
from .appli import api_wikisearch

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
    try:
        tata = request.get_json()
        parse = Parser()
        question_for_api = parse.formated_question(tata['data'])
        coordinates = googlemaps.get_coords_from_address(question_for_api)
        # print(coordinates_returned)
        result_wiki = api_wikisearch.research_page(coordinates)
        # print(result_wiki)
        return jsonify(result_wiki, coordinates)

    except googlemaps.GoogleException as err:
        error = {'error': str(err)}
        return jsonify(error)
    except:
        error = {'error': " Désolé, une erreur technique s'est produite "}
        return jsonify(error)


if __name__ == "__main__":
    app.run()
