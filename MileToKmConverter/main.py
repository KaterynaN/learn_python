from tkinter import *
window = Tk()
window.title("Miles To Km Converter")
window.minsize(250, 200)
window.config(padx=20, pady=50)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

label = Label(text="0")
label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

def convert():
    km = float(mile_input.get()) * 1.609
    label.config(text=f"{round(km, 2)}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()