
def fibonnaci(valorProcurado):
    fib1 = 1
    fib2=1
    soma = 0
    
    flag_achou = 0
    
    if (valorProcurado >=0 and valorProcurado <= 2):
        flag_achou = 1
    
    while (flag_achou == 0):
        soma = fib2+fib1
        fib1 = fib2
        fib2 = soma
        if (soma == valorProcurado):
            flag_achou = 1
        
        if (soma > valorProcurado):
            print("Valor n pertece")
            return 0
        
    
    
    print("Valor pertence.") 

fibonnaci(14)
