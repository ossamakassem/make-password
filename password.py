from tkinter import *
import random
import string
from tkinter import messagebox
def osa():
    n=int(leng11.get())
    f=int(letter11.get())
    g=int(number11.get())
    h=int(symbol11.get())
    if n != (f+g+h):
        messagebox.showerror("Authentication Failed", "تأكد من اجمالى ما ادخلته")
        leng1.delete(0, "end")
        letter1.delete(0, "end")
        number1.delete(0, "end")
        symbol1.delete(0, "end")

    else:
        r=string.ascii_letters
        t=string.digits
        o=string.punctuation
        smail = ["\U0001F600", "\U0001F605", "\U0001F601", "\U0001F642"]
        password=(random.choices(r,k=f)+random.choices(t,k=g)+random.choices(o,k=g)+random.choices(smail))
        random.shuffle(password)
        pas="".join(password)
        use.set(pas)
        leng1.delete(0,"end")
        letter1.delete(0,"end")
        number1.delete(0,"end")
        symbol1.delete(0,"end")

root = Tk()
root.geometry('510x410')
root.title("ossamko")
leng11=StringVar()
titel=Label(root,text="برنامج انشاء كلمه السر",width=14,font=("Arial",25),bg="white",fg="black")
titel.grid(row=1,column=0,padx=120,pady=5,sticky=W,ipady=5)
#########################################################
leng=Label(root,text="ادخل طول كلمة السر",width=16,font=("Arial",20),bg="white",fg="black")
leng.grid(row=2,column=0,padx=240,pady=5,sticky=W,ipady=5)
leng1 = Entry(root, textvar=leng11, width=12, font=("Arial", 25), bg="white", fg="black")
leng1.grid(row=2, column=0, padx=5, pady=5, sticky=W)
####################################################
letter11=StringVar()
length_letter= Label(root, text="ادخل عدد احرف كلمه السر",width=16, font=("Arial", 20), bg="white", fg="black")
length_letter.grid(row=3, column=0, padx=240, pady=5, sticky=W,ipady=5)
letter1 = Entry(root, textvar=letter11, width=12, font=("Arial", 25), bg="white", fg="black")
letter1.grid(row=3, column=0, padx=5, pady=5, sticky=W)
######################################################
number11=StringVar()
length_number= Label(root, text="ادخل عدد ارقام كلمه السر",width=16, font=("Arial", 20), bg="white", fg="black")
length_number.grid(row=4, column=0, padx=240, pady=5, sticky=W,ipady=5)
number1 = Entry(root, textvar=number11, width=12, font=("Arial", 25), bg="white", fg="black")
number1.grid(row=4, column=0, padx=5, pady=5, sticky=W)
######################################################
symbol11=StringVar()
length_symbol= Label(root, text="ادخل عدد الرموز بكلمه السر",width=16, font=("Arial", 20), bg="white", fg="black")
length_symbol.grid(row=5, column=0, padx=240, pady=5, sticky=W,ipady=5)
symbol1 = Entry(root, textvar=symbol11, width=12, font=("Arial", 25), bg="white", fg="black")
symbol1.grid(row=5, column=0, padx=5, pady=5, sticky=W)
######################################################

use=StringVar()
user = Entry(root, textvar=use, width=12, font=("Arial", 25), bg="white", fg="black")
user.grid(row=6, column=0, padx=150, pady=5, sticky=W)


con = Button(root, text="موافق", width=8, font=("Arial", 20), bg="white", fg="black",command=osa)
con.grid(row=7, column=0, padx=155, pady=5, sticky=W)


root.resizable(False, False)
root.config(bg='cyan4')
root.mainloop()
