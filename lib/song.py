class Song:
    # Class attributes
    count = 0
    genres = set()    # Track all unique genres
    artists = set()   # Track all unique artists
    genre_count = {}  # Track count of songs for each genre
    artist_count = {} # Track count of songs for each artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the total count of songs
        Song.count += 1

        # Add the genre and artist to their respective sets
        Song.genres.add(genre)
        Song.artists.add(artist)

        # Update the genre_count dictionary
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update the artist_count dictionary
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
