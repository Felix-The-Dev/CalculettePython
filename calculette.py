import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


import sys




class UltimateCalculator(tk.Tk):
    def __init__(self):
        """Constructeur de la classe"""

        super().__init__() # Classe fenêtre Tkinter

        self.title("Calculatrice version Félix")
        self.geometry("550x700") #320x120
        self.resizable(False, False) # Empêche le redimensionnement de la fenêtre
        self.configure(bg="white")
        self.iconbitmap('assets/logo.ico')
        self.grid_columnconfigure(0, weight=1)
        
        self.mainFont = tkFont.Font(family="Arial", size=22, weight="normal", slant="roman")
        
        self.expressionsHistory = ""
        self.resultsHistory = ""
        self.historyDisplayed = 8
        self.mode = "standard"

        self.init_widgets()
        
        self.bind("<Key>", self.onKeyPress)


    def init_widgets(self):
        """Initialise les widgets"""
        

        # ----- Création des trois principales Frames (du bas vers le haut)-----
        self.buttonsFrame = tk.Frame(self, bg="white")
        self.buttonsFrame.pack(side="bottom", fill=tk.X)
        
        self.expressionFrame = tk.Frame(self, bg="white")
        self.expressionFrame.pack(side="bottom", fill=tk.X)
        
        self.resultsFrame = tk.Frame(self, bg="white")
        self.resultsFrame.pack(side="bottom", fill=tk.X)
        
        self.headerFrame = tk.Frame(self, bg="white")
        self.headerFrame.pack(side="top", fill=tk.X)
        
        
        
        # ----- Création du header -----
        
        
        # # Label du header
        # self.headerLabel = tk.Label(
        #     self.headerFrame, 
        #     textvariable=self.headerStringVar, 
        #     font=self.mainFont, 
        #     anchor="w",
        #     fg="black", bg ="white"
        # )
        
        
        # Bouton du Header
        # image = Image.open("assets/menu_icon.webp") 
        # image = image.resize((50, 50), Image.LANCZOS)
        # photo = ImageTk.PhotoImage(image)
        
        self.headerStringVar = tk.StringVar()
        self.headerStringVar.set("Calculette")
        
        self.menuButton = tk.Menubutton(
            self.headerFrame, 
            textvariable=self.headerStringVar, 
            font=self.mainFont, 
            anchor="w",
            fg="black", bg ="white",
            relief=tk.RAISED
        )
        
        self.menu = tk.Menu(self.menuButton, tearoff=0)
        
        self.menu.add_command(label="Standard", command=lambda: self.changeMode("standard"))
        self.menu.add_command(label="Scientifique", command=lambda: self.changeMode("scientifique"))
        self.menu.add_command(label="Experte", command=lambda: self.changeMode("expert"))
        
        self.menuButton.configure(menu=self.menu)
        self.menuButton.pack(side="left")
        
        
        



        # ----- Création des labels -----
        
        # Label de l'expression entrée
        self.expressionStringVar = tk.StringVar()
        self.expressionStringVar.set(">   ")
        self.expressionLabel = tk.Label(
            self.expressionFrame, 
            textvariable=self.expressionStringVar, 
            font=self.mainFont, 
            anchor="w",
            fg="red", bg ="#d1d1d1"
        )        
        self.expressionLabel.pack(fill=tk.X, expand=True)
        
        
        # Label des dernières expressions entrées
        self.lastExpressionsStringVar = tk.StringVar()
        self.lastExpressionsStringVar.set("")
        self.lastExpressionsLabel = tk.Label(
            self.resultsFrame, 
            textvariable=self.lastExpressionsStringVar, 
            font=self.mainFont, 
            anchor="w",
            fg="black", bg ="white"
        )
        self.lastExpressionsLabel.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        
        # Label des derniers résulats
        self.lastResultsStringVar = tk.StringVar()
        self.lastResultsStringVar.set("")
        self.lastResultsLabel = tk.Label(
            self.resultsFrame, textvariable=self.lastResultsStringVar, 
            font=self.mainFont, 
            anchor="e",
            fg ="gray", bg ="white"
        )
        self.lastResultsLabel.pack()
        
        
        
        
        # --------- Création des boutons ----------
        
        self.changeMode("standard")
                    
                    
           
    def changeMode(self, mode):
        
        self.mode = mode
        
        if mode in ["standard", "scientifique", "expert"]:
            # On détruit tout les boutons déjà présent dans la frame des boutons
            for widget in self.buttonsFrame.winfo_children():
                widget.destroy()
            
            buttons_size = 5
            
            
            
            if mode == "standard":
                self.headerStringVar.set("Calculette")
                     
                # Liste des boutons par lignes
                buttons_contents = [
                    ["1", "2", "3", "+"],
                    ["4", "5", "6", "-"],
                    ["7", "8", "9", "*", "C"],
                    [".", "0", "⌫", "/", "="]
                ]
                buttons_size = 2
                
                
            elif mode == "scientifique":
                self.headerStringVar.set("Calculatrice scientifique")
                
                # Liste des boutons par lignes
                buttons_contents = [
                    ["(", ")", "√", "**"],
                    ["1", "2", "3", "+"],
                    ["4", "5", "6", "-"],
                    ["7", "8", "9", "*", "C"],
                    [".", "0", "⌫", "/", "="]
                ]
                buttons_size = 1
                
                
            elif mode == "expert":
                self.headerStringVar.set("Calculatrice experte")
                
                # Liste des boutons par lignes
                buttons_contents = [
                    ["(", ")", "√", "**"],
                    ["1", "2", "3", "+"],
                    ["4", "5", "6", "-"],++
                    ["7", "8", "9", "*", "C"],
                    [".", "0", "⌫", "/", "="]
                ]
                buttons_size = 1
                
                
                
                
                
                
            for i in range(len(buttons_contents)):
                for j in range(len(buttons_contents[i])):

                    numberButton = tk.Button(
                        self.buttonsFrame, 
                        text=buttons_contents[i][j], 
                        font=self.mainFont, 
                        width=buttons_size*3, height=buttons_size,
                        command = lambda text=buttons_contents[i][j]: self.addToExpression(text)
                    )
                    
                    
                    # --- Cas particuliers de boutons aux commandes spécifiques
                    if buttons_contents[i][j] == "⌫": #cas particulier du C qui efface un chiffre
                        numberButton.config(command=lambda: self.clearExpression(1))

                    if buttons_contents[i][j] == "C": #cas particulier du C qui efface tout  
                        numberButton.config(command=self.clearExpression)

                    
                    elif buttons_contents[i][j] == "=": #cas particulier du = pour valider
                        numberButton.config(command=lambda: self.calculate(self.getExpression()))
        

                    numberButton.grid(row=i,column=j)
            
        else:
            raise(Exception("Incorrect mode"))

    
    def clearExpression(self, n=-1):
        """Clear la zone de l'expression"""
        if n <= 0:
            self.expressionStringVar.set("> ")
            
        elif len(self.expressionStringVar.get())>2:
            self.expressionStringVar.set(self.expressionStringVar.get()[:-n])


    def getExpression(self):
        """Récupérer l'expression entrée'"""
    
        print("Expression :", self.expressionStringVar.get()[len("> "):], end="")
        return self.expressionStringVar.get()[len("> "):]
    

    def addToExpression(self, text):
        """Ajouter un caractère à l'expression"""
        
        print(len(self.expressionStringVar.get()[2:]))
        if len(self.expressionStringVar.get()[2:]) == 0 and text in ["+", "-", "*", "/", "%"]:
            self.expressionStringVar.set(self.expressionStringVar.get()+'\n'.join(self.resultsHistory.splitlines()[-1:])+text)

        else:
            self.expressionStringVar.set(self.expressionStringVar.get()+text)
    
    
    def calculate(self, expression):
        """Calcule l'expression"""

        # Calcul du résultat
        result = ""
        try:
            result = str(eval(expression))
            print(" = ", result)
            
        except Exception:
            result = "error"
            print(" = ", "error")
        
        # Enregistrement du résultat
        self.expressionsHistory += "\n"+str(expression)
        self.resultsHistory += "\n"+str(result)
        
            
        # On affiche seulement les 3 dernières lignes de l'historique
        self.lastExpressionsStringVar.set('\n'.join(self.expressionsHistory.splitlines()[-self.historyDisplayed:]))
        self.lastResultsStringVar.set('\n'.join(self.resultsHistory.splitlines()[-self.historyDisplayed:]))
        
        self.clearExpression()
        
        
    def onKeyPress(self, event):
        # On vérifie si la touche pressée est un chiffre
        if event.keysym.isdigit():
            
            self.addToExpression(event.keysym)
            

        elif event.keysym in ["plus", "minus", "asterisk", "slash", "period", "comma", "percent"]:
            # caractères de calcul
            symbol_map = {
                "plus": "+",
                "minus": "-",
                "asterisk": "*",
                "period": ".",
                "comma": ".",
                "percent": "%"
            }
            self.addToExpression(symbol_map[event.keysym])
        
        elif event.keysym in ["Up", "Left", "parenleft", "parenright"]:
            # caractères de calcul autres
            symbol_map = {
                "parenleft": "(",
                "parenright": ")",
                "Up": '\n'.join(self.resultsHistory.splitlines()[-1:]),
                "Left": '\n'.join(self.expressionsHistory.splitlines()[-1:])
            }
            
            self.addToExpression(symbol_map[event.keysym])
            
        elif event.keysym == "Return":
            self.calculate(self.getExpression())
        
        elif event.keysym == "BackSpace":
            self.clearExpression(1)

         
        
    def open(self):
        """Ouvre la fenêtre de la calculette"""
        self.mainloop()
        
# Initialisation
calculette = UltimateCalculator()
# Ouverture de la calculette
calculette.open()


 



