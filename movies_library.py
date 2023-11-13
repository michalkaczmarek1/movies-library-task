import random


class Movie:
    def __init__(self, title, year, type, amount_plays):
        self.title = title
        self.year = year
        self.type = type
        self.amount_plays = amount_plays

    def play(self):
        return self.amount_plays + 1

    def __str__(self):
        return f"{self.title} ({self.year})"


class Serie(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number}E{self.episode_number}"


movie_1 = Movie(title="Pulp Fiction", year=1994, type="action", amount_plays=2)
movie_2 = Movie(title="Kac Vegas", year=2009, type="comedy", amount_plays=4)
serie_1 = Serie(title="Ferry", year=2023, type="action",
                amount_plays=1, episode_number="02", season_number="01")
serie_2 = Serie(title="Friends", year=1995, type="comedy",
                amount_plays=5, episode_number="04", season_number="02")

movies_and_series = [movie_1, movie_2, serie_1, serie_2]


def get_series(movies_and_series):
    series = []
    for elem in movies_and_series:
        if hasattr(elem, "episode_number"):
            series.append(elem)
    return sorted(series, key=lambda serie: serie.title)


def get_movies(movies_and_series):
    movies = []
    for elem in movies_and_series:
        if hasattr(elem, "episode_number") == False:
            movies.append(elem)
    return sorted(movies, key=lambda movie: movie.title)


def launcher_function(func, amount, movies_and_series):
    elems = set()
    for i in range(amount):
        elems.update({func(movies_and_series)})
    return list(elems)


def search_movies_and_series_by_title(movies_and_series, title):
    for elem in movies_and_series:
        if elem.title == title:
            return True
    return False


def generate_views(movies_and_series):
    random_elem = movies_and_series[random.randint(
        0, len(movies_and_series) - 1)]
    random_elem.amount_plays = random.randint(1, 100)
    return random_elem


def top_titles(movies_and_series, amount_chose_movies_and_series, content_type):
    """
        function returns top titles set based on amount plays

        movies_and_series - list from movies and series
        amount_chose_movies_and_series - amount movies or series which user want to choose
        content_type - type of content where 1 - movie and 2 - series
    """

    if amount_chose_movies_and_series > len(movies_and_series):
        print("Podaj inna liczbe zadanych filmow lub seriali. Podan liczba jest za duza")
        return

    elems_with_random_amount_plays = launcher_function(
        generate_views, 10, movies_and_series)
    by_amount_plays = sorted(
        elems_with_random_amount_plays, key=lambda elem: elem.amount_plays)
    by_amount_plays.reverse()
    if content_type == 1 and len(get_movies(by_amount_plays)[:amount_chose_movies_and_series]) <= amount_chose_movies_and_series:
        return get_movies(by_amount_plays)[:amount_chose_movies_and_series]
    elif content_type == 2 and len(get_series(by_amount_plays)[:amount_chose_movies_and_series]) <= amount_chose_movies_and_series:
        return get_series(by_amount_plays)[:amount_chose_movies_and_series]


if __name__ == "__main__":
    for serie in get_series(movies_and_series):
        print(serie)

    for movie in get_movies(movies_and_series):
        print(movie)

    print(search_movies_and_series_by_title(movies_and_series, "Ferry"))
    print(generate_views(movies_and_series))
    print(launcher_function(generate_views, 10, movies_and_series))
    top_titles(movies_and_series=movies_and_series,
               amount_chose_movies_and_series=10, content_type=2)
