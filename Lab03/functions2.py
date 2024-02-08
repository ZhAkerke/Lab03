#From the functions2
#1
def is_high_rated(movie):
    return movie['imdb'] > 5.5

#2
def filter_high_rated_movies(movies):
    return [movie for movie in movies if is_high_rated(movie)]

#3
def filter_movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

#4
def calculate_average_imdb(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies) if len(movies) > 0 else 0

#5
def calculate_average_imdb_by_category(movies, category):
    category_movies = filter_movies_by_category(movies, category)
    return calculate_average_imdb(category_movies)

#Some testings
test_movie = {
    "name": "Test Movie",
    "imdb": 6.0,
    "category": "Test"
}
print("Is the movie high rated?", is_high_rated(test_movie))

high_rated_movies = filter_high_rated_movies(movies)
print("Sublist of high rated movies:", high_rated_movies)

category = "Romance"
print(f"Movies under the {category} category:", filter_movies_by_category(movies, category))

print("Average IMDB score of all movies:", calculate_average_imdb(movies))

category = "Romance"
print(f"Average IMDB score of movies under the {category} category:", calculate_average_imdb_by_category(movies, category))
