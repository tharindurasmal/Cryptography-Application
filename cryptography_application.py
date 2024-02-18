from tkinter import* #tkinter for GUI.  import everything from the module
import tkinter as tk
import os

#Form
root=Tk()
root.title("Art and science of keeping secrets - Group 20")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#button funcions
def encrypt(key,plain_text):

    #plain text
    plain_text1= plain_text.get("1.0", "end-1c")
    #print(plain_text1)
    #plain_text.delete(1.0,END)
    #plain_text.insert(END, plain_text1)
    #key
    key1= key.get("1.0", "end-1c")
    #print(key1)
    key.delete(1.0,END)
    key.insert(END, key1)

    ciphertext=""
    for letter in plain_text1:
        if not letter == ' ':
            letter = letter.lower()
            position = letters.index(letter)
            new_index=(position+int(key1)) % 26
            ciphertext+=letters[new_index]
        else:
            ciphertext+='$'
    #print(ciphertext)
    plain_text.delete(1.0,END)
    plain_text.insert(END, ciphertext)
       

def decrypt (key1, cipher_text):


    #plain text
    cipher_text1= cipher_text.get("1.0", "end-1c")
    #print(cipher_text1)
    cipher_text.delete(1.0,END)
    cipher_text.insert(END, cipher_text1)
    #key
    key2= key1.get("1.0", "end-1c")
    #print(key2)
    key1.delete(1.0,END)
    key1.insert(END, key2)

    plaintext=""
    for letter in cipher_text1:
        if not letter == '$':
            letter = letter.lower()
            position = letters.index(letter)
            new_index=(position-int(key2)) % 26
            plaintext+=letters[new_index]
        else:
            plaintext+=' '
    #print(plaintext)
    cipher_text.delete(1.0,END)
    cipher_text.insert(END, plaintext)  

Label(root, text="Art and Science of Keeping Secret", bg="#2d4155",fg="white", font="arial 25 bold").place(x=100,y=20)

#first frame
f=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

plain_text=Text(f,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
plain_text.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(f)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=plain_text.yview)
plain_text.configure(yscrollcommand=scrollbar1.set)

#second frame
f2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

cipher_text=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
cipher_text.place(x=0,y=0,width=320,height=295)


scrollbar2=Scrollbar(f2)
scrollbar2.place(x=320,y=0,height=300)

scrollbar2.configure(command=cipher_text.yview)
cipher_text.configure(yscrollcommand=scrollbar2.set)


#third frame
f3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Label(f3,text="Please provide key and press encrypt button",bg="#2f4155",fg="yellow").place(x=20,y=5)
Label(f3,text="Enter KEY -->",bg="#2f4155",fg="yellow").place(x=170,y=50)
key=Text(f3,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
key.place(x=250,y=40,width=40,height=40)

Button(f3,text="Encrypt",width=10,height=2,font="arial 14 bold",command=lambda:encrypt(key,plain_text)).place(x=20,y=30)


#forth frame
f4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Label(f4,text="Enter KEY -->",bg="#2f4155",fg="yellow").place(x=170,y=50)
key1=Text(f4,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
key1.place(x=250,y=40,width=40,height=40)


Button(f4,text="Decrypt",width=10,height=2,font="arial 14 bold",command=lambda:decrypt(key1,cipher_text)).place(x=20,y=30)

Label(f4,text="Please provide key and press Decrypt button",bg="#2f4155",fg="yellow").place(x=20,y=5)


root.mainloop()
