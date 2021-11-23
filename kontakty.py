from tkinter import *

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Książka adresowa')
contactlist = []

def wczytajPlik():
    plik = open("log.txt", "r")
    linie = plik.readlines()
    for x in linie:
        linijka = x.split("/")
        contactlist.append(linijka)
    plik.close()

def zapiszPlik():
    plik = open("log.txt", "w")
    for line in contactlist:
        plik.write(line[0] + "/" + line[1][:-1] + "\n")
    plik.close()

Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack()
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=14)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)
frame.place(x=230, y=110)

def Selected():
    return int(select.curselection()[0])
def dodajOsobe():
    contactlist.append([Name.get(), Number.get()])
    Lista()
    zapiszPlik()
def Usun():
    del contactlist[Selected()]
    Lista()
    zapiszPlik()
def Wyswietl():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
def Reset():
    Name.set('')
    Number.set('')
def Lista() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
    zapiszPlik()

wczytajPlik()
Lista()

Label(root, text = 'Nazwa', font='Calibri 12').place(x=30, y=20)
Entry(root, textvariable = Name).place(x=100, y=20)
Label(root, text = 'Numer tel.', font='Calibri 12').place(x=30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)
Button(root,text="Dodaj", font='Calibri 12', width=15, command = dodajOsobe).place(x= 50, y=110)
Button(root,text="Usuń", font='Calibri 12', width=15, command = Usun).place(x= 50, y=210)
Button(root,text="Wyświetl", font='Calibri 12', width=15, command = Wyswietl).place(x= 50, y=160)
Button(root,text="Resetuj", font='Calibri 12', width=15, command = Reset).place(x= 50, y=310)
root.mainloop()