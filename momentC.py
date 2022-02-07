Månadslön = float(input("skriv din månadslön: "))
KommunalSkatt = Månadslön * 0.2136
LandstingSkatt = Månadslön * 0.1148
Årslön = Månadslön * 12
StatligSkatt = Månadslön * 0.2
VärnSkatt = Månadslön * 0.05

print("Utskrift")
print("Månadsinkomst      ",(Månadslön), 'Årsinkomst' ,(Årslön))
print("Kommunal skatt     ",(KommunalSkatt))
print("Landstingskatt     ",(LandstingSkatt))

if Årslön > 468700 and Årslön < 675700:
    print("Statlig skatt      ",(StatligSkatt))
    print("Kvar efter skatt   ",(Månadslön) - (KommunalSkatt) - (LandstingSkatt) - (StatligSkatt))

elif Årslön >= 675700:
    print("Statlig skatt      ",(StatligSkatt))
    print("Värnskatt          ",(VärnSkatt))
    print("Kvar efter skatt   ",(Månadslön) - (KommunalSkatt) - (LandstingSkatt) - (StatligSkatt) - (VärnSkatt));
else:
    print("Kvar efter skatt   ",(Månadslön) - (KommunalSkatt) - (LandstingSkatt))

if Årslön <= 19247:
    print("Du behöver inte betala skatt");