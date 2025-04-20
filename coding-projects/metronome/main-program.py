from tkinter import font
from tkinter import *
import pygame

# create the gui + name + size
root = Tk()
root.title('Jems41\'s Metronome')
root.geometry("640x560") #increase the window height, now able to see to the player options -linktr.ee/kp08
root.resizable(width=False, height=False) #disabling window adjusting -linktr.ee/kp08

pygame.init()
pygame.mixer.init()  # Initialize the mixer module.

sound1 = pygame.mixer.Sound('block-sound.wav')  # Load a sound.
sound2 = pygame.mixer.Sound('filler-sound.wav')

pause_btn_image = PhotoImage(file='play-button3.png')

control_panel = Frame(root)
control_panel.pack()

paused = True

METRONOME_INTERVAL = 500
beat_index = 0
beat_sequence = [sound1, sound2, sound2, sound2]

bpm_var = IntVar()

def change_bpm():
    global METRONOME_INTERVAL
    bpm = bpm_var.get()
    METRONOME_INTERVAL = round(60000 / bpm)
    bpm_var.set("")

def play_metronome():
    global beat_index
    if not paused:
        beat_sequence[beat_index].play()
        beat_index = (beat_index + 1) % len(beat_sequence)
        root.after(METRONOME_INTERVAL, play_metronome)

def play_sound():
    global paused
    
    paused = not paused
    change_icon(not paused)
    if not paused:
        play_metronome()

def change_icon(condition):
    global pause_btn_image
    if condition:
        pause_btn_image = PhotoImage(file='play-button3.png')
    else:
        pause_btn_image = PhotoImage(file='pause-button1.png')
    pause_btn.config(image=pause_btn_image)

pause_btn = Button(control_panel, image=pause_btn_image, borderwidth=0, command=play_sound)

enter_bpm = Label(control_panel, text='Enter BPM', font="Orbitron")
bpm_num = Entry(control_panel, textvariable=bpm_var, font="Orbitron")
bpm_var.set("150")

bpm_btn = Button(control_panel, command=change_bpm, text='Confirm BPM', font="Orbitron")

bpm_num.grid(row=1, column=1, padx=7, pady=9)
pause_btn.grid(row=2, column=1, padx=7, pady=9)
enter_bpm.grid(row=0, column=1, padx=7, pady=9)
bpm_btn.grid(row=1, column=2, padx=7, pady=9)

root.mainloop()