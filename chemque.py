import numpy as np
import pandas as pd
from IPython.display import display, Math, Latex                                                                                                                                                                                             
 #display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))                                                                                                                                                                     
 #display(Math(r'\ce{H2O}'))  

class mixque():
    def __init__():
    return pass
    q1 = ("Q-1. What is mixture?", 
          "A. Composition of more than one substance", 
          "B. Composition of more than two substance ", 
          "C. Composition of more than three substance ", 
          "D. Composition of at least one substance")
    q2 = 'Q-2. State the types of mixture -',
          "A. Homogeneous", 
          "B. Hetrogeneous " 
          )
    
    def printque(x):
        
        for x in mixque.q1:
            print(x)
       
        
    def mixans(x):
        a1 = 'A mixture is a composition of more than one pure substance.'
        if x == a1:
            print ("Correct")
        else:
            print("Not correct")
   
    def queLatex():
             
        return display(Math(r'\ce{H2O}')) 
