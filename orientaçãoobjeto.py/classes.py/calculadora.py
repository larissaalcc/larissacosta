class calculadora():
    def __init__(self,op): 
        if op == "+":
            result = self._adicionar()
            return result
        elif op == "-":
            result = self._subtrair()
            return result
      
            
    def _adicionar (self,):
        a = int(input("Primeiro: ")) 
        b = int(input("Segundo:"))
        c = a+b
        return c
    def _subtrair (self):
        a = int(input("Primeiro: ")) 
        b = int(input("Segundo:"))
        c = a-b
        return c
 




        
        
        
        
        
        
        
        
        