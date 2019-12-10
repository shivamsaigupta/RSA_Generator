import tkinter
from tkinter import *
import random
import sys
from GUI_gen import *
from GUI_decrypt import *
from GUI_encrypt import *

sys.setrecursionlimit(1000000)

    
class GUI:

    def gen(self):
        self.my_Gen = GUIGen()

    def encrypt(self):
        self.my_Encrypter = GUIE()

    def decrypt(self):
        self.my_Decrypter = GUID()
        
    def __init__(self):
        self.root = Tk()

        self.frame = Frame(self.root)

        
        self.label = Label(self.root, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        
        self.button1 = Button(self.root, text="Generate", command=self.gen)
        self.button2 = Button(self.root, text="Encrypt", command=self.encrypt)
        self.button3 = Button(self.root, text="Decrypt", command=self.decrypt)
        
        self.label.pack()

        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        

        self.root.title("RSA Key Generator by Shivam Sai Gupta")


        self.root.mainloop()

myGUI = GUI()

