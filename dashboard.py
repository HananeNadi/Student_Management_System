import webbrowser
from tkinter import *
import io
from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk
import PIL.Image
import pymysql
import datetime
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import *


dash = tk.Tk()
dash.title('e-connect')
dash.geometry('1366x768')
dash.config(background='#f2f5ff')
dash.iconbitmap('logo.ico.ico')

# sider_field
side = Frame(dash, bg='#eaefff')
side.place(x=0, y=0, height=750, width=300)

# header_field
head = Frame(dash, bg='white')
head.place(x=300, y=0, height=60, width=1200)

# main_frame_field
main = Frame(dash, bg='white')
main.place(x=300, y=60, height=750, width=1200)

develop_frame=Frame(dash, bg='white')
titre_label = Label(develop_frame, text=' Dévelopée par H. NADI ', font=('arial', 10),
                    fg='black',
                    bg='white')
titre_label.place(x=330, y=0)
develop_frame.place(x=300, y=620, height=50, width=1200)

# logo_field
logo_image = PhotoImage(file='photos/logo_hananePNG.png')
logo = Label(master=side, image=logo_image, background='#eaefff')
logo.place(x=65, y=7)


def infomation():
    global words
    hidden()

    clear_toggle()
    with open('current_user.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        words = line.split(':')

    info_frame = tk.Frame(main, bg='white')
    titre_label = Label(info_frame, text=' IDENTIFICATION DE L\'ETUDIANT ', font=('arial', 15, 'bold'),
                        fg='#3a3aff',
                        bg='white')
    titre_label.place(x=30, y=30)

    con = pymysql.connect(host='localhost', user='root', password='hanane12345@',database='student_management_system')
    mycursor = con.cursor()

    query = "SELECT nom, prénom, date_de_naissance, CNE, CIN, Pays, ville, Adresse, sexe, Telephone, email, annee_de_bac, niveau, filiere, image FROM student where CNE=%s"
    mycursor.execute(query,words[0])
    row = mycursor.fetchone()

    if row is not None:

        tk.Label(info_frame, text="Nom:", font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=80)
        tk.Label(info_frame, text=row[0],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=80)

        tk.Label(info_frame, text="Prénom:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=110)
        tk.Label(info_frame, text=row[1],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=110)

        tk.Label(info_frame, text="Date de naissance:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=140)
        tk.Label(info_frame, text=row[2],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=140)

        tk.Label(info_frame, text="CNE:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=170)
        tk.Label(info_frame, text=row[3],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=170)

        tk.Label(info_frame, text="CIN:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=200)
        tk.Label(info_frame, text=row[4],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=200)

        tk.Label(info_frame, text="Pays:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=230)
        tk.Label(info_frame, text=row[5],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=230)

        tk.Label(info_frame, text="Ville:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=260)
        tk.Label(info_frame, text=row[6],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=260)

        tk.Label(info_frame, text="Adresse:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=290)
        tk.Label(info_frame, text=row[7],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=290)

        tk.Label(info_frame, text="Sexe:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=320)
        tk.Label(info_frame, text=row[8],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=320)

        tk.Label(info_frame, text="Téléphone:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=350)
        tk.Label(info_frame, text=row[9],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=350)

        tk.Label(info_frame, text="Email:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=380)
        tk.Label(info_frame, text=row[10],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=380)

        tk.Label(info_frame, text="Année de bac:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=410)
        tk.Label(info_frame, text=row[11],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=410)

        tk.Label(info_frame, text="Niveau:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=440)
        tk.Label(info_frame, text=row[12],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=440)

        tk.Label(info_frame, text="Filière:",font=('arial', 14, 'bold'),
                        fg='black',bg='white').place(x=30, y=470)
        tk.Label(info_frame, text=row[13],font=('arial', 14),
                        fg='black',bg='white').place(x=217, y=470)


        img = PIL.Image.open(io.BytesIO(row[14]))
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(info_frame, image=img, width=150, height=150)
        img_label.image = img  # keep a reference to the image to prevent garbage collection
        img_label.place(x=650, y=80)

    else:

        tk.Label(info_frame, text="User not found", font=("Helvetica", 14, "bold")).place()

    con.close()

    info_frame.place(x=0, y=30, height=600, width=1200)


# profile_field
def toggle_menu():
    global toggle_menu_frame
    toggle_menu_frame = tk.Frame(main, bg='#ededee')  #
    photo_profil = tk.PhotoImage(file='photos/profile.png')
    profil = ctk.CTkButton(toggle_menu_frame, border_width=0, height=20, width=130, image=photo_profil, compound='left',
                           fg_color='#ededee', corner_radius=0, hover_color='white', text='Mon compte',command=infomation,
                           text_color='#565659',
                           font=('Open sans', 14))

    profil.place(x=3, y=15)

    photo_change = tk.PhotoImage(file='photos/change_pass.png')
    change_password = ctk.CTkButton(toggle_menu_frame, border_width=0, height=20, width=120, image=photo_change,
                                    compound='left',
                                    fg_color='#ededee', corner_radius=0, hover_color='white',
                                    text='Changer le mot\nde pass',
                                    text_color='#565659', command=mot_de_passe,
                                    font=('Open sans', 14))

    change_password.place(x=10, y=50)

    photo_log_out = tk.PhotoImage(file='photos/log_out.png')
    log_out = ctk.CTkButton(toggle_menu_frame, border_width=0, height=20, width=120, image=photo_log_out,
                            compound='left',
                            fg_color='#ededee', corner_radius=0, hover_color='white',
                            text='Se deconecter',
                            text_color='#565659', command=out,
                            font=('Open sans', 14))

    log_out.place(x=10, y=100)
    toggle_menu_frame.place(x=805, y=3, height=150, width=150)
    user_bttn.configure(command=lambda: delete_menu(toggle_menu_frame))


def delete_menu(menu_frame):
    menu_frame.destroy()
    user_bttn.configure(command=toggle_menu)

with open('current_user.txt', 'r') as f:
    line = f.readline()
    curr = line.split(':')[1]


def clear_toggle():
    toggle_menu_frame.configure(bg='white')
    for widgets in toggle_menu_frame.winfo_children():
        widgets.destroy()


def out():
    dash.destroy()


def valid():
    special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']',
                  '|',
                  '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
    if new_passEntry.get() == '' or confirm_passEntry.get() == '':
        lab = ctk.CTkLabel(mot_frame, text_color='red',
                           text='ERREUR Certains ou tous les champs sont vides.',
                           bg_color='white')
        lab.place(x=300, y=380)



    elif not any(ch in special_ch for ch in new_passEntry.get()) or not any(
            ch.isupper() for ch in new_passEntry.get()) or not any(
            ch.islower() for ch in new_passEntry.get()) or not any(ch.isdigit() for ch in new_passEntry.get()) or len(
            new_passEntry.get()) < 8:
        lab = ctk.CTkLabel(mot_frame, text_color='red',
                           text='ERREUR : Mot de pass invalid                                                                 ',
                           bg_color='white')
        lab.place(x=300, y=380)

        new_passEntry.configure(border_width=1, border_color='red')


    elif new_passEntry.get() != confirm_passEntry.get():
        lab = ctk.CTkLabel(mot_frame, text_color='red',
                           text='ERREUR :Les deux mots de passe doivent être identiques.          ',
                           bg_color='white').place(x=300, y=380)
    else:
        con = pymysql.connect(host='localhost', user='root', password='hanane12345@',
                              database='student_management_system')
        mycursor = con.cursor()
        # get the current date and time
        now = datetime.datetime.now()
        with open('current_user.txt', 'r') as f:
            line = f.readline()
            curr = line.split(':')[0]

        query = 'UPDATE student SET mot_de_passe=%s,confirme_pass=%s,date_time=%s WHERE CNE=%s '
        mycursor.execute(query, (new_passEntry.get(), confirm_passEntry.get(), now,curr))
        con.commit()
        updated_rows = mycursor.rowcount
        con.close()


        lab = ctk.CTkLabel(mot_frame, text_color='#0a7f4c',
                           text='Votre mot de passe a été modifié avec succès !.                                                          ',
                           bg_color='white').place(x=300, y=380)


def mot_de_passe():
    hidden()
    global new_passEntry, confirm_passEntry, mot_frame
    clear_toggle()

    mot_frame = tk.Frame(main, bg='white')
    titre_label = Label(mot_frame, text=' Changer le mot de pass ', font=('arial', 15, 'bold'),
                        fg='#3a3aff',
                        bg='white')
    titre_label.place(x=30, y=30)

    new_passLabel = ctk.CTkLabel(master=mot_frame, text="Nouveau mot de passe :", bg_color='white', font=('', 18, 'bold'))
    new_passLabel.place(x=298, y=120)
    new_passEntry = ctk.CTkEntry(master=mot_frame, placeholder_text="Entrer le nouveau mot de passe ", width=320, height=50,
                                 border_width=0, corner_radius=0)
    new_passEntry.place(x=300, y=146)

    confirm_passLabel = ctk.CTkLabel(master=mot_frame, text="Confirmer le nouveau mot de passe :", bg_color='white',
                                     font=('', 18, 'bold'))
    confirm_passLabel.place(x=298, y=230)
    confirm_passEntry = ctk.CTkEntry(master=mot_frame, placeholder_text="Confirmer le nouveau mot de passe ", width=320,
                                     height=50,
                                     border_width=0, corner_radius=0)
    confirm_passEntry.place(x=300, y=256)

    valider_button = ctk.CTkButton(mot_frame, text="Valider!", width=320, height=35, fg_color='#0c9f5f',
                                   text_color='white', font=('', 18, 'bold')
                                   , corner_radius=0, border_width=0, hover_color='#0a7f4c',
                                   command=valid)
    valider_button.place(x=300, y=340)

    mot_frame.place(x=0, y=30, height=600, width=1200)


# dashboard_field--------------------------------------------------------------------------------------------------------------------

def hidden():
    dash_lab.configure(bg='#eaefff')
    button_dash.configure(text_color='#565659')
    button_dash.configure(image=photo_gris)

    emploi_lab.configure(bg='#eaefff')
    button_emploi.configure(text_color='#565659')
    button_emploi.configure(image=emploi_gris)

    button_cours.configure(text_color='#565659')
    button_cours.configure(image=cours_gris)
    cours_lab.configure(bg='#eaefff')

    button_notes.configure(text_color='#565659')
    button_notes.configure(image=notes_gris)
    notes_lab.configure(bg='#eaefff')

    button_activite.configure(text_color='#565659')
    button_activite.configure(image=activite_gris)
    activite_lab.configure(bg='#eaefff')

    button_clubs.configure(text_color='#565659')
    button_clubs.configure(image=clubs_gris)
    clubs_lab.configure(bg='#eaefff')

    button_about.configure(text_color='#565659')
    button_about.configure(image=about_gris)
    about_lab.configure(bg='#eaefff')

def open_calender():
        calendrier = tk.Toplevel()
        calendrier.geometry('900x700+220+5')
        calendrier.resizable(False, False)
        image = Image.open("photos/calender.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(calendrier, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        calendrier.title("Calendrier 2022-2023")
def open_act1():
    webbrowser.open("D:\PycharmProjects\gestion_etudiants\pdf\Journée sur l’Intelligence Artificielle & Mathématiques Appliquées.pdf")#give the absolate path of the pdf
def open_act2():
    webbrowser.open_new("D:\PycharmProjects\gestion_etudiants\pdf\Avis aux étudiants en mobilité à l'international.pdf")
def open_act3():
    webbrowser.open("D:\PycharmProjects\gestion_etudiants\pdf\Avis aux élèves ingénieurs GEER1. Module  Modélisation numérique 1  Contrôle Continu.pdf")
def actualite():
    actualite_frame = tk.Frame(main, bg='white')
    titre_label = Label(actualite_frame, text=' Actualités ', font=('arial', 14, 'bold'),
                        fg='#3a3aff',
                        bg='white')
    titre_label.place(x=30, y=50)

    button_act1 = ctk.CTkButton(actualite_frame, border_width=0, fg_color='white'
                                  , height=50, width=160, hover_color='white',
                                  text='• Journée sur l’Intelligence Artificielle & Mathématiques Appliquées ', font=('', 17, 'bold', 'underline'), text_color='#565659',
                                  corner_radius=10,
                                  command=open_act1)
    button_act1.place(x=30, y=100)

    button_act2 = ctk.CTkButton(actualite_frame, border_width=0, fg_color='white'
                                , height=50, width=160, hover_color='white',
                                text='• Avis aux étudiants en mobilité à l\'international ',
                                font=('', 17, 'bold', 'underline'), text_color='#565659',
                                corner_radius=10,
                                command=open_act2)
    button_act2.place(x=30, y=150)

    button_act2 = ctk.CTkButton(actualite_frame, border_width=0, fg_color='white'
                                , height=50, width=160, hover_color='white',
                                text='• Avis aux élèves ingénieurs GEER1. Module : Modélisation numérique 1 : Contrôle Continu ',
                                font=('', 17, 'bold', 'underline'), text_color='#565659',
                                corner_radius=10,
                                command=open_act3)
    button_act2.place(x=30, y=200)

    actualite_frame.place(x=0, y=30, height=600, width=1200)


def ensah():
    webbrowser.open_new('https://ensah.ma/index.php')

def home_page():
    home_frame = tk.Frame(main, bg='white')
    titre_label = Label(home_frame, text=' Bienvenue sur la plateforme e- Connect ', font=('arial', 14, 'bold'),
                        fg='#3a3aff',
                        bg='white')
    titre_label.place(x=30, y=50)

    ensah_image = tk.PhotoImage(file='photos/Ensah.png')
    ensah_bttn = ctk.CTkButton(home_frame, border_width=1, image=ensah_image, height=80, width=120, text_color='#606062',
                               compound='left',
                               fg_color='white', corner_radius=10, hover_color='#eaefff', font=('arial', 18, 'bold'),
                               text='     Ensah              ', command=ensah)
    ensah_bttn.place(x=670, y=70)

    calendrier_image = tk.PhotoImage(file='photos/calendrier-blue.png')
    calendrier_bttn = ctk.CTkButton(home_frame, border_width=1, image=calendrier_image, height=80, width=120,
                                    text_color='#606062', compound='left',
                                    fg_color='white', corner_radius=10, hover_color='#eaefff',
                                    font=('arial', 18, 'bold'), text='    Calendrier       ', command=open_calender)
    calendrier_bttn.place(x=670, y=170)

    actualtie_image = tk.PhotoImage(file='photos/actualitee.png')
    actualie_bttn = ctk.CTkButton(home_frame, border_width=1,image=actualtie_image, height=80, width=120,
                                  text_color='#606062', compound='left',
                                  fg_color='white', corner_radius=10, hover_color='#eaefff', font=('arial', 18, 'bold'),
                                  text='    Actualité          ', command=actualite)
    actualie_bttn.place(x=670, y=275)

    cal = Calendar(home_frame, selectmode="day", date_pattern="mm/dd/y", year=2023, month=4, day=4,
                   normalbackground='#eaefff', normalforeground='blue', weekendforeground='blue'
                   , background="#eaefff", foreground="blue")
    cal.place(x=670,y=375)
    with open('login_nbr.txt', 'r') as f:
        data = f.readlines()[1:]
    # separate date and number_of_logins into separate lists
    dates = []
    logins = []
    for d in data:
        date, num_logins = d.strip().split(':')
        dates.append(date)
        logins.append(int(num_logins))
    if len(dates) > 6:
        dates = dates[-6:]
        logins = logins[-6:]

    figure = Figure(figsize=(6, 4))
    figure_plot = figure.add_subplot(111)
    figure_plot.plot(dates, logins, color='#3a3aff', marker='o')
    figure_plot.fill_between(dates, logins, color='#eaefff')
    figure_plot.figure.autofmt_xdate()
    figure_plot.figure.tight_layout(pad=2.0)
    line_graph = FigureCanvasTkAgg(figure, master=main)
    line_graph.get_tk_widget().place(x=0, y=100)
    line_graph.draw()

    home_frame.place(x=0, y=0, height=600, width=1200)




def home_click(home):
    hidden()
    button_dash.configure(text_color='blue')
    button_dash.configure(image=photo_blue)
    dash_lab.configure(bg='blue')
    home()


# Load the gris image and create a button with the image
photo_gris = tk.PhotoImage(file='photos/accueil_gris.png')
photo_blue = tk.PhotoImage(file='photos/accueil_blue.png')
button_dash = ctk.CTkButton(side, border_width=0, image=photo_blue, fg_color='#eaefff'
                            , compound="left", height=50, width=160, hover_color='#eaefff',
                            text=' Accueil', font=('', 17, 'bold'), text_color='blue', corner_radius=10,
                            command=lambda: home_click(home_page))
button_dash.place(x=4, y=160)

#the_open_window--------------------------------------------------------------------------------------------------------------------------------------------------------------

user_image = tk.PhotoImage(file='photos/user_blue_gha.png')
user_bttn = ctk.CTkButton(head, border_width=0, image=user_image, height=80, width=90,text_color='#606062',
                          fg_color='white', corner_radius=0, hover_color='white', font=('arial', 18, 'bold'),text=curr, command=toggle_menu)
user_bttn.place(x=820, y=0)
titre_label = Label(main, text=' Bienvenue sur la plateforme e- Connect ', font=('arial', 14, 'bold'),
                    fg='#3a3aff',
                    bg='white')
titre_label.place(x=30, y=50)
# indicator
dash_lab = tk.Label(side, text='', bg='blue')
dash_lab.place(x=3, y=160, width=5, height=40)

search_entry = ctk.CTkEntry(master=head, width=410, font=('Microsoft Yahei UI Light', 12, 'bold'),
                       placeholder_text=" Rechercher : ", height=38, border_width=1,
                       corner_radius=0)
search_entry.place(x=145, y=19)
def cherche():
    search_entry.delete(0,END)
search_image = tk.PhotoImage(file='photos/search.png')
search_button = ctk.CTkButton(head, border_width=0, image=search_image, height=0, width=30,text='',
                          fg_color='#3a3aff', corner_radius=0, hover_color='blue', font=('arial', 18, 'bold'),command=cherche)
search_button.place(x=550, y=19)

def open_calender():
        calendrier = tk.Toplevel()
        calendrier.geometry('900x700+220+5')
        calendrier.resizable(False, False)
        image = Image.open("photos/calender.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(calendrier, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        calendrier.title("Calendrier 2022-2023")


def ensah():
    webbrowser.open_new('https://ensah.ma/index.php')



ensah_image = tk.PhotoImage(file='photos/Ensah.png')
ensah_bttn = ctk.CTkButton(main, border_width=1, image=ensah_image, height=80, width=120,text_color='#606062',compound='left',
                          fg_color='white', corner_radius=10, hover_color='#eaefff', font=('arial', 18, 'bold'),text='     Ensah              ',command=ensah)
ensah_bttn.place(x=670, y=70)



calendrier_image = tk.PhotoImage(file='photos/calendrier-blue.png')
calendrier_bttn = ctk.CTkButton(main, border_width=1, image=calendrier_image, height=80, width=120,text_color='#606062',compound='left',
                          fg_color='white', corner_radius=10, hover_color='#eaefff', font=('arial', 18, 'bold'),text='    Calendrier       ',command=open_calender)
calendrier_bttn.place(x=670, y=170)


actualtiee_image = tk.PhotoImage(file='photos/actualitee.png')
actualie_bttn = ctk.CTkButton(main, border_width=1, image=actualtiee_image, height=80, width=120,text_color='#606062',compound='left',
                          fg_color='white', corner_radius=10, hover_color='#eaefff', font=('arial', 18, 'bold'),text='    Actualité          ',command=actualite)
actualie_bttn.place(x=670, y=275)

cal = Calendar(main, selectmode="day", date_pattern="mm/dd/y", year=2023, month=4, day=4,
                   normalbackground='#eaefff', normalforeground='blue', weekendforeground='blue'
                   , background="#eaefff", foreground="blue")
cal.place(x=670,y=375)



#plot

with open('login_nbr.txt', 'r') as f:
    data = f.readlines()[1:]
# separate date and number_of_logins into separate lists
dates = []
logins = []
for d in data:
    date, num_logins = d.strip().split(':')
    dates.append(date)
    logins.append(int(num_logins))
if len(dates) > 6:
    dates = dates[-6:]
    logins = logins[-6:]

figure = Figure(figsize=(6, 4))
figure_plot = figure.add_subplot(111)
figure_plot.plot(dates, logins,color='#3a3aff', marker='o')
figure_plot.fill_between(dates, logins, color='#eaefff')
figure_plot.figure.autofmt_xdate()
figure_plot.figure.tight_layout(pad=2.0)
line_graph = FigureCanvasTkAgg(figure, master=main)
line_graph.get_tk_widget().place(x=0, y=100)
line_graph.draw()




# emploi_field--------------------------------------------------------------------------------------------------------------------------------------------------
def emploi_page():
    emploi_frame = tk.Frame(main, bg='white')
    titre_label = Label(emploi_frame, text=' Emplois du temps', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=30)  # •

    def open_civil1():
        civil1_s2 = tk.Toplevel()
        civil1_s2.geometry('900x700+220+5')
        civil1_s2.resizable(False, False)
        image = Image.open("emplois/civil1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(civil1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        civil1_s2.title("Emploi du temps GC1-s2")

    button_civil1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                  , height=50, width=160, hover_color='white',
                                  text='• Genie civile 1 ', font=('', 17, 'bold', 'underline'), text_color='#565659',
                                  corner_radius=10,
                                  command=open_civil1)
    button_civil1.place(x=20, y=150)

    def open_civil2():
        civil2_s4 = tk.Toplevel()
        civil2_s4.geometry('900x700+220+5')
        civil2_s4.resizable(False, False)
        image = Image.open("emplois/GC2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(civil2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        civil2_s4.title("Emploi du temps GC2-s4")

    button_civil2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                  , height=50, width=160, hover_color='white',
                                  text='• Genie civile 2 ', font=('', 17, 'bold', 'underline'), text_color='#565659',
                                  corner_radius=10,
                                  command=open_civil2)
    button_civil2.place(x=20, y=200)

    def open_gee1():
        gee1_s2 = tk.Toplevel()
        gee1_s2.geometry('900x700+220+5')
        gee1_s2.resizable(False, False)
        image = Image.open("emplois/GEE1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gee1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gee1_s2.title("Emploi du temps GEE1-s2")

    button_gee1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                , height=50, width=160, hover_color='white',
                                text='• Génie de l\'eau et de l\'Environnement 1 ', font=('', 17, 'bold', 'underline'),
                                text_color='#565659', corner_radius=10,
                                command=open_gee1)
    button_gee1.place(x=30, y=250)

    def open_gee2():
        gee2_s4 = tk.Toplevel()
        gee2_s4.geometry('900x700+220+5')
        gee2_s4.resizable(False, False)
        image = Image.open("emplois/GEE2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gee2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gee2_s4.title("Emploi du temps GEE2-s4")

    button_gee2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                , height=50, width=160, hover_color='white',
                                text='• Génie de l\'eau et de l\'Environnement 2 ', font=('', 17, 'bold', 'underline'),
                                text_color='#565659', corner_radius=10,
                                command=open_gee2)
    button_gee2.place(x=30, y=300)

    def open_geer1():
        geer1_s2 = tk.Toplevel()
        geer1_s2.geometry('900x700+220+5')
        geer1_s2.resizable(False, False)
        image = Image.open("emplois/GEER1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(geer1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        geer1_s2.title("Emploi du temps GEER1-s2")

    button_geer1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                 , height=50, width=160, hover_color='white',
                                 text='• Génie Energétique et Energies renouvelables 1',
                                 font=('', 17, 'bold', 'underline'), text_color='#565659', corner_radius=10,
                                 command=open_geer1)
    button_geer1.place(x=30, y=350)

    def open_geer2():
        geer2_s4 = tk.Toplevel()
        geer2_s4.geometry('900x700+220+5')
        geer2_s4.resizable(False, False)
        image = Image.open("emplois/GEER2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(geer2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        geer2_s4.title("Emploi du temps GEER2-s4")

    button_geer2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                                 , height=50, width=160, hover_color='white',
                                 text='• Génie Energétique et Energies renouvelables',
                                 font=('', 17, 'bold', 'underline'), text_color='#565659', corner_radius=10,
                                 command=open_geer2)
    button_geer2.place(x=30, y=400)

    def open_GI1():
        gi1_s2 = tk.Toplevel()
        gi1_s2.geometry('900x700+220+5')
        gi1_s2.resizable(False, False)
        image = Image.open("emplois/GI1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gi1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gi1_s2.title("Emploi du temps GI1-s2")

    button_gi1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Génie informatique 1 ', font=('', 17, 'bold', 'underline'), text_color='#565659',
                               corner_radius=10,
                               command=open_GI1)
    button_gi1.place(x=500, y=150)

    def open_gi2():
        gi2_s4 = tk.Toplevel()
        gi2_s4.geometry('900x700+220+5')
        gi2_s4.resizable(False, False)
        image = Image.open("emplois/GI2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gi2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gi2_s4.title("Emploi du temps GI2-s4")

    button_gi2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Génie informatique 2 ', font=('', 17, 'bold', 'underline'), text_color='#565659',
                               corner_radius=10,
                               command=open_gi2)
    button_gi2.place(x=500, y=200)

    def open_gm1():
        gm1_s2 = tk.Toplevel()
        gm1_s2.geometry('900x700+220+5')
        gm1_s2.resizable(False, False)
        image = Image.open("emplois/GM1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gm1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gm1_s2.title("Emploi du temps GM1-s2")

    button_gm1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Génie Mécanique 1', font=('', 17, 'bold', 'underline'), text_color='#565659',
                               corner_radius=10,
                               command=open_gm1)
    button_gm1.place(x=500, y=250)

    def open_gm2():
        gm2_s4 = tk.Toplevel()
        gm2_s4.geometry('900x700+220+5')
        gm2_s4.resizable(False, False)
        image = Image.open("emplois/GM2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(gm2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        gm2_s4.title("Emploi du temps GM2-s4")

    button_gm2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Génie Mécanique 2', font=('', 17, 'bold', 'underline'), text_color='#565659',
                               corner_radius=10,
                               command=open_gm2)
    button_gm2.place(x=500, y=300)

    def open_ID1():
        id1_s2 = tk.Toplevel()
        id1_s2.geometry('900x700+220+5')
        id1_s2.resizable(False, False)
        image = Image.open("emplois/ID1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(id1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        id1_s2.title("Emploi du temps ID1-s2")

    button_id1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Ingénierie des données 1', font=('', 17, 'bold', 'underline'),
                               text_color='#565659', corner_radius=10,
                               command=open_ID1)
    button_id1.place(x=500, y=350)

    def open_ID2():
        id2_s4 = tk.Toplevel()
        id2_s4.geometry('900x700+220+5')
        id2_s4.resizable(False, False)
        image = Image.open("emplois/ID2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(id2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        id2_s4.title("Emploi du temps ID2-s4")

    button_id2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Ingénierie des données 2', font=('', 17, 'bold', 'underline'),
                               text_color='#565659', corner_radius=10,
                               command=open_ID2)
    button_id2.place(x=500, y=400)

    def open_CP1():
        cp1_s2 = tk.Toplevel()
        cp1_s2.geometry('900x700+220+5')
        cp1_s2.resizable(False, False)
        image = Image.open("emplois/AP1.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(cp1_s2, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        cp1_s2.title("Emploi du temps CP1-s2")

    button_cp1 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Première Année Cycle Préparatoire ', font=('', 17, 'bold', 'underline'),
                               text_color='#565659', corner_radius=10,
                               command=open_CP1)
    button_cp1.place(x=30, y=450)

    def open_CP2():
        cp2_s4 = tk.Toplevel()
        cp2_s4.geometry('900x700+220+5')
        cp2_s4.resizable(False, False)
        image = Image.open("emplois/AP2.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(cp2_s4, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=0, y=0)
        cp2_s4.title("Emploi du temps CP2-s4")

    button_cp2 = ctk.CTkButton(emploi_frame, border_width=0, fg_color='white'
                               , height=50, width=160, hover_color='white',
                               text='• Deuxième Année Cycle Préparatoire ', font=('', 17, 'bold', 'underline'),
                               text_color='#565659', corner_radius=10,
                               command=open_CP2)
    button_cp2.place(x=500, y=450)

    semestre_label = Label(emploi_frame, text='Semestre : printemps', font=('arial', 12), fg='#0a7f4c',
                           bg='white')
    semestre_label.place(x=40, y=120)

    annee_label = Label(emploi_frame, text='Année Universitaire : 2023/2024', font=('arial', 12), fg='#0a7f4c',
                        bg='white')
    annee_label.place(x=730, y=500)

    emploi_frame.place(x=0, y=0, height=600, width=1200)


def emploi_click(emploi):
    hidden()
    emploi_lab.configure(bg='blue')
    button_emploi.configure(text_color='blue')
    button_emploi.configure(image=emploi_blue)
    emploi()


emploi_gris = tk.PhotoImage(file='photos/emploi_image_gris.png')
button_emploi = ctk.CTkButton(side, border_width=0, image=emploi_gris, fg_color='#eaefff'
                              , compound="left", height=50, width=160, hover_color='#eaefff',
                              text=' Emploi', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                              command=lambda: emploi_click(emploi_page))

emploi_blue = tk.PhotoImage(file='photos/emploi_image_blue.png')
button_emploi.place(x=4, y=230)

emploi_lab = tk.Label(side, text='', bg='#eaefff')
emploi_lab.place(x=3, y=230, width=5, height=40)


def create_button(frame,name,x,y,fonc=None):
    button1 = ctk.CTkButton(frame, border_width=0, fg_color='white'
                            , height=50, width=100, hover_color='white',
                            text=name, font=('', 17, 'bold'),
                            text_color='#3456ce', corner_radius=10,command=fonc)
    button1.place(x=x, y=y)
def dessin():
    webbrowser.open("D:\PycharmProjects\gestion_etudiants\pdf\Dessin, architecture.pdf")
def frame1():
    button_frame = tk.Frame(main, bg='white')
    button_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button_frame, '• Dessin, architecture',x=40, y=10,fonc=dessin)
    create_button(button_frame, '• Langues et Communication 1  ', x=40, y=50)
    create_button(button_frame, '• Matériaux de construction', x=40, y=90)
    create_button(button_frame, '• Mathématiques de l\'ingénieur', x=40, y=130)
    create_button(button_frame, '• Mécanique des Fluides et des Solides', x=400, y=10)
    create_button(button_frame, '• Urbanisme, Topographie  ', x=400, y=50)
    create_button(button_frame, '• Résistance des Matériaux 1Dessin, architecture ', x=400,y=90)
    create_button(button_frame, '•  Programmation événementielle et Initiations aux bases de données ', x=400, y=130)





def frame2():
    button2_frame = tk.Frame(main, bg='white')
    button2_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button2_frame, '• Béton Armé 1', x=40, y=10)
    create_button(button2_frame, '• Comptabilité général et analytique  ', x=40, y=50)
    create_button(button2_frame, '• Equation de la physique mathématiques', x=40, y=90)
    create_button(button2_frame, '• Géotechnique 1', x=40, y=130)
    create_button(button2_frame, '• Langues et Communication 2', x=400, y=10)
    create_button(button2_frame, '• Logistique et transport : routes 1  ', x=400, y=50)
    create_button(button2_frame, '• Résistance des Matériaux 2 ', x=400, y=90)
    create_button(button2_frame, '•  Probabilité Statistiques et Recherche Opérationnelle ', x=400, y=130)


def frame3():
    button3_frame = tk.Frame(main, bg='white')
    button3_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button3_frame, '• Béton Armé 2', x=40, y=10)
    create_button(button3_frame, '• Géotechnique 2 et Hydraulique Souterraine ', x=40, y=50)
    create_button(button3_frame, '• Hydraulique et Machines Hydrauliques', x=40, y=90)
    create_button(button3_frame, '• Hydrologie', x=40, y=130)
    create_button(button3_frame, '• Langues et Communication 3', x=400, y=10)
    create_button(button3_frame, '• Résistance des Matériaux 3  ', x=400, y=50)
    create_button(button3_frame, '• Stratégie de gestion et gestion de l’entreprise ', x=400, y=90)
    create_button(button3_frame, '• Voirie, réseaux divers et éclairagisme', x=400, y=130)

def frame4():
    button4_frame = tk.Frame(main, bg='white')
    button4_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button4_frame, '• Béton précontraint', x=40, y=10)
    create_button(button4_frame, '• Construction Métallique 1  ', x=40, y=50)
    create_button(button4_frame, '• Gestion et Analyse de Projets', x=40, y=90)
    create_button(button4_frame, '• Hydraulique Urbaine', x=40, y=130)
    create_button(button4_frame, '• Marchés publics et droit social', x=400, y=10)
    create_button(button4_frame, '• Modélisations Numériques ', x=400, y=50)
    create_button(button4_frame, '• Route 2 ', x=400, y=90)
    create_button(button4_frame, '• Pratiques des Constructions et Installations Electriques', x=400, y=130)

def frame5():
    button5_frame = tk.Frame(main, bg='white')
    button5_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button5_frame, '• Analyse numérique matricielle\net Statistique Inférentielle', x=40, y=20)
    create_button(button5_frame, '• Architecture des ordinateurs\net systèmes d’exploitation ', x=40, y=80)
    create_button(button5_frame, '• Théorie des langages et compilation', x=40, y=140)


    create_button(button5_frame, '• Structure de données et Algorithmique avancée' , x=400, y=20)
    create_button(button5_frame, '• Systèmes d’Information et Bases de Données', x=400, y=80)
    create_button(button5_frame, '• Communication Professionnelle et Soft Skills I', x=400, y=140)



def frame6():
    button6_frame = tk.Frame(main, bg='white')

    def mining():
        webbrowser.open("D:\PycharmProjects\gestion_etudiants\pdf\Data_mining.pdf")
    button6_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button6_frame, '• Administration et Optimisation des Bases de Données', x=40, y=20)
    create_button(button6_frame, '• Data Mining ', x=40, y=60, fonc=mining)
    create_button(button6_frame, '• Entreprenariat I', x=40, y=100)

    def python():
        webbrowser.open("D:\PycharmProjects\gestion_etudiants\pdf\Programmation Python.pdf")

    create_button(button6_frame, '• Programmation Python / Les bases du Web' , x=500, y=20,fonc=python)
    create_button(button6_frame, '• Programmation Orientée Objet Java', x=500, y=60)
    create_button(button6_frame, '• Statistique en grande dimension', x=500, y=100)


def frame7():
    button7_frame = tk.Frame(main, bg='white')
    button7_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button7_frame, '• Architecture Logicielle et UML', x=40, y=20)
    create_button(button7_frame, '• Bases de données avancées ', x=40, y=60)
    create_button(button7_frame, '• Fondements du Big Data Communication Professionnelle et Soft Skills -II-', x=40, y=100)

    create_button(button7_frame, '• Intelligence Artificielle I – Machine Learning' , x=400, y=20)
    create_button(button7_frame, '• Communication Professionnelle et Soft Skills -II-', x=400, y=60)
    create_button(button7_frame, '• Modélisation Stochastique\Techniques Mathématiques d’Optimisation', x=400, y=100)


def frame8():
    button8_frame = tk.Frame(main, bg='white')
    button8_frame.place(x=0, y=360, height=350, width=1200)

    create_button(button8_frame, '• Intelligence Artificielle II – Deep Learning', x=40, y=20)
    create_button(button8_frame, '• Big Data Avancées ', x=40, y=60)
    create_button(button8_frame, '• Data Warehouse et Data Lake', x=40, y=100)


    create_button(button8_frame, '• Applications Web avancées avec Java et Spring' , x=400, y=20)
    create_button(button8_frame, '• Entreprenariat II', x=400, y=60)
    create_button(button8_frame, '• Traitement Automatique de Langue (TAL) naturelle et ses applications', x=400, y=100)




# cours_field---------------------------------------------------------------------------------------------------------------
def cours_page():
    global niveau_gc,niveau_gi,niveau_id,niveau_geer,niveau_gee,niveau_gm,niveau_cp
    cours_frame = tk.Frame(main, bg='white')

    titre_label = Label(cours_frame, text=' Consultation des cours', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=30)  # •

    sous_titre_label = Label(cours_frame, text=' *Veuillez saisir tous les critères de recherche', font=('arial', 11),
                             fg='red',
                             bg='white')
    sous_titre_label.place(x=40, y=90)

    # Options for first dropdown
    filiere = ['', "Génie Civil", "Génie Informatique", "Ingénierie des données",
               "Génie énergétique et énergies renouvelables",
               "Génie de l’Eau et de l’Environnement", "Génie Mécanique", 'Cycle préparatoire']

    niveau_gc = ["Génie Civil 1 ", "Génie Civil 2 ", "Génie Civil 3 Option HYD", "Génie Civil 3 Option BPC"]
    niveau_gi = ["Génie Informatique 1 ", "Génie Informatique 2 ", "Génie Informatique 3 Option GL ",
                 "Génie Informatique 3 Option BI", "Génie Informatique 3 Option Médias et Interactions"]
    niveau_id = ['Ingénierie des données 1', 'Ingénierie des données 2', 'Ingénierie des données 3 ']
    niveau_geer = ["Génie énergétique et énergies renouvelables 1 ", "Génie énergétique et énergies renouvelables 2 ",
                   "Génie énergétique et énergies renouvelables 3 "]
    niveau_gee = ["Génie  de l’Eau et de l’Environnement 1 ", "Génie  de l’Eau et de l’Environnement 2 ",
                  "Génie de l’Eau et de l’Environnement 3 "]
    niveau_gm = ["Génie Mécanique 1 ", "Génie Mécanique 2 ", "Génie Mécanique 3 "]
    niveau_cp = ["Première année préparatoire", "Deuxiéme année préparatoire"]

    # Options for second dropdown
    semestre1 = ["1", '2']
    semestre2 = ['3', '4']

    # Callback function for first dropdown
    def pick_filiere(e):
        # Add options based on the selected value in the first dropdown
        if filiere_menu.get() == "Génie Civil":
            combo_niveau.configure(values=niveau_gc)
        elif filiere_menu.get() == "Génie Informatique":
            combo_niveau.configure(values=niveau_gi)
        elif filiere_menu.get() == "Ingénierie des données":
            combo_niveau.configure(values=niveau_id)
        elif filiere_menu.get() == "Génie énergétique et énergies renouvelables":
            combo_niveau.configure(values=niveau_geer)
        elif filiere_menu.get() == "Génie de l’Eau et de l’Environnement":
            combo_niveau.configure(values=niveau_gee)
        elif filiere_menu.get() == "Génie Mécanique":
            combo_niveau.configure(values=niveau_gm)
        elif filiere_menu.get() == "Cycle préparatoire":
            combo_niveau.configure(values=niveau_cp)

    def pick_semestre(e):
        # Add options based on the selected value in the first dropdown
        if combo_niveau.get() == "Génie Civil 1 " or combo_niveau.get() == "Génie Informatique 1" or combo_niveau.get() == "Ingénierie des données 1" or combo_niveau.get() == "Génie énergétique et énergies renouvelables 1 " or combo_niveau.get() == "Génie de l’Eau et de l’Environnement 1 " or combo_niveau.get() == "Génie Mécanique 1" or combo_niveau.get() == "Première année préparatoire":
            combo_semestre.configure(values=semestre1)
        elif combo_niveau.get() == "Génie Civil 2 " or combo_niveau.get() == "Génie Informatique 2" or combo_niveau.get() == "Ingénierie des données 2" or combo_niveau.get() == "Génie énergétique et énergies renouvelables 2" or combo_niveau.get() == "Génie de l’Eau et de l’Environnement 2" or combo_niveau.get() == "Génie Mécanique 2" or combo_niveau.get() == "Deuxiéme année préparatoire":
            combo_semestre.configure(values=semestre2)
        elif combo_niveau.get() == "Génie Civil 3 Option HYD" or combo_niveau.get() == "Génie Civil 3 Option BPC" or combo_niveau.get() == "Génie Informatique 3 Option GL" or combo_niveau.get() == "Génie Informatique 3 Option BI" or combo_niveau.get() == "Génie Informatique 3 Option Médias et Interactions" or combo_niveau.get() == 'Ingénierie des données 3 ' or combo_niveau.get() == "Génie énergétique et énergies renouvelables 3 " or combo_niveau.get() == "Génie de l’Eau et de l’Environnement 3 " or combo_niveau.get() == "Génie Mécanique 3 ":
            combo_semestre.configure(values=["5"])

    def pick_modul(e):
        if filiere_menu.get() == "Génie Civil" and combo_niveau.get() == "Génie Civil 1 " and combo_semestre.get() == "1":
            frame1()
        elif filiere_menu.get() == "Génie Civil" and combo_niveau.get() == "Génie Civil 1 " and combo_semestre.get() == "2":
            frame2()
        elif filiere_menu.get() == "Génie Civil" and combo_niveau.get() == "Génie Civil 2 " and combo_semestre.get() == "3":
            frame3()
        elif filiere_menu.get() == "Génie Civil" and combo_niveau.get() == "Génie Civil 2 " and combo_semestre.get() == "4":
            frame4()
        if filiere_menu.get() == "Ingénierie des données" and combo_niveau.get() == 'Ingénierie des données 1' and combo_semestre.get() == "1":
            frame5()
        elif filiere_menu.get() == "Ingénierie des données"  and combo_niveau.get() == 'Ingénierie des données 1' and combo_semestre.get() == "2":
            frame6()
        elif filiere_menu.get() == "Ingénierie des données"  and combo_niveau.get() == 'Ingénierie des données 2'and combo_semestre.get() == "3":
            frame7()
        elif filiere_menu.get() == "Ingénierie des données"  and combo_niveau.get() == 'Ingénierie des données 2' and combo_semestre.get() == "4":
            frame8()



        #elif filiere_menu.get() == "Génie Civil" and combo_niveau.get() == " Génie Civil 3 Option HYD " and combo_semestre.get() == "5":
         #   frame3()


    # Create the first dropdown
    filiere_label = ctk.CTkLabel(master=cours_frame, text='Filiere :', bg_color='white', font=('arial', 15))
    filiere_label.place(x=190, y=153)

    filiere_menu = ctk.CTkOptionMenu(cours_frame, values=filiere, width=400, height=40, bg_color='white',
                                     button_hover_color='#3a3aff',
                                     fg_color='#bdbfc6', command=pick_filiere, button_color='#3a3aff', font=('', 13),
                                     text_color=('#091226'), dropdown_fg_color='#eeefef',
                                     dropdown_hover_color='#d7dcdc')
    filiere_menu.place(x=270, y=150)

    # Create the second dropdown
    semestre_label = ctk.CTkLabel(master=cours_frame, text=' Niveau :', bg_color='white', font=('arial', 15))
    semestre_label.place(x=190, y=233)

    combo_niveau = ctk.CTkOptionMenu(cours_frame, values=[" "], width=400, height=40, bg_color='white',
                                     button_hover_color='#3a3aff', command=pick_semestre,
                                     fg_color='#bdbfc6', button_color='#3a3aff', font=('', 13),
                                     text_color='#091226', dropdown_fg_color='#eeefef', dropdown_hover_color='#d7dcdc')
    combo_niveau.place(x=270, y=230)

    semestre_label = ctk.CTkLabel(master=cours_frame, text=' Semestre:', bg_color='white', font=('arial', 15))
    semestre_label.place(x=180, y=313)

    combo_semestre = ctk.CTkOptionMenu(cours_frame, width=400, values=[" "], height=40, bg_color='white',
                                       button_hover_color='#3a3aff',
                                       fg_color='#bdbfc6', button_color='#3a3aff', font=('', 13),
                                       text_color='#091226', dropdown_fg_color='#eeefef',
                                       dropdown_hover_color='#d7dcdc', command=pick_modul)
    combo_semestre.place(x=270, y=310)

    cours_frame.place(x=0, y=0, height=600, width=1200)


def cours_click(cours):
    hidden()
    cours_lab.configure(bg='blue')
    button_cours.configure(text_color='blue')
    button_cours.configure(image=cours_blue)
    cours()


cours_gris = tk.PhotoImage(file='photos/cours_gris.png')
button_cours = ctk.CTkButton(side, border_width=0, image=cours_gris, fg_color='#eaefff'
                             , compound="left", height=50, width=160, hover_color='#eaefff',
                             text=' Cours ', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                             command=lambda: cours_click(cours_page))

cours_blue = tk.PhotoImage(file='photos/cours_blue.png')
button_cours.place(x=4, y=300)

cours_lab = tk.Label(side, text='', bg='#eaefff')
cours_lab.place(x=3, y=300, width=5, height=40)


# Notes_field--------------------------------------------------------------------------------------------------------------------------------
def notes_page():
    notes_frame = tk.Frame(main, bg='white')
    titre_label = Label(notes_frame, text=' Tableau d\'affichage des notes', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=30)
    choix = ['',"Délibérations", 'Affichage par module']
    semestre1 = ['',"1", '2']
    semestre2 = ['','3', '4']

    gc = ["Génie Civil 1 ", "Génie Civil 2 ", "Génie Civil 3 Option HYD", "Génie Civil 3 Option BPC"]
    gi = ["Génie Informatique 1 ", "Génie Informatique 2 ", "Génie Informatique 3 Option GL ",
                 "Génie Informatique 3 Option BI", "Génie Informatique 3 Option Médias et Interactions"]
    id = ['Ingénierie des données 1', 'Ingénierie des données 2', 'Ingénierie des données 3 ']
    geer = ["Génie énergétique et énergies renouvelables 1 ", "Génie énergétique et énergies renouvelables 2 ",
                   "Génie énergétique et énergies renouvelables 3 "]
    gee = ["Génie  de l’Eau et de l’Environnement 1 ", "Génie  de l’Eau et de l’Environnement 2 ",
                  "Génie de l’Eau et de l’Environnement 3 "]
    gm = ["Génie Mécanique 1 ", "Génie Mécanique 2 ", "Génie Mécanique 3 "]
    cp = ["Première année préparatoire", "Deuxiéme année préparatoire"]
    def pick_choix1(e):
        global combo_sem
        if combo_niveau.get() == "Génie Civil 1 " and combo_choix.get() == "Délibérations":
            dele_gc = tk.Toplevel()
            dele_gc.geometry('900x1300+220+5')
            dele_gc.resizable(False, False)
            image = Image.open("notes/deleberation/GC1-DELE.jpg")
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(dele_gc, image=photo)
            label.image = photo  # Store the photo as an attribute of the label
            label.place(x=0, y=0)
            dele_gc.title("Calendrier 2022-2023")
        if combo_niveau.get() == "Génie Civil 1 " and combo_choix.get() == "Affichage par module":
            combo_sem = ctk.CTkOptionMenu(civil_frame, values=semestre1, width=400, height=40, bg_color='white',
                                          button_hover_color='#3a3aff', command=pick_choix2,
                                          fg_color='#bdbfc6', button_color='#3a3aff', font=('', 13),
                                          text_color='#091226', dropdown_fg_color='#eeefef',
                                          dropdown_hover_color='#d7dcdc')

            combo_sem.place(x=270, y=260)



    def pick_choix2(e):
            if  combo_niveau.get() == "Génie Civil 1 " and combo_choix.get() == "Affichage par module"  and combo_sem.get() == "1":
                frame1()
            elif combo_niveau.get() == "Génie Civil 1 " and combo_choix.get() == "Affichage par module"  and combo_sem.get() == "2":
                frame2()


    def civil():
        global combo_niveau,combo_choix,civil_frame,combo_sem
        civil_frame = tk.Frame(main, bg='white')
        titre_label = Label(civil_frame, text=' Génie Civil ', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
        titre_label.place(x=20, y=30)

        civil_frame.place(x=0, y=30, height=600, width=1200)

        combo_niveau = ctk.CTkOptionMenu(civil_frame, values=gc,width=400, height=40, bg_color='white',
                                         button_hover_color='#3a3aff',
                                         fg_color='#bdbfc6', button_color='#3a3aff', font=('', 13),
                                         text_color='#091226', dropdown_fg_color='#eeefef',
                                         dropdown_hover_color='#d7dcdc')
        combo_niveau.place(x=270, y=100)

        combo_choix = ctk.CTkOptionMenu(civil_frame, values=choix, width=400, height=40, bg_color='white',
                                         button_hover_color='#3a3aff', command=pick_choix1,
                                         fg_color='#bdbfc6', button_color='#3a3aff', font=('', 13),
                                         text_color='#091226', dropdown_fg_color='#eeefef',
                                         dropdown_hover_color='#d7dcdc')
        combo_choix.place(x=270, y=180)



        civil_frame.place(x=0, y=30, height=600, width=1200)

#the front 1 of notes---------------------------------------------------------------
    note_gc = tk.PhotoImage(file='notes/gc.png')
    button_notegc = ctk.CTkButton(notes_frame, border_width=0, image=note_gc, fg_color='#eaefff'
                                 , compound="left", height=70, width=200, hover_color='#dee3f2',
                                 text='         Génie civil                  ', font=('', 18, 'bold'), text_color='#565659', corner_radius=10,command=civil)
    button_notegc.place(x=60, y=100)


    note_gi = tk.PhotoImage(file='notes/gi.png')
    button_notegi = ctk.CTkButton(notes_frame, border_width=0, image=note_gi, fg_color='#eaefff'
                                  , compound="left", height=70, width=200, hover_color='#dee3f2',
                                  text='        Génie informatique                ', font=('', 18, 'bold'), text_color='#565659', corner_radius=10)
    button_notegi.place(x=450, y=100)


    note_id = tk.PhotoImage(file='notes/id.png')
    button_noteid = ctk.CTkButton(notes_frame, border_width=0, image=note_id, fg_color='#eaefff'
                                  , compound="left", height=70, width=200, hover_color='#dee3f2',
                                  text='  Ingénierie des données      ', font=('', 18, 'bold'), text_color='#565659', corner_radius=10)
    button_noteid.place(x=60, y=200)

    note_geer = tk.PhotoImage(file='notes/geer.png')
    button_notegeer = ctk.CTkButton(notes_frame, border_width=0, image=note_geer, fg_color='#eaefff'
                                  , compound="left", height=70, width=200, hover_color='#dee3f2',
                                  text='Génie énergétique et énergies    \nrenouvelables                    ', font=('', 18, 'bold'), text_color='#565659',
                                  corner_radius=10)
    button_notegeer.place(x=450, y=200)


    note_gee = tk.PhotoImage(file='notes/gee.png')
    button_notegee = ctk.CTkButton(notes_frame, border_width=0, image=note_gee, fg_color='#eaefff'
                                    , compound="left", height=70, width=200, hover_color='#dee3f2',
                                    text='Génie de l’Eau et  \nde l’Environnement            ', font=('', 18, 'bold'),
                                    text_color='#565659',
                                    corner_radius=10)
    button_notegee.place(x=60, y=300)

    note_gm = tk.PhotoImage(file='notes/gm.png')
    button_notegm = ctk.CTkButton(notes_frame, border_width=0, image=note_gm, fg_color='#eaefff'
                                   , compound="left", height=70, width=200, hover_color='#dee3f2',
                                   text=' Génie Mécanique                         ', font=('', 18, 'bold'),
                                   text_color='#565659',
                                   corner_radius=10)
    button_notegm.place(x=450, y=300)

    note_cp = tk.PhotoImage(file='notes/cp.png')
    button_notecp = ctk.CTkButton(notes_frame, border_width=0, image=note_cp, fg_color='#eaefff'
                                  , compound="left", height=70, width=200, hover_color='#dee3f2',
                                  text='Cycle Préparatoire Intégré  ', font=('', 18, 'bold'),
                                  text_color='#565659',
                                  corner_radius=10)
    button_notecp.place(x=60, y=400)




    notes_frame.place(x=0, y=0, height=600, width=1200)
def notes_clicck(notes):
    hidden()
    button_notes.configure(text_color='blue')
    button_notes.configure(image=notes_blue)
    notes_lab.configure(bg='blue')
    notes()


notes_gris = tk.PhotoImage(file='photos/Notes_gris.png')
button_notes = ctk.CTkButton(side, border_width=0, image=notes_gris, fg_color='#eaefff'
                             , compound="left", height=50, width=160, hover_color='#eaefff',
                             text=' Notes ', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                             command=lambda: notes_clicck(notes_page))

notes_blue = tk.PhotoImage(file='photos/Notes_blue.png')
button_notes.place(x=4, y=370)

notes_lab = tk.Label(side, text='', bg='#eaefff')
notes_lab.place(x=3, y=370, width=5, height=40)


# activitee_field---------------------------------------------------------------------------------------------------------------
def butt():
    webbrowser.open_new('https:/ensah.ma/public/activitesEtudiants.php')

def activite_page():
    activite_frame = tk.Frame(main, bg='white')

    titre_label = Label(activite_frame, text=' Consultation des activitées', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=30)

    msg_label = Label(activite_frame, text='Vous pouvez consulter les activities parascolaires via le site du ENSAH ', font=('arial', 11), fg='#565659',
                           bg='white')
    msg_label.place(x=20, y=120)

    button_site = ctk.CTkButton(activite_frame, border_width=0, fg_color='#eaefff'
                                  , height=50, width=160, hover_color='#dee3f2',
                                  text='Consulter ', font=('', 17, 'bold'), text_color='blue',
                                  corner_radius=10,
                                  command=butt)
    button_site.place(x=300, y=160)
    activite_frame.place(x=0, y=0, height=600, width=1200)


def activite_click(activite_page):
    hidden()
    button_activite.configure(text_color='blue')
    button_activite.configure(image=activite_blue)
    activite_lab.configure(bg='blue')
    activite_page()

activite_blue = tk.PhotoImage(file='photos/activités_blue.png')
activite_gris = tk.PhotoImage(file='photos/activités-gris.png')
button_activite = ctk.CTkButton(side, border_width=0, image=activite_gris, fg_color='#eaefff'
                                , compound="left", height=50, width=160, hover_color='#eaefff',
                                text='Activité ', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                                command=lambda: activite_click(activite_page))
button_activite.place(x=4, y=440)

activite_lab = tk.Label(side, text='', bg='#eaefff')
activite_lab.place(x=3, y=440, width=5, height=40)


# clubs-------------------------------------------------------------------------------------

def clubs_page():
    clubs_frame = tk.Frame(main, bg='white')
    titre_label = Label(clubs_frame, text=' Consultation des clubs', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=30) # •

    text = tk.Text(clubs_frame, font=('Calibri', 12), border=0, fg='black', bg='white')
    text.insert(tk.END, 'Les clubs sont des groupes d\'étudiants qui se réunissent régulièrement pour explorer un intérêt commun ou pour participer à une activité spécifique')
    text.insert(INSERT,'\nIls peuvent se concentrer sur des sujets académiques tels que les mathématiques,les sciences ou l\'histoire, ou sur des activités récréatives et\nartistiques telles que la musique, la danse ou le théâtre.')
    text.insert(INSERT,"\nLes clubs  offrent aux etudiants l'opportunité de se connecter avec des pairs partageant les mêmes intérêts, de développer leurs compétences de\ns'impliquer dans leur communauté et de s'épanouir en dehors de la salle de classe.Ils peuvent également contribuer à renforcer le sentiment\nd'appartenance à l'école et à promouvoir un environnement d'apprentissage inclusif et diversifié.")
    text.insert(INSERT,"\n\nParmi les clubs les plus compétitifs de l\'école, on peut mentionner:")
    text.configure(state='disabled', spacing1=8)
    text.place(x=15, y=90, height=260, width=1200)

    def club_GC():
        club1_frame=tk.Frame(main, bg='white')
        image = Image.open("photos/GC_logo.jpeg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(club1_frame, image=photo)
        label.image = photo  # Store the photo as an attribute of the label
        label.place(x=50, y=50)

        text = tk.Text(club1_frame, font=('Calibri', 12), border=0, fg='black', bg='white')

        text.insert(INSERT,"Le Club Génie Civil est un club pédagogique de l'Ecole Nationale des Sciences Appliquées d'AlHoceima qui vise à développer la culture scientifique\net technique en Génie Civil chez les élèves ingénieurs de l'école.")
        text.insert(INSERT,"En plus des enseignements théoriques et pratiques, le Club organise des visites\naux chantiers(Grand Stade d' Al-Hoceima, Barrage oued Ghiss, Pole universitaire Ait Kamra...), des conférences,des ateliers et un évènement\nannuel du Génie Civil ENSAH CONSTRUCTORS au sein de l'ENSAd'Al-Hoceima.")
        text.insert(INSERT,"Le club a pour but d'offrir aux étudiants la possibilité de travailler\nensemble pour le développement de leur formation en génie civil dans un esprit de service et de camaraderie.\nSes objectifs sont:")
        text.insert(INSERT,"\n	• Faire connaître le GénieCivil.\n	•Créer un environnement étudiant propice à l'élargissement des partenariats avec les clubs de génie civil d'autres écoles d'ingénieurs.\n	•Participer aux manifestations et concours scientifiques à l'échelle nationale.\n	•Programmation de rencontres, conférences et séminaires en relation avec la spécialité.\n	•Organisation de stages de formation et de sorties pédagogiques.")
        text.configure(state='disabled', spacing1=6)
        text.place(x=15, y=150, height=400, width=1200)

        def inscri():
            lab = ctk.CTkLabel(club1_frame, text_color='red',font=('',15),
                               text='L\'inscription est n\'est pas ouvert actuellement.',
                               bg_color='white')
            lab.place(x=330, y=520)
        button = ctk.CTkButton(club1_frame, border_width=0, fg_color='#0c9f5f'
                                  , compound="left", height=50, width=150, hover_color='#0a7f4c',
                                  text='   Inscription    ', font=('', 18, 'bold'),
                                  text_color='white', corner_radius=10, command=inscri)
        button.place(x=400, y=460)

        club1_frame.place(x=0, y=0, height=600, width=1200)

    button_01 = ctk.CTkButton(clubs_frame, border_width=0, fg_color='#eaefff'
                                  , compound="left", height=70, width=150, hover_color='#dee3f2',
                                  text=' Génie civil   ', font=('', 18, 'bold'),
                                  text_color='blue', corner_radius=10,command=club_GC)
    button_01.place(x=50, y=350)

    button_enactus = ctk.CTkButton(clubs_frame, border_width=0, fg_color='#eaefff'
                              , compound="left", height=70, width=150, hover_color='#dee3f2',
                              text=' enactus club ', font=('', 18, 'bold'),
                              text_color='blue', corner_radius=10)
    button_enactus.place(x=230, y=350)

    button_css = ctk.CTkButton(clubs_frame, border_width=0, fg_color='#eaefff'
                                   , compound="left", height=70, width=150, hover_color='#dee3f2',
                                   text=' css club ', font=('', 18, 'bold'),
                                   text_color='blue', corner_radius=10)
    button_css.place(x=410, y=350)

    button_cct = ctk.CTkButton(clubs_frame, border_width=0, fg_color='#eaefff'
                               , compound="left", height=70, width=150, hover_color='#dee3f2',
                               text=' cct club ', font=('', 18, 'bold'),
                               text_color='blue', corner_radius=10)
    button_cct.place(x=590, y=350)

    button_id = ctk.CTkButton(clubs_frame, border_width=0, fg_color='#eaefff'
                               , compound="left", height=70, width=150, hover_color='#dee3f2',
                               text=' data club ', font=('', 18, 'bold'),
                               text_color='blue', corner_radius=10)
    button_id.place(x=770, y=350)


    clubs_frame.place(x=0, y=0, height=600, width=1200)


def clubs_click(clubs):
    hidden()
    button_clubs.configure(text_color='blue')
    button_clubs.configure(image=clubs_blue)
    clubs_lab.configure(bg='blue')
    clubs()


clubs_gris = tk.PhotoImage(file='photos/clubs_gris.png')
button_clubs = ctk.CTkButton(side, border_width=0, image=clubs_gris, fg_color='#eaefff'
                             , compound="left", height=50, width=160, hover_color='#eaefff',
                             text=' Clubs ', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                             command=lambda: clubs_click(clubs_page))

clubs_blue = tk.PhotoImage(file='photos/clubs_blue.png')
button_clubs.place(x=4, y=510)

clubs_lab = tk.Label(side, text='', bg='#eaefff')
clubs_lab.place(x=3, y=510, width=5, height=40)


# about_us_field---------------------------------------------------------------------------------------------------------------
def about_page():
    about_frame = tk.Frame(main, bg='white')
    titre_label = Label(about_frame, text=' L\'application e-Connect de l\'ENSAH', font=('arial', 16, 'bold'), fg='#3a3aff',
                        bg='white')
    titre_label.place(x=20, y=40)

    logo = tk.PhotoImage(file='photos/logo_hananePNG.png')
    photo_logo = ctk.CTkButton(about_frame, border_width=0, image=logo, fg_color='white'
                                 ,  height=50, width=160,hover_color='white',
                                 text='', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,)
    photo_logo.place(x=350, y=70)

    text = tk.Text(about_frame, font=('Calibri', 12),border=0,fg='black', bg='#eaefff')
    text.insert(tk.END, 'Bienvenue dans notre application de gestion du système pour les étudiants')
    text.insert(INSERT, ' "e-Connect" ', ('bold_blue'))
    text.insert(INSERT,'!\nNotre application est conçue pour vous aider à gérer efficacement vos tâches et vos activités liées à vos études.L\'interface utilisateur est\nconviviale et facile à naviguer, ce qui facilite l\'utilisation de l\'application pour les utilisateurs de tous niveaux.Les informations sont stockées\ndans une base de données mySQL intégrée à l\'application pour une utilisation efficace.')
    text.insert(INSERT,"\nL\'une des caractéristiques clés de notre application est sa facilité d\'utilisation.Nous avons travaillé durs pour créer une interface utilisateur\nattrayante et facile à naviguer,permettant aux étudiants d\'accéder rapidement aux fonctionnalités dont ils ont besoin. Grâce à un agencement\n bien organisé des boutons,des menus et des options, les étudiants peuvent facilement gérer leur emploi du temps, leurs cours et leurs notes\nsans se sentir dépassés.")
    text.insert(INSERT,"\nLe noyau de l'application est développé from scratch avec le langage Python et utilisant le module Tkinter.\nAucun framework n'est utilisé, il s'agit du pur code Python.")

    text.tag_configure('bold_blue', font=('Calibri', 12, 'bold'), foreground='blue')
    text.configure(state='disabled', spacing1=6)
    text.place(x=15, y=180, height=260, width=950)

    text1 = tk.Text(about_frame, font=('Calibri', 12), border=0, fg='black', bg='white')
    text1.insert(END,"À propos du développeur:\n",('bold_red'))
    text1.insert(INSERT, "NADI HANANE")
    text1.insert(INSERT, " : Etudiante en ingénierie de données.\nEcole Nationale des Sciences Appliquées - Al HOCEIMA\nEmail: hanane.nadi@etu.uae.ac.ma")
    text1.tag_configure('bold_red', font=('Calibri', 12, 'bold'), foreground='red')
    text1.configure(state='disabled', spacing1=6)
    text1.place(x=15, y=460, height=100, width=950)
    about_frame.place(x=0, y=0, height=750, width=1200)

    about_frame.place(x=0, y=0, height=600, width=1200)

    titre_label = Label(develop_frame, text=' Dévelopée par H. NADI ', font=('arial', 10),
                        fg='white',
                        bg='white')
    titre_label.place(x=330, y=0)

def about_click(about):
    hidden()
    button_about.configure(text_color='blue')
    button_about.configure(image=about_blue)
    about_lab.configure(bg='blue')
    about()


about_gris = tk.PhotoImage(file='photos/about_gris.png')
button_about = ctk.CTkButton(side, border_width=0, image=about_gris, fg_color='#eaefff'
                             , compound="left", height=50, width=160, hover_color='#eaefff',
                             text='à propos de nous', font=('', 17, 'bold'), text_color='#565659', corner_radius=10,
                             command=lambda: about_click(about_page))

about_blue = tk.PhotoImage(file='photos/about_blue.png')

button_about.place(x=4, y=580)

about_lab = tk.Label(side, text='', bg='#eaefff')
about_lab.place(x=3, y=580, width=5, height=40)

button_dash.focus_set()

dash.mainloop()


