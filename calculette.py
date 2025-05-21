import tkinter as tk
import tkinter.font as tkFont

import math

def bin_convert(number:int) -> str:
    return bin(number).replace('0b','')

def hex_convert(number:int) -> str:
    return hex(number).replace('0x','').upper()

def dec_convert(number:str) -> int:
    return int(number, 2)

def cubiq_root(number:int):
    return number**(1/3)


class UltimateCalculator(tk.Tk):
    def __init__(self):
        """Constructeur de la classe"""

        super().__init__() # Classe fenêtre Tkinter

        self.title("Calculatrice version Félix")
        self.geometry("550x700") #320x120
        # self.resizable(False, False) # Empêche le redimensionnement de la fenêtre
        self.configure(bg="white")
        self.iconbitmap('assets/logo.ico')
        self.grid_columnconfigure(0, weight=1)
        
        self.mainFont = tkFont.Font(family="Arial", size=22, weight="normal", slant="roman")
        
        self.realExpression = []
        self.displayedExpression = []
        
        self.displayedExpressionsHistory = []
        self.realExpressionsHistory = []
        self.resultsHistory = ""
        
        self.waitingParenthesisNum = 0
        self.waitingBlock = False
        self.endAfterBlock = ")"
        
        self.historyDisplayed = 8
        self.mode = "standard"
        self.seconde = False
        self.degrad= "deg"

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
        self.headerStringVar = tk.StringVar()
        self.headerStringVar.set("Calculette")
        
        self.menuButton = tk.Menubutton(
            self.headerFrame, 
            textvariable=self.headerStringVar, 
            font=self.mainFont, 
            anchor="w",
            fg="black", bg ="white",
            cursor="hand2",
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
        self.expressionStringVar.set(">  ")
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
                    
        
    def changeMode(self, mode, switch_second=False, switch_degrad=False):
        """Permet de changer le mode de la calculette (standard, scientifique, expert), d'activer le bouton 2nd et de passer de gradient en degrès"""
        
        self.mode = mode
        
        if mode in ["standard", "scientifique", "scientifique2nd", "expert", "expert2nd"]:
            # On détruit tout les boutons déjà présent dans la frame des boutons
            for widget in self.buttonsFrame.winfo_children():
                widget.destroy()
            
            buttons_size = 5
            buttons_padding = 1
            
            
            
            if mode == "standard":
                self.headerStringVar.set("Calculette")
                self.mode = "standard"
                     
                # Liste des boutons par lignes
                buttons_contents = [
                    ["1", "2", "3", "+"],
                    ["4", "5", "6", "-"],
                    ["7", "8", "9", "*", "C"],
                    [".", "0", "⌫", "/", "="]
                ]
                buttons_size = 2
                buttons_padding = 0
                
                
            elif mode == "scientifique":
                self.headerStringVar.set("Calculatrice scientifique")
                
                if not switch_second or self.second :
                    self.second = False
                
                    # Liste des boutons par lignes
                    buttons_contents = [
                        ["2nd", "(", ")", "√", "**", "deg"],
                        ["π", "1", "2", "3", "/"],
                        ["sin", "4", "5", "6", "*"],
                        ["cos", "7", "8", "9", "-", "C"],
                        ["tan", ".", "0", "⌫", "+", "="]
                    ]
                else:
                    self.second = True

                    # Liste des boutons par lignes
                    buttons_contents = [
                        ["2nd", "(", ")", "³√", "x10ˣ", "deg"],
                        ["π", "1", "2", "3", "//"],
                        ["asin", "4", "5", "6", "mod"],
                        ["acos", "7", "8", "9", "%", "C-h"],
                        ["atan", ".", "0", "⌫", "+", "="]
                    ]
                buttons_size = 1
                buttons_padding = 5.5
                
                
            elif mode == "expert":
                self.headerStringVar.set("Calculatrice experte")
                self.mode = "expert"

                if not switch_second or self.second :
                    self.second = False
                
                    # Liste des boutons par lignes
                    buttons_contents = [
                        ["2nd",   "log",    "%", "(", ")", "√", "**", "deg"],
                        ["φ",     "e" ,    "π", "1", "2", "3", "/"],
                        ["dec", "asin", "sin", "4", "5", "6", "*"],
                        ["bin", "acos", "cos", "7", "8", "9", "-", "C"],
                        ["hex", "atan", "tan", ".", "0", "⌫", "+", "="]
                    ]
                else:
                    self.second = True
                    
                    # Liste des boutons par lignes
                    buttons_contents = [
                        ["2nd",   "log",    "%", "(", ")", "³√", "x10ˣ", "deg"],
                        ["φ",     "e" ,    "π", "1", "2", "3", "//"],
                        ["dec", "asin", "sin", "4", "5", "6", "mod"],
                        ["bin", "acos", "cos", "7", "8", "9", "-", "C-h"],
                        ["hex", "atan", "tan", ".", "0", "⌫", "+", "="]
                    ]
                buttons_size = 1
                buttons_padding = 1.75
                
                
            if switch_degrad:
                if self.degrad == "rad":
                    self.degrad = "deg"
                    
                elif self.degrad == "deg":
                    self.degrad = "rad"
                
                
                
            for i in range(len(buttons_contents)):
                for j in range(len(buttons_contents[i])):

                    numberButton = tk.Button(
                        self.buttonsFrame, 
                        text=buttons_contents[i][j], 
                        font=self.mainFont, 
                        width=buttons_size*3, height=buttons_size,
                        padx=buttons_padding*3, pady=buttons_padding,
                        cursor="hand2",
                        command = lambda text=buttons_contents[i][j]: self.addToExpression(text)
                    )
                    
                    # --- Cas particuliers de boutons aux commandes ou couleurs spécifiques ----
                    
                    
                    if buttons_contents[i][j].isdigit(): #les boutons de chiffres sont plus sombres
                        numberButton.config(bg="#dddddd")
                    
                    elif buttons_contents[i][j] == "2nd": #le bouton 2nd est violet
                        numberButton.config(bg="#ddddff")
                        if self.second:
                            numberButton.config(relief="sunken")
                        numberButton.config(command=lambda: self.changeMode(self.mode, True))
                    
                    
                    elif buttons_contents[i][j] == "deg": #le bouton deg/rad est violet
                        if self.degrad == "deg":
                            numberButton.config(bg="#fff5dd")
                            numberButton.config(command=lambda: self.changeMode(self.mode, False, True))
                            
                        elif self.degrad == "rad":
                            numberButton.config(bg="#fff0aa")
                            numberButton.config(relief="sunken")
                            numberButton.config(text="rad")
                            numberButton.config(command=lambda: self.changeMode(self.mode, False, True))
                        
                    
                    elif buttons_contents[i][j] == "⌫": #cas particulier du ⌫ qui efface un chiffre
                        numberButton.config(command=lambda: self.clearExpression(1))
                        numberButton.config(bg="#ffdddd")

                    elif buttons_contents[i][j] == "C": #cas particulier du C qui efface tout  
                        numberButton.config(command=self.clearExpression)
                        numberButton.config(bg="#ddeeff")
                        
                    elif buttons_contents[i][j] == "C-h": #cas particulier du C-h (clear historique obtenu en faisant 2nd + C) qui efface tout,même l'historique  
                        numberButton.config(command=lambda : self.clearExpression(clear_historique=True))
                        numberButton.config(bg="#9fbeff")

                    
                    elif buttons_contents[i][j] == "=": #cas particulier du = pour valider
                        numberButton.config(command=lambda: self.calculate())
                        numberButton.config(bg="#ddffdd")
                        
                    elif buttons_contents[i][j] == "π": # pi
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "math.pi"))
                        
                    elif buttons_contents[i][j] == "φ": # phi
                        numberButton.config(command=lambda  text=buttons_contents[i][j]: self.addToExpression(text, "(1 + math.sqrt(5)) / 2"))
                    
                    elif buttons_contents[i][j] == "e": # exponentiel
                        numberButton.config(command=lambda  text=buttons_contents[i][j]: self.addToExpression(text, "math.e"))
                    
                    
                    elif buttons_contents[i][j] in ["sin", "cos", "tan", "asin", "acos", "atan"]: # trigo
                        if self.degrad == "deg":
                            numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "math.degrees(math."+text+"(math.radians(", ")))"))
                        
                        elif self.degrad == "rad":
                            numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "math."+text+"(", ")"))


                    elif buttons_contents[i][j] in ["√"]: # racine carrée
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "math.sqrt(", ")"))
                    
                    elif buttons_contents[i][j] in ["³√"]: # racine cubique
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "cubiq_root(", ")"))
                    elif buttons_contents[i][j] in ["%"]: # pourcentage
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "*0.01*"))
                    
                    elif buttons_contents[i][j] in ["mod"]: # modulo
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "%"))

                    elif buttons_contents[i][j] in ["x10ˣ"]: # puissance de 10
                        numberButton.config(command=lambda: self.addToExpression("*10**", "*10**"))

                    
                    elif buttons_contents[i][j] in ["log"]: # logarythme
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "math.log(", ")"))
                    
                    # binaire, hexa et décimal
                    elif buttons_contents[i][j] == "bin": 
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "bin_convert(", ")"))
                    
                    elif buttons_contents[i][j] == "hex": 
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "hex_convert(", ")"))
                
                    elif buttons_contents[i][j] == "dec": 
                        numberButton.config(command=lambda text=buttons_contents[i][j]: self.addToExpression(text, "dec_convert('", "')"))
                    
                    
                    
        

                    numberButton.grid(row=i,column=j)
            
        else:
            raise(Exception("Incorrect mode"))

    
    def clearExpression(self, n=-1, clear_historique=False):
        """Clear la zone de l'expression"""
        if n <= 0:
            self.realExpression.clear()
            self.displayedExpression.clear()
            self.expressionStringVar.set(">  ")
            
        elif len(self.displayedExpression)>0:
            # on enlève n caractères
            if self.realExpression[-1].isdigit(): 
                self.realExpression[-1] = self.realExpression[-1][:-1]
                self.displayedExpression[-1] = self.displayedExpression[-1][:-1]
            else:
                self.realExpression = self.realExpression[:-n]
                self.displayedExpression = self.displayedExpression[:-1]
                
            self.expressionStringVar.set(">  " + "".join(self.displayedExpression))
            
            
        if clear_historique:
            self.displayedExpressionsHistory.clear()
            self.resultsHistory = ""
            
            self.lastExpressionsStringVar.set("")
            self.lastResultsStringVar.set("")



    def addToExpression(self, text, realtext=None, endOfBlock=None):
        """Ajouter un caractère à l'expression"""

        if realtext==None:
            realtext = text
        
        # Si l'expression est pour l'instant vide
        if len(self.realExpression) == 0 :    
            if realtext in ["+", "-", "*", "*0.01*", "/", "//", "%"]:
                #Si on met un caractère d'opération sans rien derrière, on prend le dernier résultat
                print("Dernier résulat : ", self.resultsHistory.splitlines()[-1])
                self.realExpression.append(self.resultsHistory.splitlines()[-1] + realtext )
                self.displayedExpression.append(self.resultsHistory.splitlines()[-1]+text )
            else:
                if endOfBlock != None: # si la fonction de l'opération nécessite une fermeture de parenthèse
                    self.waitingBlock = True
                    self.endAfterBlock = endOfBlock
                
                self.displayedExpression.append(text)
                self.realExpression.append(realtext)
                
            
        else :
            # Si c'est un chiffre qui fait partie d'un nombre
            if (text.isdigit() or text==".") and self.realExpression[-1].replace(")", "").replace("'", "").replace(".", "").isdigit(): 

                if self.realExpression[-1].count(')') > 0:
                    
                    end_parenthesis_num = 0
                    
                    for char in self.realExpression[-1][::-1]:
                        if char != ")" and  char != "'":
                            break
                        else:
                            end_parenthesis_num+=1
                                            
                    
                    self.realExpression[-1] =  self.realExpression[-1][:-end_parenthesis_num] + text + self.realExpression[-1][-end_parenthesis_num:]
                    self.displayedExpression[-1] = self.displayedExpression[-1] + text
                
                # Sinon, on place juste le chiffre avec le précédent pour ne former qu'un seul nombre-élément dans la liste de l'expression
                else :
                    self.realExpression[-1] += text
                    self.displayedExpression[-1] += text
            
            else:
                 
                # Si il forme un nombre à lui tout seul
                if text.isdigit() or text in ["π", "φ", "e"] :  
                    if self.waitingBlock:
                        self.waitingBlock = False
                        realtext += self.endAfterBlock
                        
                    if self.realExpression[-1].isdigit() or self.realExpression[-1] in ["π", "φ", "e"]:
                        realtext = "*"+realtext    
                
                # Si c'est une parenthèse ouvrante
                elif text == "(":                          
                    if self.waitingBlock:
                        self.waitingBlock = False
                        self.waitingParenthesisNum += 1
                
                # Si c'est une parenthèse fermante
                elif text == ")":                          
                    if self.waitingParenthesisNum > 0:
                        self.waitingParenthesisNum -= 1
                        realtext = ")"+self.endAfterBlock
                
                
                #Ssi c'est un caractère d'opération
                else: 
                    if endOfBlock != None:
                        self.waitingBlock = True
                        self.endAfterBlock = endOfBlock
                            
                            
                self.displayedExpression.append(text)
                self.realExpression.append(realtext)
                    
            
        
            
                                
            
        # print(self.waitingBlock)
        print(self.displayedExpression)
        print(self.realExpression)
        print("\n")
        self.expressionStringVar.set(">  " + "".join(self.displayedExpression))
    
    def calculate(self):
        """Calcule l'expression"""

        if len(self.realExpression) == 0:
            return False
        
        print("Expression :", "".join(self.realExpression), end="")

        expression_str = "".join(self.realExpression)
        
        # Calcul du résultat
        result = ""
        try:
            result = str(eval(expression_str))
            print(" = ", result)
            
        except Exception:
            result = "error"
            print(" = ", "error")
        
        # Enregistrement du résultat
        self.displayedExpressionsHistory.append(self.displayedExpression.copy())
        self.realExpressionsHistory.append(self.realExpression.copy())
        
        if self.resultsHistory != "":
            self.resultsHistory += "\n"
        self.resultsHistory+=str(result)
        
        
        # On affiche seulement les n dernières lignes de l'historique
        entire_expression_history_str = ""
        for expression in self.displayedExpressionsHistory[-self.historyDisplayed:]:
            entire_expression_history_str += "".join(expression) + "\n"
            
        self.lastExpressionsStringVar.set(entire_expression_history_str[0:-1])
        self.lastResultsStringVar.set('\n'.join(self.resultsHistory.splitlines()[-self.historyDisplayed:]))
        
        self.clearExpression()
        
        
    def onKeyPress(self, event):
        """"Méthode qui gère les entrées au clavier"""
        # On vérifie si la touche pressée est un chiffre
        if event.keysym.isdigit():
            
            self.addToExpression(event.keysym)
            

        elif event.keysym in ["plus", "minus", "asterisk", "slash", "period", "comma", "parenleft", "parenright"]:
            # caractères de calcul
            symbol_map = {
                "plus": "+",
                "minus": "-",
                "asterisk": "*",
                "period": ".",
                "comma": ".",
                "parenleft": "(",
                "parenright": ")",
            }
            self.addToExpression(symbol_map[event.keysym][0], )
        
        elif event.keysym in ["percent", "s", "c", "t", "!"]:
            # caractères de calcul dont l'affichage sur la calculette n'est pas le même que selon python le reconnais
            symbol_map = {
                "percent": ("%", "%")
            }
            
            self.addToExpression(symbol_map[event.keysym][0], symbol_map[event.keysym][1])
            
        
        elif event.keysym in ["Up", "Left"]:
            # flèches
            if event.keysym == "Up" :
                self.addToExpression( '\n'.join(self.resultsHistory.splitlines()[-1:]))
            elif event.keysym == "Left":
                self.addToExpression("".join(self.displayedExpressionsHistory[-1]), "".join(self.realExpressionsHistory[-1]))
            
            
        elif event.keysym == "Return":
            self.calculate()
        
        elif event.keysym == "BackSpace":
            self.clearExpression(1)
            
            
            
         
        
    def open(self):
        """Ouvre la fenêtre de la calculette"""
        self.mainloop()
        

if __name__ == "__main__":
    # Initialisation
    calculette = UltimateCalculator()
    # Ouverture de la calculette
    calculette.open()


 



