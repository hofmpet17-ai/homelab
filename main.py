# neue Programm struktur 
# prüfpunkt 1 gibt es Überschuss oder Defizit 
# ja 
# wie viel kann batterie laden 
# rest einpeisung
# nein 
# wie viel kann batteirie entladen 
#rest einspeisung 
#main.py liest Daten ein 
print("Willkommen zu Andis Dashboard")
print("Bitte die aktuelle PV-Leistung in Watt angeben:")
p_pv = int(input())
print("Bitte den akutellen Hausverbrauch in Watt angeben:")
p_haus = int(input())
print("Bitte Kapazität der Batterie in kwh eingeben:")
k = float(input())*1000 
print("Bitte den aktuellen SOC der Batterie angeben: ")
soc = int(input())
p_ov = p_pv- p_haus
print("Bitte maximale Ladeleistung eingeben:")
p_lad = int(input())
p_ent = p_lad