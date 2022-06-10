number_movies = int(input())
total_rating = 0


max_rating_movie = -1
min_rating_movie = 10

best_movie = ""
worst_movie = ""

for movie in range(1, number_movies + 1):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > max_rating_movie:
        best_movie = movie_name
        max_rating_movie = movie_rating

    elif movie_rating < min_rating_movie:
        worst_movie = movie_name
        min_rating_movie = movie_rating

    total_rating += movie_rating
print(f"{best_movie} is with highest rating: {max_rating_movie}")
print(f"{worst_movie} is with lowest rating: {min_rating_movie}")
print(f"Average rating: {total_rating / number_movies:.1f}")
