Månadslön = float(input("skriv din månadslön: ")) 
Kommunalskatt = Månadslön * 0.2136
Landstingsskatt = Månadslön * 0.1148
Nettolön = Månadslön - Kommunalskatt - Landstingsskatt
Årslön = Månadslön * 12 

print("Utskrift:") 

print("Månadslön", Månadslön, "Kr", "(Årslön:", Årslön, "Kr)" ) 

#if-sats
if Årslön < 19257.00: 
    print("Du behöver inte betala skatt")  

else:
    print("Komunalskatt{0:20}kr".format(round(Kommunalskatt)))
    print("Landstingsskatt{0:20}kr".format(round(Landstingsskatt)))
    print("Nettolön{0:20}kr".format(round(Nettolön)))