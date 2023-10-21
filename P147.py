# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:38:48 2023

@author: Aidan
"""

from tkinter import*

root = Tk()

root.title("Encryption_With_Asquii_code")

root.geometry("400x400")

root.configure(background="orange")

word = Entry(root)

word.place(relx=0.5, rely=0.4, anchor=CENTER)

etiqueta = Label(root, text="Name in asquii", bg="yellow", fg="pink")

etiqueta2 = Label(root, text="Encrypted name", bg="yellow", fg="pink")

def asquii_converter ():
    
    guardar_campo = str(word.get())
    
    for letter in guardar_campo:
        
        etiqueta["text"]+=str(ord(letter))
        
        asquii = int(ord(letter))
        
        encrypted = asquii-1
        
        etiqueta2["text"] += str(chr(encrypted))
        
btn=Button(root,text="Display the Ascii Code and Encrypted value",command=asquii_converter, bg='royalblue', fg = 'white')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)




etiqueta.place(relx=0.5,rely=0.6,anchor=CENTER)
etiqueta2.place(relx=0.5,rely=0.7,anchor=CENTER)


    
    

root.mainloop()