from tkinter import *#necessary for GUI creation
from PIL import ImageTk#necessary for displaying images
from tkinter import messagebox#for displaying messages

def login():
    if usernameField.get()=='' or passwordField.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameField.get()=='Disha' and passwordField.get()=='1111':#hardcoded username and password for login
        messagebox.showinfo('Success','Welcome to the system')
        root.destroy()
        import main
    else:
        messagebox.showerror('Error','Invalid username or password')
        usernameField.delete(0,END)
        passwordField.delete(0,END)


root=Tk()#creating an object of Tk class
root.configure(bg='lightgray')
root.title('Login Authentication')

loginFrame=Frame(root)#container for login
loginFrame.place(x=500, y=200)
loginFrame.configure(bg='lightgray',padx=100)

logoImage=PhotoImage(file='studentIcon.png')

photoLabel=Label(loginFrame,image=logoImage)
photoLabel.grid(row=0,column=0,columnspan=4)

usernameLabel=Label(loginFrame,text='Username',font=("Cambria",14,"bold"),bg='lightgray')#label for the input field
usernameLabel.grid(row=2,column=0,padx=10,pady=10)
usernameField=Entry(loginFrame,font=("Cambria",14,"bold"))#input field for username
usernameField.grid(row=2,column=2,padx=10,pady=10)

passwordLabel=Label(loginFrame,text='Password',font=("Cambria",14,"bold"),bg='lightgray')
passwordLabel.grid(row=4,column=0,padx=10,pady=10)
passwordField=Entry(loginFrame,font=("Cambria",14,"bold"),show="*")#input field for password
passwordField.grid(row=4,column=2,padx=10,pady=10)

loginButton=Button(loginFrame,text='Submit',font=("Cambria",14,"bold"),bg='black',activebackground='black',activeforeground='white',
                   fg='white',padx=5,pady=5,cursor='hand2',command=login)
loginButton.grid(row=7,column=0,columnspan=4)

root.state('zoomed')#window is displayed on the entire screen

root.mainloop()#calling the mainloop of root
