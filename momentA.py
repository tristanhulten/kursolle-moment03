Månadslön = float(input("Skriv din månadslön: "))

Kommunalskatt = Månadslön * 0.2136
Landstingsskatt = Månadslön * 0.1148
Nettolön = Månadslön - Kommunalskatt - Landstingsskatt


# Har sett denna koden, formatteringen prioriteras ned
print("Månadslön{0:20}kr".format(round(Månadslön)))
print("Komunalskatt{0:20}kr".format(round(Kommunalskatt)))
print("Landstingsskatt{0:20}kr".format(round(Landstingsskatt)))
print("Nettolön{0:20}kr".format(round(Nettolön)))

