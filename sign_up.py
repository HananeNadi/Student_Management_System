
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import filedialog
import os
import pymysql
import re
import datetime




cne=r"^[A-Z]\d{9}$"
cin=r"^[A-Z]{1,2}\d{6}$"
phone=r"^(?:\+212|0)[5-7]\d{8}$"
email=r'^[a-zA-Z]+\.[a-zA-Z]+@etu\.uae\.ac\.ma$'
special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']
root = tk.Tk()
root.resizable(False, True)
root.geometry('760x973+250+20')
root.title("Inscription")
root.iconbitmap('logo.ico.ico')


def exit():
    root.destroy()
    import sign_in

def connect_database():

    if nameEntry.get()==''or prenomEntry.get()==''or dateEntry.get()=='' or CNEEntry.get()=='' or CINEntry.get=='' or combo_pays.get()=='' or ville.get()=='' or adressEntry.get()==''or gender_var.get=='' or phoneEntry.get()=='' or EmailEntry.get()=='' or combo_annee.get()==''or combo_niveau.get()==''or combo_filiere.get()=='' or PasswordEntry.get()==''or Password_con_Entry.get()=='' :
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='red', text='ERREUR Certains ou tous les champs sont vides, veuillez vérifier à nouveau ', bg_color='#eaefff')
        lab.place(x=170, y=1220)


    if  nameEntry.get().isalpha()==False  or len(nameEntry.get())  <= 2 or len (nameEntry.get()) > 100 :
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='ERREUR Certains ou tous les champs sont vides, veuillez vérifier à nouveau ', bg_color='#eaefff')
        lab.place(x=170, y=1210)
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='red',
                           text='ERREUR : Le champ NOM doit contenir uniquement des lettres et être compris  ',
                           bg_color='#eaefff').place(x=170, y=1210)
        labb=ctk.CTkLabel(frame.scrollable_frame,text_color='red',text='entre 2 et 100 caractères.', bg_color='#eaefff').place(x=170,y=1231)
        nameEntry.configure(border_width=1,border_color='red')


    elif prenomEntry.get().isalpha()==False or len(prenomEntry.get())  <= 2 or len (prenomEntry.get()) > 100  :
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='   ', bg_color='#eaefff')
        lab.place(x=170, y=1210)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',text='ERREUR :Le champ PRÉNOM doit contenir uniquement des lettres et être compris',
                         bg_color='#eaefff')
        lab.place(x=170, y=1210)
        labb = ctk.CTkLabel(frame.scrollable_frame, text_color='red', text=' entre 2 et 100 caractères.',
                            bg_color='#eaefff')
        labb.place(x=170, y=1231)
        prenomEntry.configure(border_width=1,border_color='red')
        nameEntry.configure(border_width=0, border_color='white')

    elif not re.match(cne,CNEEntry.get()):
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                      ', bg_color='#eaefff').place(x=170,y=1231)
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='red', text='ERREUR : Le champ CNE doit contenir une lettre majuscule suivie de 9 chiffres.                ', bg_color='#eaefff').place(x=170, y=1210)
        CNEEntry.configure(border_width=1,border_color='red')
        prenomEntry.configure(border_width=0, border_color='white')
        nameEntry.configure(border_width=0, border_color='white')


    elif not re.match(cin,CINEntry.get()):
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff',
                           text='                                                                      ',
                           bg_color='#eaefff').place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR : Le champ CIN doit contenir une ou deux lettres majuscules suivies de 6 chiffres.                      ',
                      bg_color='#eaefff').place(x=170, y=1210)
        CINEntry.configure(border_width=1,border_color='red')
        CNEEntry.configure(border_width=0, border_color='white')


    elif not re.match(phone,phoneEntry.get()):
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                      ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR :  Le champ TÉLÉPHONE  doit contenir le format +212XXXXXXXXX                                                                  ',
                      bg_color='#eaefff').place(x=170, y=1210)
        labb = ctk.CTkLabel(frame.scrollable_frame, text_color='red',
                           text=' ou 0XXXXXXXXX                                                ',
                           bg_color='#eaefff')
        labb.place(x=170, y=1231)
        phoneEntry.configure(border_width=1,border_color='red')
        CINEntry.configure(border_width=0, border_color='white')


    elif not re.match(email, EmailEntry.get()):
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                      ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR : Le champ EMAIL doit contenir une adress email de la forme                                                                ',
                      bg_color='#eaefff').place(x=170, y=1210)
        labb = ctk.CTkLabel(frame.scrollable_frame, text_color='red',
                           text='  xxxxx.xxxxx@etu.uae.ac.ma.                                                ',
                           bg_color='#eaefff')
        labb.place(x=170, y=1231)
        EmailEntry.configure(border_width=1, border_color='red')
        phoneEntry.configure(border_width=0, border_color='white')

    elif not any(ch in special_ch for ch in PasswordEntry.get())  or not any(ch.isupper() for ch in PasswordEntry.get()) or not any(ch.islower() for ch in PasswordEntry.get()) or not any(ch.isdigit() for ch in PasswordEntry.get()) or len(PasswordEntry.get()) <8 :
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                                   ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR : Le champ MOT DE PASSE doit contenir au moins 8 caractères, au moins un chiffre,                                                                      ',
                      bg_color='#eaefff').place(x=170, y=1210)
        labb = ctk.CTkLabel(frame.scrollable_frame, text_color='red', text='au moins une lettre majuscule, au moins une lettre minuscule et au moins un caractere.',
                            bg_color='#eaefff').place(x=170, y=1231)

        PasswordEntry.configure(border_width=1, border_color='red')
        EmailEntry.configure(border_width=0, border_color='white')


    elif PasswordEntry.get()!=Password_con_Entry.get() :

        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                                                                                              ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR :Les deux mots de passe doivent être identiques.                                                                                                 ',
                      bg_color='#eaefff').place(x=170, y=1210)

        Password_con_Entry.configure(border_width=1, border_color='red')
        PasswordEntry.configure(border_width=1, border_color='red')
        PasswordEntry.configure(border_width=0, border_color='white')

    elif path == '':
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                                                                                                                              ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab=ctk.CTkLabel(frame.scrollable_frame,text_color='red',
                      text='ERREUR : Veuillez importer une photo                                                                                                                     .                                           ',
                      bg_color='#eaefff').place(x=170, y=1210)
        image_button.configure(border_width=1, border_color='red')
        Password_con_Entry.configure(border_width=0, border_color='white')
        PasswordEntry.configure(border_width=0, border_color='white')

    else:
        image_button.configure(border_width=0, border_color='white')
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#eaefff', text='                                                                                 ', bg_color='#eaefff')
        lab.place(x=170, y=1231)
        lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#0a7f4c', text='Les champs ont été remplis avec succès.                 .          '
                        '                                                                                                                                                                                                             ',
                           bg_color='#eaefff').place(x=170,y=1210)
        try:
             con=pymysql.connect(host='localhost',user='root',password='hanane12345@')
             mycursor=con.cursor()
        except:
            lab = ctk.CTkLabel(frame.scrollable_frame, text_color='#0a7f4c',text='ERROR : Database connectivity issues , Please try again later  '
                                    '                                                                                                                                                                                                             ',
                               bg_color='#eaefff').place(x=170, y=1210)
            return
        try:
            query = 'create database student_management_system'
            mycursor.execute(query)
            query = 'use student_management_system'
            mycursor.execute(query)
            query = 'create table student (id int auto_increment primary key not null, nom varchar(50) , prénom varchar(50), date_de_naissance varchar(10), CNE varchar(20), CIN varchar (20) not null, Pays varchar(20), ville varchar(30), Adresse varchar(200), sexe varchar (5), Telephone varchar (20), email varchar (50), annee_de_bac varchar (4), niveau varchar (20), filiere varchar (100), mot_de_passe varchar (100), confirme_pass varchar (100),date_time,image)'


            mycursor.execute(query)
        except:
            query='use student_management_system'
            mycursor.execute(query)

        query='select * from student where CIN=%s '
        mycursor.execute(query,(CINEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            lab = ctk.CTkLabel(frame.scrollable_frame, text_color='red',
                               text='ERREUR :Le nom d\'utilisateur existe déjà.                                                                                                 ',
                               bg_color='#eaefff').place(x=170, y=1210)
        else:
            with open(image_path, 'rb') as f:
                img_data = f.read()

            query = 'insert into student(nom,prénom,date_de_naissance,CNE,CIN,Pays,ville, Adresse,sexe,Telephone,email, annee_de_bac,niveau,filiere, mot_de_passe,confirme_pass,image,date_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # get the current date and time
            now = datetime.datetime.now()
            mycursor.execute(query, (
                nameEntry.get(), prenomEntry.get(), dateEntry.get(), CNEEntry.get(), CINEntry.get(), combo_pays.get(),
                ville.get(), adressEntry.get(), gender_var.get(), phoneEntry.get(), EmailEntry.get(), combo_annee.get(),
                combo_niveau.get(), combo_filiere.get(), PasswordEntry.get(), Password_con_Entry.get(),img_data,now))

            con.commit()
            con.close()

            exit()



    



# scrollbare_field
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # bind the resize event to update the canvas size
        self.bind("<Configure>", self._on_frame_configure)

        canvas.pack(side="left", fill="both", expand=1)
        scrollbar.pack(side="right", fill="y")

    def _on_frame_configure(self, event):
        canvas_height = event.height
        self.scrollable_frame.config(height=canvas_height)



def pick_date(event):
    global cal,date_window
    date_window = tk.Toplevel()
    date_window.grab_set()
    date_window.geometry("250x220")
    date_window.resizable(False, False)
    date_window.title("choisir la date de naissance :")
    cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y", year=2023, month=4, day=4)
    cal.place(x=0, y=0)
    submit = tk.Button(date_window, text="Submit", command=grab_date)
    submit.place(x=100, y=190)
    date_window.mainloop()


def grab_date():
    dateEntry.delete(0, tk.END)
    dateEntry.insert(0, cal.get_date())
    date_window.destroy()



frame = ScrollableFrame(root)

# load the image and set it as the background
back = ImageTk.PhotoImage(file="photos/sign_up_template.png")
canvas = tk.Canvas(frame.scrollable_frame, width=back.width(), height=back.height())
canvas.create_image(0, 0, anchor="nw", image=back)
canvas.pack(fill="both", expand=1)
frame.pack(fill="both", expand=1)




lab1 = tk.Label(frame.scrollable_frame, text='Inscription', font=('Open sans', 21, 'bold'), fg='#3a3aff', bg='#eaefff')
lab1.place(x=325, y=130)

lab2 = tk.Label(frame.scrollable_frame,
                text='Veuillez remplir le formulaire avec soin et vous assurer que toutes les informations sont '
                     'exactes et non vides.',
                font=('Open sans', 10), fg='black', bg='#eaefff')
lab2.place(x=80, y=188)

# Nom_field
nameLabel = ctk.CTkLabel(master=frame.scrollable_frame, text="Nom:", bg_color='#eaefff')
nameLabel.place(x=170, y=230)
nameEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre nom ", width=200, height=35,
                         border_width=0, corner_radius=0)
nameEntry.place(x=170, y=253)

# prenom_field
prenomLabel = ctk.CTkLabel(master=frame.scrollable_frame, text="Prénom:", bg_color='#eaefff')
prenomLabel.place(x=390, y=230)
prenomEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre Prénom ", width=200,
                           height=35, border_width=0, corner_radius=0)
