from tkinter import *
from PIL import ImageTk,Image
import customtkinter as ctk
import tkinter as tk
import re
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql
import datetime

root1=Tk()
root1.geometry("1024x576+150+30")
root1.iconbitmap('logo.ico.ico')
root1.resizable(False,False)
root1.title("Mot de passe oublié")
back=Image.open("photos/reset2.jpg")
back=ImageTk.PhotoImage(back)
lab1=Label(root1,image=back)
lab1.place(x=0,y=0)




def verife3():
    special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                  '|',
                  '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
    if nouveau_entry.get()=='' or confirm_entry.get()=='':
        empty_Label = ctk.CTkLabel(root1, text="ERREUR :Certains ou tous les champs sont vides.", bg_color='#eaefff',
                                    font=('Calibri', 13),text_color='red')
        empty_Label.place(x=400,y=400)

    elif not any(ch in special_ch for ch in nouveau_entry.get()) or not any(
            ch.isupper() for ch in nouveau_entry.get()) or not any(
        ch.islower() for ch in nouveau_entry.get()) or not any(ch.isdigit() for ch in nouveau_entry.get()) or len(
        nouveau_entry.get()) < 8:
        empty_Label = ctk.CTkLabel(root1, text="ERREUR :Mot de pass invalid.                                    ", bg_color='#eaefff',
                                   font=('Calibri', 13), text_color='red')
        empty_Label.place(x=400, y=400)


    elif nouveau_entry.get() != confirm_entry.get():
        empty_Label = ctk.CTkLabel(root1, text='ERREUR :Les deux mots de passe doivent être identiques.         ', bg_color='#eaefff',
                                   font=('Calibri', 13), text_color='red')
        empty_Label.place(x=400, y=400)

    else:
        con = pymysql.connect(host='localhost', user='root', password='hanane12345@',
                              database='student_management_system')
        mycursor = con.cursor()

        query = 'select * from student where email=%s '
        mycursor.execute(query, (email_entry.get()))
        row = mycursor.fetchone()

        if row == None:
            empty_Label = ctk.CTkLabel(root1, text="ERREUR :Email does not existe.                                    ",
                                       bg_color='#eaefff',
                                       font=('Calibri', 13), text_color='red')
            empty_Label.place(x=400, y=400)

        else:
            # get the current date and time
            now = datetime.datetime.now()
            query = 'UPDATE student SET mot_de_passe=%s,confirme_pass=%s,date_time=%s WHERE email=%s'
            mycursor.execute(query, (nouveau_entry.get(), confirm_entry.get(), now, email_entry.get()))
            con.commit()
            updated_rows = mycursor.rowcount
            con.close()
            root1.destroy()
            import sign_in


def nouveau():

    global nouveau_entry,confirm_entry

    nouveau = tk.Frame(root1, bg='#eaefff')
    nouveau_Label = ctk.CTkLabel(nouveau, text="Nouveau Mot de pass", bg_color='#eaefff', font=('Calibri', 13, 'bold'))
    nouveau_Label.place(x=62, y=30)

    nouveau_entry = ctk.CTkEntry(master=nouveau, width=250, font=('Microsoft Yahei UI Light', 12, 'bold'),
                       placeholder_text=" Nouveau Mot de passe: ", height=35, border_width=0,
                       corner_radius=0)
    nouveau_entry.place(x=62, y=60)

    confirmLabel = ctk.CTkLabel(nouveau, text="Confirmer le Mot de passe", bg_color='#eaefff', font=('Calibri', 13, 'bold'))
    confirmLabel.place(x=62, y=110)

    confirm_entry= ctk.CTkEntry(master=nouveau, width=250, font=('Microsoft Yahei UI Light', 12, 'bold'),
                       placeholder_text=" Confirmer le Mot de passe : ", height=35, border_width=0,
                       corner_radius=0)
    confirm_entry.place(x=62, y=136)

    Réinitialiser_button = ctk.CTkButton(nouveau, text='Réinitialiser ', width=250, height=35, fg_color='#0c9f5f',
                                   text_color='white', font=('', 18, 'bold')
                                   , corner_radius=0, border_width=0, hover_color='#0a7f4c',command=verife3)

    Réinitialiser_button.place(x=62, y=200)

    nouveau.place(x=327, y=230, width=377, height=275)
def verife2():
    if code_entry.get() == '':
        empty_Label = ctk.CTkLabel(root1, text="ERREUR : Champ Code de vérification est vide.", bg_color='#eaefff',
                                   font=('Calibri', 13), text_color='red')
        empty_Label.place(x=400, y=400)

    elif code_entry.get() != str(random_num):
        empty_Label = ctk.CTkLabel(root1,
                                   text="ERREUR : Code de vérification incorrect.                             ",
                                   bg_color='#eaefff',
                                   font=('Calibri', 13), text_color='red')
        empty_Label.place(x=400, y=400)
    else:
        nouveau()

