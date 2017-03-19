import media
import fresh_tomatoes
import sys,os

"""This will read the input from a text file
   parse the text file to create Movies and
   then generate the webpage"""

#this helps to use relative paths in the program
sys.path.append(os.path.realpath('..'))
movies = []

#read all the lines into a list
with open('./movie_details.txt') as f:
    lines = f.readlines()

#parse these lines and create new movie for each line
for line in lines:
    content = line.split("###")
    new_movie = media.Movie(content[0], content[1], content[2], content[3])
    movies.append(new_movie) #append new movie to the list

#generate the webpage using the data that is parsed previously
fresh_tomatoes.open_movies_page(movies)
