from tkinter import *


from PIL import Image,ImageTk

root = Tk()
root.geometry('500x600')
root.title("Registration Form")
#root.config(background="white")


def exitt():
    exit()


imge=Image.open("Team Male.png")
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()

fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()

def printent():
    first=fn.get()
    sec=ln.get()
    dob1=dob.get()
    var1=var.get()
    print(f"Your Fullname is, {first} {sec}")
    print(f"Your Age is, {dob1}")
    print(f"Your Country is, {var1}")
    
    

label_0 = Label(root, text="Registration form",relief="solid",width=20,font=("arial", 19,"bold"))
label_0.place(x=90,y=150)


label_1 = Label(root, text="FirstName :",width=20,font=("bold", 10))
label_1.place(x=80,y=240)

entry_1 = Entry(root,textvar=fn)
entry_1.place(x=240,y=242)


label_2 = Label(root, text="LastName :",width=20,font=("bold", 10))
label_2.place(x=80,y=280)

entry_2 = Entry(root,textvar=ln)
entry_2.place(x=240,y=282)

label_3 = Label(root, text="DOB :",width=20,font=("bold", 10))
label_3.place(x=80,y=320)

entry_3 = Entry(root,textvar=dob)
entry_3.place(x=240,y=320)

label_3 = Label(root, text="Country :",width=20,font=("bold", 10))
label_3.place(x=75,y=370)

var=StringVar()

#day = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'];
#Month = ['1','2','3','4','5','6','7','8','9','10','11','12'];
#Month= ['January','February','March','April','May','June','July','August','September','October','November','December'];
list1=["Nepal","India",'America','China',"Canada",'Japan','South Africa']
droplist=OptionMenu(root,var,*list1)
var.set("Select Country")
droplist.config(width=15)
 
droplist.place(x=238,y=370)


label_0 = Label(root, text="DOB :",width=20,font=("bold",10))
label_0.place(x=65,y=320)


but_login=Button(root, text='Signup',width=12,bg='brown',fg='white',command=printent).place(x=150,y=450)
but_quit=Button(root, text='Quit',width=12,bg='brown',fg='white',command=exitt).place(x=280,y=450)

root.mainloop()























