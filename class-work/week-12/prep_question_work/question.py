'''
Type: Long Answer
Topic: Exceptions

You're given a list of song file names in the format shown below. Your task is to 
write a function called validation that takes a parameter lst_songs and checks 
whether each file has a valid audio extension. The function should return a new 
list called valid_songs that contains only the correctly formatted audio files. The 
correct file extensions to play audio are ".mp3", ".wav", and ".ogg" files. 

To handle invalid songs, you must:
- Use exception handling ONLY to deal with file names that are missing an 
extension, and print to the user in the format: "Missing Extension: <song_name>".

- If a file has an extension but it is incorrect, like (".txt", ".mp4") you 
cannot use exceptions, and also print to the user in the format:
"Invalid file extension: <song_name>".

INPUT:
lst_songs = ["track1.mp3", "track2.wav", "track3.txt", "track4", "track5.ogg"]

OUTPUT:
Invalid file extension: track3.txt
Missing extension: track4
["track1.mp3", "track2.wav"]
'''