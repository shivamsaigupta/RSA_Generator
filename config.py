from distutils.core import setup
import py2exe

setup(name="RSA_Program",
      description="Simple RSA Generator, Encrypter and Decrypter for Discrete Maths, Prof. Mahavir Jhawar, Ashoka University",
      author="Shivam Sai Gupta",
      url="http://shivamsaigupta.com",
      scripts=[r"d:\intro to programming\rsa\with gui\gui_decrypt.py", r"d:\intro to programming\rsa\with gui\gui_encrypt.py", r"d:\intro to programming\rsa\with gui\gui_gen.py", r"d:\intro to programming\rsa\with gui\main.py"],
)
