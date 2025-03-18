from tkinter import *
import pygame
import os

# create the gui + name + size
root = Tk()
root.title('Jspect\'s Music Player')
root.geometry("640x480")

# import the pygame sound system
pygame.mixer.init()
sound = pygame.mixer.Sound('example.wav')
sound.play() 

# add a menubar to the root window
menubar = Menu(root)
root.config(menu=menubar)

organise_menu = Menu(menubar, tearoff=False) # creating an organise menu
organise_menu.add_command(label='Select Folder') # add a command to the menu
menubar.add_cascade(label='Organise', menu=organise_menu) # display it

# adding a songlist
songlist = Listbox(root, bg='#18363E', fg= 'white', width=102, height=25)
songlist.pack()

# importing all the images
play_btn_image = PhotoImage(file='play-button3.png')
pause_btn_image = PhotoImage(file='pause-button1.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='previous.png')

# adding a widget at the bottom for the controls
control_panel = Frame(root)
control_panel.pack()

# creating a button for the image
play_btn = Button(control_panel, image=play_btn_image, borderwidth=0)
pause_btn = Button(control_panel, image=pause_btn_image, borderwidth=0)
next_btn = Button(control_panel, image=next_btn_image, borderwidth=0)
prev_btn = Button(control_panel, image=prev_btn_image, borderwidth=0)

# adding it to the root
play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop() # main code to display a screen
