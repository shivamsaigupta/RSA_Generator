#Km to miles converter by Shivam Sai Gupta
import tkinter
from tkinter import *
import random
import sys

sys.setrecursionlimit(1000000)

    
class GUID:

    def decrypt(self):

        my_cipher = self.entryMsg.get()


        cipher_ascii = []

        for char in my_cipher:
            cipher_ascii.append(int(ord(char)))
            
        plain_ascii = []

        my_d = int(self.entryD.get())
        my_pn = int(self.entryN.get())

        for ints in cipher_ascii:
            plain_ascii.append((ints**my_d)%my_pn)

        decoded = ""

        print(plain_ascii)

        for item in plain_ascii:
            decoded += chr(int(item))
            
        print("Decrypted Msg: " + decoded)
        
        self.text.insert(END,decoded)
        self.text.config(state='disabled')



    
    def __init__(self):
        self.root = Tk()


        self.entryMsg = Entry(self.root)
        self.entryN = Entry(self.root)
        self.entryD = Entry(self.root)
        
        self.label = Label(self.root, text="Decrypt Text")

        self.button = Button(self.root, text="Decrypt", command=self.decrypt)
        self.text = Text(self.root,width=80,height=5)

        self.label.pack()
        
        self.text.pack()
        

        self.labelN = Label(self.root, text="Private Key - N: ")
        self.labelD = Label(self.root, text="Private Key - D: ")
        self.labelMsg = Label(self.root, text="Message: ")

        self.labelN.pack(side="left")
        
        
        self.entryN.pack(side="left")
        self.labelD.pack(side="left")
        self.entryD.pack(side="left")
        
        
        self.labelMsg.pack(side="left")
        self.entryMsg.pack(side="left")
        
        self.button.pack()

        self.root.title("RSA Program by Shivam Sai Gupta: Decryption")


        self.root.mainloop()


