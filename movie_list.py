import movie_property
import fresh_tomatoes

"""
    This file contains the details of each movie. It creates a single instance
    of Movie class for each movie in movie_property file.
    Each movie contains the following properties inside the function
    'movie_property.Movie'(from top to bottom).
        title,
        poster_url
        youtube_tralier_url
        description
"""

#creating instances of my favorite movies

ratatouille = movie_property.Movie(
                "Ratatouille",
                "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",
                "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                "This is an amazing movie where a rat can cook awesome meals. He was" \
                " the best chef in paris after the owner died.");

a_walk_in_the_clouds = movie_property.Movie(
                "A Walk In The Clouds",
                "http://static.tvgcdn.net/rovi/showcards/movie/130837/thumbs/16977680_1300x1733.jpg",
                "https://www.youtube.com/watch?v=cULvtpaIK9I",
                "A Walk in the Clouds is a 1995 American romantic drama.It is" \
                " about a young soldier returning home from World War II who is" \
                " looking to settle down and start a family with the woman he" \
                " impulsively married just before enlisting. After learning" \
                " she is not what he imagined her to be, he heads north alone" \
                " to Sacramento in search of work. Along the way he meets a" \
                " beautiful young woman who is heading home from college to" \
                " her family vineyard to help with the grape harvest. When he" \
                " learns she is pregnant and was abandoned by her boyfriend," \
                " he offers to stand in as her husband.");
        

frozen = movie_property.Movie(
                "Frozen",
                "https://images-na.ssl-images-amazon.com/images/I/A1BJgyIPnrL._SY445_.jpg",
                "https://www.youtube.com/watch?v=TbQm5doF_Uc",
                "This is an amazing story of true love of sisters.");

kungfu_panda = movie_property.Movie(
                "Kungfu Panda",
                "http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",
                "https://www.youtube.com/watch?v=PXi3Mv6KMzY",
                "The story is about a panda becoming a dragon warrior. Awesome way to" \
                " teach him kungfu.");

shrek = movie_property.Movie(
                "Shrek",
                "http://t2.gstatic.com/images?q=tbn:ANd9GcS_OkJKQ6ZpDV_xhC0L9zyHEcKMlV9x3Q30LF6MOE0nV1U6r09p",
                "https://www.youtube.com/watch?v=W37DlG1i61s",
                "Once upon a time, in a far away swamp, there lived an ogre" \
                " named Shrek (Mike Myers) whose precious solitude is suddenly" \
                " shattered by an invasion of annoying fairy tale characters." \
                " They were all banished from their kingdom by the evil Lord" \
                " Farquaad (John Lithgow). Determined to save their home -- not" \
                " to mention his -- Shrek cuts a deal with Farquaad and sets out" \
                " to rescue Princess Fiona (Cameron Diaz) to be Farquaad's bride." \
                " Rescuing the Princess may be small compared to her deep, dark" \
                " secret.");

angry_birds = movie_property.Movie(
                "The Angry Birds Movie",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcTL4cM7wCCXjCEoxmzvs_vmiQtNqrpMQ80rgdjABG2_N-IEE-tp",
                "https://www.youtube.com/watch?v=1U2DKKqxHgE",
                "This movie shows how an agnry bird saved the lives of all birds in the" \
                " same community he used to live.");

hero = movie_property.Movie(
                "Big Hero 6",
                "http://vignette4.wikia.nocookie.net/big-hero-6/images/9/98/BH6_Hiro_and_Baymax_Poster.jpg/revision/latest?cb=20140611014857",
                "https://www.youtube.com/watch?v=rD5OA6sQ97M",
                "This is an amazing story of awesome invention of an elder" \
                " brother which saved him from danger even after he died of" \
                " an accident.");

moana = movie_property.Movie(
                "Moana",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
                "https://www.youtube.com/watch?v=LKFuXETZUsI",
                "How the heart of tefiti was stolen and how it was returned by" \
                " a brave girl Moana is the heart of this movie. Kids love it. ");

terminator2 = movie_property.Movie(
                "Terminator 2: Judgement Day",
                "http://t1.gstatic.com/images?q=tbn:ANd9GcS5J6Ay6y1UT7WAI4U7Zm2KDYITrvfOI3vmaCNdGhx_0jmWiI1d",
                "https://www.youtube.com/watch?v=7QXDPzx71jQ",
                "Amazing story of bonding between a terminator robot and a boy.");

#creating an array of movie instances which is required to feed into
#fresh_tomatoes.py to generate the movie web trailers
movies = [ratatouille, a_walk_in_the_clouds, frozen, kungfu_panda, shrek,
          angry_birds, hero, moana, terminator2]

#sending this movie array as a parameter to fresh_tomatoes.py so that we can
#see the movie trailer in the web
#fresh_tomatoes1.open_movies_page(movies)
fresh_tomatoes.open_movies_page(movies)
