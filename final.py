import json
import os
import IMDb_top250_movie as imdb


def check_cache_file():
    '''
        Check if the cache file exists.
            Parameters:
                None
            Returns:
                None
    '''
    if os.path.exists("Combined_top250_movie.json"):
        print("Cache file exists: Yes")
    else:
        print("Cache file exists: No")
        print("Please wait for the cache file to be created.")
        imdb_list = imdb.save_movie_data_form_imdb()
        imdb.save_movie_data_form_imdb(imdb_list)
        print("Cache file created.")

def save_to_watchlist(movie: dict):
    '''
        Save the movie to favorite list.
            Parameters: movie: the movie json file
            Returns: None
    '''
    with open("watchlist.json", 'a') as f:
        f.write(json.dumps(movie, indent=4))
    print("Movie saved to favorite.")


def search_movie_name(movie_name, movie):
    '''
        Perform a movie name search.
            Parameters:
                movie_name: the movie name to be searched
                movie: the movie json file
            Returns:
                movie_name_list: the list of movies that match the movie name
    '''
    name_list = []
    for i in range(0, len(movie)):
        name_list.append(movie[i]['name'].lower())
    match_list = [j for j in name_list if movie_name.lower() in j]
    for k in match_list:
        print("Found: " + k.title())
    movie_name_list = [p for p in movie if p['name'].lower() in match_list]
    return movie_name_list

def search_movie_year(year, movie):
    '''
        Perform a movie year search.
            Parameters:
                movie: the movie json file
                year: the movie year to be searched
            Returns:
                movie_year_list: the list of movies that match the movie year
    '''
    movie_year_list = []
    for i in range(0, len(movie)):
        if year in movie[i]['detail info']['year'].lower():
            movie_year_list.append(movie[i])
    for j in movie_year_list:
        print("Name: {} ({})".format(j['name'], j['detail info']['year']))
    return movie_year_list

def movie_ranking_search(lower, upper, movie):
    '''
        Perform a movie ranking search.
            Parameters:
                movie: the movie json file
                lower: the lower bound of the movie ranking to be searched
                upper: the upper bound of the movie ranking to be searched
            Returns:
                movie_ranking_list: the list of movies that match the movie ranking
    '''
    movie_ranking_list = []
    for index in range(lower-1, upper):
        movie_ranking_list.append(movie[index])
    for i in movie_ranking_list:
        print("Name: {} ({})".format(i['name'], i['rating info']['ranking']))
    return movie_ranking_list

def search_movie_review_by_name(movie_name, combined):
    '''
        Perform a movie review search.
            Parameters:
                movie_name: the movie name to be searched
                combine: the movie json file
            Returns:
                match_list: the review of movies that match the movie name
    '''
    name_list = []
    for i in range(0, len(combined)):
        name_list.append(combined[i])

    match_list = [j for j in name_list if movie_name.lower() in j['name'].lower()]
    for k in match_list:
        for j in k['review']:
           print("Name: {} ({})".format(k['name'], j['link']['url']))
    return match_list

def movie_review_menu(combined):
    '''
        Perform a movie name search.
            Parameters:
                movie_json: the movie json file
            Returns:
                movie_list: the list of movies that match the movie name
    '''
    movie_name = input("Please enter the movie name: ").lower()
    first_result = search_movie_review_by_name(movie_name, combined)
    if first_result == [] or first_result == None:
        choice = input("No result found. \nDo you want to search another name? [Y/N]").lower()
        if choice == 'y':
            movie_name2 = input("Please enter another movie name: ").lower()
            second_result = search_movie_review_by_name(movie_name2, combined)
            if second_result == [] or second_result == None:
                print("No result found.")
                input("Press Enter to continue...")
            else :
                save_choice = input("Do you want to save those movie to your watchist? [Y/N]")
                if save_choice == 'y':
                    save_to_watchlist(second_result)
                    input("Press Enter to continue...")
    elif first_result != None:
            save_choice = input("Do you want to save this movie to your watchlist? [Y/N]")
            if save_choice == 'y':
                    save_to_watchlist(first_result)
            input("Press Enter to continue...")