prenomEntry.place(x=390, y=253)

# date_field
datelabel = ctk.CTkLabel(master=frame.scrollable_frame, text='Entrer votre date de naissance:', bg_color='#eaefff')
datelabel.place(x=170, y=300)
dateEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="dd/mm/yyyy", width=430, height=35,
                         border_width=0, corner_radius=0)
dateEntry.place(x=170, y=323)
dateEntry.bind("<1>", pick_date)

# CNE_field
CNELabel = ctk.CTkLabel(master=frame.scrollable_frame, text="CNE:", bg_color='#eaefff' )
CNELabel.place(x=170, y=370)
CNEEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre CNE ", width=200, height=35,border_width=0, corner_radius=0)
CNEEntry.place(x=170, y=394)

# CIN_field
CINLabel = ctk.CTkLabel(master=frame.scrollable_frame, text="CIN:", bg_color='#eaefff')
CINLabel.place(x=390, y=370)
CINEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre CIN ", width=200, height=35,border_width=0, corner_radius=0)
CINEntry.place(x=390, y=394)

# pays_field
pays = ["","Algerie", "Egypt", "France", "Maroc", "Tunisia", "Ukraine", "Zambia"]

algerie = ["Adrar", "Ain Defla", "Ain Temouchent", "Alger", "Annaba", "Batna", "Bechar", "Bejaia", "Biskra", "Blida",
           "Bordj Bou Arreridj", "Bouira", "Boumerdes", "Chlef", "Constantine", "Djelfa", "El Bayadh", "El Oued",
           "El Tarf", "Ghardaia", "Guelma", "Illizi", "Jijel", "Khenchela", "Laghouat", "Muaskar", "Medea", "Mila",
           "Mostaganem", "M'Sila", "Naama", "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida", "Setif",
           "Sidi Bel Abbes", "Skikda", "Souk Ahras", "Tamanghasset", "Tebessa", "Tiaret", "Tindouf", "Tipaza",
           "Tissemsilt", "Tizi Ouzou", "Tlemcen"]
