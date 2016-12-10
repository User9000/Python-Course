from tkinter import *

#this is how it starts
window=Tk()

#function that converts km to miles.
def km_to_miles():
    #print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)
    
#button
b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

#Entry
#input value to the window
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#text area
t1=Text(window,height=1,width=20)
t1.grid(row=0, column=2)


#always at the end
window.mainloop()

