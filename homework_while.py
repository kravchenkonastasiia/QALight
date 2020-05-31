А = float(input("Number 1="))
Б = float(input("Number 2="))
В = float(input("Number 3="))
while А <= Б:
    А = А + В
    if А <= Б:
        print("Значение А:" + str(А) + "- Пока что нет")
    elif А > Б:
        print("Дождались!" + "Финальный А:" + str(А))