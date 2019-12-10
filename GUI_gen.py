#Km to miles converter by Shivam Sai Gupta
import tkinter
from tkinter import *
import random
import sys

sys.setrecursionlimit(1000000)

    
class GUIGen:

    def gen(self):

        #Check if the given number is prime
        choice = 1
        
        def is_prime(num):
           if num == 2:
              return True
           if num < 2 or num % 2 == 0:
              return False
           for n in range(3, int(num**0.5)+2, 2):
              if num % n == 0:
                 return False
           return True

        # GCD Function

        def gcd(a,b):
           if ( b == 0 ):
              return a
           else:
              return gcd(b, a%b)

        # Multiplicity Inverse
        # d≡e−1(modϕ(n))

        def mulinv(b, n):
           
           g, x, _ = xgcd(b, n)
           # _Debug_
           #print('g',g,'x',x,'_',_)
           #print(g,'=',b,'(',x,')','+',n,'(',_,')')
           if g == 1:
              print(x%n)
              return x % n

              # A iterative function to find x and y using the Extended Euclidian Theorem.
              # Returns in this order: gcd(b,n),x,y

        def xgcd(b, n):
            x0, x1, y0, y1 = 1, 0, 0, 1
            while n != 0:
                q, b, n = b // n, n, b % n
                x0, x1 = x1, x0 - q * x1
                y0, y1 = y1, y0 - q * y1

            # _Debug_
            #print('b',b,'x0',x0,'y0',y0)
            return  b, x0, y0

        if(choice == 1):
                 
              #Take inputs from the user
              p = int(self.entryP.get())
              q = int(self.entryQ.get())

              #Raise errors if the given p& q are equal or not primes
              if( p == q):
                 raise ValueError('Both numbers cannot be equal.')
              elif( is_prime(p) == False or is_prime(q) == False):
                 raise ValueError('Both numbers must be primes.')

              #If there are no errors, calculate n
              n = p*q

              print("n: " + str(n))

              #Calculate phi of n
              phi = (p-1)*(q-1)
              print("phi: " + str(phi))

              # Find a number e such that 1 < e < φ(n)
              e = random.randint(2,phi-1)

              # Keep generating random number e until e and φ(n) are coprimes or the GCD of e and φ(n) is = 1.
              while(gcd(e,phi) != 1):
                  e = random.randint(2,phi-1)
                  
              # Find d. D is the multiple inverse of e and phi(n)
              # d≡ e^(−1) (modϕ(n))
              d = mulinv(e,phi)
              

              #Print public key and private key
              outputString = "Public key: (" + str(n) + ", " + str(e)+") \n" + "Private key: (" + str(n) + ", " + str(d)+")"

              print("Public key: ( modulus: " + str(n) + ", public key exponent (e): " + str(e)+")")

              print("Private key: ( modulus: " + str(n) + ", private key exponent (d): " + str(d)+")")

              self.label.config(text=outputString)


    
    def __init__(self):
        self.root = Tk()

        self.frame = Frame(self.root)

        self.entryP = Entry(self.root)
        self.entryQ = Entry(self.root)
        
        self.label = Label(self.root, text="Generated Keys")
        self.labelP = Label(self.root, text="P: ")
        self.labelQ = Label(self.root, text="Q: ")
        
        self.button = Button(self.root, text="Generate", command=self.gen)

        self.label.pack()

        self.labelP.pack(side='left')
        self.entryP.pack(side='left')
        
        self.labelQ.pack(side='left')
        self.entryQ.pack(side='left')
        
        self.button.pack(side='right')



        

        self.root.title("RSA Key Generator by Shivam Sai Gupta")


        self.root.mainloop()


