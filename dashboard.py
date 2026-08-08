from bat import Battery
def show_status(p_haus,p_pv, bat: Battery): 
    pov = p_pv - p_haus
    p_bat = bat.update(pov)
    if(pov > 0): 
        p_ein = pov - p_bat
    print("Leistungsbilanz im Haus")
    print("="*15)
    print("PV_Leistung: {}".format(p_pv))
    print("Hausverbrauch: {}".format(p_haus))
    print("Batterieleistung: {}".format(p_bat))
    print("Aktuelle Einspeisung: {}".format(p_ein))
def show_welcome(name): 
    print("Willkommen zu Ihrem Dashboard {}".format(name))
    print("Was wollen Sie heute machen ?")

def 