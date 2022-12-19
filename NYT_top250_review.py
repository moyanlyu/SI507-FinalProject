from asyncio.windows_events import NULL
import requests
import json
import time
# import urllib library
from urllib.request import urlopen
def get_json(url):
    # url = "http://api.nytimes.com/svc/movies/v2/reviews/all.json?&query=The%20Shawshank%20Redemption&api-key=09YtZvPGt7bLLByPxBXALLNu2mIF8ksS"
    # requestHeaders = {
    #     "Accept": "application/json"
    # }
    time.sleep(2.0)
    response = urlopen(url)
    # requests.get(url, headers = {'User-agent': 'your bot 5.0'})
    # if response.status == 429:
    #     time.sleep(int(response.headers["Retry-After"]))
    data_json = json.loads(response.read())
    data = data_json['results']
    return data
# print(data)
# url = "http://api.nytimes.com/svc/movies/v2/reviews/all.json?&query=The%20Shawshank%20Redemption&api-key=09YtZvPGt7bLLByPxBXALLNu2mIF8ksS"

# data = get_json(url)
# print(data)
# requestUrl = "http://api.nytimes.com/svc/movies/v2/reviews/all.json?&query=The%20Shawshank%20Redemption&api-key=09YtZvPGt7bLLByPxBXALLNu2mIF8ksS"

