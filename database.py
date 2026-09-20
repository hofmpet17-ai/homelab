import sqlite3 

def create_db(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS data \
                 (id INTEGER PRIMARY KEY, time TEXT NOT NULL, p_pv INTEGER,\
                  p_haus INTEGER, p_bat INTEGER, p_netz INTEGER, soc REAL);")
    conn.commit() 

def insert_data (conn,data: list): 
    try:
        for e in data:
            conn.execute("INSERT INTO data (time, p_pv, p_haus, p_bat, p_netz, soc) \
                        VALUES(?,?,?,?,?,?)",(e['time'], e['p_pv'],\
                                              e['p_haus'],e['p_bat'],\
                                            e['p_netz'],round(e['soc'],3))) 
        conn.commit()
    except TypeError: 
        return "WRONG PARAMETERS"

def get_data(conn): 
    cursor1 = conn.execute("SELECT * FROM data")
    for element in cursor1: 
        print(element)
    
def delete_data(conn, id: int):
    try:
         cursor = conn.execute(" DELETE FROM data WHERE id = ?",(id,))
         conn.commit()
         return bool(cursor.rowcount)     
    except sqlite3.Error: 
        return False

def update_data(conn, id, column, value): 
    allowed_columns = ["time", "p_pv", "p_haus", "p_bat", "p_netz", "soc"]
    if column not in allowed_columns: 
        return False 
    try: 
        cursor =conn.execute(f"UPDATE data SET {column} = ? WHERE id = ?",(value,id))
        conn.commit()
        return bool(cursor.rowcount)
    except sqlite3.Error: 
        return False
    
def update_row(conn, id:int,e:dict):
    cursor = conn.execute("UPDATE data SET time = ?, p_pv= ?, p_haus=?, p_bat = ?, p_netz= ?, soc= ? WHERE id = ?",(e['time'], e['p_pv'],\
                                              e['p_haus'],e['p_bat'],\
                                            e['p_netz'],round(e['soc'],3), id))
    conn.commit()
    return bool(cursor.rowcount)

def clear_data(conn):
    cursor = conn.execute("DELETE FROM data")
    conn.commit()
    return bool(cursor.rowcount)
def get_latest(conn): 
    cursor = conn.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
    my_list = []
    for element in cursor: 
        my_list.append(element)
    my_dict = {
            "id": my_list[0][0], 
            "time": my_list[0][1], 
            "p_pv": my_list[0][2], 
            "p_haus": my_list[0][3], 
            "p_bat" : my_list[0][4], 
            "p_netz": my_list[0][5],  
            "soc" : my_list[0][6]
        }
    return my_dict