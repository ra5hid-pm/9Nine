# $$\require{mhchem}$$ 
import numpy as np
import pandas as pd
from IPython.display import display, Math, Latex, Markdown   
  
 #display(Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'))                                                                                                                                                                     
 #display(Math(r'\ce{H2O}'))  

class mixque():
    def __init__(self,testkind):
        self.tetskind = testkind
        pass
    score = 0
    attempts ={ }
    
    
    
    q1 = {"Q-1. " : "What is mixture?", 
          "  A. " : "Composition of more than one substance", 
          "  B. " : "Composition of more than two substance ", 
          "  C. " : "Composition of more than three substance ", 
          "  D. " : 'Composition of atleast one substance'
         }
    
    q2 = {"Q-2. " : "A mixture with uniform composition throughout is called-",
          "  A. " : "Homogeneous", 
          "  B. " : "Hetrogeneous ",
          "  C. " : "Saturated",
          "  D. " : "Suspension"
         }
    q3 = {" Q-3. " : "Which of the following is a homogeneous mixture?",
          "  A. " : "Copper Sulphate mixed with Common Salt", 
          "  B. " : "Water mixed with oil ", 
          "  C. " : "Iron filings mixed with common salt", 
          "  D. " : 'Common salt mixed with water'
          
    
    }
    q4 = {" Q-4. " : "What is meant by saturated solution?",
          "  A. " : "Solution which does not accept further solute at any temprature", 
          "  B. " : "Solution which does not accept further solute at a given temprature", 
          "  C. " : "Solution which allows the solute to absorb all the solvent ", 
          "  D. " : 'Solution which do not accept further solute even if volume of solvent is increased'
          
    }
    q5 = {" Q-5. " : """Four Students P, Q, R and S have been given Copper Sulphate, Common Salt, Wheat Flour and Ink respectively.
          All of them have been asked to mix the given substance separately in a glass of water. Who will get a colloidal solution  """,
          "  A. " : "P", 
          "  B. " : "Q and R", 
          "  C. " : "S", 
          "  D. " : 'P and Q'
          
    }
    que =[q1,q2,q3,q4,q5]
    ans=["A", "A", "D", "B", "C"]
    
    def printque(y):
        # print a question with options from dictionary of questions as enumerated in the list que.
        # This means that y will be the list item which are then searched through x for priniting the questions
        # with its options.
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
    def printkey():
        for i in mixque.attempts:
            print(i, mixque.attempts[i])
            
       
   
