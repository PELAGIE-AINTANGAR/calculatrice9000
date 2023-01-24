from tkinter import *
from math import *
import tkinter.messagebox



root = Tk()
root.title("calculatrice scientifique")
root.configure(background="powder blue")
root.resizable(width=False, height=False )
root.geometry("500x568")
calculator = Frame(root)
calculator.grid()
#-----------Entry information------------

txtDisplay = Entry(calculator, font=("arial", 20, "bold"), bg="powder blue", bd=30, width=28, justify=RIGHT )
txtDisplay.grid(row=0, column=0, columnspan=6, pady=1)
txtDisplay.insert(0, "0")



text = ""
phase1=0
phase2=0
final=0
signe=""
memorie=[]# Capte les calculs effectués 
       
       
def afficher_Nb(text): # Afficher les nombre sur écran 
        txtDisplay.delete(0, END) #supprime tous ce qui est present dans l'ecran
        txtDisplay.insert(INSERT, text) #insert le nombr passe en parametre dans l'ecran

# permet d'entrer des chiffres.
def numberEnter(num):
    global text
    text += num
    afficher_Nb(text)
    
#Fonction pour gérer les entrées utilisateur (opérateurs)
def operation(op):
    global text, phase1, phase2, final, signe
    phase1 = float(text)
    text=""
    signe = op
    afficher_Nb(text)

# Fonction pour effectuer les calculs
def equal():
    global text, phase1, phase2, final, signe, memorie
    phase2 = float(text)
    text = ""
    if signe == "+":
        final = phase1 + phase2
    elif signe == "-":
        final = phase1 - phase2
    elif signe == "*":
        final = phase1 * phase2
    elif signe == "/":
        final = phase1 / phase2
    elif signe == "%":
        final=phase1 % phase2
    elif signe == "1/X":
        final= 1 / phase2
    memorie.append(final)
    afficher_Nb(final)
    
    
#affiche la memoire    
def affiche_memory():
    global memorie
   
    for i in range(len(memorie)):
        print("Calcul " + str(i+1) + ": " + str(memorie[i]))
    afficher_Nb(memorie)
    
    
# Fonction pour effacer les variables les unes apres les autres
def clear():
    global text, phase1, phase2, final, signe
    if len(text)>0:
        text = text[:-1]
        
    afficher_Nb(text)

#fonction pour reinitialiser toutes les variables
def all_clear():
    global text, phase1, phase2, final, signe
    text = ""
    phase1 = 0
    phase2 = 0
    final = 0
    signe = ""
    afficher_Nb(text)
 
 
#pour calculer la rasine carre   
def square_root():
    global text
    result = sqrt(float(text))
    afficher_Nb(result)
       
#les fonctions suivantes permette d'entrer les signes et d'effectues les calcules      
def point():
    global text
    text += "."
    afficher_Nb(text)
    
    
def add():
    operation("+")

    
def sub():
    operation("-")
    

def mul():
    operation("*")
    
def zero():
    global text
    text += "0"
    afficher_Nb(text)
    
def negate():
    global text
    if len(text)>0:
        if text[0] == "-":
            text = text[1:]
        else:
            text = "-" + text
    afficher_Nb(text)
    
    
def div():
    operation("/")
    
    

def fraction():
    operation("1/X")
    
# Fonction pour calculer le cosinus
def carrer():
    global text
    total=float(text) * float(text)
    afficher_Nb(total)

    
    
# Fonction pour calculer le logarithme naturel
def mod():
    operation("%")
  

# Fonction pour afficher e sur l'écran
def afficher_e():
    global text
    text += str(e)
    afficher_Nb(text)
    
# Fonction pour calculer le logarithme base 10


#permetd'attribuer des grids et d'introduire chaque chiffre dans un grid
number = "789456123"
btn=[]
i=0
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculator, width=5, height=2, font=("arial",20,"bold"), bd=4, text=number[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=number[i]: numberEnter(x)
        i+=1
        

#-----------------standard-------------------------------------------------------------------------------------------------
btnCleare = Button(calculator, text=chr(67), width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=clear).grid(row=1, column=0, pady=1)
btnAllCleare = Button(calculator, text=chr(67)+chr(69), width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=all_clear).grid(row=1, column=1, pady=1)
btnsq = Button(calculator, text=chr(8730), width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=square_root).grid(row=1, column=2, pady=1)
btnAdd = Button(calculator, text="+", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=add).grid(row=1, column=3, pady=1)
btnSub= Button(calculator, text="-", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=sub).grid(row=2, column=3, pady=1)
btnMul = Button(calculator, text="*", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=mul).grid(row=3, column=3, pady=1)
btnDiv = Button(calculator, text="/", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=div).grid(row=4, column=3, pady=1)
btnZero = Button(calculator, text="0", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=zero).grid(row=5, column=0, pady=1)
btnPoint = Button(calculator, text=".", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=point).grid(row=5, column=1, pady=1)
btnSigne = Button(calculator, text=chr(177), width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=negate).grid(row=5, column=2, pady=1)
btnEgale = Button(calculator, text="=", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=equal).grid(row=5, column=3, pady=1) 


btnfrac = Button(calculator, text="1/x", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=fraction).grid(row=1, column=4, pady=1)              
btncarre = Button(calculator, text="x²", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=carrer).grid(row=2, column=4, pady=1) 
btnmodulo = Button(calculator, text="%", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=mod).grid(row=3, column=4, pady=1)
btnexpo = Button(calculator, text="e", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=afficher_e).grid(row=4, column=4, pady=1)
btnmemory = Button(calculator, text="Memo", width=5, height=2, font=("arial", 20,"bold"), bd=4, bg="powder blue", command=affiche_memory).grid(row=5, column=4, pady=1)                                     
                        

      
        
#----------------------memu-----------
def quitter():
    quitter = tkinter.messagebox.askyesno("scientific", "etes-vous sure de vouloir quitter?")
    if quitter >0:
        root.destroy()
        return

def standard():
    root.resizable(width=False, height=False )
    root.geometry("695x568+0+0")
    
   
    
menubar = Menu(calculator)
filemenu=Menu(menubar, tearoff=0)

menubar.add_cascade(label="fichier", menu=filemenu)
filemenu.add_command(label="standard", command=standard)
filemenu.add_separator()
filemenu.add_command(label="quitter", command=quitter)


editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="editer", menu=editmenu)
editmenu.add_command(label="couper")
editmenu.add_command(label="copier")
editmenu.add_separator()
editmenu.add_command(label="coller")

helpmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Aide", menu=helpmenu)
helpmenu.add_command()

root.config(menu=menubar)
root.mainloop()



  
