from tkinter import *


FONT = ("Century Gothic", 10, "normal")



window = Tk()
window.minsize(width=500, height=500)
window.title("Password Manager")
window.config(padx=100, pady=100)

logo = PhotoImage(file ="./logo.png")

canvas = Canvas(height=250, width=189, highlightthickness=0)
canvas.create_image(125,100, image =logo)
canvas.grid(row=0, column=1)

# LABELS-------------------------------
website_label = Label(text="Website", font=FONT)
website_label.grid(row =1, column=0,columnspan=1)
username_label = Label(text="Email/Username", font=FONT)
username_label.grid(row=2,column=0,columnspan=1)
password_label = Label(text="Password", font=FONT)
password_label.grid(row=3,column=0,columnspan=1)

# ENTRIES ------------------------------------
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(width=45)
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1, columnspan=1)

# BUTTONS----------------------------
generate_password_button = Button(text= "Generate Password", width=15)
generate_password_button.grid(row=3,column=2, columnspan=1)

add_button = Button(width=40, text="Add")
add_button.grid(row=4, column=1, columnspan=2)








window.mainloop()