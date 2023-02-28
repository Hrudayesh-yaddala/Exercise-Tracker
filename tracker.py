from email.mime import image
from pydoc import cli
from tkinter import *
from tkinter import ttk
#from msilib import Table
#from venv import create
import psycopg2
from tkcalendar import DateEntry
from PIL import ImageTk,Image

hostname='localhost'
database='fitness'
username='postgres'
pwd='Majorhrudayesh@22'
port_id=5432
def init():
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    cur=conn.cursor()
    cre_script='''CREATE TABLE IF NOT EXISTS tracker(date DATE,day varchar(20),type varchar(10),totas integer,reps integer,food varchar(20))'''
    cur.execute(cre_script)
    conn.commit()
    cur.close()
    
def submit():
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    cur=conn.cursor()
    cur.execute('''insert into tracker(date,day,type,totas,reps,food,calories_burned) values(%s,%s,%s,%s,%s,%s,%s)'''
    ,(dateEntry.get(),dayEntry.get(),clicked.get(),totasEntry.get(),repsEntry.get(),foodEntry.get(),calEntry.get())) 
    conn.commit()
    cur.close()
    conn.close()

def viewexpense():
    return None

def Calories_Burned():
    if(clicked.get()=='pushups'):
        res=round((int(totasEntry.get())*int(repsEntry.get())*0.36),2)
    elif(clicked.get()=='shoulders'):
        res=int(totasEntry.get())*int(repsEntry.get())*0.54
    elif(clicked.get()=='weight-lifting'):
        res=int(totasEntry.get())*int(repsEntry.get())*0.89
    elif(clicked.get()=='legs'):
        res=int(totasEntry.get())*int(repsEntry.get())*0.54
    calEntry.insert(1,res)

res=0
init()
root=Tk()
root.title("Personal exercise tracker")
root.geometry('1200x600')
img=Image.open('sampl.png')
bk=ImageTk.PhotoImage(img)
root.geometry('1200x600')
lb=Label(root,image=bk)
lb.place(x=5,y=5)

clicked=StringVar()
clicked.set("pushups")


dateLabel=Label(root,text="Date",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
dateLabel.grid(row=4,column=2,padx=7,pady=7)

dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=4,column=3,padx=7,pady=7)

Day=StringVar()
dayLabel=Label(root, text="Day",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
dayLabel.grid(row=5,column=2,padx=7,pady=7)

dayEntry=Entry(root,textvariable=Day,font=('arial',15,'bold'))
dayEntry.grid(row=5,column=3,padx=7,pady=7)

Type=StringVar()
typeLabel=Label(root, text="workout-type",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
typeLabel.grid(row=6,column=2,padx=7,pady=7)

typ=OptionMenu(root,clicked,"pushups","weight-lifting","shoulders","legs","pullups","benchworkout","dumbells")
typ.grid(row=6,column=3,padx=7,pady=7)


#typeEntry=Entry(root,textvariable=Type,font=('arial',15,'bold'))
#typeEntry.grid(row=6,column=3,padx=7,pady=7)

Totas=IntVar()
totasLabel=Label(root,text="Total-sets",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
totasLabel.grid(row=7,column=2,padx=7,pady=7)

totasEntry=Entry(root,textvariable=Totas,font=('arial',15,'bold'))
totasEntry.grid(row=7,column=3,padx=7,pady=7)

Reps=IntVar()
repsLabel=Label(root,text="Total-reps for each set",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
repsLabel.grid(row=8,column=2,padx=7,pady=7)

repsEntry=Entry(root,textvariable=Reps,font=('arial',15,'bold'))
repsEntry.grid(row=8,column=3,padx=7,pady=7)

Food=StringVar()
foodLabel=Label(root, text="food-consumed",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=18)
foodLabel.grid(row=9,column=2,padx=7,pady=7)

foodEntry=Entry(root,textvariable=Food,font=('arial',15,'bold'))
foodEntry.grid(row=9,column=3,padx=7,pady=7)

cal=IntVar()
calbtn=Button(root, command=Calories_Burned,text="calories-Burned",font=('arial',15,'bold'),bg="grey",fg="white",width=18)
calbtn.grid(row=10,column=2,padx=13,pady=13)


calEntry=Entry(root,textvariable=cal,font=('arial',15,'bold'))
calEntry.grid(row=10,column=3,padx=7,pady=7)

submitbtn=Button(root,command=submit,text="Submit",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
submitbtn.grid(row=11,column=2,padx=13,pady=13)

viewtn=Button(root,command=viewexpense,text="View History",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
viewtn.grid(row=11,column=3,padx=13,pady=13)

exit_button = Button(root, text="Exit", command=root.destroy,font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
exit_button.grid(row=12,column=1,padx=13,pady=13)


# # all saved history--------------
# Elist=['Date','Day','Type','Totas','Reps','Food']
# Etable=ttk.Treeview(root,column=Elist,show='headings',height=4)
# for c in Elist:
#     Etable.heading(c,text=c.title())
# Etable.grid(row=15,column=0,padx=7,pady=7,columnspan=3)


mainloop()