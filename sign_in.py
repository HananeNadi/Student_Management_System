from tkinter import *
from PIL import ImageTk,Image
import customtkinter as ctk
from customtkinter import CTkImage
import pymysql
import datetime






def login():
    if username.get()=='' or password.get()=='':
        lab = ctk.CTkLabel(root1, text_color='red',
                           text='ERREUR : Certains ou tous les champs sont vides.',
                           bg_color='#eaefff')
        lab.place(x=640, y=170)

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='hanane12345@')
            mycursor = con.cursor()
        except:
            lab = ctk.CTkLabel(root1, text_color='#0a7f4c',text='ERROR : Database connectivity issues , Please try again later',
                               bg_color='#eaefff').place(x=640, y=170)
            return
        query = 'use student_management_system'
        mycursor.execute(query)

        query = 'select * from student where CNE=%s and mot_de_passe=%s  ' #the username=cne even though here we heve CIN=%s
        mycursor.execute(query, (username.get(), password.get()))
        row = mycursor.fetchone()

        if row == None:
            lab = ctk.CTkLabel(root1, text_color='red',
                               text='ERREUR :Invalid nom d\'utilisateur ou mot de passe.                                                                                                 ',
                               bg_color='#eaefff').place(x=640, y=170)

        else:
            with open('current_user.txt','w') as f:
                f.write(f'{row[4]}:{row[1]}:{row[2]}')


            lab = ctk.CTkLabel(root1, text_color='#eaefff',
                               text='                                                                                                 ',
                               bg_color='#eaefff').place(x=640, y=170)

            with open('login_nbr.txt', "r") as f:
                lines = f.readlines()

            last_line = lines[-1].strip()
            now = datetime.datetime.now()
            today = str(now.date())
            if last_line.split(':')[0] == today:
                parts = last_line.split(':')
                parts[-1] = ':' + str(int(parts[-1]) + 1)
                new_last_line = "".join(parts)

                lines[-1] = new_last_line

                with open('login_nbr.txt', "w") as f:
                    f.writelines(lines)
            else:
                with open('login_nbr.txt', "a") as f:
                    f.write(f'\n{today}:1')
            root1.destroy()
            import dashboard


def inscription():
    root1.destroy()
    import sign_up

def hidden():
    open_eye.configure(file='photos/close_eye.png')
    password.configure(show='')
    eyebutton.configure(command=show)

def show():
    open_eye.configure(file='photos/open_eye.png')
    password.configure(show='*')
    eyebutton.configure(command=hidden)


root1=Tk()
root1.geometry("1024x576+125+15")
root1.resizable(False,False)
root1.iconbitmap('logo.ico.ico')
root1.title("Login page")

back=Image.open("photos/sign_in_template.jpg")
back=ImageTk.PhotoImage(back)
lab1=Label(root1,image=back)
lab1.place(x=0,y=0)


#username_field
username=ctk.CTkEntry(master=root1,width=280,font=('Microsoft Yahei UI Light',13,'bold'),
                          placeholder_text=" Nom d'utilisateur(CNE) ",height=55, border_width=0, corner_radius=0)
username.place(x=640,y=200)
#user_icone_field
user_icone=PhotoImage(file="photos/user_icon.png")
lab3=Label(root1,image=user_icone,bg='#eaefff')
lab3.place(x=616,y=214)


#password_field
password=ctk.CTkEntry(master=root1,width=280,font=('Microsoft Yahei UI Light',13,'bold'),
                          placeholder_text=' Mot de passe',height=55,show='*', border_width=0, corner_radius=0)
password.place(x=640,y=240)

#password_icone_field
key_icone=PhotoImage(file='photos/pass_icon.png')
lab4=Label(root1,image=key_icone,bg='#eaefff')
lab4.place(x=616,y=257)


#eye_field
open_eye=PhotoImage(file='photos/open_eye.png')
eyebutton=Button(root1,image=open_eye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hidden)
eyebutton.place(x=895,y=262)




Connectbutton=Button(root1,bd=0, text='Se connecter'
                         ,font=('Open sans',15,'bold')
                         , activebackground='#0b36cb',activeforeground='white'
                         ,fg='white',bg='#3a3aff',width=23
                         ,cursor='hand2',command=login)
Connectbutton.place(x=640,y=340)


def reset():
    root1.destroy()
    import reset


forgotbutton = Button(root1, bd=0, text="mot de passe oublié ?", font=('Microsoft Yahei UI Light', 9, 'bold'),
                          fg='#0e32a4', bg='#eaefff',
                          activebackground='#eaefff', activeforeground='#0e32a4', cursor='hand2', command=reset)
forgotbutton.place(x=770, y=294)


lab2 = Label(root1, text='Vous n\'avez pas de compte ?', font=('Microsoft Yahei UI Light', 8, 'bold'), fg='#0e32a4',
                 bg='#eaefff')
lab2.place(x=640, y=400)

createbutton = Button(root1, bd=0, text="Créer un compte!", font=('Microsoft Yahei UI Light', 8, 'bold underline'),
                          fg='red', bg='#eaefff',
                          activebackground='#eaefff', activeforeground='#e62918', cursor='hand2', command=inscription)
createbutton.place(x=820, y=398)

root1.mainloop()




