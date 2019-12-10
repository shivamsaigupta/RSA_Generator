#Km to miles converter by Shivam Sai Gupta
import tkinter
from tkinter import *
import random
import sys

sys.setrecursionlimit(1000000)

    
class GUIE:

    def encrypt(self):
        # Encrypter

        msg = self.entryMsg.get()

        msg_ascii = []

        cipher_ascii = []

        my_n = int(self.entryN.get())
        my_e = int(self.entryE.get())

        for char in msg:
            #Make sure 0<= char <n
            if(int(ord(char)) >= my_n):
                raise ValueError("Message exceeds n.")
            else:
                msg_ascii.append(int(ord(char)))


        for ints in msg_ascii:
            cipher_ascii.append((ints**my_e)%my_n)
            
        #cipher = (msg**my_e)%my_n

        decoded = ""

        for item in cipher_ascii:
            decoded += chr(int(item))
    
        print("Cipher Msg (Encrypted): " + decoded)

        self.text.insert(END,decoded)
        self.text.config(state='disabled')


    
    def __init__(self):
        self.root = Tk()

        self.frame = Frame(self.root)

        self.entryMsg = Entry(self.root)
        self.entryN = Entry(self.root)
        self.entryE = Entry(self.root)
        
        self.label = Label(self.root, text="Encrypt Text")

        self.button = Button(self.root, text="Encrypt", command=self.encrypt)
        self.text = Text(self.root,width=80,height=5)

        self.text.pack()

        self.labelN = Label(self.root, text="Public Key - N: ")
        self.labelE = Label(self.root, text="Public Key - E: ")
        self.labelMsg = Label(self.root, text="Message: ")

        self.labelN.pack(side="left")
        
        
        self.entryN.pack(side="left")
        self.labelE.pack(side="left")
        self.entryE.pack(side="left")
        
        
        self.labelMsg.pack(side="left")
        self.entryMsg.pack(side="left")
        
        self.button.pack()

        self.root.title("RSA Program by Shivam Sai Gupta: Decryption")



        self.root.mainloop()