def main():
    main=tk.Frame(root1, bg='#eaefff')

    CNELabel = ctk.CTkLabel(main, text="E-mail académique:", bg_color='#eaefff', font=('Calibri', 13, 'bold'))
    CNELabel.place(x=62, y=42)
    CNE = ctk.CTkEntry(master=main, width=250, font=('Microsoft Yahei UI Light', 12, 'bold'),
                       placeholder_text=" Entrer votre email : ", height=35, border_width=0, corner_radius=0)
    CNE.place(x=62, y=72)

    suivant_button = ctk.CTkButton(main, text='Suivant', width=250, height=35, fg_color='#0c9f5f',
                                   text_color='white', font=('', 18, 'bold')
                                   , corner_radius=0, border_width=0, hover_color='#0a7f4c', command=verife1)

    suivant_button.place(x=58, y=132)

    main.place(x=327, y=230, width=377, height=275)
def code():
    global code_entry
    code = tk.Frame(root1, bg='#eaefff')

    code_Label = ctk.CTkLabel(code, text="Code-Vérification:", bg_color='#eaefff', font=('Calibri', 13, 'bold'))
    code_Label.place(x=62, y=42)

    code_entry = ctk.CTkEntry(master=code, width=250, font=('Microsoft Yahei UI Light', 12, 'bold'),
                              placeholder_text=" Entrer le code de vérification : ", height=35, border_width=0,
                              corner_radius=0)
    code_entry.place(x=62, y=72)

    back_button = ctk.CTkButton(code, text='back', width=130, height=35, fg_color='#eaefff',
                                text_color='gray', font=('', 18, 'bold'), border_color='gray'
                                , corner_radius=0, border_width=2, hover_color='#d1d1d2',
                                command=main)
    back_button.place(x=58, y=132)

    suivant2_button = ctk.CTkButton(code, text='Suivant', width=130, height=35, fg_color='#0c9f5f',
                                    text_color='white', font=('', 18, 'bold')
                                    , corner_radius=0, border_width=0, hover_color='#0a7f4c',
                                    command=verife2)
    suivant2_button.place(x=200, y=132)

    code.place(x=327, y=230, width=377, height=275)


def send_msg():

    global random_num
    sender_email = "hanane.nadi@etu.uae.ac.ma"
    sender_password = 'hanane12345'
    random_num = random.randint(0, 10000)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    who_will_recive_email = email_entry.get()

    subject = "Réinitialisation de votre mot de passe"
    text = f"Votre code de vérification est : {random_num}"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = who_will_recive_email
    message['Subject'] = subject
    body = MIMEText(text.encode('utf-8'), 'plain', 'utf-8')
    message.attach(body)

    server.sendmail(sender_email, who_will_recive_email, message.as_string())
    server.quit()

email=r'^[a-zA-Z]+\.[a-zA-Z]+@etu\.uae\.ac\.ma$'
def verife1():
    global email_entry
    if email_entry.get()=='':
        empty_Label = ctk.CTkLabel(root1, text="ERREUR : Champ E-mail est vide.", bg_color='#eaefff',
                                    font=('Calibri', 13),text_color='red')
        empty_Label.place(x=400,y=435)

    elif not re.match(email, email_entry.get()):

        empty_Label = ctk.CTkLabel(root1, text="ERREUR : E-mail invalid.                                        ", bg_color='#eaefff',
                                   font=('Calibri', 13), text_color='red')
        empty_Label.place(x=400, y=435)

    else:
            send_msg()
            code()

#main_page_field------------------------------------------------------------------------------------
#logo_field
image = Image.open('photos/logo_hananePNG.png')
photo = ImageTk.PhotoImage(image)
label = tk.Label(root1, image=photo,bg='#eaefff')
label.image = photo  # Store the photo as an attribute of the label
label.place(x=450, y=90)

#titre_field
titre_label = tk.Label(root1, text='Réinitialiser le Mot de passe ',font=('Calibri', 14, 'bold'),fg='#3a3aff', bg='#eaefff')
titre_label.place(x=400, y=200)

#text_field
text = tk.Text(root1, bg='#eaefff',font=('Calibri',10,'bold'),border=0)
text.insert(INSERT,"*Veuillez saisir votre adresse e-mail ci-dessous et nous vous\nenverrons un code de vérification à utiliser pour finaliser le\nprocessus de réinitialisation de votre Mot de passe.  ")
text.configure(state='disabled', spacing1=6)
text.place(x=350, y=235,height=100,width=353)

#email_field
email_Label = ctk.CTkLabel(root1, text="E-mail académique:", bg_color='#eaefff',font=('Calibri',13,'bold'))
email_Label.place(x=407, y=320)
email_entry=ctk.CTkEntry(master=root1,width=250,font=('Microsoft Yahei UI Light',12,'bold'),
                      placeholder_text=" Entrer votre email : ",height=35, border_width=0, corner_radius=0)
email_entry.place(x=400,y=350)

#suivant_field
suivant_button=ctk.CTkButton(root1,text='Suivant', width=250, height=35, fg_color='#0c9f5f',
                                   text_color='white', font=('', 18, 'bold')
                                   , corner_radius=0, border_width=0, hover_color='#0a7f4c',command=verife1)
suivant_button.place(x=400,y=400)


root1.mainloop()