def movie_year_menu(combined):
    '''
        Perform a movie year search.
            Parameters:
                movie: the movie json file
            Returns:
                movie_list: the list of movies that match the movie year
    '''
    year = input("Please enter the movie year: ").lower()
    first_result = search_movie_year(year, combined)
    if first_result == [] or first_result == None:
        choice = input("No result found. Do you want to search another year? [Y/N]").lower()
        if choice == 'y':
            year2 = input("Please enter the movie year: ").lower()
            second_result = search_movie_year(year2, combined)
            if second_result == [] or second_result == None:
                print("No result found in another source, sorry.")
                input("Press Enter to continue...")
            else :
                save_choice = input("Do you want to save those movie to your watchlist? [Y/N]")
    elif first_result != None:
            save_choice = input("Do you want to save this movie to your watchlist? [Y/N]")
            if save_choice == 'y':
                    save_to_watchlist(first_result)
            input("Press Enter to continue...")

def movie_name_menu(combined):
    '''
        Perform a movie name search.
            Parameters:
                movie_json: the movie json file
            Returns:
                movie_list: the list of movies that match the movie name
    '''
    movie_name = input("Please enter the movie name: ").lower()
    first_result = search_movie_name(movie_name, combined)
    if first_result == [] or first_result == None:
        choice = input("No result found. Do you want to search another name? [Y/N]").lower()
        if choice == 'y':
            movie_name2 = input("Please enter the movie name: ").lower()
            second_result = search_movie_name(movie_name2, combined)
            if second_result == [] or second_result == None:
                print("No result found.")
                input("Press Enter to continue...")
            else :
                # print(json.dumps(second_result, indent=4))
                save_choice = input("Do you want to save those movie to your watchist? [Y/N]")
                if save_choice == 'y':
                    save_to_watchlist(second_result)
                    input("Press Enter to continue...")
    elif first_result != None:
            # print(json.dumps(first_result, indent=4))
            save_choice = input("Do you want to save this movie to your watchlist? [Y/N]")
            if save_choice == 'y':
                    save_to_watchlist(first_result)
            input("Press Enter to continue...")


def movie_ranking_menu(combined):
    '''
        Perform a movie ranking search.
            Parameters:
                movie_json: the movie json file
            Returns:
                movie_list: the list of movies that match the movie ranking
    '''
    upper = int(input("Please enter the higher ranking, want to search 1- 5, enter upper 5: "))
    lower = int(input("Please enter the lower ranking, want to search 1- 5, enter lower 1: "))
    first_result = movie_ranking_search(lower, upper, combined)
    if first_result == [] or first_result == None:
        choice = input("No result found. Do you want to search again in another source? [Y/N]").lower()
        if choice == 'y':
            second_result = movie_ranking_search(lower, upper, combined)
            if second_result == [] or second_result == None:
                print("No result found in another source, sorry.")
                input("Press Enter to continue...")
            else :
                save_choice = input("Do you want to save those movie to your watchlist? [Y/N]")
                if save_choice == 'y':
                    save_to_watchlist(second_result)
                    input("Press Enter to continue...")
    elif first_result != None:
            save_choice = input("Do you want to save this movie to your watchlist? [Y/N]")
            if save_choice == 'y':
                    save_to_watchlist(first_result)
            input("Press Enter to continue...")

def search_menu(json_file):
    '''
        Perform a search.
            Parameters:
                json_one: the movie json file
                json_two: the movie json file
            Returns:
                None
    '''
    print("Please enter the Search Preference:")
    print("1. Search by Movie Name in Top 250 Movies")
    print("2. Search by Movie Year in Top 250 Movies")
    print("3. Search by Ranking Range in Top 250 Movies")
    print("4. Search Review by Movie Name in Top 250 Movies")
    print("5. Back to home")
    while True:
        try:
            search_preference = int(input("Please enter the number you want: "))
            if search_preference < 1 or search_preference > 5:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    if search_preference == 1:
        movie_name_menu(json_file)
    if search_preference == 2:
        movie_year_menu(json_file)
    if search_preference == 3:
        movie_ranking_menu(json_file)
    if search_preference == 4:
        movie_review_menu(json_file)
    if search_preference == 5:
        return


def main():
    '''
        The main function.
    '''
    print("Welcome to IMDb+ New York Times Movie Reviewer!")
    print("The Movie Reviewer is an application that combine the movie's information with NYT critical articles.")
    print("Check if the cache file exist.")
    check_cache_file()
    imdb_json = json.load(open("Combined_top250_movie.json"))
    
    while True:
        print("Please select :")
        print("1. Search")
        print("2. Exit")
        source = input("Please enter the number you like: ")
        if source == '1':
            search_menu(imdb_json)
        elif source == '2':
            print("Thank you for using the Movie Reviewer!")
            return
        else:
            print("Please enter a valid number.")


if __name__ == '__main__':
     main()