egypt = ["Ad Daqahliyah", "Al Bahr al Ahmar", "Al Buhayrah", "Al Fayyum", "Al Gharbiyah", "Al Iskandariyah",
         "Al Isma'iliyah", "Al Jizah", "Al Minufiyah", "Al Minya", "Al Qahirah", "Al Qalyubiyah", "Al Wadi al Jadid",
         "Ash Sharqiyah", "As Suways", "Aswan", "Asyut", "Bani Suwayf", "Bur Sa'id", "Dumyat", "Janub Sina'",
         "Kafr ash Shaykh", "Matruh", "Qina", "Shamal Sina'", "Suhaj"]
france = ["Alsace", "Aquitaine", "Auvergne", "Basse-Normandie", "Bourgogne", "Bretagne", "Centre", "Champagne-Ardenne",
          "Corse", "Franche-Comte", "Haute-Normandie", "Ile-de-France", "Languedoc-Roussillon", "Limousin", "Lorraine",
          "Midi-Pyrenees", "Nord-Pas-de-Calais", "Pays de la Loire", "Picardie", "Poitou-Charentes",
          "Provence-Alpes-Cote d'Azur", "Rhone-Alpes"]
maroc = ["Agadir", "Al Hoceima", "Azilal", "Beni Mellal", "Ben Slimane", "Boulemane", "Casablanca", "Chaouen",
         "El Jadida", "El Kelaa des Sraghna", "Er Rachidia", "Essaouira", "Fes", "Figuig", "Guelmim", "Ifrane",
         "Kenitra", "Khemisset", "Khenifra", "Khouribga", "Laayoune", "Larache", "Marrakech", "Meknes", "Nador",
         "Ouarzazate", "Oujda", "Rabat-Sale", "Safi", "Settat", "Sidi Kacem", "Tangier", "Tan-Tan", "Taounate",
         "Taroudannt", "Tata", "Taza", "Tetouan", "Tiznit"]
