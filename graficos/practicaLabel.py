from tkinter import*
root=Tk()

miFrame=Frame(root, width=800 , height=600)

miFrame.pack()

miImage=PhotoImage(file="REY.png")
Label(miFrame , image=miImage).place(x=400 , y=300)                                                         #TEXTO              (miFrame , text= " Viva España" , fg="green" , font=("Cambria" , 18))



root.mainloop()