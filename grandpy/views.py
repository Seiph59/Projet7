"""
Core file, displaying all the html pages, and receive ajax's requests.

"""
import os
from flask import Flask, render_template, request, jsonify
from .appli.question_parser import Parser
from .appli import googlemaps
from .appli import api_wikisearch

app = Flask(__name__)

try:
    from config import SECRET_KEY, API_GOOGLE_FRONT
    app.secret_key = SECRET_KEY

except ImportError:
    app.secret_key = os.environ.get('SECRET_KEY')
    API_GOOGLE_FRONT = os.environ.get('API_GOOGLE_FRONT')

@app.route('/')
@app.route('/home')
def home():
    """
    Displaying the home page, by two differents manners (/home) or (/)
    """
    return render_template('home.html', googlemapskey=API_GOOGLE_FRONT)


@app.route('/about')
def about():
    """
    Displaying the about page, used to give developer's informations
    """
    return render_template('about.html')


@app.route('/user_question', methods=['POST'])
def ajax():
    """
    Method managing the differents communication between back-end(python)
    and front-end(js)
    """
    try:
        user_question = request.get_json()
        parse = Parser()
        question_for_api = parse.formated_question(user_question['data'])
        coordinates = googlemaps.get_coords_from_address(question_for_api)
        result_wiki = api_wikisearch.research_page(coordinates)
        return jsonify(result_wiki, coordinates)

    except googlemaps.GoogleException as err:
        error = {'error': str(err)}
        return jsonify(error)
    except api_wikisearch.WikiException:
        error = {'error': " Désolé, une erreur technique s'est produite "}
        return jsonify(error)
    except Exception:
        error = {'error': " Impossible de trouver une réponse à cette question"}
        return jsonify(error)


if __name__ == "__main__":
    app.run()
