from tkinter import *
from password_generator import generate_password
from tkinter import messagebox
FONT = ("Century Gothic", 10, "normal")

def gen_pass():
    password_entry.delete(0,END)
    password_entry.insert(0,generate_password())


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    

    if len(website)==0 or len(username) ==0 or len(password) ==0:
        messagebox.showinfo(title="Invalid fields",message="Some fields are mepty")
    else:
        output = messagebox.askyesno(title=website, message=f"These are the details entered for {website}\n username/email: {username} \n password: {password}\n Are you sure you want to continue?")
        if output:
            with open("data.txt","a") as data:
                data.write(f"{website} | {username} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


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
website_entry = Entry(width=45, font=FONT)
website_entry.grid(row=1, column=1, columnspan=2)

username_entry = Entry(width=45, font=FONT)
username_entry.insert(0, "nzfishrak60@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=28, font=FONT)
password_entry.grid(row=3, column=1, columnspan=1)

# BUTTONS----------------------------
generate_password_button = Button(text= "Generate Password", width=15,command=gen_pass)
generate_password_button.grid(row=3,column=2, columnspan=1)

add_button = Button(width=45, text="Add", command = save)
add_button.grid(row=4, column=1, columnspan=2)








window.mainloop()