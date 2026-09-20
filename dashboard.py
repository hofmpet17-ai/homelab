from bat import Battery
import analysis
def show_status(p_haus,p_pv, bat: Battery): 
    pov = p_pv - p_haus
    p_bat = bat.update(pov)
    p_netz  = pov - p_bat 
    print("Leistungsbilanz im Haus")
    print("="*15)
    print("PV_Leistung: {}".format(p_pv))
    print("Hausverbrauch: {}".format(p_haus))
    print("Batterieleistung: {}".format(p_bat))
    print("Netz: {}".format(p_netz))
    print("SOC: {}".format(bat.getSoc()))
def calculate_status(t, p_haus, p_pv, bat):

    p_ov = p_pv - p_haus
    p_bat = bat.update(p_ov)
    p_netz = p_ov - p_bat

    return {
        "time": t, 
        "p_pv": p_pv,
        "p_haus": p_haus,
        "p_bat": p_bat,
        "p_netz": p_netz,
        "soc": bat.getSoc()
    }

def get_summary(conn):
    bez, eins = analysis.e_netz(conn) 
    return { 
        "e_pv": analysis.calc_e_pv(conn), 
        "e_haus": analysis.calc_e_haus(conn), 
        "max_pv": analysis.max_pv(conn), 
        "max_haus": analysis.max_haus(conn), 
        "min_soc": analysis.min_soc(conn), 
        "max_soc": analysis.max_soc(conn), 
        "e_bezug": bez,
        "e_einspeisung": eins 
    }