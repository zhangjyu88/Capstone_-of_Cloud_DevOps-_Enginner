import media, fresh_tomatoes

toy_story = media.Movie("Toy Story 4",
                        "A story of a boy and his toys that come to life",
                        "https://m.media-amazon.com/images/M/MV5BMTYzMDM4NzkxOV5BMl5BanBnXkFtZTgwNzM1Mzg2NzM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE")
avatar = media.Movie("Avatar 2",
                     "A marine on an alien planet",
                     "https://m.media-amazon.com/images/M/MV5BNmM1NmY4N2QtNmVkOS00MjMyLWI5ZGUtYWYxMDRjY2MzNDdiXkEyXkFqcGdeQXVyMTAwMDAwMA@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=yUXd-enstO8")
frozen = media.Movie("Frozen II",
                             "Two sisters set out to find the origin of Elsa's powers in order to save their kingdom.",
                             "https://m.media-amazon.com/images/M/MV5BMjA0YjYyZGMtN2U0Ni00YmY4LWJkZTItYTMyMjY3NGYyMTJkXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_SY1000_SX675_AL_.jpg",
                             "https://www.youtube.com/watch?v=bwzLiQZDw2I")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chief in Paris",
                          "https://m.media-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
joker = media.Movie("Joker",
                                "A mentally-troubled comedian embarks on a downward spiral of revolution and bloody crime",
                                "https://m.media-amazon.com/images/M/MV5BNGVjNWI4ZGUtNzE0MS00YTJmLWE0ZDctN2ZiYTk2YmI3NTYyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=zAGVQLHvwOY")
hunger_games = media.Movie("The Hunger Games: Mockingjay",
                           "A really real reality show",
                           "https://m.media-amazon.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5BanBnXkFtZTgwNTAyMDQ5NjE@._V1_SY1000_CR0,0,657,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=n-7K_OjsDCQ")

movies = [toystory, avatar, frozen, ratatouille, joker, hungergames]
fresh_tomatoes.open_movies_page(movies)
