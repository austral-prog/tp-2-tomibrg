def change():
    expense = 23.75
    money = 100
    pesos = int(money - expense)
    centavos = int(((money - expense) - 76)*100)
    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}")

change()    
