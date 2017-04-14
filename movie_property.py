class Movie():
    """
        Movie:

        members:
        title: string. This contains the title of the movie

        poster_image_url: string. This contains the url to the poster of the
        movie.

        trailer_youtube_url: string. This contains the url to movie trailer
        in youtube.

        movie_desc: string. This contains a brief description of the movie.
    """
    
    def __init__(self, title, image_url, youtube_url, movie_desc):
        """This is the constructor which creates a memory
        space for each movie"""
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url
        self.movie_desc = movie_desc
