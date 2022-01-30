from tkinter import *
from cryptography.fernet import Fernet
import os

i = 0
passwords = []
users = []
emails = []
appNames = []
fernet = Fernet(b'HHWGjhU_UKFrTtkEOY1zZrd2hu6o8zchLHbGLesXbIc=')
generalPassword = ""

if os.path.isfile('genPass.txt'):
    with open('genPass.txt', 'r') as f:
        if(f.read()):
            f.seek(0)
            passw = f.read()
            s = passw.replace("'", "")
            s2 = s.replace("b", "", 1)
            s3 = bytes(s2, 'utf-8')
            generalPassword = fernet.decrypt(s3).decode()

if generalPassword != "":
    if input("Please type in your password: ") == generalPassword:
        root = Tk()
        root.title="Password Manager"

        if os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'r') as f:
                tempPass = f.read()
                tempPass = tempPass.split(',')
                passwords1 = [x for x in tempPass if x.strip()]
                for app in passwords1:
                    s = app.replace("'", "")
                    s2 = s.replace("b", "", 1)
                    s3 = bytes(s2, "utf-8")
                    app = fernet.decrypt(s3).decode()
                    passwords.append(app)

        if os.path.isfile('users.txt'):
            with open('users.txt', 'r') as f:
                tempPass = f.read()
                tempPass = tempPass.split(',')
                users1 = [x for x in tempPass if x.strip()]
                for app in users1:
                    s = app.replace("'", "")
                    s2 = s.replace("b", "", 1)
                    s3 = bytes(s2, "utf-8")
                    app = fernet.decrypt(s3).decode()
                    users.append(app)

        if os.path.isfile('emails.txt'):
            with open('emails.txt', 'r') as f:
                tempPass = f.read()
                tempPass = tempPass.split(',')
                emails1 = [x for x in tempPass if x.strip()]
                for app in emails1:
                    s = app.replace("'", "")
                    s2 = s.replace("b", "", 1)
                    s3 = bytes(s2, "utf-8")
                    app = fernet.decrypt(s3).decode()
                    emails.append(app)

        if os.path.isfile('site.txt'):
            with open('site.txt', 'r') as f:
                tempPass = f.read()
                tempPass = tempPass.split(',')
                appNames1 = [x for x in tempPass if x.strip()]
                for app in appNames1:
                    s = app.replace("'", "")
                    s2 = s.replace("b", "", 1)
                    s3 = bytes(s2, "utf-8")
                    app = fernet.decrypt(s3).decode()
                    appNames.append(app)

        def deleteSave():
            f = open('passwords.txt', 'r+')
            f.truncate(0)
            f = open('emails.txt', 'r+')
            f.truncate(0)
            f = open('users.txt', 'r+')
            f.truncate(0)
            f = open('site.txt', 'r+')
            f.truncate(0)

            for widget in frame.winfo_children():
                widget.destroy()
            for widget in frame2.winfo_children():
                widget.destroy()
            for widget in frame3.winfo_children():
                widget.destroy()
            for widget in frame4.winfo_children():
                widget.destroy()

            passwords.clear()
            users.clear()
            emails.clear()
            appNames.clear()

        def submit():
            password = passwordEntry.get()
            user = userEntry.get()
            email = emailEntry.get()
            name = nameEntry.get()
            
            if(password and user and email and name):
                passwordEntry.delete(0, END)
                passwordEntry.insert(0, "")

                userEntry.delete(0, END)
                userEntry.insert(0, "")

                emailEntry.delete(0, END)
                emailEntry.insert(0, "")

                nameEntry.delete(0, END)
                nameEntry.insert(0, "")

                for widget in frame.winfo_children():
                    widget.destroy()
                for widget in frame2.winfo_children():
                    widget.destroy()
                for widget in frame3.winfo_children():
                    widget.destroy()
                for widget in frame4.winfo_children():
                    widget.destroy()

                users.append(user)
                emails.append(email)
                passwords.append(password)
                appNames.append(name)

                with open('passwords.txt', 'w') as f:
                    for app in passwords:
                        label = Label(frame, text=app, bg="white")
                        label.pack()
                        print("password:", app)
                        f.write(str(fernet.encrypt(app.encode())) + ',')

                with open('users.txt', 'w') as f:
                    for app in users:
                        print("user:", app)
                        label = Label(frame2, text=app, bg="white")
                        label.pack()
                        f.write(str(fernet.encrypt(app.encode())) + ',')

                with open('emails.txt', 'w') as f:
                    for app in emails:
                        label = Label(frame3, text=app, bg="white")
                        label.pack()
                        print("emails:", app)
                        f.write(str(fernet.encrypt(app.encode())) + ',')

                with open('site.txt', 'w') as f:
                    for app in appNames:
                        label = Label(frame4, text=app, bg="white")
                        label.pack()
                        print("site:", app)
                        f.write(str(fernet.encrypt(app.encode())) + ',')

        canvas = Canvas(root, height=700, width=750, bg="#263D42")
        canvas.pack()

        passwordsLabel = Label(root, text="Passwords", bg="#263D42")
        passwordsLabel.place(relwidth=0.25, relheight = 0.05, rely=0.03)
        frame = Frame(root, bg="white")
        frame.place(relwidth=0.25, relheight=0.66, rely=0.1) 
        line1 = Frame(root, bg="black")
        line1.place(relwidth=0.01, relheight=0.66, rely=0.1, relx=0.25)

        usersLabel = Label(root, text="Users", bg="#263D42")
        usersLabel.place(relwidth=0.25, relheight = 0.05, relx=0.26, rely=0.03)
        frame2 = Frame(root, bg="white")
        frame2.place(relwidth=0.26, relheight=0.66, relx=0.26, rely=0.1)
        line1 = Frame(root, bg="black")
        line1.place(relwidth=0.01, relheight=0.66, rely=0.1, relx=0.51)

        emailsLabel = Label(root, text="Emails", bg="#263D42")
        emailsLabel.place(relwidth=0.25, relheight = 0.05, relx=0.51, rely=0.03)
        frame3 = Frame(root, bg="white")
        frame3.place(relwidth=0.25, relheight=0.66, relx=0.52, rely=0.1)
        line1 = Frame(root, bg="black")
        line1.place(relwidth=0.01, relheight=0.66, rely=0.1, relx=0.76)

        appLabel = Label(root, text="App/site name", bg="#263D42")
        appLabel.place(relwidth=0.25, relheigh= 0.05, relx=0.76, rely=0.03)
        frame4 = Frame(root, bg="white")
        frame4.place(relwidth=0.25, relheigh=0.66, relx=0.77, rely=0.1)

        submit = Button(root, text= "Submit Password",  fg="white", bg="#263D42", command=submit)
        submit.pack()

        passwordEntry = Entry(root, fg="white", bg="#263D42")
        passwordEntry.pack()

        userEntry = Entry(root, fg="white", bg="#263D42")
        userEntry.pack()

        emailEntry = Entry(root, fg="white", bg="#263D42")
        emailEntry.pack()

        nameEntry = Entry(root, fg="white", bg="#263D42")
        nameEntry.pack()

        deleteSave = Button(root, text="delete save", padx=10, pady=5, fg="white", bg="#263D42", command = deleteSave)
        deleteSave.pack()


        for app in passwords:
            label = Label(frame, text=app, bg="white")
            label.pack()

        for app in users:
            label = Label(frame2, text=app, bg="white")
            label.pack()

        for app in emails:
            label = Label(frame3, text=app, bg="white")
            label.pack()

        for app in appNames:
            label = Label(frame4, text=app, bg="white")
            label.pack()


        root.mainloop()
    else:
        print("Incorrect")
        exit()
else:
    generalPassword = input("Please choose a password: ")
    with open('genPass.txt', 'w') as f:
        f.write(str(fernet.encrypt(generalPassword.encode())))
    
#hi