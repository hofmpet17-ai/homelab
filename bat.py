class Battery: 
    TIME_MESS = 60 
    SOC_MIN = 20 
    def __init__(self, capacity, max_power, soc): 
        self.k = capacity
        self.p_max = max_power 
        self.e = soc*self.k/100  
        self.e_min = self.k * self.SOC_MIN /100 

    def getSoc(self): 
         return self.e *100 / self.k
    

    def entladen(self, p):
        p_lad = abs(p)
        if (p_lad> self.p_max): 
            p_lad = self.p_max 
        e_lad = self.e - p_lad* self.TIME_MESS/3600 
        if(e_lad< self.e_min):
            p_lad = (self.e - self.e_min)*3600/self.TIME_MESS 
            e_lad = self.e_min 
        self.e = e_lad  
        return p_lad 
    def laden(self, p):
            p_lad = p
            if (p_lad> self.p_max): 
                p_lad = self.p_max 
            e_lad = self.e + p_lad* self.TIME_MESS/3600 
            if(e_lad> self.k ):
                p_lad = (self.k -self.e)*3600/self.TIME_MESS 
                e_lad = self.k  
            self.e = e_lad  
            return p_lad 

    def update(self, p): 
        if p< 0: 
              e = self.entladen(p)
        else: 
             e = self.laden(p)
        return e 
    
        

            