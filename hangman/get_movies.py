from bs4 import BeautifulSoup
import requests

def get():
    source = requests.get("https://www.empireonline.com/movies/features/500-greatest-movies/").text
    soup = BeautifulSoup(source,'html5lib')
    all_movies = soup.find_all('h2')
    file = open("movies.txt","wt")
    for movie in all_movies:
        if movie == all_movies[0]:
            continue
        movie = movie.text.split(' ',1)
        movie = movie[1]
        movie = movie.split('(',1)
        print(movie[0])
        try:
            file.write(movie[0]+"\n")
        except:
            continue
    file.close()
        
if __name__=='__main__':
    get()
