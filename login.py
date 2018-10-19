from tkinter import *

root = Tk()

root.geometry("500x500")
root.resizable(0,0)

#def show():
#    print("Login Done")
#    root.configure(background="green")


show = lambda e:root.configure(background="pink")

 

un = Label(root,text="Enter Name",font=("Arial",20))
un.grid(row=0,column=0,pady=25,sticky=W)

e1 = Entry(root,font=("Arial",20))
e1.grid(row=0,column=1,pady=25)

up = Label(root,text="Enter Password",font=("Arial",20))
up.grid(row=1,column=0,pady=25)

 

e2 = Entry(root,show="*",font=("Arial",20))
e2.grid(row=1,column=1,pady=25)



#b1 = Button(root,text="Login",font=("Arial",20),command=show)

b1 = Button(root,text="Login",font=("Arial",20))

#b1.bind("<Button>",show)#L
#Enter # Leave #Key-a #Shift-Up,Down,Left,Right,Alt-Up,Control-Up#button-release
b1.bind("<Double-1>",show)#L

root.bind("<F1>",lambda e:root.configure(background="blue"))
b1.grid(row=2,column=0,columnspan=2)

root.mainloop()


