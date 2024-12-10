x = int(input('insira um número: '))
y = int(input('insira outro número: '))
 
a = (input('insira a operação que você deseja: '))

if a == 'soma':
    print (f"O resultado da adição é: {int (x + y)}")
    
if a == 'subtração':   
    print (f"O resultado da subtração é: {int (x - y)}")

if a == 'multiplicação':
    print (f"O resultado da multiplicação é: {int (x * y)}")
    
if a == 'divisão':
    print (f"O resultado da divisão é: {int (x / y)}")
