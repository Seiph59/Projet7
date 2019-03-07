from flask import Flask, render_template, request
import json
from appli.question_parser import Parser

app = Flask(__name__)

app.config['SECRET_KEY'] = '3e58fbf601a27176a461'

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
    return (question_for_api)

if __name__ == "__main__":
    app.run(debug=True)