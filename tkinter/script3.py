from tkinter import *

#this is how it starts
window=Tk()

#function that converts km to miles.
def kg_to_everythin():
    #print(e1_value.get())
   grams=float(e1_value.get())*100
   pounds= float(e1_value.get())/0.45359237
   ounces =float(e1_value.get())/0.02834952 
   t1.insert(END,grams)
   t2.insert(END,pounds)
   t3.insert(END,ounces)
#LabelEntry

l1=Label(window, height=1, width=20,text="Kg")
l1.grid(row=0, column=0)


#button
b1 = Button(window,text="Execute",command=kg_to_everythin)
b1.grid(row=0,column=3)

#Entry
#input value to the window
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#text area
t1=Text(window,height=1,width=20)
t1.grid(row=1, column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1, column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1, column=2)

#always at the end
window.mainloop()