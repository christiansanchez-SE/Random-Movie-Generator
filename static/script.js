// Event listener for picking a random movie
document.getElementById('randomMovieBtn').addEventListener('click', async function() {
    // When the button is clicked, we send a request to the '/random-movie' URL on the server
    const response = await fetch('/random-movie');
    
    // We wait for the server to send back the data, and then convert the response to JSON (a format to easily handle data)
    const data = await response.json();
    
    // Now, we update the HTML by showing the random movie in the <p> element with id "movieDisplay"
    document.getElementById('movieDisplay').textContent = `Random Movie: ${data.movie}`;
});

// -- Spacer -- //

// Event listener for adding a movie
document.getElementById('addMovieForm').addEventListener('submit', async function(event) {
    // Prevent the form from reloading the page when it's submitted
    event.preventDefault();

    // Get the movie name that the user entered in the text input field
    const movieInput = document.getElementById('movieInput').value;

    // Create a new FormData object to package the movie name and send it to the server
    const formData = new FormData();
    formData.append('movie', movieInput);  // We append the movie input to the FormData object

    // Send the movie name to the server using a POST request to '/add-movie'
    const response = await fetch('/add-movie', {
        method: 'POST',  // We're sending data to the server
        body: formData   // The movie name is in the formData object, sent in the body of the request
    });

    // Get the response from the server and convert it to JSON
    const data = await response.json();

    // Check if the server successfully added the movie
    if (data.success) {
        // Update the page to show a success message and add the new movie to the list on the page
        document.getElementById('addMovieResponse').textContent = `${data.movie} added to the list!`;
        
        // Create a new list item for the new movie and add it to the list of movies
        const movieList = document.getElementById('movieList');
        const newMovieItem = document.createElement('li');
        newMovieItem.textContent = data.movie;
        movieList.appendChild(newMovieItem);
    } else {
        // If there was an error (like the movie is already in the list), show an error message
        document.getElementById('addMovieResponse').textContent = data.message;
    }

    // Clear the input field after the movie is added
    document.getElementById('movieInput').value = '';
});

