import math

numberOfMovies = int(input())

bestMovie = ""
bestScore = 0.0

worstMovie = ""
worstScore = 11111111

totalScore = 0.0

for i in range(1, numberOfMovies+1):
    movieName = input()
    movieRating = float(input())

    if movieRating > bestScore:
        bestMovie = movieName
        bestScore = movieRating

    if movieRating < worstScore:
        worstMovie = movieName
        worstScore = movieRating

    totalScore += movieRating

averageScore = totalScore / numberOfMovies

print(f'{bestMovie} is with highest rating: {bestScore:.1f}')
print(f"{worstMovie} is with lowest rating: {worstScore:.1f}")
print(f'Average rating: {averageScore:.1f}')
