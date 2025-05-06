import random
from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    input_password.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=150,pady=100)

canvas = Canvas(width = 300, height = 224, highlightthickness = 0)
lockImg = PhotoImage(file="logo.png")
canvas.create_image(80,100,image = lockImg)
canvas.grid(column=1 ,row=1)

def save():
    password = input_password.get()
    email = input_email.get()
    web = input_web.get()
    new_data = {
        web:{
            "email":email,
            "password":password
        }
    } 

    if len(web) == 0 or len(password) == 0:
            messagebox.showwarning("Warning", "Please fill in all fields before saving.")
    else:
        try:
            with open ("data.json", "r")  as data_file:
                # rading new data
                data = json.load(data_file)
                #uppdateing new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            with open("data.json", "w") as data_file:
                #Saving uppdated data
                json.dump(data,data_file,indent=4)
        finally:
            input_password.delete(0,END)
            input_web.delete(0,END)
def find_password():
    website = input_web.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        if website in data:
            messagebox.showinfo(f"{website}",f"Email:{data[website]["email"]}\nPassword:{data[website]["password"]}")
        else:
            messagebox.showinfo(f"{website}","No details for the website found")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
        return

# ---------------------------- UI SETUP ------------------------------- #
lable_web = Label(text="Website:", font=("Courier",15,"bold"))
lable_web.grid(row=3, column=0)
lable_email = Label(text="Email/username", font=("Courier",15,"bold"))
lable_email.grid(row=4, column=0)
lable_password = Label(text="Password", font=("Courier",15,"bold"))
lable_password.grid(row=5, column=0)

input_web = Entry(width= 35)
input_web.grid(row=3, column=1,columnspan=2)
input_email = Entry(width= 60)
input_email.grid(row=4, column=1,columnspan=3)
input_email.insert(0, "Nenad@gmail.com")
input_password = Entry(width= 35)
input_password.grid(row=5, column=1,columnspan= 2)

button_add = Button(text="add",width=32, command=save)
button_add.grid(row=6, column=1,columnspan=2)
button_password = Button(text="Generate Password",width=20, command = password_generator)
button_password.grid(row=5, column=3 )
button_search = Button(text="Search",width=20,command = find_password)
button_search.grid(row = 3,column=3, columnspan= 1 )

#Postavljanej prozor programa na sredini ekrana
# window_width = 600 
# window_height = 600
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
# x_position = (screen_width - window_width) // 2
# y_position = (screen_height - window_height) // 2
# window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
#----------------------------------------------------------- #

window.mainloop()