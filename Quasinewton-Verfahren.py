from CG import *
from Funktionsklasse import *
import random
from tkinter import *


# global variables for calculating**************************************************************************************
dim = 0
listOfFunctions = []
listOfFunctionsChoosen = []
numbersOfFunctionsNotChoosen = []
x = np.zeros(2)
choosen = False
numberOfFunctions = 0
f_N = np.zeros((2, 2))


# Funktionserstellung***************************************************************************************************

# Produces random numbers for the entries of matrix A and vector b.
# input:    n: dimension of A and b,
#           m: number of functions
# output:   array of lists for A und b

def init(n, m):
    b = np.zeros(n)
    A = np.zeros(n)
    functions = []
    for i in range(0,n):
        b[i] = random.randint(-50, 50)
        A[i] = random.randint(1, 100)

    print("Diagonaleinträge von A: " + str(A))
    print("Einträge von b: " + str(b))

    for i in range(0,m):
        Ai = np.zeros((n, n))
        bi = np.zeros(n)
        for j in range(0,n):
            Ai[i,i] = A[j % n]+(random.random()/2)-0.25
            bi[i] = b[j%n]+(random.random()/2)-0.25
        functions.append(Funktion(Ai, bi))
    return functions


# Function to activate funktion 'init'. Produces a set of diagonal matrices
# Produced list will be stored in two variables. First one is storage and wont be
# touched be any function. Second one will be manipulated by choosing a subset.
# Function gets triggert by pressing button1 with label 'Erzeuge zufällige Funktionen'

def functionMaker():
    global listOfFunctions
    global listOfFunctionsChoosen
    global dim
    global choosen
    global nonDiagonal
    global numberOfFunctions
    try:
        dim = int(entry1.get())
        numberOfFunctions = int(entry2.get())
        list = init(int(entry1.get()), int(entry2.get()))

    except:
        print("Eingegebene Werte sind keine Integer oder nicht mehr im Zulässigen Bereich!")
        return
    listOfFunctions = list
    listOfFunctionsChoosen = list
    choosen = False

#________________________________________

# Produces random matrices for matrix A and random vectors for vector b.
# input:    n: dimension of A and b,
#           m: number of functions
# output:   list of lists for A und b

def init2(n, m):
    functions = []

    for i in range(0, m):
        b = np.zeros(n)
        A = np.zeros((n, n))

        a = [random.uniform(0.1, 7) for j in range(int(n*(n+1)/2))]
        A[np.tril_indices(n, 0)] = a

        for k in range(0,n):
            b[k] = random.randint(-50,50)

        functions.append(Funktion(np.dot(A, np.transpose(A)), np.copy(b)))

    print("Erstellte Funktionen: " + str(functions))

    return functions

# Produces random functions
def functionMaker2():
    global listOfFunctions
    global listOfFunctionsChoosen
    global dim
    global choosen
    global numberOfFunctions
    try:
        dim = int(entry1.get())
        numberOfFunctions = int(entry2.get())
        list = init2(int(entry1.get()), int(entry2.get()))
    except:
        print("Eingegebene Werte sind keine Integer oder nicht mehr im Zulässigen Bereich!")
        return
    listOfFunctions = list
    listOfFunctionsChoosen = list
    choosen = False

#________________________________________

# Produces a random tridiagonal matrix A' and changed copies of it. A ist builded by formel A = A' * A'^t
# input:    n: dimension of A and b,
#           m: number of functions
# output:   list of lists for A und b

def init3(n, m):
    b = np.zeros(n)
    A = np.zeros((n, n))
    functions = []

    a = [random.uniform(0.1, 7) for j in range(int(n * (n + 1) / 2))]
    A[np.tril_indices(n, 0)] = a
    print("A = " + str(np.dot(A, np.transpose(A))))

    for k in range(0, n):
        b[k] = random.randint(-50, 50)
    print("b = " + str(b))

    for i in range(0, m):
        ai = np.copy(a)
        for j in range(0, len(a)):
            ai[j] = ai[j] + (random.random()/2)-0.25
        A[np.tril_indices(n, 0)] = ai

        for k in range(0, n):
            b[k] = b[k]+(random.random()/2)-0.25
        functions.append(Funktion(np.dot(A, np.transpose(A)), np.copy(b)))

    return functions


def functionMaker3():
    global listOfFunctions
    global listOfFunctionsChoosen
    global dim
    global choosen
    global numberOfFunctions
    try:
        dim = int(entry1.get())
        numberOfFunctions = int(entry2.get())
        list = init3(int(entry1.get()), int(entry2.get()))
    except:
        print("Eingegebene Werte sind keine Integer oder nicht mehr im Zulässigen Bereich!")
        return
    listOfFunctions = list
    listOfFunctionsChoosen = list
    choosen = False

#________________________________________

