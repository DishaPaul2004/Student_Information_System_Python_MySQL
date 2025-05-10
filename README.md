# Student Information System using Python and MySQL
## Introduction
This is a system which I had previously implemented using Python Tkinter and MS Excel file as the data store. It had the limited functionalities of only adding new student information and displaying the current student information.
I have upgraded my previous project and added functionalities of searching for students, updating and deleting student information along with the aforementioned functionalities. Additionally, I have also used MySQL database instead of an Excel file.
## Objectives
- Login authentication
- Database connection
- Adding new student information
- Updating old student information
- Searching for students based on known data
- Deleting student records
## Implementation
This system has been implemented using Python Tkinter and MySQL.
I have used tkinter, pymysql modules as well as used the present features for creating scroll bars, displaying data as well as binding and unbinding hover actions when a button is enabled and disabled respectively.
For MySQL, I have availed the use of SELECT, INSERT, UPDATE and DELETE queries to implement the functionalities.
## Output
![python output 1](https://github.com/user-attachments/assets/c908c662-18bf-4444-8a8b-68f25346f69b)
![python output 2](https://github.com/user-attachments/assets/4c23966b-7b20-4b31-bdc4-ecf345693513)
This is the original window which opens for login authentication. On entering valid login credentials, a message box showing a "Success" message is displayed.
Since login is successful, the main window for the student information system opens.
![python output 3](https://github.com/user-attachments/assets/dd1ab195-eee7-47d1-89ed-074e7e1ca702)
This is the main window for the student information system. At this point, all the functionality buttons except "Exit" button are disabled since the user has not logged into the database yet.
![python output 4](https://github.com/user-attachments/assets/64cc0471-cb2d-4b50-a866-ea9e500666f8)
On clicking the "Connect" button, a window for database connection opens.
![python output 5](https://github.com/user-attachments/assets/09594435-d840-43e5-82cc-c6a20d5fd503)
After entering the valid details for host name, user name and password, clicking the "Connect to DB" button will enable the buttons for providing the functionalities.
![python output 6](https://github.com/user-attachments/assets/b868f871-34cc-4954-aef3-7c7956ce5356)
The "Show students" button displays the current student information stored in the database.
![python output 7](https://github.com/user-attachments/assets/7983a786-8969-4cac-89e4-a5a98032925d)
When "Search student" button is clicked, a form appears in which the user can enter the data they already know so as to search for the specific student record.
![python output 8i](https://github.com/user-attachments/assets/02598cf5-91e0-4d00-8e8d-a71a085030bd)
![python output 8](https://github.com/user-attachments/assets/4027d842-a10e-49f2-973d-c99b4fd61f60)
When "Add student" button is clicked, a message box appears regarding the guidelines for adding data and then the form opens for adding the new information.
![python output 9](https://github.com/user-attachments/assets/493eac23-632b-43c6-b430-7ea4274ba497)
When a student record is selected and "Delete student" button is clicked, the corresponding selected student record gets deleted from the database.
![python output 10](https://github.com/user-attachments/assets/228acd2b-6460-41a0-86b0-dcb7d7ee0e83)
When a student record is selected and "Update student" button is clicked, then the form for updating student information opens with the current information already filled in. The user simply needs to modify those fields so as to update the selected record.
## Conclusion
I have been trying to upgrade my old project so as to add new functionalities to it and am deeply grateful to various online tutorials which have helped me in improving my project as well as deepen my understanding of Python and MySQL.