new_list=[]
top250_list = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Godfather Part II', '12 Angry Men', "Schindler's List", 'The Lord of the Rings: The Return of the King', 'Pulp Fiction', 'The Lord of the Rings: The Fellowship of the Ring', ' The Good, the Bad and the Ugly', 'Forrest Gump', 'Fight Club', 'The Lord of the Rings: The Two Towers', 'Inception', 'Star Wars: Episode V - The Empire Strikes Back', 'The Matrix', 'Goodfellas', "One Flew Over the Cuckoo's Nest", 'Se7en', 'Seven Samurai', "It's a Wonderful Life", 'The Silence of the Lambs', 'City of God', 'Saving Private Ryan', 'Life Is Beautiful', 'Interstellar', 'The Green Mile', 'Star Wars', 'Terminator 2: Judgment Day', 'Back to the Future', 'Spirited Away', 'Psycho', 'The Pianist', 'Parasite', 'Leon: The Professional', 'The Lion King', 'Gladiator', 'American History X', 'The Departed', 'The Usual Suspects', 'The Prestige', 'Whiplash', 'Casablanca', 'Harakiri', 'Grave of the Fireflies', 'The Intouchables', 'Modern Times', 'Once Upon a Time in the West', 'Rear Window', 'Cinema Paradiso', 'Alien', 'City Lights', 'Apocalypse Now', 'Memento', 'Raiders of the Lost Ark', 'Django Unchained', 'WALL·E', 'The Lives of Others', 'Sunset Blvd', 'Paths of Glory', 'The Great Dictator', 'The Shining', 'Avengers: Infinity War', 'Witness for the Prosecution', 'Aliens', 'Spider-Man: Into the Spider-Verse', 'American Beauty', 'Dr Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 'The Dark Knight Rises', 'Oldboy', 'Amadeus', 'Inglourious Basterds', 'Joker', 'Coco', 'Toy Story', 'Braveheart', 'The Boat', 'Avengers: Endgame', 'Princess Mononoke', 'Once Upon a Time in America', 'Good Will Hunting', 'Your Name', 'Top Gun: Maverick', 'Requiem for a Dream', '3 Idiots', "Singin' in the Rain", 'Toy Story 3', 'High and Low', 'Star Wars: Episode VI - Return of the Jedi', 'Capernaum', 'Eternal Sunshine of the Spotless Mind', '2001: A Space Odyssey', 'Reservoir Dogs', 'The Hunt', 'Come and See', 'Citizen Kane', 'M', 'Lawrence of Arabia', 'North by Northwest', ' Vertigo', 'Amélie', 'A Clockwork Orange', 'The Apartment', 'Ikiru', 'Double Indemnity', 'Full Metal Jacket', 'Hamilton', 'Scarface', 'To Kill a Mockingbird', 'The Sting', 'Incendies', 'Up', 'Heat', 'Taxi Driver', 'A Separation', 'Metropolis', 'LA Confidential', 'Die Hard', 'Snatch', 'Bicycle Thieves', 'Indiana Jones and the Last Crusade', 'Like Stars on Earth', '1917', 'Downfall', 'For a Few Dollars More', 'Dangal', 'Batman Begins', 'The Kid', 'Some Like It Hot', 'The Father', 'All About Eve', 'Green Book', 'The Wolf of Wall Street', 'Judgment at Nuremberg', 'Ran', 'Casino', "Pan's Labyrinth", 'Unforgiven', 'There Will Be Blood', 'The Truman Show', 'The Sixth Sense', 'A Beautiful Mind', 'Shutter Island', 'Yojimbo', 'Monty Python and the Holy Grail', 'The Treasure of the Sierra Madre', 'Spider-Man: No Way Home', 'Jurassic Park', 'The Great Escape', 'Rashomon', 'Kill Bill: Vol 1', 'No Country for Old Men', 'Finding Nemo', 'The Thing', 'The Elephant Man', 'Chinatown', 'Raging Bull', 'Gone with the Wind', 'V for Vendetta', 'Inside Out', 'Lock, Stock and Two Smoking Barrels', 'Dial M for Murder', 'The Secret in Their Eyes', "Howl's Moving Castle", 'The Bridge on the River Kwai', 'Three Billboards Outside Ebbing, Missouri', 'Trainspotting', 'Warrior', 'Fargo', 'Gran Torino', 'Prisoners', 'My Neighbor Totoro', 'Catch Me If You Can', 'Million Dollar Baby', 'Children of Heaven', 'Blade Runner', 'The Gold Rush', 'On the Waterfront', 'Before Sunrise', '12 Years a Slave', 'Harry Potter and the Deathly Hallows: Part 2', 'Ben-Hur', 'Wild Strawberries', 'Gone Girl', 'The Third Man', 'The General', 'The Grand Budapest Hotel', 'The Deer Hunter', 'In the Name of the Father', 'Klaus', 'Barry Lyndon', 'The Wages of Fear', 'Hacksaw Ridge', 'Sherlock Jr', 'Mr Smith Goes to Washington', 'Memories of Murder', 'Wild Tales', 'The Seventh Seal', 'Mad Max: Fury Road', 'Room', 'Mary and Max', 'How to Train Your Dragon', 'Monsters, Inc', 'The Big Lebowski', 'Jaws', 'Dead Poets Society', 'The Passion of Joan of Arc', 'Tokyo Story', 'Hotel Rwanda', 'Ford v Ferrari', 'Rocky', 'Platoon', 'Spotlight', 'The Terminator', 'Stand by Me', 'Ratatouille', 'Logan', 'Rush', 'Pather Panchali', 'Network', 'Into the Wild', 'The Wizard of Oz', 'Before Sunset', 'Groundhog Day', 'The Best Years of Our Lives', 'The Exorcist', 'To Be or Not to Be', 'The Incredibles', 'The Battle of Algiers', 'Jai Bhim', "Hachi: A Dog's Tale", 'La haine', 'Pirates of the Caribbean: The Curse of the Black Pearl', 'The Grapes of Wrath', 'Rebecca', 'My Father and My Son', 'Amores Perros', 'Cool Hand Luke', 'The 400 Blows', 'The Handmaiden', 'Persona', 'It Happened One Night', 'The Sound of Music', 'Life of Brian', 'Everything Everywhere All at Once', 'Dersu Uzala', 'The Iron Giant', 'Aladdin', 'The Help', 'Gandhi']
for top in top250_list:
    top = top.replace('·','%C2%B7')
    top = top.replace(':','%3A')
    top = top.replace(' ','%20')
    new_list.append(top)
# print(new_list)

new_url=[]
for new in new_list:
    movie_url = "http://api.nytimes.com/svc/movies/v2/reviews/all.json?query={new}&api-key=09YtZvPGt7bLLByPxBXALLNu2mIF8ksS".format(new=new)
    # print(url)
    new_url.append(movie_url)
# print(new_url)

data = []
for url in new_url:
    movie_data = []
    movie_data = get_json(url)
    # print(movie_data)
    data.append(movie_data)
# for url in new_url[6:10]:
#     movie_data = get_json(url)
#     # print(movie_data)
#     data.append(movie_data)
# print(data)

def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)

write_json('nyt24.json', data)