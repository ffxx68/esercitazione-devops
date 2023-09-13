# esercizio 2
from operazioni import * 

op_list = ["+","-","*","/"]
while True:
    oper = input ("operazione "+str(op_list)+", x=fine) ")
    if oper != "x":
        if oper == "+" or oper == "-" or oper == "*" or oper == "/":
            num1 = input ("numero 1 ")
            num2 = input ("numero 2 ")
            if num1.isnumeric() and num2.isnumeric():
                if oper == "-":
                    risul = diff (float(num1), float(num2))
                elif oper == "+":
                    risul = somma (float(num1), float(num2))
                elif oper == "*":
                    risul = moltip(float(num1), float(num2))
                elif oper == "/":
                    risul = divis(float(num1), float(num2))
                else :
                    pass
            else:
                print ("valori non numerici")
                quit()
        else :
            print ("operazione non ammessa")
            quit()
    else:
        quit()

    print ("risultato: "+str(risul))

