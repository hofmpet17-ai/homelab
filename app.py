from flask import Flask, render_template
import sqlite3
import database 
app = Flask(__name__)

@app.route("/")
def home(): 
    conn= sqlite3.connect("EMS.db")
    data = database.get_latest(conn)
    pv = data["p_pv"]
    p_haus = data["p_haus"]
    p_bat= data["p_bat"]
    p_netz = data["p_netz"]
    soc = data["soc"]
    date = "20.09.2026"
    time = data["time"]
    weather = "12°C"
    user = "admin"
    p_anlage = 15
    nenn_kap = 10
    
    return  render_template("index.html",pv = pv , p_haus = p_haus, p_bat = p_bat, p_netz = p_netz,soc = soc \
                            , date= date, time = time,weather = weather,\
                            user = user,p_anlage= p_anlage,nenn_kap= nenn_kap) 

if __name__ == "__main__": 
    app.run(debug=True)