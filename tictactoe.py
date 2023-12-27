from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk() # loga objekts
mansLogs.title("TicTacToe")

speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus
count=0 #aizpildīto rūtiņu skaits

def btnClick(button): #padod visu pogu
    global speletajsX,count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==" " and speletajsX==True: #spēlē X spēlētājs
        button["text"]="X"#maina uz X
        speletajsX=False
        count+=1 # palielina rūtiņu skaitu
        checkWinner()

    elif button["text"]==" " and speletajsX==False: #mainās spēlētāji
        button["text"]="O"
        speletajsX=True
        count+=1
        checkWinner()

    else:
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")
    return

def disableButtons(): #spēle beidzas, pogas izslēgtas
    btn1.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn2.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn3.config(state=DISABLED) #pogas stāvoklis izslēgts

    btn4.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn5.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn6.config(state=DISABLED) #pogas stāvoklis izslēgts

    btn7.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn8.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn9.config(state=DISABLED) #pogas stāvoklis izslēgts
    return 0

def disableButtons(): #spēle beidzas, pogas izslēgtas
    btn1.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn2.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn3.config(state=DISABLED) #pogas stāvoklis izslēgts

    btn4.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn5.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn6.config(state=DISABLED) #pogas stāvoklis izslēgts

    btn7.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn8.config(state=DISABLED) #pogas stāvoklis izslēgts
    btn9.config(state=DISABLED) #pogas stāvoklis izslēgts
    return 0

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

    global winner, count, speletajsX
    winner=False
    count=0
    speletajsX=True
    return 0

btn1=Button(mansLogs, text=" ", width=6, height=3, font=('Helvica', 24), command=lambda:btnClick(btn1), bg='light green', fg='black')

btn2=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn2), bg='light green',fg='black')
btn3=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn3), bg='light green',fg='black')
btn4=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn4), bg='light green',fg='black')
btn5=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn5), bg='light green',fg='black')
btn6=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn6), bg='light green',fg='black')

btn7=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn7), bg='light green',fg='black')
btn8=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn8), bg='light green',fg='black')
btn9=Button(mansLogs,text=" ",width=6,height=3,font=('Helvica',24), command=lambda:btnClick(btn9), bg='light green',fg='black')

btn1.grid(row=0,column=0) #pievieno pogas 
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)

btn4.grid(row=1,column=0) #pievieno pogas 
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)

btn7.grid(row=2,column=0) #pievieno pogas 
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
















    #Lielā izvēlne
galvenaIzvelne=Menu(mansLogs)#izveido galveno izvēlni
mansLogs.config(menu=galvenaIzvelne)#pievieno galvenajam logam
opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvēlne

galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas)

def infoLogs():
        jaunsLogs=Toplevel()
        jaunsLogs.title('Info par programmu')
        jaunsLogs.geometry("300x300")
        
        apraksts=Label(jaunsLogs,text='Spēles noteikumi')
        apraksts.grid (row=0, column=0)
        apraksts=Label(jaunsLogs,text='Esiet sveicināti krustiņos un nullītēs!')
        apraksts.grid (row=1, column=0)
        apraksts=Label(jaunsLogs,text='Spēli jāspēlē 2 cilvēkiem no vienas ierīces.')
        apraksts.grid (row=2, column=0)
        apraksts=Label(jaunsLogs,text='1. spēlētājs spēlē kā X, bet 2. spēlētajs - kā O.')
        apraksts.grid (row=3, column=0)
        apraksts=Label(jaunsLogs,text='Spēlētāji pēc kārtas liek X vai O tukšajos laukumos.')
        apraksts.grid (row=4, column=0)
        apraksts=Label(jaunsLogs,text='Uzvar tas, kurš pirmais iegūst 3 X vai O pēc kārtas - horizontāli, vertikāli vai pa diagonāli.')
        apraksts.grid (row=5, column=0)
        apraksts=Label(jaunsLogs,text='Nospiežot pugu "Jauna spēle", spēle sāksies no sākuma.')
        apraksts.grid (row=6, column=0)
        apraksts=Label(jaunsLogs,text='Izbaudi!')
        apraksts.grid(row=7,column=0)
        return 
    
opcijas.add_command(label="Par prgrammu",command=infoLogs)
opcijas.add_command(label="Jauna spēle",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)

def checkWinner():
    global winner
    winner=False #noteiks, ja būs neizšķirts

    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or 
        btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or 
        btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or 

        btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or 
        btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" or 
        btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" or

        btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X" or 
        btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        
        winner=True
        disableButtons()
        messagebox.showinfo("TicTacToe","Spēlētējs X ir uzvarētājs.")

    elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" or 
        btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" or 
        btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" or 

        btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O" or
        btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O" or 
        btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O" or

        btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O" or 
        btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):

            winner=True
            disableButtons()
            messagebox.showinfo("TicTacToe","Spēlētējs O ir uzvarētājs.")

    elif count == 9:
        winner = False
        disableButtons()
        messagebox.showinfo("TicTacToe"," Spēles rezultāts ir neizšķirts.")
        return
    

mansLogs.mainloop()