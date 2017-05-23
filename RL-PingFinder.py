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
import time
from threading import Thread
main=Tk()
name=['?ms','?ms','?ms','?ms','?ms']
hosts = ['45.76.153.116','hkserverworks.com','72.5.161.230','185.179.203.27','109.22.215.75']
cmd="ping 72.5.161.230"
i=0
line=''



def create_worker(target):
    return Thread(target=target)


def start_worker(worker):
    worker.start()

    
    
    
def GetPings():
    while(True):
        for i in range(5):
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
                
            var1.set(name[0])
            var2.set(name[1])
            var3.set(name[2])
            var4.set(name[3])
            var5.set(name[4])
    
    #GetPings()

main.title("Ping Finder")
main.minsize(width=300, height=200)
main.maxsize(width=300, height=200)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()

label1 = Label( main, text="Ping to ASCxx :\n\nPing to ASCxxxxxx :\n\nPing to ASC1000/1001 :\n\nPing to Middle-East :\n\nPing to Oceania :" ,anchor=W, justify=RIGHT)
ping1 = Label( main, textvariable=var1 , justify=LEFT)

ping2 = Label( main, textvariable=var2 , justify=RIGHT)

ping3 = Label( main, textvariable=var3 , justify=RIGHT)

ping4 = Label( main, textvariable=var4 , justify=RIGHT)

ping5 = Label( main, textvariable=var5 , justify=RIGHT)

label1.grid(row=4,column=0,rowspan=5,padx=0)
ping1.grid(row=4,column=2)
ping2.grid(row=5,column=2)
ping3.grid(row=6,column=2)
ping4.grid(row=7,column=2)
ping5.grid(row=8,column=2)
worker = create_worker(GetPings)


Bmain=Button(main, text ="Find Pings",command=lambda: start_worker(worker))
Bmain.grid(row=0,column=1,pady=10)

main.mainloop()


