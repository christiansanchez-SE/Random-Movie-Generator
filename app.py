from flask import Flask, render_template, request, jsonify
import random

# Initialize the Flask application
app = Flask(__name__)

# List of movies
# This is a Python list that stores movie names. It is accessible throughout the app.
movies = ['Shawn of the Dead', 'Treasure Planet', 'Zombieland', 'Interstellar', 'Lord of the Rings', 'Star Wars', 'Scott Pilgrim vs. the World']

# Route to serve the main page
@app.route('/')
def index():
    # This function is responsible for serving the main HTML page.
    # The render_template function renders the HTML file called 'index.html'.
    # The list of movies is passed to the template so it can display them.
    return render_template('index.html', movies=movies)

# Route to get a random movie
@app.route('/random-movie')
def pick_random_movie():
    # This function picks a random movie from the 'movies' list using the random.choice function.
    movie = random.choice(movies)
    
    # jsonify() converts the Python object (in this case, the movie) into JSON format, which is sent back to the client (the browser).
    return jsonify(movie=movie)

# Route to add a new movie
@app.route('/add-movie', methods=['POST'])
def add_movie():
    # Get the new movie name from the form data sent in the POST request.
    new_movie = request.form['movie']
    
    # Check if the new movie is not empty and is not already in the list.
    if new_movie and new_movie not in movies:
        # If the movie is valid and not already in the list, append it to the 'movies' list.
        movies.append(new_movie)
        
        # Send a success response back to the client with the new movie in JSON format.
        return jsonify(success=True, movie=new_movie)
    
    # If the movie is invalid or already exists in the list, return an error message.
    return jsonify(success=False, message="Movie is already in the list or invalid input.")

# This runs the application when the script is executed directly.
if __name__ == "__main__":
    # app.run() starts the Flask development server with 'debug' mode enabled.
    # 'debug=True' will give detailed error messages and automatically reload the server when you make changes to the code.
    app.run(debug=True)
