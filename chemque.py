import numpy as np
import pandas as pd
from IPython.display import display, Math, Latex                                                                                                                                                                                             
 #display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))                                                                                                                                                                     
 #display(Math(r'\ce{H2O}'))  

class mixque():
    def __init__():
        pass
    def queLatex():
        return display(Math(r'\ce{H2O}')) 
    
    q1 = {"Q-1. " : "What is mixture?", 
          "  A. " : "Composition of more than one substance", 
          "  B. " : "Composition of more than two substance ", 
          "  C. " : "Composition of more than three substance ", 
          "  D. " : queLatex() 
         }
    q2 = {"Q-2. " : "State the types of mixture -",
          "  A. " : "Homogeneous", 
          "  B. " : "Hetrogeneous " 
         }
    
    def printque():
        
        for x in mixque.q1:
            print(f'{x}{mixque.q1[x]}')
       
        
    def mixans(x):
        a1 = 'A mixture is a composition of more than one pure substance.'
        if x == a1:
            print ("Correct")
        else:
            print("Not correct")
