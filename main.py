import pandas
from tkinter import *
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


try:
    file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("./data/polish_words.csv")


to_learn_dict = file.to_dict(orient="records")
current_card = {}


# ------------------------- KNOWN CLICK   ---------------------------- #


def known_click():
    to_learn_dict.remove(current_card)
    df = pandas.DataFrame(to_learn_dict)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# -------------------------FLIP CARD   ---------------------------- #


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back_img)

# -------------------------RANDOM FRENCH WORD   ---------------------------- #


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(card_title, text="Polish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Polish"], fill="black")
    flip_timer = window.after(3000, flip_card)


# -------------------------UI DESIGN ---------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263,text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=known_click)
button_right.grid(column=1, row=1)


next_card()



window.mainloop()
