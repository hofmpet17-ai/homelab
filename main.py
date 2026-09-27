import bat
import dashboard
import sqlite3
import database
import analysis
import csv_gen
# ab hier neue main
# hier der setup Teil  
print("Willkomen zu Andis Dashboard!")
print("Erfassung der Systemparameter beginnt...")
p_nenn = 15000
sma_st = bat.Battery(10000, 8000, 40)
username = "Nerdiger Nerd"
conn = sqlite3.connect("EMS.db")
database.create_db(conn)
flag = True 
timer_day = 0
# ab jetzt beginnt der Teil in der Schleife 

while(flag is True): 
    csv_gen.get_sens()
    measurements = []
    with open("csv_data.txt", "r") as f: 
        data = []
        for lines in f: 
            data.append(lines.strip().split(","))
        data = data[1:]
    measurements.append(dashboard.calculate_status(data[0][0], int(data[0][1]), int(data[0][2]), \
                                                                sma_st))
    print(measurements)
    database.insert_data(conn, measurements)
    timer_day +=1
    if(timer_day % 1440 ==0 ): 
        timer_day = 0 
        auswertung = dashboard.get_summary(conn)
    if timer_day == 5: 
        flag = False
    # hier noch ein Delay einfügen bis die nächste messung ausgeführt werden soll.
        
database.get_data(conn)







