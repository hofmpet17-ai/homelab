def entladen(soc, p_ent, k, t): 
    e_ent = p_ent * t /3600 
    new_soc = soc - e_ent/ k 
    return new_soc  
def laden(soc, p_lad, k , t): 
    e_lad = p_lad * t/3600 
    new_soc = soc + e_lad/k
    return new_soc
 
time_refresh = 60

# neue Programm struktur 
# prüfpunkt 1 gibt es Überschuss oder Defizit 
# ja 
# wie viel kann batterie laden 
# nein 
# 
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
if p_ov >0: 
    if soc < 100:
        if p_ov > p_lad: 
            soc_neu = laden(soc, p_lad,k,time_refresh) 
            if soc_neu > 100: 
                e_dif = k - soc * k
                p_lad = e_dif*3600 / time_refresh 
                soc_neu = laden(soc, p_lad,k,time_refresh) 
            p_ein = p_ov - p_lad

            
            print("Die batterie wird gerade mit {} W geladen und es werden {} W eingespeist"
                  "" .format(p_lad,p_ein))
        else: 
            p_lad = p_ov
            soc_neu = laden(soc, p_lad,k,time_refresh) 

            if soc_neu > 100: 
                e_dif = k - soc * k
                p_lad = e_dif*3600 / time_refresh
                soc_neu = laden(soc, p_lad,k,time_refresh) 
  
            p_ein = p_ov - p_lad
            soc = soc_neu 
            print("Die batterie wird gerade mit {} W geladen und es werden {} W eingespeist" \
            "" .format(p_lad,p_ein))
    else:
        print("Es werden gerade {} W ins Netz eingespeist".format(p_ov))
if p_ov <0:
    if soc > 20: 
        if abs(p_ov) > p_ent: 
            e_ent = p_ent * time_refresh / 3600 
            soc_neu = entladen(soc, p_ent, k, time_refresh) 
            if soc_neu < 20: 
                e_dif = k*0.2 - soc * k
                p_ent = e_dif*3600 / time_refresh
                soc_neu = entladen(soc, p_ent, k, time_refresh) 
  
            soc = soc_neu 
            p_netz = abs(p_ov) - p_ent
            print("Die batterie wird gerade mit {} W entladen und es werden {} W aus dem Netzbezogen" 
                "" .format(p_ent,p_netz))
        else: 
            p_ent = abs(p_ov)
            soc_neu = entladen(soc, p_ent, k, time_refresh) 
            if soc_neu < 20: 
                            e_dif = k*0.2 - soc * k
                            p_ent = e_dif*3600 / time_refresh
                            soc_neu = entladen(soc, p_ent, k, time_refresh) 
            soc = soc_neu
            p_netz = abs(p_ov)- p_ent 
            soc = soc_neu 
            print("Die batterie wird gerade mit {} W entladen und es werden {} W aus dem Netzbezogen" 
                            "" .format(p_ent,p_netz))

 
    else: 
        p_netz = abs(p_ov)
        print("Die Batterie ist zu niedrig geladen, es müssen {} W aus dem Netz bezogen werden".format(p_netz))
if p_ov == 0:
    print("Das Haus ist energieautark")

print("Der neue SOC der Batterie beträgt: ", soc)

