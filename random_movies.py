import random

# List of movies
movies = ['Shawn of the Dead', 'Treasure Planet', 'Zombieland', 'Interstellar','Lord of the Rings', 'Star Wars', 'Scot Pilgrim vs the World']

# Function to pick a random movie
def pick_random_movie():
    return random.choice(movies)

# Function to add a movie to the list
def add_movie(movie):
    if movie not in movies:
        movies.append(movie)
        print(f'{movie} added to the list!')
    else:
        print(f'{movie} is already in the list!')

# Function to display all movies
def display_movies():
    if movies:
        print("Current list of movies:")
        for index, movie in enumerate(movies, 1):
            print(f"{index}. {movie}")
    else:
        print("No movies in the list.")

# Main program
def main():
    while True:
        print("\nMovie Picker Menu:")
        print("1. Pick a random movie")
        print("2. Add a movie")
        print("3. Display all movies")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print(f'Random Movie: {pick_random_movie()}')
        elif choice == '2':
            new_movie = input("Enter the name of the movie: ")
            add_movie(new_movie)
        elif choice == '3':
            display_movies()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
