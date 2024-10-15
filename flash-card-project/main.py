from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    row_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    row_data = pandas.read_csv("data/french_words.csv")
finally:
    data = row_data.to_dict(orient="records")

current_card = None


# french_english_list = [{dict_item["French"]: dict_item["English"]} for dict_item in data]
#
# nato_dict = [{row["French"]: row["English"]} for (index, row) in row_data.iterrows()]

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=f"{current_card["French"]}", fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=f"{current_card["English"]}", fill='white')


def remove_card():
    global current_card
    data.remove(current_card)
    df = pandas.DataFrame(data)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 163, text="", font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 293, text="", font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, bd=0, command=remove_card)
right_btn.grid(column=1, row=1)

next_card()
window.mainloop()
