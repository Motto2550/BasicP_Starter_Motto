def show_movies(movie_list):
    print(movies)

movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]


menu = int(input("Type 1 to get movie list / Type 2 to buy ticket : "))
if menu == 1 :
    print(movies)
    moviechoose = str(input("Which movie do you want to watch? : "))
    if moviechoose == ("Avengers Endgame"):
        movie_name = ("Avengers Endgame")
        ticket_price = 300
        Genre = ("Action")
        age_restriction = 13
    if moviechoose == ("Inception"):
        movie_name = ("Inception")
        ticket_price = 300
        Genre = ("Scifi")
        age_restriction = 13
    if moviechoose == ("It"):
        movie_name = ("It")
        ticket_price = 300
        Genre = ("Horror")
        age_restriction = 18
    if moviechoose == ("The Notebook"):
        movie_name = ("The Notebook")
        ticket_price = 300
        Genre = ("Romantic")
        age_restriction = 13
    if moviechoose == ("Harry Potter and the Sorcerer\'s Stone"):
        movie_name = ("Harry Potter and the Sorcerer\'s Stone")
        ticket_price = 300
        Genre = ("Fantasy")
        age_restriction = ("G")
    print(movie_name,ticket_price,Genre,"Age :",age_restriction)