# Function to calculate the average of the given functions
# input:    list_Ab: two dimensional list of matrices A and vectors b (first entrie: A's, second entrie: b's
# output:   list with A and b

def average(list_of_functions):
    m = len(listOfFunctions)
    A = np.zeros((dim, dim))
    b = np.zeros(dim)

    for f in list_of_functions:
        A = A + f.A()
        b = b + f.b()

    A = A/m
    b = b/m
    return Funktion(A, b)


#Funktionsauswahl*******************************************************************************************************


# Takes a subset of the produced functions. Amount of functions choosen is given by user via gui.
# Function gets triggert by pressing button2 with label 'Wähle Funktionen'

def chooseFunctions():
    global listOfFunctionsChoosen
    global numbersOfFunctionsNotChoosen
    global choosen
    global f_N

    try:
        try:
            m = numberOfFunctions
            n = int(entry3.get())
            if n == 0:
                print("Eingegebene Werte sind keine Integer oder nicht mehr im Zulässigen Bereich!")
                return
        except:
            print("Eingegebene Werte sind keine Integer oder nicht mehr im Zulässigen Bereich!")
            return
        if n > m:
            print("Eingabe muss kleiner sein als zuvor festgelegte Anzahl an Funktionen!")
            return
        liste = random.sample(range(m), n)
        numbersOfFunctionsNotChoosen = [*range(m)]
        for k in liste:
            numbersOfFunctionsNotChoosen.remove(k)
        functions = []
        for i in liste:
            functions.append(listOfFunctions[i])
        listOfFunctionsChoosen = functions
        print("Funktionen ausgewählt!")
        A = np.zeros((dim, dim))
        for fi in listOfFunctionsChoosen:
            A = A + fi._A
        A = (1 / len(listOfFunctionsChoosen)) * A
        f_N = A
        if n < m:
            choosen = True

    except:
        print("Es ist ein Fehler aufgetreten! Überprüfen Sie ihr Eingaben und stellen Sie sicher, dass bereits "
              "Funktionen existieren!")
        return


# Takes a subset of the produced functions. Amount of functions choosen is given by number.

def chooseFunctionsAutomatic(number):
    global listOfFunctionsChoosen
    global numbersOfFunctionsNotChoosen
    global choosen
    global f_N

    try:
        m = numberOfFunctions
        if number > m:
            print("Eingabe muss kleiner sein als zuvor festgelegte Anzahl an Funktionen!")
            return
        liste = random.sample(range(m), number)
        numbersOfFunctionsNotChoosen = [*range(m)]
        for k in liste:
            numbersOfFunctionsNotChoosen.remove(k)
        functions = []
        for i in liste:
            functions.append(listOfFunctions[i])
        listOfFunctionsChoosen = functions
        print("Funktionen ausgewählt!")
        A = np.zeros((dim, dim))
        for fi in listOfFunctionsChoosen:
            A = A + fi._A
        A = (1 / len(listOfFunctionsChoosen)) * A
        f_N = A
        if number < m:
            choosen = True

    except:
        print(
            "Es ist ein Fehler aufgetreten! Überprüfen Sie ihr Eingaben und stellen Sie sicher, dass bereits Funktionen"
            " existieren!")
        return


# Adds another function of numbersofFunctionsNotChoosen to the set of functionsChoosen

def addFunctionsAutomatic():
    global listOfFunctionsChoosen
    global numbersOfFunctionsNotChoosen
    global choosen
    global f_N

    i = random.choice(numbersOfFunctionsNotChoosen)
    m = numberOfFunctions

    listOfFunctionsChoosen.append(listOfFunctions[i])
    numbersOfFunctionsNotChoosen.remove(i)
    print("Funktionen ausgewählt!")
    A = np.zeros((dim, dim))
    for fi in listOfFunctionsChoosen:
        A = A + fi._A
    A = (1 / len(listOfFunctionsChoosen)) * A
    f_N = A
    if len(listOfFunctionsChoosen) < m:
        choosen = True


# Optimierung***********************************************************************************************************

def f(x):
    value = 0
    for fi in listOfFunctions:
        value = value + fi.wert(x)
    value = value / len(listOfFunctions)
    return value

def grad_f(x):
    grad = np.zeros(dim)
    for fi in listOfFunctions:
        grad = grad + fi.gradient(x)
    grad = (1 / len(listOfFunctions)) * grad
    return grad

def hesse_f(x):
    A = np.zeros((dim, dim))
    for fi in listOfFunctions:
        A = A + fi.A
    A = (1 / len(listOfFunctions)) * A
    return A

def hesse_f_N(x):
    return f_N




