from flask import Flask, render_template, jsonify
import sqlite3
import database 
app = Flask(__name__)

@app.route("/")
def home(): 
   
    return  render_template("index.html") 

@app.route("/api/data")
def send_data(): 
    conn = sqlite3.connect("EMS.db")
    data = database.get_latest(conn)
    return jsonify(data)

if __name__ == "__main__": 
    app.run(debug=True)