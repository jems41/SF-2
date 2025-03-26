from tkinter import filedialog
from tkinter import *
import pygame
import os
import random

# create the gui + name + size
root = Tk()
root.title('Jems41\'s Music Player')
root.geometry("640x560") #increase the window height, now able to see to the player options -linktr.ee/kp08
root.resizable(width=False, height=False) #disabling window adjusting -linktr.ee/kp08

# import the pygame sound system
pygame.init()
pygame.mixer.init()

# add a menubar to the root window
menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False
shuffled = False

# event create something idk had to google this
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

def load_song():
    global current_song, scale, songlist, songs
    root.directory = filedialog.askdirectory()
    
    songlist.delete(0, 'end')  # Clear the Listbox if there's already songs added
    songs.clear()
    

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".wav" or ext == ".mp3" or ext == ".ogg": #ogg update! -linktr.ee/kp08
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)
    
    if songs:
        songlist.selection_set(0) # selecting first song at the top of the song list
        current_song = songs[songlist.curselection()[0]] # set the current song to the song that selected in the song list
        pygame.mixer.music.load(os.path.join(root.directory, current_song)) # constructs the full file path
        pygame.mixer.music.play() # play the song
    check_next_song()

def pause_song():
    global paused

    if not paused:
        pygame.mixer.music.pause()
        paused = True
        change_icon(True)
    else:
        pygame.mixer.music.unpause()
        paused = False
        change_icon(False)

    check_next_song()

def next_song():
    global current_song, paused
    change_icon(False)
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
    except:
        songlist.selection_clear(0, END)
        songlist.selection_set(0)
        current_song = songs[songlist.curselection()[0]]

    pygame.mixer.music.load(os.path.join(root.directory, current_song))
    pygame.mixer.music.play()
    paused = False
    check_next_song()

def prev_song():
    global current_song, paused
    change_icon(False)
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
    except:
        songlist.selection_clear(0, END)
        songlist.selection_set(len(songs) - 1)
        current_song = songs[songlist.curselection()[0]]

    pygame.mixer.music.load(os.path.join(root.directory, current_song))
    pygame.mixer.music.play()
    check_next_song()

def random_song():
    global current_song, index_songs, shuffled, paused
    if index_songs: # verifies if there are songs in the list
        random_index = index_songs.pop(0) # get the first song in the randomized list
        
        songlist.selection_clear(0, END)
        songlist.selection_set(random_index)
        current_song = songs[songlist.curselection()[0]]
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pause_song()
        shuffled = False
        paused = True
        change_icon2(False)

# change image of play/resume button
def change_icon(condition):
    global pause_btn_image
    if condition:
        pause_btn_image = PhotoImage(file='play-button3.png')
    else:
        pause_btn_image = PhotoImage(file='pause-button1.png')
    pause_btn.config(image=pause_btn_image)

# change image of shuffle button
def change_icon2(condition):
    global shuffle_btn_image
    if condition:
        shuffle_btn_image = PhotoImage(file='shuffleselected.png')
    else:
        shuffle_btn_image = PhotoImage(file='shuffle.png')
    shuffle_btn.config(image=shuffle_btn_image)

# getting value of volume
def change_volume():
    volume = scale.get()
    pygame.mixer.music.set_volume(volume/10)

# shuffles the songs (similar to pause_song)
def toggle_random_song():
    global shuffled, index_songs
    if not shuffled:
        shuffled = True
        change_icon2(True)  # Update shuffle button icon to indicate shuffle mode
        index_songs = list(range(len(songs)))
        random.shuffle(index_songs) # [1, 0, 2]
    else:
        shuffled = False
        change_icon2(False) 

organise_menu = Menu(menubar, tearoff=False) # creating an organise menu
organise_menu.add_command(label='Select Folder', command=load_song) # add a command to the menu
menubar.add_cascade(label='Import', menu=organise_menu) # display it

# adding a songlist
songlist = Listbox(root, bg='#18363E', fg= 'white', width=102, height=25)
songlist.pack()

# importing all the images
pause_btn_image = PhotoImage(file='pause-button1.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='previous.png')
shuffle_btn_image = PhotoImage(file='shuffle.png')

# adding a widget at the bottom for the controls
control_panel = Frame(root)
control_panel.pack()

# creating a button for the image
pause_btn = Button(control_panel, image=pause_btn_image, borderwidth=0, command=pause_song)
next_btn = Button(control_panel, image=next_btn_image, borderwidth=0, command=next_song)
prev_btn = Button(control_panel, image=prev_btn_image, borderwidth=0, command=prev_song)
scale = Scale(control_panel, from_=0, to=10, orient="horizontal", label='Volume')
volume_btn = Button(control_panel, text='Update Volume', command=change_volume)
shuffle_btn = Button(control_panel, image=shuffle_btn_image, borderwidth=0, command=toggle_random_song)

# adding it to the root
pause_btn.grid(row=0, column=1, padx=7, pady=10)
next_btn.grid(row=0, column=2, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)
scale.grid(row=0, column=4, padx=7, pady=10, in_=control_panel)
volume_btn.grid(row=0, column=5, padx=7, pady=10)
shuffle_btn.grid(row=0, column=3, padx=7, pady=10)
scale.set(10)

def check_next_song():
    global paused

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            root.destroy()
            pygame.quit()
            return
        elif event.type == SONG_END:
            if shuffled:
                random_song()
            else:
                next_song()

    if paused:
        return

    root.after(100, check_next_song)

root.mainloop()

pygame.quit()