tunisia = ["Ariana (Aryanah)", "Beja (Bajah)", "Ben Arous (Bin 'Arus)", "Bizerte (Banzart)", "Gabes (Qabis)",
           "Gafsa (Qafsah)", "Jendouba (Jundubah)", "Kairouan (Al Qayrawan)", "Kasserine (Al Qasrayn)",
           "Kebili (Qibili)", "Kef (Al Kaf)", "Mahdia (Al Mahdiyah)", "Manouba (Manubah)", "Medenine (Madanin)",
           "Monastir (Al Munastir)", "Nabeul (Nabul)", "Sfax (Safaqis)", "Sidi Bou Zid (Sidi Bu Zayd)",
           "Siliana (Silyanah)", "Sousse (Susah)", "Tataouine (Tatawin)", "Tozeur (Tawzar)", "Tunis",
           "Zaghouan (Zaghwan)"]
ukraine = ["Cherkasy", "Chernihiv", "Chernivtsi", "Crimea", "Dnipropetrovs'k", "Donets'k", "Ivano-Frankivs'k",
           "Kharkiv", "Kherson", "Khmel'nyts'kyy", "Kirovohrad", "Kiev", "Kyyiv", "Luhans'k", "L'viv", "Mykolayiv",
           "Odesa", "Poltava", "Rivne", "Sevastopol'", "Sumy", "Ternopil'", "Vinnytsya", "Volyn'", "Zakarpattya",
           "Zaporizhzhya", "Zhytomyr"]
zambia = ["Central", "Copperbelt", "Eastern", "Luapula", "Lusaka", "Northern", "North-Western", "Southern",
          "Western"]


