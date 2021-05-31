# $$\require{mhchem}$$ 
import numpy as np
import pandas as pd
from IPython.display import display, Math, Latex, Markdown   
  
 #display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))                                                                                                                                                                     
 #display(Math(r'\ce{H2O}'))  

class mixque():
    def __init__():
        pass
    score = 0
    attempts ={ }
    ans=["A", "B", "A"]
    
    
    q1 = {"Q-1. " : "What is mixture?", 
          "  A. " : "Composition of more than one substance", 
          "  B. " : "Composition of more than two substance ", 
          "  C. " : "Composition of more than three substance ", 
          "  D. " : '$\ce{H2O}$'
         }
    
    q2 = {"Q-2. " : "State the types of mixture -",
          "  A. " : "Homogeneous", 
          "  B. " : "Hetrogeneous " 
         }
    q3 = {" Q-3. " : " क्या हम हिंदी में काम कर सकते हैं ",
          "  A. " : "No", 
          "  B. " : "Not at all ", 
          "  C. " : "Yes, Occasionally  ", 
          "  D. " : 'Yes, Always'
          
    
    }
    que =[q1,q2,q3]
    
    def printque(y):
        
        for x in mixque.que[y]:
            display(Markdown(rf'{x}{mixque.que[y][x]}'))
            
            
        # Capture answer choice   
        input_choice = input ("Enter your choice from the given options: ")
        
        
        # Answer response variable y ensures
        if input_choice==mixque.ans[y]:
            print("Correct")
            mixque.attempts["Q"+str(y+1)] = "Right"
            mixque.score = mixque.score+1
        else:
            print(f'{"Not Correct"}')
            mixque.attempts["Q"+str(y+1)] = "Wrong"         
            
       
   
