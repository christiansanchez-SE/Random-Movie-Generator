from flask import Flask, render_template
import random

app = Flask(__name__)

movies = ['Shawn of the Dead', 'Treasure Planet', 'Zombieland', 'Interstellar', 'Monsters Inc.', 'Shrek', 'Nacho Libre']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-movie')
def pick_random_movie():
    return random.choice(movies)

if __name__ == "__main__":
    app.run(debug=True)
