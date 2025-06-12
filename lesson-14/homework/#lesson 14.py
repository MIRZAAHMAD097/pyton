#lesson 14

#1

[
  {
    "name": "Ali",
    "age": 20,
    "grade": "A"
  },
  {
    "name": "Vali",
    "age": 21,
    "grade": "B"
  }
]


import json 

def read_students(file_path):
    try:
        with open(file_path, 'r') as file:
            students = json.load(file)
            print("student details: \n")
            for i, student in enumerate(students, 1):
                print(f"student {i}: ")
                print(f"name: {student.get('name')}")
                print(f"age: {student.get('age')}")
                print(f"grade: {student.get('grade')}\n")
    except FileNotFoundError:
        print(f"error:file '{file_path}' not found")
    except json.JSONDecodeError:
        print("error: failed to decode JSON")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")

read_students('students.json')


#2

import requests

def get_weather(city_name, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code !=200:
            print("error:", data.get("message", "unknown error"))
            return
        print(f"weather in {city_name}: ")
        print(f"temperature: {data['main']['temp']} °C")
        print(f"humidity: {data['main']['humidity']}%")
        print(f"pressure: {data['main']['pressure']} hPa")
        print(f"conditions: {data['weather'][0]['description'].title()}")
    except Exception as e:
        print("error: ", str(e))

api_key = "7f7e6493f607470437253649c75ca79f"
get_weather("Tashkent", api_key)


#3

import json
import os

BOOKS_FILE = "books.json"


def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE,'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[]
    return[]

def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("enter book title: ")
    author = input("enter author name: ")
    year = input("enter publication year: ")
    books = load_books()
    books.append({"title":title, "author":author, "year":year})
    save_books(books)
    print("book added successfully.")

def update_book():
    books = load_books()
    title = input("enter the title of the book to update: ")
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input(f"new author (was {book['author']}): ")
            book["year"] = input(f"new year (was{book['year']}): ")
            save_books(books)
            print("book updated successfully. ")
            return
    print("book not found.")

def delete_book():
    books = load_books()
    title = input("enter the title of the book to delete: ")
    new_books = [book for book in books if book["title"].lower() != title.lower()]
    if len(new_books) == len(books):
        print("book not found.")
    else:
        save_books(new_books)
        print("book deleted successfully. ")
    
def list_books():
    books = load_books()
    if not books:
        print("no book found. ")
        return
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']})")

def main():
    while True:
        print("\n--- Book manager ---")
        print("1.list books")
        print("2.add books")
        print("3.update books")
        print("4.delete books")
        print("5.exit")
        choice = input("choice an option(1-5): ")
        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("exit")
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()


#4

import requests
import random

api_key = "ea5c0223"

movies_by_genre = {
    "action": ["mad max", "Die Hard", "Lord of the rings", "John Wick", "Gladiator"],
    "comedy": ["Superbad", "The Hangover", "Beverly Hills police", "Naked Gun"],
    "drama": ["Forrest Gump", "Fight club", "The Godfather", "Hobbit"],
    "horror": ["The Conjuring", "Get Out", "Resident evil", "Silent Hill"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix", "Blade Runner 2049"]
}

def get_movie_info(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        print("\n Movie Recommendation:")
        print(f"Title: {data['Title']}")
        print(f"Year: {data['Year']}")
        print(f"Genre: {data['Genre']}")
        print(f"Plot: {data['Plot']}")
        print(f"IMDB Rating: {data['imdbRating']}")
    else:
        print(" Movie not found.")
def main():
    genre = input("Enter a genre (action, comedy, drama, horror, sci-fi): ").lower()
    if genre in movies_by_genre:
        movie_title = random.choice(movies_by_genre[genre])
        get_movie_info(movie_title, api_key)
    else:
        print(" Genre not supported. Please choose from the list.")
if __name__ == "__main__":
    main()

