import random 
from datetime import datetime, timedelta
def get_sens(): 
    with open("csv_data.txt","w") as f: 
        f.write("time, p_haus, p_pv\n")
        time = datetime(2026,8,12, 12,0,0)

         
        p_haus = random.randint(0, 10000)
        p_pv = random.randint(0, 15000)
        time = time + timedelta(minutes=1)
        text = "{},{},{}\n".format(time.strftime("%H:%M"), p_haus, p_pv)
        f.write(text)



if __name__ == "__main__": 
        get_sens()
        vals = []
        with open("csv_data.txt","r") as f: 
             for lines in f: 
                 vals.append(lines.strip().split(","))
        vals = vals[1:]
        print(vals) 