# Algorithmus zum Optimieren der gegebenen Funktionen.
# Ausgabe des Optimierers sowie der bestimmten Werte erfolgt auf der Konsole.
def optimize():

    try:
        tolerance = math.pow(10, -1 * int(entry4.get()))   # Toleranzschwelle des Nutzers
    except:
        tolerance = 5* math.pow(10, -1 * 8)

    if numberOfFunctions < 5:
        number = numberOfFunctions
    else:
        number = 5

    chooseFunctionsAutomatic(number)
    iteration = 0
    x  = np.zeros(dim)
    p  = CG(hesse_f_N(x), -1 * grad_f(x), 10 * dim, math.pow(10,-5), x)
    F = f(x)
    Grad = grad_f(x)

    alpha = 1           # Armijo-Backtrackin-Verfahren
    while f(x + (alpha * p)) > F + 0.5 * alpha * np.dot(Grad, p):
        alpha = 0.5 * alpha

    xold  = np.copy(x)     # Sicherung x
    x     = x + alpha * p  # Update von x
    F = f(x)
    Grad = grad_f(x)

    iteration = 1

    while ((np.linalg.norm(Grad) > tolerance * (1 + (abs(F)))) and
           (abs(np.linalg.norm(Grad) - np.linalg.norm(grad_f(xold)))) > math.pow(10, -7)) \
            or (abs(F - f(xold)) > math.pow(10, -8) * (1 + abs(F)))\
            or (np.linalg.norm(xold - x) > math.pow(10, -8) * (1 + np.linalg.norm(x))):

        if np.linalg.norm(xold - x) <= math.pow(10, -6) * (1 + np.linalg.norm(x)):
            if number < numberOfFunctions:
                addFunctionsAutomatic()
                number += 1
            else:
                break

        p = CG(hesse_f_N(x), -1 * Grad, 10 * dim, math.pow(10,-4), x)

        alpha = 1           # Armijo-Backtracking-Verfahren
        while f(x + (alpha * p)) > F + 0.5 * alpha * np.dot(Grad, p):
            alpha = 0.5 * alpha
        xold = np.copy(x)  # Sicherung x
        x = x + alpha * p  # Update von x
        F = f(x)
        Grad = grad_f(x)
        iteration += 1


    print("Iterationen: " + str(iteration - 1))
    print("Anzahl gewählter Funktionen: " + str(number))
    print("Minimierer x der Funktionen ist: " + str(x))
    print("Der Fehler im Gradienten liegt bei: " + str(
        np.linalg.norm(Grad)))

    print("f(x) = " + str(F))
    print("Norm Gradient: " + str(np.linalg.norm(Grad)))
    print("Toleranz Gradient: " + str(tolerance * (1 + abs(F))))
    print("Unterschied Norm Gradient: " + str(abs(np.linalg.norm(Grad) - np.linalg.norm(Grad))))
    print("Toleranz Unterschied Gradient: " + str((10 ** -7)))
    print("Unterschied f: " + str(abs(F - f(xold))))
    print("Tolleranz f: " + str((10 ** -8) * (1 + abs(F))))
    print("Unterschied x: " + str(np.linalg.norm(xold - x)))
    print("Tolleranz x: " + str(math.pow(10, -8) * (1 + np.linalg.norm(x))))

#alpha = (np.dot(-1 * grad_f(x), p)) / np.dot(p, np.dot(hesse_f(x), p))  # optimale Schrittweite
# GUI*******************************************************************************************************************

# initiate window
GUI = Tk()
GUI.title("Eingabefeld")
GUI.geometry("500x500+500+500")

# input for function 'functionMaker'
label1 = Label(GUI, text = "Dimension der Matrix: ")
label1.pack()

entry1 = Entry(GUI)
entry1.pack()

label2 = Label(GUI, text = "Anzahl Funktionen: ")
label2.pack()

entry2 = Entry(GUI)
entry2.pack()

# triggers function 'functionMaker'
button1 = Button(GUI, text = "Erzeuge Diagonalmatrix Funktionen", command = functionMaker)
button1.pack(pady = 5)

# triggers function 'functionMaker2'
button2 = Button(GUI, text = "Erzeuge zufällige Funktionen", command = functionMaker2)
button2.pack()

# triggers function 'functionMaker3'
button2 = Button(GUI, text = "Erzeuge zufällige Funktionen auf Basis Einer", command = functionMaker3)
button2.pack(pady = 20)

# input for function 'chooseFunctions'
label3 = Label(GUI, text = "Anzahl der auszuwählenden Funktionen: ")
label3.pack()

entry3 = Entry(GUI)
entry3.pack()

# triggers function 'chooseFunction'
button3 = Button(GUI, text = "Wähle Funktionen", command = chooseFunctions)
button3.pack(pady = 20)

label4 = Label(GUI, text = "Fehlertoleranz: 10^-x")
label4.pack()

entry4 = Entry(GUI)
entry4.pack()

button4 = Button(GUI, text = "Finde Optimierer", command = optimize)
button4.pack(pady = 20)


mainloop()