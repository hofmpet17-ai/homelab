from bat import Battery
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
