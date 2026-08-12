import bat
import dashboard

print("Willkommen zu Andis Dashboard")

with open ("csv_data.txt", "r") as f: 
    data = []
    e_pv = 0 
    e_st = 0 
    e_haus = 0 
    for lines in f:
       data.append(lines.strip().split(","))
    data = data[1:]
print("Daten wurden erfasst!")
sma_st = bat.Battery(10000, 8000, 40)
for element in data: 
    p_ov = int(element[2]) - int(element[1]) 
    p_st = sma_st.update(p_ov)
    e_pv += int(element[2]) * 60/3600
    e_haus += int(element[1]) * 60/3600
    e_st += p_st * 60/3600
    #dashboard.show_status(int(element[1]), int(element[2]), sma_st)

 
    

print("gesamte erzeugte Energie:",e_pv )
print("gesamte verbrauchte Energie im Haus:",e_haus )
print("Energie speicher:",e_st)
print("Neuer SOC: {}".format(sma_st.getSoc()))



