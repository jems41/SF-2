def validation(lst_songs):
    valid_songs = []

    for song in lst_songs:
        try:
            song_name = song.split(".")
            if song_name[1] in ["mp3", "wav", "ogg"]:
                valid_songs.append(song)
            else:
                print(f"Invalid file extension: {song}")
        except IndexError:
            print(f"Missing extension: {song}")
    return valid_songs