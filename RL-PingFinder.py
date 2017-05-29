# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:03:13 2017

@author: Kushal
"""
#185.179.203.27 m-e
#109.22.215.75 oceania
#45.32.110.9 Ascxx
#hkserverworks.com ascxxxxxx
#72.5.161.230 ASC1000
import subprocess
import re
from tkinter import *
main=Tk()
import webbrowser
from threading import Thread
import urllib.request
hosts=''

#with urllib.request.urlopen("file:///E:/Projects/Server-Pinger-For-RL/IP.txt") as url:
with urllib.request.urlopen("https://raw.githubusercontent.com/kushalnaidu/Server-Pinger-For-RL/master/IP.txt") as url:
    s = url.read()

qq=(s.decode('utf-8'))

hosts=qq.split()
#print(hosts)

name=['?ms']*len(hosts)
cmd="ping 72.5.161.230"

line=''
stringvar=[]
for i in range(len(hosts)):
    stringvar.append(StringVar())
    
continue_ping=False;

def callback(event):
    webbrowser.open_new(r"https://steamcommunity.com/id/CsProDude/")
    
def StopWorker():
    global continue_ping
    if not continue_ping:
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
        


def GetPings():
    global continue_ping
    continue_ping=True
    for i in range(len(stringvar)):
        stringvar[i].set(name[i])
    while(continue_ping):
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
    #            try:
    #                if(i==0):
    #                    result = subprocess.check_output("ping 45.76.177.233 -n 1",shell=True)
    #                    name[i]=(re.findall(r'Average = (.*?)ms',str(result))[0])
    #                else:
    #                    name[i]=0
    #            except:
                
            for i in range(len(stringvar)):
                stringvar[i].set(name[i])
#            stringvar[1].set("2")
            if not continue_ping:
                break;
#    print(continue_ping)
    #worker._stop()
    main.destroy()
                
    

main.title("Ping Finder")
main.minsize(width=350, height=300)
main.maxsize(width=350, height=300)

label1 = Label( main, text="Ping to ASCxx :\n\nPing to ASCxxxxxx :\n\nPing to ASC1000/1001 :\n\nPing to Asia-East(JPN) :\n\nPing to Middle-East :\n\nPing to Oceania :" ,anchor=W, justify=RIGHT)
ping1 = Label( main, textvariable=stringvar[0] , justify=RIGHT)

ping2 = Label( main, textvariable=stringvar[1] , justify=RIGHT)

ping3 = Label( main, textvariable=stringvar[2] , justify=RIGHT)

ping4 = Label( main, textvariable=stringvar[3] , justify=RIGHT)

ping5 = Label( main, textvariable=stringvar[4] , justify=RIGHT)

ping6 = Label( main, textvariable=stringvar[5] , justify=RIGHT)

label1.grid(row=4,column=0,rowspan=6,padx=0)
ping1.grid(row=4,column=2)
ping2.grid(row=5,column=2)
ping3.grid(row=6,column=2)
ping4.grid(row=7,column=2)
ping5.grid(row=8,column=2)
ping6.grid(row=9,column=2)
worker = CreateWorker(GetPings)

Bmain=Button(main, text ="Find Pings",command=lambda: StartWorker(worker))
Bmain2=Button(main, text ="Exit",command=StopWorker)
linkt = Label(main, text="For Suggestions/Feedback : ")
link = Label(main, text="Steam ID", fg="blue", cursor="hand2")
linkt.grid(row=11,column=0,columnspan=3,padx=5)
link.grid(row=11,column=4,padx=5)
link.bind("<Button-1>", callback)
Bmain.grid(row=0,column=1,pady=10)
Bmain2.grid(row=10,column=1,pady=10)
main.protocol("WM_DELETE_WINDOW", StopWorker)
main.mainloop()