def pick_ville(e):
    if combo_pays.get() == "France":
        ville.configure(values=france)
    if combo_pays.get() == "Maroc":
        ville.configure(values=maroc)
    if combo_pays.get() == "Egypt":
        ville.configure(values=egypt)
    if combo_pays.get() == "Tunisia":
        ville.configure(values=tunisia)
    if combo_pays.get() == "Ukraine":
        ville.configure(values=ukraine)
    if combo_pays.get() == "Zambia":
        ville.configure(values=zambia)


pays_label = ctk.CTkLabel(master=frame.scrollable_frame, text='Pays:', bg_color='#eaefff')
pays_label.place(x=175, y=444)
# Create a drop box
combo_pays = ctk.CTkOptionMenu(frame.scrollable_frame, values=pays, width=200, height=35, bg_color='white',
                             button_hover_color='#3a3aff',
                             fg_color='white', command=pick_ville, button_color='#3a3aff', font=('', 13),
                             text_color=('#091226'), dropdown_fg_color='#eeefef', dropdown_hover_color='#d7dcdc')
combo_pays.place(x=175, y=470)
# bind the combobox
combo_pays.bind("<<ComboboxSelected>>", pick_ville)

# ville Combo box
ville_label = ctk.CTkLabel(master=frame.scrollable_frame, text=' Ville:', bg_color='#eaefff')
ville_label.place(x=390, y=444)
ville = ctk.CTkOptionMenu(frame.scrollable_frame, values=[" "], width=200, height=35, bg_color='white',
                          button_hover_color='#3a3aff',
                          fg_color='white', button_color='#3a3aff', font=('', 13),
                          text_color='#091226',dropdown_fg_color='#eeefef', dropdown_hover_color='#d7dcdc')
ville.place(x=390, y=470)


#adress_field
adresslabel = ctk.CTkLabel(master=frame.scrollable_frame, text='Adresse:', bg_color='#eaefff')
adresslabel.place(x=170, y=517)
adressEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre adresse", width=430, height=35,
                         border_width=0, corner_radius=0)
adressEntry.place(x=170, y=543)



#sexe_field
sexelabel = ctk.CTkLabel(master=frame.scrollable_frame, text='Sexe:', bg_color='#eaefff')
sexelabel.place(x=170, y=595)
gender_var = ctk.StringVar()
maleRadioButton = ctk.CTkRadioButton(master=frame.scrollable_frame,text="Homme",bg_color='#eaefff',hover=False,
                                     radiobutton_width=20,radiobutton_height=20,fg_color='#3a3aff',
                                     value='Homme',variable=gender_var)
maleRadioButton.place(x=250,y=595)
femmeRadioButton = ctk.CTkRadioButton(master=frame.scrollable_frame,text="Femme",bg_color='#eaefff',radiobutton_width=20,
                                      radiobutton_height=20,fg_color='#3a3aff',hover_color='black',hover=False,
                                      value='Femme',variable=gender_var)
femmeRadioButton.place(x=430,y=595)

#phone_field
phonelabel = ctk.CTkLabel(master=frame.scrollable_frame, text='Téléphone:', bg_color='#eaefff')
phonelabel.place(x=170, y=642)
phoneEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre téléphone ", width=430, height=35,
                         border_width=0, corner_radius=0)
phoneEntry.place(x=170, y=668)


#E-mail_field
Emaillabel = ctk.CTkLabel(master=frame.scrollable_frame, text='E-mail( Académique ):', bg_color='#eaefff')
Emaillabel.place(x=170, y=715)
EmailEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre E-mail ", width=430, height=35,
                         border_width=0, corner_radius=0)
EmailEntry.place(x=170, y=741)


#annee_filed
annee=['',"2023","2022","2021","2020","2019","2018"]
annee_label = ctk.CTkLabel(master=frame.scrollable_frame, text='Année du Baccalureat:', bg_color='#eaefff')
annee_label.place(x=175, y=788)
combo_annee = ctk.CTkOptionMenu(frame.scrollable_frame, values=annee, width=430, height=35, bg_color='white',
                             button_hover_color='#3a3aff',
                             fg_color='white', button_color='#3a3aff', font=('', 13),
                             text_color='#091226', dropdown_fg_color='#eeefef',
                             dropdown_hover_color='#d7dcdc')
combo_annee.place(x=175, y=814)


#niveau_field

# Options for first dropdown
niveau = ['',"Cycle préparatoire", "Cycle d'ingénieur"]

