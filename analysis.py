

def calc_e_pv(conn):
    e_pv = 0
    cursor = conn.execute("SELECT p_pv FROM data ")
    for row in cursor: 
        e_pv += row[0]/1000/60
    return e_pv  

def calc_e_haus(conn): 
    e_haus = 0
    cursor = conn.execute("SELECT p_haus FROM data")
    for row in cursor: 
        e_haus += row[0]/1000/60
    return e_haus 

def max_pv(conn): 
    cursor = conn.execute("SELECT MAX(p_pv) FROM data")
    max_pv =  cursor.fetchone()
    return max_pv[0]

def max_haus(conn): 
    cursor = conn.execute("SELECT MAX(p_haus) FROM data")
    max_haus =  cursor.fetchone()
    return max_haus[0]

def min_soc(conn): 
    cursor = conn.execute("SELECT MIN(soc) FROM data ")
    result =  cursor.fetchone()
    return result[0]

def max_soc(conn): 
    cursor = conn.execute("SELECT MAX(soc) FROM data ")
    result =  cursor.fetchone()
    return result[0]

def e_netz(conn): 
    e_einsp = 0
    e_bez = 0 
    cursor = conn.execute("SELECT p_netz FROM data WHERE p_netz > 0")
    cursor1 = conn.execute("SELECT p_netz FROM data WHERE p_netz < 0")
    for row in cursor: 
        e_einsp += row[0]/1000/60
    for row1 in cursor1: 
        e_bez += abs(row1[0])/1000/60
    return e_bez, e_einsp