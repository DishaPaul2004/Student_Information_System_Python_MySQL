from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def on_hover(e):#to change colour on hover
    e.widget['bg']='gold'

def on_leave(e):#to change colour when not hovered
    e.widget['bg']='white'

def add_student():
    def submit_data():
        try:
            if idField.get()=='' or nameField.get()=='' or deptField.get()=='' or addressField.get()=='' or dobField.get()=='' or emailField.get()=='' or phoneField.get()=='' or class10Field.get()=='' or class12Field.get()=='':
                messagebox.showerror('Error','Please fill out the required fields',parent=window1)#empty fields for insertion of data
            else:
                query='INSERT INTO student_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);'
                myCursor.execute(query,(idField.get(),nameField.get(),deptField.get(),addressField.get(),dobField.get(),emailField.get(),phoneField.get(),class10Field.get(),class12Field.get()))
                connection.commit()#permanent updation of data
                idField.delete(0,END)
                nameField.delete(0,END)
                deptField.delete(0,END)
                addressField.delete(0,END)
                dobField.delete(0,END)
                emailField.delete(0,END)
                phoneField.delete(0,END)
                class10Field.delete(0,END)
                class12Field.delete(0,END)
        except:
            messagebox.showerror('Error','Invalid data cannot be added')
            return

        query='SELECT * FROM student_data'
        myCursor.execute(query)
        selectedData=myCursor.fetchall()
        studentData.delete(*studentData.get_children())
        for data in selectedData:
            dataList=list(data)
            studentData.insert('',END,values=dataList)

    messagebox.showinfo('Instructions',
                        'Please follow the following instructions while adding data :\n 1. The IDs can begin with the letter S only followed by 3 numbers\n2. The departments can only be CSE,IT,ECE,AIML or EE\n 2. Enter the DOB in yyyy-mm-dd format')
    
    window1=Toplevel()
    window1.geometry('500x700+500+60')
    window1.grab_set()
    window1.resizable(False,False)
    window1.config(bg='light blue')
    window1.title('Form for adding students')

    idLabel=Label(window1,text='ID',font=("Cambria",14,"bold"),bg='light blue')
    idLabel.grid(row=0,column=0,padx=40,pady=20)
    idField=Entry(window1,font=("Cambria",14,"bold"))
    idField.grid(row=0,column=1,padx=40,pady=20)

    nameLabel=Label(window1,text='Name',font=("Cambria",14,"bold"),bg='light blue')
    nameLabel.grid(row=1,column=0,padx=40,pady=20)
    nameField=Entry(window1,font=("Cambria",14,"bold"))
    nameField.grid(row=1,column=1,padx=40,pady=20)

    deptLabel=Label(window1,text='Department',font=("Cambria",14,"bold"),bg='light blue')
    deptLabel.grid(row=2,column=0,padx=40,pady=20)
    deptField=Entry(window1,font=("Cambria",14,"bold"))
    deptField.grid(row=2,column=1,padx=40,pady=20)

    addressLabel=Label(window1,text='Address',font=("Cambria",14,"bold"),bg='light blue')
    addressLabel.grid(row=3,column=0,padx=40,pady=20)
    addressField=Entry(window1,font=("Cambria",14,"bold"))
    addressField.grid(row=3,column=1,padx=40,pady=20)

    dobLabel=Label(window1,text='DOB',font=("Cambria",14,"bold"),bg='light blue')
    dobLabel.grid(row=4,column=0,padx=40,pady=20)
    dobField=Entry(window1,font=("Cambria",14,"bold"))
    dobField.grid(row=4,column=1,padx=40,pady=20)

    emailLabel=Label(window1,text='Email',font=("Cambria",14,"bold"),bg='light blue')
    emailLabel.grid(row=5,column=0,padx=40,pady=20)
    emailField=Entry(window1,font=("Cambria",14,"bold"))
    emailField.grid(row=5,column=1,padx=40,pady=20)

    phoneLabel=Label(window1,text='Phone no.',font=("Cambria",14,"bold"),bg='light blue')
    phoneLabel.grid(row=6,column=0,padx=40,pady=20)
    phoneField=Entry(window1,font=("Cambria",14,"bold"))
    phoneField.grid(row=6,column=1,padx=40,pady=20)

    class10Label=Label(window1,text='Class 10 %',font=("Cambria",14,"bold"),bg='light blue')
    class10Label.grid(row=7,column=0,padx=40,pady=20)
    class10Field=Entry(window1,font=("Cambria",14,"bold"))
    class10Field.grid(row=7,column=1,padx=40,pady=20)

    class12Label=Label(window1,text='Class 12 %',font=("Cambria",14,"bold"),bg='light blue')
    class12Label.grid(row=8,column=0,padx=40,pady=20)
    class12Field=Entry(window1,font=("Cambria",14,"bold"))
    class12Field.grid(row=8,column=1,padx=40,pady=20)

    submitButton=Button(window1,text='SUBMIT',font=("Cambria",16,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',command=submit_data)
    submitButton.bind("<Enter>",on_hover)
    submitButton.bind("<Leave>",on_leave)
    submitButton.grid(row=9,columnspan=2,padx=2,pady=20)

def search_for_student():
    def search_data():
        query='SELECT * FROM student_data WHERE ID=%s OR Name=%s OR Department=%s OR Address=%s OR DOB=%s OR Email=%s OR Phone_no=%s OR Class_10=%s OR Class_12=%s'
        myCursor.execute(query,(idField.get(),nameField.get(),deptField.get(),addressField.get(),dobField.get(),emailField.get(),phoneField.get(),class10Field.get(),class12Field.get()))
        selectedData=myCursor.fetchall()
        studentData.delete(*studentData.get_children())#deleting previous data
        for data in selectedData:
            dataList=list(data)
            studentData.insert('',END,values=dataList)#showing current data

    window2=Toplevel()
    window2.geometry('500x800+500+20')
    window2.grab_set()
    window2.resizable(False,False)
    window2.config(bg='light blue')
    window2.title('Form for searching students')

    infoLabel=Label(window2,text='KNOWN DATA',font=("Cambria",16,"bold"),fg='white',bg='light blue')
    infoLabel.grid(row=0,columnspan=2,padx=40,pady=20)

    idLabel=Label(window2,text='ID',font=("Cambria",14,"bold"),bg='light blue')
    idLabel.grid(row=1,column=0,padx=40,pady=20)
    idField=Entry(window2,font=("Cambria",14,"bold"))
    idField.grid(row=1,column=1,padx=40,pady=20)

    nameLabel=Label(window2,text='Name',font=("Cambria",14,"bold"),bg='light blue')
    nameLabel.grid(row=2,column=0,padx=40,pady=20)
    nameField=Entry(window2,font=("Cambria",14,"bold"))
    nameField.grid(row=2,column=1,padx=40,pady=20)

    deptLabel=Label(window2,text='Department',font=("Cambria",14,"bold"),bg='light blue')
    deptLabel.grid(row=3,column=0,padx=40,pady=20)
    deptField=Entry(window2,font=("Cambria",14,"bold"))
    deptField.grid(row=3,column=1,padx=40,pady=20)

    addressLabel=Label(window2,text='Address',font=("Cambria",14,"bold"),bg='light blue')
    addressLabel.grid(row=4,column=0,padx=40,pady=20)
    addressField=Entry(window2,font=("Cambria",14,"bold"))
    addressField.grid(row=4,column=1,padx=40,pady=20)

    dobLabel=Label(window2,text='DOB',font=("Cambria",14,"bold"),bg='light blue')
    dobLabel.grid(row=5,column=0,padx=40,pady=20)
    dobField=Entry(window2,font=("Cambria",14,"bold"))
    dobField.grid(row=5,column=1,padx=40,pady=20)

    emailLabel=Label(window2,text='Email',font=("Cambria",14,"bold"),bg='light blue')
    emailLabel.grid(row=6,column=0,padx=40,pady=20)
    emailField=Entry(window2,font=("Cambria",14,"bold"))
    emailField.grid(row=6,column=1,padx=40,pady=20)

    phoneLabel=Label(window2,text='Phone no.',font=("Cambria",14,"bold"),bg='light blue')
    phoneLabel.grid(row=7,column=0,padx=40,pady=20)
    phoneField=Entry(window2,font=("Cambria",14,"bold"))
    phoneField.grid(row=7,column=1,padx=40,pady=20)

    class10Label=Label(window2,text='Class 10 %',font=("Cambria",14,"bold"),bg='light blue')
    class10Label.grid(row=8,column=0,padx=40,pady=20)
    class10Field=Entry(window2,font=("Cambria",14,"bold"))
    class10Field.grid(row=8,column=1,padx=40,pady=20)

    class12Label=Label(window2,text='Class 12 %',font=("Cambria",14,"bold"),bg='light blue')
    class12Label.grid(row=9,column=0,padx=40,pady=20)
    class12Field=Entry(window2,font=("Cambria",14,"bold"))
    class12Field.grid(row=9,column=1,padx=40,pady=20)

    searchButton=Button(window2,text='SEARCH',font=("Cambria",16,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',command=search_data)
    searchButton.bind("<Enter>",on_hover)
    searchButton.bind("<Leave>",on_leave)
    searchButton.grid(row=10,columnspan=2,padx=2,pady=20)

def update_student():
    def update():
        query='UPDATE student_data SET Name=%s,Department=%s,Address=%s,DOB=%s,Email=%s,Phone_no=%s,Class_10=%s,Class_12=%s WHERE ID=%s'
        myCursor.execute(query,(nameField.get(),deptField.get(),addressField.get(),dobField.get(),emailField.get(),phoneField.get(),class10Field.get(),class12Field.get(),idField.get()))
        connection.commit()
        window3.destroy()
        show_students()

    window3=Toplevel()
    window3.geometry('500x700+500+60')
    window3.grab_set()
    window3.resizable(False,False)
    window3.config(bg='light blue')
    window3.title('Form for updating students')

    idLabel=Label(window3,text='ID',font=("Cambria",14,"bold"),bg='light blue')
    idLabel.grid(row=0,column=0,padx=40,pady=20)
    idField=Entry(window3,font=("Cambria",14,"bold"))
    idField.grid(row=0,column=1,padx=40,pady=20)

    nameLabel=Label(window3,text='Name',font=("Cambria",14,"bold"),bg='light blue')
    nameLabel.grid(row=1,column=0,padx=40,pady=20)
    nameField=Entry(window3,font=("Cambria",14,"bold"))
    nameField.grid(row=1,column=1,padx=40,pady=20)

    deptLabel=Label(window3,text='Department',font=("Cambria",14,"bold"),bg='light blue')
    deptLabel.grid(row=2,column=0,padx=40,pady=20)
    deptField=Entry(window3,font=("Cambria",14,"bold"))
    deptField.grid(row=2,column=1,padx=40,pady=20)

    addressLabel=Label(window3,text='Address',font=("Cambria",14,"bold"),bg='light blue')
    addressLabel.grid(row=3,column=0,padx=40,pady=20)
    addressField=Entry(window3,font=("Cambria",14,"bold"))
    addressField.grid(row=3,column=1,padx=40,pady=20)

    dobLabel=Label(window3,text='DOB',font=("Cambria",14,"bold"),bg='light blue')
    dobLabel.grid(row=4,column=0,padx=40,pady=20)
    dobField=Entry(window3,font=("Cambria",14,"bold"))
    dobField.grid(row=4,column=1,padx=40,pady=20)

    emailLabel=Label(window3,text='Email',font=("Cambria",14,"bold"),bg='light blue')
    emailLabel.grid(row=5,column=0,padx=40,pady=20)
    emailField=Entry(window3,font=("Cambria",14,"bold"))
    emailField.grid(row=5,column=1,padx=40,pady=20)

    phoneLabel=Label(window3,text='Phone no.',font=("Cambria",14,"bold"),bg='light blue')
    phoneLabel.grid(row=6,column=0,padx=40,pady=20)
    phoneField=Entry(window3,font=("Cambria",14,"bold"))
    phoneField.grid(row=6,column=1,padx=40,pady=20)

    class10Label=Label(window3,text='Class 10 %',font=("Cambria",14,"bold"),bg='light blue')
    class10Label.grid(row=7,column=0,padx=40,pady=20)
    class10Field=Entry(window3,font=("Cambria",14,"bold"))
    class10Field.grid(row=7,column=1,padx=40,pady=20)

    class12Label=Label(window3,text='Class 12 %',font=("Cambria",14,"bold"),bg='light blue')
    class12Label.grid(row=8,column=0,padx=40,pady=20)
    class12Field=Entry(window3,font=("Cambria",14,"bold"))
    class12Field.grid(row=8,column=1,padx=40,pady=20)

    updateButton=Button(window3,text='UPDATE',font=("Cambria",16,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',command=update)
    updateButton.bind("<Enter>",on_hover)
    updateButton.bind("<Leave>",on_leave)
    updateButton.grid(row=9,columnspan=2,padx=2,pady=20)

    index=studentData.focus()
    record=studentData.item(index)
    datalist=record['values']
    idField.insert(0,datalist[0])
    nameField.insert(0,datalist[1])
    deptField.insert(0,datalist[2])
    addressField.insert(0,datalist[3])
    dobField.insert(0,datalist[4])
    emailField.insert(0,datalist[5])
    phoneField.insert(0,datalist[6])
    class10Field.insert(0,datalist[7])
    class12Field.insert(0,datalist[8])

def delete_student():
    index=studentData.focus()
    record=studentData.item(index)
    idToDelete=record['values'][0]
    query='DELETE FROM student_data WHERE ID=%s'
    myCursor.execute(query,idToDelete)
    connection.commit()
    show_students()

def show_students():
    query='SELECT * FROM student_data'
    myCursor.execute(query)
    selectedData=myCursor.fetchall()
    studentData.delete(*studentData.get_children())
    for data in selectedData:
        dataList=list(data)
        studentData.insert('',END,values=dataList)

def connectDB():

    def connect():
        try:
            global myCursor
            global connection
            connection=pymysql.connect(host=hostnameField.get(),user=usernameField.get(),password=passwordField.get())
            myCursor=connection.cursor()
            query='USE student_information;'
            myCursor.execute(query)

            messagebox.showinfo('Success','Successfully connected to the database',parent=connectToDBWindow)
            connectToDBWindow.destroy()

            addButton.config(state=NORMAL)
            addButton.bind("<Enter>",on_hover)
            addButton.bind("<Leave>",on_leave)

            searchButton.config(state=NORMAL)
            searchButton.bind("<Enter>",on_hover)
            searchButton.bind("<Leave>",on_leave)

            updateButton.config(state=NORMAL)
            updateButton.bind("<Enter>",on_hover)
            updateButton.bind("<Leave>",on_leave)

            deleteButton.config(state=NORMAL)
            deleteButton.bind("<Enter>",on_hover)
            deleteButton.bind("<Leave>",on_leave)

            showButton.config(state=NORMAL)
            showButton.bind("<Enter>",on_hover)
            showButton.bind("<Leave>",on_leave)

            dbButton.config(state=DISABLED)
            dbButton.unbind("<Enter>")
            dbButton.unbind("<Leave>")

        except:
            messagebox.showerror('Error','Invalid credentials',parent=connectToDBWindow)
            return

    connectToDBWindow=Toplevel()#creates a new GUI window on top of the existing GUI window
    connectToDBWindow.grab_set()#to prevent the window from getting minimized
    connectToDBWindow.title('Database login connection')
    connectToDBWindow.config(bg='light blue')
    connectToDBWindow.geometry('500x250+800+300')#width=500 and height=200 with 800 distance from X and 300 distance from Y
    connectToDBWindow.resizable(False,False)

    hostnameLabel=Label(connectToDBWindow,text='Host name',font=("Cambria",14,"bold"),bg='light blue')
    hostnameLabel.grid(row=0,column=0,padx=40,pady=20)
    hostnameField=Entry(connectToDBWindow,font=("Cambria",14,"bold"))
    hostnameField.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectToDBWindow,text='User name',font=("Cambria",14,"bold"),bg='light blue')
    usernameLabel.grid(row=1,column=0,padx=40,pady=20)
    usernameField=Entry(connectToDBWindow,font=("Cambria",14,"bold"))
    usernameField.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectToDBWindow,text='Password',font=("Cambria",14,"bold"),bg='light blue')
    passwordLabel.grid(row=2,column=0,padx=40,pady=20)
    passwordField=Entry(connectToDBWindow,font=("Cambria",14,"bold"),show="*")
    passwordField.grid(row=2,column=1,padx=40,pady=20)

    connectButton=Button(connectToDBWindow,text='Connect to DB',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',command=connect)
    connectButton.grid(row=3,columnspan=2)
    connectButton.bind("<Enter>", on_hover)
    connectButton.bind("<Leave>", on_leave)

window=Tk()
window.configure(bg='light green')
window.title('Student Management System')

headingLabel=Label(window,text='Student Management System',font=("Cambria",20,"italic bold"),bg='light green')
headingLabel.place(x=600,y=30)

dbButton=Button(window,text='Connect',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',command=connectDB)
dbButton.place(x=1400,y=30)
dbButton.bind("<Enter>", on_hover)
dbButton.bind("<Leave>", on_leave)

buttonFrame=Frame(window)
buttonFrame.place(x=50,y=100,width=300,height=600)
buttonFrame.configure(bg='light green')

logoImage=PhotoImage(file='student.png')
logoLabel=Label(buttonFrame,image=logoImage)
logoLabel.grid(row=0,column=2)

addButton=Button(buttonFrame,text='Add student',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,state=DISABLED,command=add_student)
addButton.grid(row=1,column=2,pady=20,padx=20)

searchButton=Button(buttonFrame,text='Search student',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,state=DISABLED,command=search_for_student)
searchButton.grid(row=2,column=2,pady=20,padx=20)

updateButton=Button(buttonFrame,text='Update student',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,state=DISABLED,command=update_student)
updateButton.grid(row=3,column=2,pady=20,padx=20)

deleteButton=Button(buttonFrame,text='Delete student',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,state=DISABLED,command=delete_student)
deleteButton.grid(row=4,column=2,pady=20,padx=20)

showButton=Button(buttonFrame,text='Show students',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,state=DISABLED,command=show_students)
showButton.grid(row=5,column=2,pady=20,padx=20)

exitButton=Button(buttonFrame,text='Exit',font=("Cambria",14,"bold"),bg='white',fg='black',activebackground='white',activeforeground='black',width=25,command=window.destroy)
exitButton.grid(row=6,column=2,pady=20,padx=20)
exitButton.bind("<Enter>",on_hover)
exitButton.bind("<Leave>",on_leave)

displayFrame=Frame(window)
displayFrame.place(x=400,y=100,width=1100,height=600)
displayFrame.configure(bg='light green')

scrollbarX=Scrollbar(displayFrame,orient=HORIZONTAL)
scrollbarX.pack(side=BOTTOM,fill=X)

scrollbarY=Scrollbar(displayFrame,orient=VERTICAL)
scrollbarY.pack(side=RIGHT,fill=Y)

studentData=ttk.Treeview(displayFrame,columns=('ID','Name','Department','Address','DOB','Email','Phone no.','Class 10 %','Class 12 %'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
studentData.pack(fill=BOTH,expand=1)
scrollbarX.config(command=studentData.xview)
scrollbarY.config(command=studentData.yview)

studentData.config(show='headings')
studentData.heading('ID',text='ID')
studentData.heading('Name',text='Name')
studentData.heading('Department',text='Department')
studentData.heading('Address',text='Address')
studentData.heading('DOB',text='DOB')
studentData.heading('Email',text='Email')
studentData.heading('Phone no.',text='Phone no.')
studentData.heading('Class 10 %',text='Class 10 %')
studentData.heading('Class 12 %',text='Class 12 %')

window.state('zoomed')
window.mainloop()