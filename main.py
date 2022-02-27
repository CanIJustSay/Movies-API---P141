from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

with open('movies.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

likeMovies = []
dislikeMovies = []
notWatched = []


@app.route('/getMovies')
def GetAllMovies():
    return jsonify({
        'data': allMovies[0],
        'status':'Success'
    })








if(__name__ == '__main__'):
    app.run(debug=True)