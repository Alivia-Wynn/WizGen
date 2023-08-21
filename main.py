import random
from tkinter import *
import tkinter as tk
import pygame
from PIL import ImageTk, Image
import math
pygame.mixer.init()

def play():
    pygame.mixer.music.load("magic1.mp3")
    pygame.mixer.music.play(loops=0)

def play_error():
    pygame.mixer.music.load("magic2.mp3")
    pygame.mixer.music.play(loops=0)

def output(num):
    my_canvas.create_image(10,0, image=new_image2, anchor='nw')
    my_canvas.create_text(500, 150, text="You're magic\nnumber is", font= "none 50 bold", fill="black", justify=CENTER)
    output = my_canvas.create_text(510, 250, text=num, font= "none 60 bold", fill="black")
    play()
    restart = Button(root, text="Restart", command=start)
    my_canvas.create_window(550, 300, anchor='e', window=restart)

def click():
    is_int = False
    entered_lower = answer1.get()
    entered_upper = answer2.get()
    my_canvas.delete('all')
    my_canvas.create_image(0,0, image=bg, anchor='nw')
    try:
        int(entered_lower)
        int(entered_upper)
        is_int = True
    except:
        try:
            float(entered_lower)
            float(entered_upper)
        except:
            my_canvas.create_image(10,0, image=new_image3, anchor='nw')
            my_canvas.create_text(530, 200, text="Please enter numbers\nbetween negative\nand positive infinity",
                                  font= "none 30 bold", fill="black", justify=CENTER)       
            retry = Button(root, text="Try Again!", command=start)
            my_canvas.create_window(550, 300, anchor='e', window=retry)
            play_error()
    if is_int:
        if int(entered_lower) > int(entered_upper):
            my_canvas.create_image(10,0, image=new_image3, anchor='nw')
            my_canvas.create_text(530, 200, 
                                  text="You entered an invalid range\nwhere the lower bound was higher\n than the upper bound.\nPlease enter a valid range", 
                                  font= "none 20 bold", fill="#000000", justify=CENTER)    
            retry = Button(root, text="Try Again!", command=error_start)
            my_canvas.create_window(550, 300, anchor='e', window=retry)
            play_error()
        else:
             magic_num = str(random.randint(int(entered_lower), int(entered_upper)))
             output(magic_num)
    else:
        if float(entered_lower) > float(entered_upper):
            my_canvas.create_image(10,0, image=new_image3, anchor='nw')
            my_canvas.create_text(530, 200, 
                                  text="You entered an invalid range\nwhere the lower bound was higher\n than the upper bound.\nPlease enter a valid range", 
                                  font= "none 20 bold", fill="#000000", justify=CENTER)    
            retry = Button(root, text="Try Again!", command=error_start)
            my_canvas.create_window(550, 300, anchor='e', window=retry)
            play_error()
        else:
             magic_num = str((random.uniform(float(entered_lower), float(entered_upper))))[:4]
             output(magic_num)
    
   
    

def start():
   
    my_canvas.delete('all')
    my_canvas.create_image(0,0, image=bg2, anchor='nw')
    my_canvas.create_image(10,0, image=new_image, anchor='nw')
    question1 = my_canvas.create_text(501, 100, text="Minimum Value:",
                                       font= "none 20 bold", fill="#000000")
    my_canvas.create_window(620, 130, anchor='e', window=answer1)

    question2 = my_canvas.create_text(508, 200, text="Maximum Value:", 
                                      font= "none 20 bold", fill="#000000")
    my_canvas.create_window(620, 230, anchor='e', window=answer2)
    
    my_canvas.create_window(550, 300, anchor='e', window=submit)
    answer1.delete(0, END)
    answer2.delete(0, END)

def error_start():
   
    my_canvas.delete('all')
    my_canvas.create_image(0,0, image=bg2, anchor='nw')
    my_canvas.create_image(10,0, image=new_image, anchor='nw')
    question1 = my_canvas.create_text(501, 100, text="MINIMUM Value:", font= "none 20 bold", fill="black")
    my_canvas.create_window(620, 130, anchor='e', window=answer1)

    question2 = my_canvas.create_text(508, 200, text="MAXIMUM Value:", font= "none 20 bold", fill="black")
    my_canvas.create_window(620, 230, anchor='e', window=answer2)
    
    my_canvas.create_window(560, 300, anchor='e', window=submit)
    answer1.delete(0, END)
    answer2.delete(0, END)


root =Tk()
root.title("🧙‍♂️WizGen: Magic Number Generator")
root.geometry('700x400')
root.resizable(width=False, height=False)
# initialise pygame
pygame.mixer.init()

#define images
bg = PhotoImage(file="bg.png")
image_obj = Image.open('wiz1.png')
    #resize the image or else it will be blown up
resized = image_obj.resize((300,400))
new_image = ImageTk.PhotoImage(resized)

bg2 = PhotoImage(file="bg2.png")


image2_obj = Image.open('wiz2.png')
    #resize the image or else it will be blown up
resized2 = image2_obj.resize((300,400), Image.Resampling.LANCZOS)
new_image2 = ImageTk.PhotoImage(resized2)

image3_obj = Image.open('wiz_err.png')
    #resize the image or else it will be blown up
resized3 = image3_obj.resize((300,400), Image.Resampling.LANCZOS)
new_image3 = ImageTk.PhotoImage(resized3)

##Create Canvas
my_canvas = Canvas(root, width=700, height=400)
my_canvas.pack(fill="both", expand=True)

#put the image in the cavas
my_canvas.create_image(0,0, image=bg, anchor='nw')
my_canvas.create_image(10,0, image=new_image, anchor='nw')


#add a label
text1= my_canvas.create_text(510, 200, text="I am the Random Wizard,\nhere to help you \npick a random number!", 
                            font= "none 29 bold", fill="#000000", justify="center")

start_button = Button(root, text="Start", command=start, bg=None)
button1 = my_canvas.create_window(550, 300, anchor='e', window=start_button)
#button_window = my_canvas.create_window(550, 300, anchor="e", window=start_button)
#render_image('wizard1.png', my_canvas)




'''Question page'''
'''defined here so that the click function has access'''
answer1 = Entry(root, width=20, bg="white", fg="#3B2C2C")
answer2 = Entry(root, width=20, bg="white", fg="#3B2C2C")
submit= Button(root, text="Submit", command=click)





root.mainloop()
