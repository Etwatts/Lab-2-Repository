"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Ethan Watts',
        'studentID': '10262692',
        'pizza toppings': [
            'bacon',
            'pepperoni',
            'olives'
        ],
        'movies': [
            {
                'title': 'Fight Club',
                'genre': 'Thriller',
            },
            {
                'title': 'V for Vendetta',
                'genre': 'Action',
            }
        ]
    }
    
    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # Change to pizza toppings you like
    add_pizza_toppings(about_me, ['basil', 'mushrooms'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # Change to a movie you like
    add_movie(about_me, 'taxi driver', 'psycological thriller')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Complete function body per Step 3

    full_name = my_info['name'].split()
    first_name = full_name[0]
    # Print sentence containing name
    print(F"My name is {my_info['name']} but you can call me {first_name} ")
    # Print sentence containing student ID
    print(F"My student ID is {my_info['studentID']}")

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    print("My favourite pizza toppings are: ")
    # Print bullet list of favourite pizza toppings
    for topping in my_info['pizza toppings']:
        print(f"- {topping}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # Complete function body per Step 5
    # Append new pizza toppings to end of list 
    my_info['pizza toppings'].extend(toppings)
    # Convert all pizza toppings to lowercase
    for i, topping_name in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = topping_name.casefold() 
    # Sort toppings list alphabetically
    my_info['pizza toppings'].sort()
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    new_movie = {
                'title': title,
                'genre': genre
            }
    my_info['movies'].append(new_movie)
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Complete function body per Step 7
    movie_list = my_info['movies']
    movie_genres = [movie['genre'] for movie in movie_list]
    print("My favourite movies genre's are: "+ ", ".join(movie_genres).title())

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # Complete function body per Step 8
    movie_titles = [movie['title'] for movie in movie_list]
    print ("My favourite movies are: "+ ", ".join(movie_titles).title())
  


if __name__ == '__main__':
    main()