from tkinter import *
from password_generator import generate_password
from tkinter import messagebox
import json
import pyperclip
FONT = ("Century Gothic", 10, "normal")


def search():
    """
    Searches for a given website if in the json file it shows the message box  with the corresponding password and user name with the password copied to the clipboard
    If not found it shows an error message box
    """
    searched_value = website_entry.get()
    with open("data.json", "r") as data:
        data_dict: dict = json.load(data)

        # data_dict = {key:val for (key,val) in data_dict.items() if key ==searched_value}
        retrieved_value:dict = data_dict.get(searched_value)
        if retrieved_value is not None:
            messagebox.showinfo(title="Your credentials", message=f"Username: {retrieved_value['username']}\n Password: {retrieved_value['password']}")
            pyperclip.copy(retrieved_value['password'])
        else:
            messagebox.showinfo(title="Info Not Found", message=f"Credentials for {searched_value} doesn't exist")

def gen_pass():
    """
    Generates a password in the password entry field
    """
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())


def save():
    """
    Saves the data inserted to the json file and clears the entry boxes
    """
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "username": username,
        "password": password
    }}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid fields",
                            message="Some fields are mepty")
    else:
        output = messagebox.askyesno(
            title=website, message=f"These are the details entered for {website}\n username/email: {username} \n password: {password}\n Are you sure you want to continue?")
        if output:

            try: #Trying to open the json file if it exists
                with open("data.json", 'r') as data:
                    data_dict: dict = json.load(data) # loads ther json data as a dict
                    data_dict.update(new_data) # adds a new element to the dict
                with open("data.json", 'w') as data: #Write Mode needed to dump
                    json.dump(data_dict,data,indent=4) # overrides the old json file with the new updated dict (json equivalent format)

            except FileNotFoundError: # If file isn't found we create a json file and add the data to it
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk() #Creating root window
window.minsize(width=500, height=500) # Setting minimum size of the window
window.title("Password Manager") #Setting window title
window.config(padx=100, pady=100) # Added padding to window

logo = PhotoImage(file="./logo.png") #created a photoImage object from a raw photo file



###Creating a canvas and added an image to appx the centre of the canvas
canvas = Canvas(height=250, width=189, highlightthickness=0)
canvas.create_image(125, 100, image=logo)
canvas.grid(row=0, column=1) #Positioned the canvas using tkinter grid convention

# LABELS-------------------------------
website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0, columnspan=1)
username_label = Label(text="Email/Username", font=FONT)
username_label.grid(row=2, column=0, columnspan=1)
password_label = Label(text="Password", font=FONT)
password_label.grid(row=3, column=0, columnspan=1)

# ENTRIES ------------------------------------
website_entry = Entry(width=28, font=FONT)
website_entry.grid(row=1, column=1, columnspan=1)

username_entry = Entry(width=45, font=FONT)
username_entry.insert(0, "nzfishrak60@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=28, font=FONT)
password_entry.grid(row=3, column=1, columnspan=1)

# BUTTONS----------------------------
generate_password_button = Button(
    text="Generate Password", width=15, command=gen_pass)
generate_password_button.grid(row=3, column=2, columnspan=1)

add_button = Button(width=45, text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, columnspan=1)


window.mainloop()
