import tkinter as tk

# Création de la fenêtre principale
window = tk.Tk()
window.title("Calculatrice version modèle")
window.geometry("320x130") #320x120


# Liste des boutons par lignes
buttons_contents = [["1", "2", "3", "+"],
                    ["4", "5", "6", "-"],
                    ["7", "8", "9", "*"],
                    [".", "0", "C", "/"],
                    ["="]]



# Création des labels
expressionStringVar = tk.StringVar()
expressionStringVar.set("Expression entrée: ")
expressionLabel = tk.Label(window, textvariable=expressionStringVar, fg ="red", bg ="white")
expressionLabel.grid(row=0,column=4)


resultStringVar = tk.StringVar()
resultStringVar.set("Résultat: ")
resultLabel = tk.Label(window, textvariable=resultStringVar, fg ="red", bg ="white")
resultLabel.grid(row=3,column=4)



def clearExpression():
    """Clear la zone de l'expression"""
    expressionStringVar.set("Expression entrée: ")

def getExpression():
    """Récupérer l'expression entrée'"""
    print("Calcul de l'expression : ", expressionStringVar.get().removeprefix("Expression entrée: "), end="")
    return expressionStringVar.get().removeprefix("Expression entrée: ")

def addToExpression(text):
    """Ajouter un caractère à l'expression'"""
    expressionStringVar.set(expressionStringVar.get()+text)



def setResult(expression):
    """Insère le résultat dans son label de l'expression'"""
    try:
        result = str(eval(expression))
        resultStringVar.set("Résultat: "+result)
        print(" = ", result)
        
    except Exception:
        expressionStringVar.set("Expression entrée: ")
        resultStringVar.set("Résultat: "+"Erreur de syntaxe")
        print(" = ", "error")
        


# Création des boutons
for i in range(len(buttons_contents)):
    for j in range(len(buttons_contents[i])):

        if buttons_contents[i][j] == "C": #cas particulier du C
            numberButton = tk.Button(window, text=buttons_contents[i][j], command = clearExpression)
            numberButton.grid(row=i,column=j)

        elif buttons_contents[i][j] == "=": #cas particulier du =
            numberButton = tk.Button(window, text=buttons_contents[i][j], command = lambda: setResult(getExpression()))
            numberButton.grid(row=i,column=1)


        else:
            
            numberButton = tk.Button(window, text=buttons_contents[i][j], command = lambda text=buttons_contents[i][j]: addToExpression(text))
            numberButton.grid(row=i,column=j)



window.mainloop()