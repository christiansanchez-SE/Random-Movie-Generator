from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# List of movies
movies = ['Shawn of the Dead', 'Treasure Planet', 'Zombieland', 'Interstellar', 'Lord of the Rings', 'Star Wars', 'Scott Pilgrim vs. the World']

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html', movies=movies)

# Route to get a random movie
@app.route('/random-movie')
def pick_random_movie():
    movie = random.choice(movies)
    return jsonify(movie=movie)

# Route to add a new movie
@app.route('/add-movie', methods=['POST'])
def add_movie():
    new_movie = request.form['movie']
    if new_movie and new_movie not in movies:
        movies.append(new_movie)
        return jsonify(success=True, movie=new_movie)
    return jsonify(success=False, message="Movie is already in the list or invalid input.")

if __name__ == "__main__":
    app.run(debug=True)
