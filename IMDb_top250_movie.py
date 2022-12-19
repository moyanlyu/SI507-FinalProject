import requests
from bs4 import BeautifulSoup
import re
from lxml import etree
import json


class imdb_movie:
    """
    A class to imdb movie.

    Attributes
    ----------
    name : movie name
    url : movie url
    rating : movie rating
    id: movie id
    year : movie year
    actors : movie actors
    ranking: movie ranking
    rating: movie rating

    Methods
    -------
    detail_information():
        return detail information of movie
    rating_information):
        return movie rating information
    movie_information():
        return all movie information
    """
    def __init__(self, id=None, url=None, name=None,
                rating=None, year=None, directors=None,
                actors=None, ranking=None, nyt_review=None):
        self.movie_id = id
        self.url = url
        self.name = name
        self.rating = rating
        self.year = year
        self.directors = directors
        self.actors = actors
        self.ranking = ranking
        self.nyt_review = nyt_review

    def add_nyt_review(self, nyt_review):
        self.nyt_review = nyt_review


    def detail_information(self):
        detail_info = {
            "url": self.url,
            "movie id": self.movie_id,
            "year": self.year,
            "actors": self.actors,
            "directors": self.directors}
        return detail_info

    def rating_information(self):
        data = {
            "ranking": self.ranking,
            "rating": self.rating,
        }
        return data
    
    def review_information(self):
        data = {
            "review": self.nyt_review
        }
        return data

    def movie_information(self):
        data = {"name": self.name,
                "detail info": self.detail_information(),
                "rating info": self.rating_information(),
                "review info": self.review_information()}
        return data


def scrap_movie_data_from_imdb():
    '''
    Returns a list of movie data from imdb.

            Parameters:
                -----------

            Returns:
                A list of imdb movie.
    '''
    page_text = requests.get('http://www.imdb.com/chart/top').text
    soup = BeautifulSoup(page_text, 'lxml')
    movies = soup.select('td.titleColumn')

    movie_url = ['https://www.imdb.com' +
                 item.attrs.get('href') for item in soup.select('td.titleColumn a')]
    movie_a = [item.attrs.get('title')
                    for item in soup.select('td.titleColumn a')]
    movie_ratings = [item.attrs.get(
        'data-value') for item in soup.select('td.posterColumn span[name=ir]')]

    movie_list = []
    movie_name_list = []

    for i in range(0, len(movies)):

        movie_id = movie_url[i].split('/')[-2]

        movie_string = movies[i].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))

        movie_actor = re.sub('^[^,]*(?=,),', '', movie_a[i])
        movie_name = movie[len(str(i))+1:-7]
        # print(movie_name)
        movie_rank = movie[:len(str(i))-(len(movie))]
        movie_year = re.search('\((.*?)\)', movie_string).group(1)

        movie_d = movie_a[i].split(',')
        movie_director = movie_d[0].strip('(.dir)')

        movie_data = imdb_movie(url=movie_url[i], id=movie_id, name=movie_name, rating=movie_ratings[i],
                                year=movie_year, actors=movie_actor, ranking=movie_rank, directors=movie_director)
        movie_name_list.append(movie_name)
        movie_list.append(movie_data)
    # print(movie_name_list)
    return movie_list



data = scrap_movie_data_from_imdb()


def save_movie_data_form_imdb(data):
    '''
        Save imdb movie list to cache.
            Parameters:
                    imdb_list: A list of imdb movie.

            Returns:
                    None
    '''
    f = open("IMDb_top250_movie.json", 'w').close()
    for index in range(0, len(data)):
        data[index].movie_information()
        with open("IMDb_top250_movie.json", 'a') as f:
            f.write(json.dumps(data[index].movie_information(), indent=4))
            if index != len(data)-1:
                f.write(',')
    with open("IMDb_top250_movie.json", 'a') as f:
        f.write(']')
    with open("IMDb_top250_movie.json", 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write('[' + content)
    f.close()

save_movie_data_form_imdb(data)
