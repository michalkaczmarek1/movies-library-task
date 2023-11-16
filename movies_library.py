import random
from datetime import date


class Library:
    def __init__(self, title, year, type, amount_plays):
        self.title = title
        self.year = year
        self.type = type
        self.amount_plays = amount_plays

    def play(self):
        return self.amount_plays + 1


class Movie(Library):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Serie(Library):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"


def get_series(movies_and_series, content_type):
    return separation_content_type(movies_and_series, content_type)


def get_movies(movies_and_series, content_type):
    return separation_content_type(movies_and_series, content_type)


def separation_content_type(movies_and_series, content_type):
    elems = []
    for elem in movies_and_series:
        if isinstance(elem, content_type):
            elems.append(elem)

    return sorted(elems, key=lambda elem: elem.title)


def launcher_function_generate_views(movies_and_series, amount_runs=10):

    for i in range(amount_runs):
        generate_views(movies_and_series)
    return movies_and_series


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

    if content_type == 1:
        choose_movies = get_movies(movies_and_series, Movie)[
            :amount_chose_movies_and_series]
        top_titles = sorted(
            choose_movies, key=lambda elem: elem.amount_plays, reverse=True)
    elif content_type == 2:
        choose_series = get_series(movies_and_series, Serie)[
            :amount_chose_movies_and_series]
        top_titles = sorted(
            choose_series, key=lambda elem: elem.amount_plays, reverse=True)

    return top_titles


if __name__ == "__main__":
    print("Biblioteka filmów:")

    movie_1 = Movie(title="Pulp Fiction", year=1994,
                    type="action", amount_plays=2)
    movie_2 = Movie(title="Kac Vegas", year=2009,
                    type="comedy", amount_plays=4)
    movie_3 = Movie(title="Kac Vegas w Bangkoku", year=2011,
                    type="comedy", amount_plays=4)
    serie_1 = Serie(title="Ferry", year=2023, type="action",
                    amount_plays=1, episode_number=2, season_number=2)
    serie_2 = Serie(title="Friends", year=1995, type="comedy",
                    amount_plays=5, episode_number=4, season_number=2)
    serie_3 = Serie(title="Gambit królowej", year=2021, type="obyczajowy",
                    amount_plays=5, episode_number=4, season_number=1)

    movies_and_series = [movie_1, movie_2, movie_3, serie_1, serie_2, serie_3]

    for elem in movies_and_series:
        print(elem)

    launcher_function_generate_views(movies_and_series)

    current_date = date.today()
    formatted_date = current_date.strftime("%d.%m.%Y")

    print(f"Najpopularniejsze filmy i seriale dnia {formatted_date}:")

    top_popular_content = top_titles(movies_and_series=movies_and_series,
                                     amount_chose_movies_and_series=3, content_type=1)

    for item in top_popular_content:
        print(item)
