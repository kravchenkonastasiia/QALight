А = float(input("Number 1="))
Б = float(input("Number 2="))
В = float(input("Number 3="))
if А > Б:
    print("Свершилось!")
elif Б > А:
    print("Да ну!")
else:
    print("А если так!")
А = А + В
Б = Б - В
if А > Б:
    print("Свершилось!")
elif Б > А:
    print("Да ну!")