# Options for second dropdown
filiere1 = ["Première année préparatoire"]
filiere2 = ["Génie Civil", "Génie Informatique", "Ingénierie des données", "Génie énergétique et énergies renouvelables",
           "Génie de l’Eau et de l’Environnement", "Génie Mécanique"]

# Callback function for first dropdown
def pick_ville(e):
    # Add options based on the selected value in the first dropdown
    if combo_niveau.get() == "Cycle préparatoire":
        combo_filiere.configure(values=filiere1)
    elif combo_niveau.get() == "Cycle d'ingénieur":
        combo_filiere.configure(values=filiere2)

# Create the first dropdown
niveau_label = ctk.CTkLabel(master=frame.scrollable_frame, text='Niveau:', bg_color='#eaefff')
niveau_label.place(x=175, y=861)

combo_niveau = ctk.CTkOptionMenu(frame.scrollable_frame, values=niveau, width=200, height=35, bg_color='white',
                               button_hover_color='#3a3aff',
                               fg_color='white', command=pick_ville, button_color='#3a3aff', font=('', 13),
                               text_color=('#091226'), dropdown_fg_color='#eeefef', dropdown_hover_color='#d7dcdc')
combo_niveau.place(x=175, y=887)

# Create the second dropdown
filiere_label = ctk.CTkLabel(master=frame.scrollable_frame, text=' Filière:', bg_color='#eaefff')
filiere_label.place(x=390, y=861)

combo_filiere = ctk.CTkOptionMenu(frame.scrollable_frame, values=[" "], width=220, height=35, bg_color='white',
                          button_hover_color='#3a3aff',
                          fg_color='white', button_color='#3a3aff', font=('', 13),
                          text_color='#091226',dropdown_fg_color='#eeefef', dropdown_hover_color='#d7dcdc')
combo_filiere.place(x=390, y=887)



#password_field
Passwordlabel = ctk.CTkLabel(master=frame.scrollable_frame, text='Mot de passe:', bg_color='#eaefff')
Passwordlabel.place(x=170, y=934)
PasswordEntry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Entrer votre mot de passe ", width=430, height=35,border_width=0, corner_radius=0)
PasswordEntry.place(x=170,y=960)


Password_con_label = ctk.CTkLabel(master=frame.scrollable_frame, text='Confirmer le mote de passe:', bg_color='#eaefff')
Password_con_label.place(x=170, y=1007)
Password_con_Entry = ctk.CTkEntry(master=frame.scrollable_frame, placeholder_text="Confirmer votre mot de passe ", width=430, height=35,
                         border_width=0, corner_radius=0)
Password_con_Entry.place(x=170, y=1033)

#Photo_field
def get_path():
    global path
    filetypes = [
        ('PNG Files', '*.png'),
        ('JPEG Files', '*.jpeg'),
        ('JPG Files', '*.jpg'),
        ('All files', '*.png;*.jpeg;*.jpg')
    ]
    path = filedialog.askopenfilename(filetypes=filetypes)
    return path
path =''

def upload():
    global image_path
    image_path = get_path()
    image_name = os.path.basename(image_path)
    lab =ctk.CTkLabel (master=frame.scrollable_frame,text=(f"file : {image_name} "),bg_color='#eaefff')
    lab.place(x=175, y=1123)


image_button=ctk.CTkButton(frame.scrollable_frame,text="Importer votre photo !",width=430,height=35,fg_color='#3a3aff',text_color='white'
                   ,command=upload,corner_radius=0,border_width=0)
image_button.place(x=170,y=1085)


valider_button=ctk.CTkButton(frame.scrollable_frame,text="Valider!",width=200,height=35,fg_color='#0c9f5f',text_color='white'
                   ,corner_radius=0,border_width=0,hover_color='#0a7f4c',command=connect_database)
valider_button.place(x=170,y=1175)

exit_button=ctk.CTkButton(frame.scrollable_frame,text="EXIT!",width=200,height=35,fg_color='#acacac',text_color='white'
                   ,corner_radius=0,border_width=0,command=exit,hover_color='#b2b2b2')
exit_button.place(x=390,y=1175)

cpy_right_lab =ctk.CTkLabel (master=frame.scrollable_frame,text=("Copyright © 2023 - Tous droits réservés"),bg_color='#eaefff',
                             font=('#b4b6ba',13))
cpy_right_lab.place(x=250,y=1250)


root.mainloop()