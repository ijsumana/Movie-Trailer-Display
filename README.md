# Movie-Trailer-Display
There are 3 files for this project:
  1. movie_property.py
  2. movie_list.py
  3. fresh_tomatoes.py

I am providing a brief description of the contents of the file below.

1. movie_property.py: 
This file contains the Movie class and the members of a movie, such as, movie title, movie poster URL, movie trailer 
URL in youtube.com and movie story line in the "movie_desc" memebr of the Movie class. This class is used to create all the movie instances
in movie_list.py file.

2. movie_list.py:
This file contains the details of each movie. It creates a single instance of Movie class for each movie. Each movie contains the following 
properties:
        i) title,
        ii) poster_url,
        iii) youtube_tralier_url,
        iv) description.
At the end of the file all the movie instances are used to create an array of movies so that it can be sent to the fresh_tomatoes.py to create
the movie trailer website. there is a function called "open_movies_page" which takes this movies as input and apply different bootstrap styling 
with JS for rendering.

3. fresh_tomatoes.py:
This file is used to display all the movies created in movie_list.py in a web page. In addition to the content of this file, I have added 
the followings:
    1. a tooltip text for each movie that shows the storyline (movie_desc member of the Movie class in movie_property.py) of the movie when
    mouse pointer is over the poster image of a movie.
    2. After clicking the movie poster image I have changed the background color to yellow so that the viewer can track which movie trailer 
    s/he has viewed already.

To run the program one needs to open the movie_list.py in Python IDLE and run it.
The generated output file "Movie Trailer.html" is also included in this project to show the outcome of the project.
