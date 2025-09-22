from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to the Flask API"

@app.route("/flashcards")
def flashcards():
	return [
    {
        "suuid": "a6bmmF",
        "category": "it",
        "front": "and it will take some time",
        "back": "e ci vorrà del tempo"
    },
    {
        "suuid": "8m60CW",
        "category": "it",
        "front": "this will ensure that you get",
        "back": "c'è garantirà di ottenere"
    },
    {
        "suuid": "Q8JQnJ",
        "category": "es",
        "front": "this has certain advantages",
        "back": "est tiene ciertas ventajas"
    },
    {
        "suuid": "nFtvs8",
        "category": "es",
        "front": "in such a way that",
        "back": "de tal manera que"
    }
]