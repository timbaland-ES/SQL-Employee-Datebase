import os,sys,sqlite3,tkinter

def erzeugen():
    connection = sqlite3.connect("uGuiListbox.db")
    cursor = connection.cursor()
    sql =   "CREATE TABLE personen(" \
        "name TEXT, "\
        "vorname TEXT, "\
        "personalnummer INTEGER PRIMARY KEY, "\
        "gehalt REAL, "\
        "geburtstag TEXT)"
    cursor.execute(sql)
    
    sql = "INSERT INTO personen VALUES ('Maier',"\
        "'Hans',6714,3500,'15.03.1962')"
    cursor.execute(sql)
    connection.commit()
    sql = "INSERT INTO personen VALUES ('Schmitz',"\
          "'Peter',81343,3750,'12.04.1958')"
    cursor.execute(sql)
    connection.commit()
    sql = "INSERT INTO personen VALUES ('Mertens',"\
          "'Julia',2297,3621.25,'30.12.1959')"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def anzeigenListbox():
    connection = sqlite3.connect("uGuiListbox.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        liDaten.insert("end",dsatz[0]+" "+dsatz[1]+" "+str(dsatz[2])+" "+str(round(dsatz[3]))+" "+dsatz[4])
    connection.close()

def leerenEntry():
    entryName.delete(0,"end")
    entryVorname.delete(0,"end")
    entryPersonalnummer.delete(0,"end")
    entryGehalt.delete(0,"end")
    entryGeburtstag.delete(0,"end")
    
def anzeigenEntry():
    listBoxZeile = liDaten.get("active")
    einzDaten = listBoxZeile.split()
    leerenEntry()
    entryName.insert(0,einzDaten[0])
    entryVorname.insert(0,einzDaten[1])
    entryPersonalnummer.insert(0,einzDaten[2])
    entryGehalt.insert(0,einzDaten[3])
    entryGeburtstag.insert(0,einzDaten[4])
    global pNrAngezeigt
    pNrAngezeigt = einzDaten[2]

def neuDatensatz():
    name = entryName.get()
    vorname = entryVorname.get()
    personalnummer = entryPersonalnummer.get()
    gehalt = entryGehalt.get()
    geburtstag = entryGeburtstag.get()

    connection = sqlite3.connect("uGuiListbox.db")
    cursor = connection.cursor()
    sql = "INSERT INTO personen VALUES('"+name+"','"+vorname+"',"+personalnummer+","\
            +gehalt+",'"+geburtstag+"')"
          
    cursor.execute(sql)
    connection.commit()
    connection.close()
    leerenEntry()
    liDaten.delete(0,"end")
    anzeigenListbox()

def ändDsatz():
    connection = sqlite3.connect("uGuiListbox.db")
    cursor = connection.cursor()
    sql = "UPDATE personen SET name = '"+entryName.get()+"' "\
          " , vorname = '"+entryVorname.get()+"' "\
            " , personalnummer = '"+str(entryPersonalnummer.get())+"' "\
            " , gehalt = '"+str(entryGehalt.get())+"' "\
            " , geburtstag = '"+str(entryGeburtstag.get())+"' "\
            " WHERE personalnummer =  '"+pNrAngezeigt+"' "
    cursor.execute(sql)
    connection.commit()
    connection.close()
    leerenEntry()
    liDaten.delete(0,"end")
    anzeigenListbox()

def löDsatz():
    connection = sqlite3.connect("uGuiListbox.db")
    cursor = connection.cursor()
    sql = "DELETE FROM personen "\
            " WHERE personalnummer =  '"+pNrAngezeigt+"' "
    cursor.execute(sql)
    connection.commit()
    connection.close()
    leerenEntry()
    liDaten.delete(0,"end")
    anzeigenListbox()

def ende():
    main.destroy()

if not os.path.exists("uGuiListbox.db"):
    erzeugen()

main = tkinter.Tk()
main.wm_geometry("300x300")

lbName = tkinter.Label(main,text="Name:")
lbName.place(x=10,y=10,anchor="nw")
entryName = tkinter.Entry(main)
entryName.place(x=290,y=10,anchor="ne")
lbVorname = tkinter.Label(main,text="Vorname:")
lbVorname.place(x=10,y=30,anchor="nw")
entryVorname = tkinter.Entry(main)
entryVorname.place(x=290,y=30,anchor="ne")
lbPersonalnummer = tkinter.Label(main,text="Personalnummer:")
lbPersonalnummer.place(x=10,y=50,anchor="nw")
entryPersonalnummer = tkinter.Entry(main)
entryPersonalnummer.place(x=290,y=50,anchor="ne")
lbGehalt = tkinter.Label(main,text="Gehalt:")
lbGehalt.place(x=10,y=70,anchor="nw")
entryGehalt = tkinter.Entry(main)
entryGehalt.place(x=290,y=70,anchor="ne")
lbGeburtstag = tkinter.Label(main,text="Geburtstag:")
lbGeburtstag.place(x=10,y=90,anchor="nw")
entryGeburtstag = tkinter.Entry(main)
entryGeburtstag.place(x=290,y=90,anchor="ne")

buAnz = tkinter.Button(main, text = "Anzeigen", command=anzeigenEntry)
buAnz.place(x=10,y=120,anchor="nw")

buNeu = tkinter.Button(main, text = "Neu", command=neuDatensatz)
buNeu.place(x=80,y=120,anchor="nw")

buÄnd = tkinter.Button(main, text = "Ändern", command=ändDsatz)
buÄnd.place(x=125,y=120,anchor="nw")

buLö = tkinter.Button(main, text = "Löschen", command=löDsatz)
buLö.place(x=185,y=120,anchor="nw")

buEnde = tkinter.Button(main,text="Ende", command=ende)
buEnde.place(x=290,y=120,anchor="ne")

liDaten = tkinter.Listbox(main, width=46, heigh=0)
anzeigenListbox()
liDaten.place(x=10,y=150,anchor="nw")

main.mainloop()    
  
print("Ende")


































