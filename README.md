# SI507-FinalProject
1. Overview
This project is a movie reviewing program which aims to scrape data from the New York Times- Movie Reviews and IMDb websites to collect ratings and reviews for movies in different media and websites. This project integrates two related but distinct dataset and therefore be able to tell us something interesting that couldn’t be found with just one.
The program will perform the following functions:
Access the New York Times Movie review data by requesting through API and scrape one single new page IMDb to collect top 250 movies’ data.
Combine the review articles with top 250 movies in one database.
Create a database using data from above sources.
Allow users to interact with the program by selecting the movies they are interested in and find the critical articles related to the movies in New York Times.

2. Data Source:
New York Times- Movies review:
Original URL: http://api.nytimes.com/svc/movies/v2/reviews/all.json?&api-key=09YtZvPGt7bLLByPxBXALLNu2mIF8ksS
Format: Json, web API I haven’t used before that requires API key
Data summary: New York Times movies review data is mainly about the top 250 movies and their corresponding article critical reviews. The length of the json file is 250. It is corresponding to IMDb top 250 movie data, but these two databases are complementary to each other.
IMDB: 
Scraping Top 250 movies in one single page: http://www.imdb.com/chart/top
Data summary: IMDB data is mainly about the top 250 movies and their corresponding information include name, year, rating, ranking and many other detailed information. The length of the json file is 250. 
Caching Evidence:
 
3. Data access and Storage:
Scrap method:
For the IMDB top 250 data, I scraped the data in one single page by implementing regular expressions and BeautifulSoup. I collected 250 movies’ information and their movie_id. Then I utilize those movie id to request each movie’s detailed information including the actors, rating, rank and genre of movie. 
For New York Times movies reviews, by scraping each movie’s name, I build a list to include all the top 250 movies’ names. And using the movies list to get the New York Times’ movie reviews by using API key to access the critical review data.
Storage:
By using soup.find and select, I successfully grabbed the detailed information of each movie and cached them in a json file.

4. Data Structure:
The data scraped from the data source is organized as a 2-level tree, as below. The two data perfectly complement each other. NYT's review articles can make a good supplementary explanation for imdb's basic information and rating. I organized the data as name information includes detailed information/ rating information/ NYT article review information. I create a class for each object to facilitate the data caching and following data presentation. For this tree structure, I could link two data sources for detailed information, rating information and additional NYT review relationships.
5. Interaction and Presentation Plan:
When users search a movie she/he is interested in, the users can search by movie name, movie opening year, ranking range and additionally users can acquire the New York Times’ review articles url. Users could see the name of the movie. After that, users have the option to see detailed information and ranking information. Besides, the database can also provide review information which we collected from IMDb. This database can also provide users with movie-review articles from New York Times to see what critics say about this movie. 


