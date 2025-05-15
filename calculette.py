import tkinter as tk
import sys




class UltimateCalculator(tk.Tk):
    def __init__(self):
        """Constructeur de la classe"""

        super().__init__() # Classe fenêtre Tkinter

        self.title("Calculatrice version Félix")
        self.geometry("1000x500") #320x120
        self.resizable(False, False) # Empêche le redimensionnement de la fenêtre
        self.configure(bg="white")

        self.init_widgets()


    def init_widgets(self):
        """Initialise les widgets"""
        # Liste des boutons par lignes
        self.buttons_contents = [["1", "2", "3", "+"],
                                ["4", "5", "6", "-"],
                                ["7", "8", "9", "*"],
                                [".", "0", "C", "/"],
                                ["="]]


        # Création des labels
        self.expressionStringVar = tk.StringVar()
        self.expressionStringVar.set("Expression entrée: ")
        self.expressionLabel = tk.Label(self, textvariable=self.expressionStringVar, fg="red", bg ="white")
        self.expressionLabel.grid(row=0,column=4)


        self.resultStringVar = tk.StringVar()
        self.resultStringVar.set("Résultat: ")
        self.resultLabel = tk.Label(self, textvariable=self.resultStringVar, fg ="red", bg ="white")
        self.resultLabel.grid(row=3,column=4)
        
    def open(self):
        """Ouvre la fenêtre de la calculette"""
        # Création des boutons
        for i in range(len(self.buttons_contents)):
            for j in range(len(self.buttons_contents[i])):

                if self.buttons_contents[i][j] == "C": #cas particulier du C
                    numberButton = tk.Button(self, text=self.buttons_contents[i][j], width=15, height=5, command = self.clearExpression)
                    numberButton.grid(row=i,column=j)

                elif self.buttons_contents[i][j] == "=": #cas particulier du =
                    numberButton = tk.Button(self, text=self.buttons_contents[i][j], width=15, height=5, command = lambda: self.setResult(self.getExpression()))
                    numberButton.grid(row=i,column=1)

                else:
                    
                    numberButton = tk.Button(self, text=self.buttons_contents[i][j], width=15, height=5, command = lambda text=self.buttons_contents[i][j]: self.addToExpression(text))
                    numberButton.grid(row=i,column=j)



        self.mainloop()
        
    
    def clearExpression(self):
        """Clear la zone de l'expression"""
        self.expressionStringVar.set("Expression entrée: ")

    def getExpression(self):
        """Récupérer l'expression entrée'"""
    
        print("Expression :", self.expressionStringVar.get()[len("Expression entrée: "):], end="")
        return self.expressionStringVar.get()[len("Expression entrée: "):]
    

    def addToExpression(self, text):
        """Ajouter un caractère à l'expression"""
        self.expressionStringVar.set(self.expressionStringVar.get()+text)
    

    def setResult(self, expression):
        """Insère le résultat dans son label de l'expression'"""
        try:
            result = str(eval(expression))
            self.resultStringVar.set("Résultat: "+result)
            print(" = ", result)
            
        except Exception:
            self.expressionStringVar.set("Expression entrée: ")
            self.resultStringVar.set("Résultat: "+"Erreur de syntaxe")
            print(" = ", "error")


# Initialisation
calculette = UltimateCalculator()
# Ouverture de la calculette
calculette.open()

 



