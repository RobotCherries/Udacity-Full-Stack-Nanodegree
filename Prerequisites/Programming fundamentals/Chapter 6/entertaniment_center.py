import media
import fresh_tomatoes
import media

# Movies
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')

avatar = media.Movie('Avatar',
                        'A marine on an alien planet',
                        'https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg',
                        'https://www.youtube.com/watch?v=-9ceBgWV8io')

school_of_rock = media.Movie('School of Rock',
                    'Using rock music to learn',
                    'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                    'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille',
                    'A rat is a chef in Paris',
                    'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                    'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in Paris',
                    'Going back in time to meet authors',
                    'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                    'https://www.youtube.com/watch?v=atLg2wQQxvU')

hunger_games = media.Movie('Hunger Games',
                    'A really real reality show',
                    'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                    'https://www.youtube.com/watch?v=PbA63a7H0bo')


# Calls
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# fresh_tomatoes.open_movies_page(movies)