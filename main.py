#Password Generator Project
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for a1 in range(nr_letters)]

    password_list += [random.choice(symbols) for a2 in range(nr_symbols)]

    password_list += [random.choice(numbers) for a3 in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_entry_text = website_entry.get()
    email_entry_text = email_entry.get()
    password_entry_text = password_entry.get()
    new_data = {
        web_entry_text:{
            "email":email_entry_text,
            "password":password_entry_text
                }
               }

    if len(web_entry_text) == 0 or len(password_entry_text) == 0:
        messagebox.showinfo(title = 'Error',message = 'You have left some fields(s) empty')

    else:
        is_ok = messagebox.askokcancel(title = web_entry_text,message = f'These are the details entered: \nEmail: {email_entry_text}\nPassword: {password_entry_text}')
        if is_ok:
            try:
                with open('day29/data.json','r') as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except:
                with open('day29/data.json','w') as data_file:
                    #Saving data for the first time
                    json.dump(new_data,data_file,indent = 4)
                
            else:
                with open('day29/data.json','w') as data_file:
                    #Updating old data with new data
                    data.update(new_data)
                    #Saving updated data
                    json.dump(data,data_file,indent = 4)
            finally:
                #Deleting data entries from Tkinter windows
                website_entry.delete(0,END)
                password_entry.delete(0, END)

def find_password():
    web_entry_text = website_entry.get()
    try:
        with open('day29/data.json','r') as f:
            data1 = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title = 'Error',message=f'No data file found')
    else:
        if web_entry_text in data1:
            email_entry_text = data1[web_entry_text]['email']
            password_entry_text = data1[web_entry_text]['password']
            messagebox.showinfo(title = web_entry_text,message=f'Email:{email_entry_text}\nPassword:{password_entry_text}')
        
        else:
            messagebox.showinfo(title = 'Error',message=f'No data present for {web_entry_text}')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
img = PhotoImage(file='day29/logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(90, 100, image=img)
canvas.grid(row=0, column=1)

website_text = Label(text='Website: ')
website_text.grid(column=0, row=1)

website_entry = Entry(width=27)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_text = Label(text='Email/Username: ')
email_text.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"dhanuka.hardik01@gmail.com")

password_text = Label(text='Password: ')
password_text.grid(column=0, row=3)

password_entry = Entry(width=27)
password_entry.grid(row=3, column=1)

gen_button = Button(text='Generate',command = generate)
gen_button.grid(column=2, row=3)

search_button = Button(text='Search',command = find_password)
search_button.grid(column=2, row=1)

add_button = Button(text='Add',width = 35,command = save)
add_button.grid(column=1, row=4,columnspan = 2)

window.mainloop()

# window.minsize(height = 500,width = 500)
