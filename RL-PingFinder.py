# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:03:13 2017

@author: Kushal
"""


#Order of ips in text file : ascxx-ascxxxxxxxx-asc1000-jpn-MidEast-Oce-EUxxxxxxx-EUxx-EUxxx
#eu has way too many servers, randomly picking 2 IP's and calculating. 

import subprocess
import re
from tkinter import *
main=Tk()
import webbrowser
from threading import Thread
import urllib.request
hosts=''
# #B9B9B9
main.configure(bg='#3f3f3f')
#with urllib.request.urlopen("file:///E:/Projects/Server-Pinger-For-RL/IP.txt") as url:
with urllib.request.urlopen("https://raw.githubusercontent.com/kushalnaidu/Server-Pinger-For-RL/master/IP.txt") as url:
    s = url.read()
qq=(s.decode('utf-8'))

hosts=qq.split()
#print(hosts)

name=['?ms']*len(hosts)

line=''
stringvar=[]
for i in range(len(hosts)):
    stringvar.append(StringVar())
both = StringVar()
continue_ping=False;

def callback(event):
    webbrowser.open_new(r"https://steamcommunity.com/id/CsProDude/")
    
def StopWorker():
    global continue_ping
    if not continue_ping:
        worker._is_running=False
        main.destroy()
    
    continue_ping=False;
def CreateWorker(target):
    return Thread(target=target)

def StartWorker(worker):
    continue_ping=True
    if(worker.is_alive()):
        pass;
    else:
        worker.daemon=True
        worker.start()
        

both.set("{}/{}".format(stringvar[7].get(),stringvar[8].get()))
def GetPings():
    global continue_ping
    continue_ping=True
    for i in range(len(stringvar)):
        stringvar[i].set(name[i])
    while(continue_ping):
        both.set("{}/{}".format(stringvar[7].get(),stringvar[8].get()))
        for i in range(len(hosts)):
            try:
                popen = subprocess.Popen(["ping",hosts[i],"-n","1"], stdout=subprocess.PIPE, bufsize=1,shell=True)
                lines_iterator = iter(popen.stdout.readline, b"")
                for line in lines_iterator:
                    pass;
                x=re.findall(b'Average = (.*?)\r\n',line)
                
                name[i]=(x[0].decode('utf-8'))
    
            except:
                name[i]='?ms'

            for i in range(len(stringvar)):
                stringvar[i].set(name[i])

            if not continue_ping:
                break;
                
    main.destroy()
    
    

def hlp():
    help=Tk()
    help['bg']="#3f3f3f"
    help.title("Help")
    width=300
    height=220
    help.geometry('%dx%d+%d+%d' % (width, height, 200,200))
#    help.minsize(width=300, height=220)
#    help.maxsize(width=300, height=220)
    lbl=Label(help,text='''1. Under EU, the pings are for 2 different servers,
    to understand your approximate pings.
    - These pings are not accurate for all servers and
    your in game pings may differ based on the server.
    \n2. ?ms indicates a timeout while pinging that server.
    \n3. Frequent display of ?ms would indicate a high % 
    of losses resulting in rubberbanding of the game.
    Such servers are not recommended for online play.
    \n4. Constant display of ?ms indicates a problem with 
    your internet connection, or a issue with cmd,
    wherein internet access is denied to it. ''',anchor = W,justify=LEFT)
    lbl.grid()
    lbl.configure(fg="#B9B9B9")
    lbl.configure(bg="#3f3f3f")
main.title("Ping Tester")
main.minsize(width=330, height=220)
main.maxsize(width=330, height=220)

label1 = Label( main, text="ASCxx :\n\nASCxxxxxx :\n\nASC1000/1001 :\n\nAsia-East(JPN) :" ,anchor=S, justify=RIGHT)
label2 = Label( main, text="Middle-East :\n\nOceania :\n\nEUxxxxxx :\n\n EUxx :",anchor=S, justify=RIGHT)
#label1 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label2 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label3 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label4 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label5 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label6 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label7 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)
#label8 = Label( main, text="ASCxx" ,anchor=S, justify=RIGHT)

ping1 = Label( main, textvariable=stringvar[0] , justify=RIGHT)
ping2 = Label( main, textvariable=stringvar[1] , justify=RIGHT)
ping3 = Label( main, textvariable=stringvar[2] , justify=RIGHT)
ping4 = Label( main, textvariable=stringvar[3] , justify=RIGHT)
ping5 = Label( main, textvariable=stringvar[4] , justify=RIGHT)
ping6 = Label( main, textvariable=stringvar[5] , justify=RIGHT)
ping7 = Label( main, textvariable=stringvar[6] , justify=RIGHT)
ping8 = Label( main, textvariable=both , justify=RIGHT)

ping1.configure(bg="#3f3f3f")
ping1.configure(fg="#B9B9B9")
ping2.configure(bg="#3f3f3f")
ping2.configure(fg="#B9B9B9")
ping3.configure(bg="#3f3f3f")
ping3.configure(fg="#B9B9B9")
ping4.configure(bg="#3f3f3f")
ping4.configure(fg="#B9B9B9")
ping5.configure(bg="#3f3f3f")
ping5.configure(fg="#B9B9B9")
ping6.configure(bg="#3f3f3f")
ping6.configure(fg="#B9B9B9")
ping7.configure(bg="#3f3f3f")
ping7.configure(fg="#B9B9B9")
ping8.configure(bg="#3f3f3f")
ping8.configure(fg="#B9B9B9")

label1.configure(bg="#3f3f3f")
label2.configure(bg="#3f3f3f")
label1.configure(fg="#B9B9B9")
label2.configure(fg="#B9B9B9")
label1.grid(row=4,column=0,rowspan=4,padx=0)
label2.grid(row=4,column=2,rowspan=4,padx=0)
ping1.grid(row=4,column=1,pady=5)
ping2.grid(row=5,column=1,pady=5)
ping3.grid(row=6,column=1,pady=5)
ping4.grid(row=7,column=1,pady=5)
ping5.grid(row=4,column=3,pady=5)
ping6.grid(row=5,column=3,pady=5)
ping7.grid(row=6,column=3,pady=5)
ping8.grid(row=7,column=3,pady=5)


worker = CreateWorker(GetPings)
Bmain=Button(main,  text ="Test Pings",command=lambda: StartWorker(worker),relief=GROOVE)
Bmain2=Button(main, text="Exit",command=StopWorker,relief=GROOVE)
Help=Button(main,  text ="Help",command=hlp,relief=GROOVE)
Bmain.configure(fg="#B9B9B9")
Bmain2.configure(fg="#B9B9B9")
Bmain.configure(bg="#3f3f3f")
Bmain2.configure(bg="#3f3f3f")


linkt = Label(main, text="For Suggestions/Feedback : ")
link = Label(main, text="Steam ID                                  ", fg="#2D7AFB", cursor="hand2")
linkt.grid(row=11,column=0,columnspan=2,padx=5)
link.grid(row=11,column=2,columnspan=2,padx=5)
link.bind("<Button-1>", callback)
link.configure(bg="#3f3f3f")
linkt.configure(bg="#3f3f3f")
linkt.configure(fg="#B9B9B9")
Bmain.grid(row=0,column=0,columnspan=4,ipadx=10,pady=5)
Bmain2.grid(row=10,column=0,columnspan=4,ipadx=10,pady=5)
Help.grid(row=0,column=3,sticky=E+N)
main.protocol("WM_DELETE_WINDOW", StopWorker)
Help.configure(fg="#B9B9B9")
Help.configure(bg="#3f3f3f")



width=330
height=220
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# calculate position x and y coordinates
x = (screen_width/4) - (width/2)
y = (screen_height/4) - (height/2)
main.geometry('%dx%d+%d+%d' % (width, height, x, y))
main.mainloop()


