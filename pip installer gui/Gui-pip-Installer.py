import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os,time
from bs4 import BeautifulSoup
import requests

data_dict={}

def clicked(event):
    package.delete(0,"end")
    package.insert(END,data_dict[event]['name'])

def search():
    global package_name,package_version,all_packs
    search_pack = package.get()
    source = requests.get('https://pypi.org/search/?q='+search_pack).text
    soup = BeautifulSoup(source,'lxml')
    i=1
    row_num=5
    all_packs = soup.find_all('a',class_='package-snippet')[0:10]
    number = len(all_packs)
    show = Label(window,text='The top {} search results are'.format(number),font=('Ariel Black',15),width=30)
    show.grid(column=0,row=4)
    for name in all_packs:
        def make_lambda(x):
            return lambda some_var:clicked(x)
        package_name = name.h3.span.text
        package_version = name.find('span',class_='package-snippet__version').text
        package_description = name.p.text
        data_dict[i]={"name":package_name , "version":package_version , "description":package_description }
        display=package_name,package_version
        result1 = Label(window,text=display,font=('Ariel Black',13),width=40,foreground="blue")
        result1.grid(column=0,row=row_num)
        result1.bind("<Button-1>",make_lambda(i))
        blank = Label(window,text="")
        blank.grid(column=0,row=row_num)
        row_num=row_num+1
        i+=1


def install():
    file=package.get()
    os.system('pip install --no-cache-dir '+file)
    messagebox.showinfo('Result','Process Finished')


def update():
    file=package.get()
    os.system('pip install --no-cache-dir --upgrade '+file)
    messagebox.showinfo('Result','Process Finished')


def uninstall():
    file=package.get()
    os.system('pip uninstall '+file)
    messagebox.showinfo('Result','Process Finished')


window = Tk()

window.title('Python package installer')

window.geometry('700x400')

main = Label(window,text='Install python packages', font=('Arial Bold',20))

main.grid(column=0,row=0)

text= Label(window,text='Enter package name to install/update', font=('Ariel Black',10))

text.grid(column=0,row=1)

package = Entry(window,width=50)

package.grid(column=0,row=3)

package.focus()

search = Button(window,text='Search',command=search)

search.grid(column=1,row=3)

install = Button(window,text='Install',command=install)

install.grid(column=2,row=3)

update = Button(window,text='Update',command=update)

update.grid(column=3,row=3)

uninstall = Button(window,text='Uninstall',command=uninstall)

uninstall.grid(column=4,row=3)

window.mainloop()



