import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Initialize the mixer (if you are using sound)
pygame.mixer.init()

# List of songs
songs = ["song1.mp3", "song2.wav", "song3.wav"]

# Set the custom event for when the song ends
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Function to play the next song
def play_next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index >= len(songs):
        current_song_index = 0  # Loop back to the first song
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

# Initialize variables
current_song_index = 0
pygame.mixer.music.load(songs[current_song_index])
pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SONG_END:
            play_next_song()