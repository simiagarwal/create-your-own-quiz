# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Story about a boy and his toys",
	"http://cdn23.us2.fansshare.com/photos/toystory3/toy-story-movie-wallpaper-movies-1531204103.jpg",
	"https://www.youtube.com/watch?v=4KPTXpQehio")

#avatar = media.Movie()

#movies = [toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
#print toy_story.storyline
johda_akbhar = media.Movie("Johda Akbhar", "Story about a mogul king and his wife",
	            "http://media1.santabanta.com/full1/Bollywood%20Movies/Jodhaa%20Akbar/jod4v.jpg",
	            "https://www.youtube.com/watch?v=5B_X2xOBpFc")
#JohdaAkbhar.show_trailer()

sholay = media.Movie("Sholay","Strory about friendship","http://hdmoviespoint.com/wp-content/uploads/2014/10/Sholay-Movie-Free-HD-Download.jpg",
	     "https://www.youtube.com/watch?v=ci_VNqzCa-Y")
veer_zara = media.Movie("Veer Zara","Love Story","http://www.romanceeternal.org/REimages/VZDVD.jpg",
	"https://www.youtube.com/watch?v=OSaVImLnnsw")

lamhe = media.Movie("Lamhe","A Love story","http://www.brns.com/bollywood/picts1/lamhe1.jpg",
	"https://www.youtube.com/watch?v=oPGyikebbn8")
skyfall=media.Movie("Skyfall","Bond Movie","https://41.media.tumblr.com/cd84e188e28440e1782e498fea79f4ab/tumblr_nla7hoUXLO1s80h8lo1_500.jpg",
	"https://www.youtube.com/watch?v=6kw1UVovByw")
spectre = media.Movie("Spectre","Bond Movie","http://www.007.com/wp-content/uploads/2015/02/FIRST-LOOK_post.jpg",
	"https://www.youtube.com/watch?v=LTDaET-JweU")

movies =[toy_story,johda_akbhar,sholay,veer_zara,lamhe,skyfall,spectre]
fresh_tomatoes.open_movies_page(movies)



