car_capacity = 4

class SpaceObject():
    def __init__(self, name, m, ro, o_o, r):
                
        if not str(name.replace(' ', '')).isalnum():
            raise NameError('Name is not valid!')
        self.name = str(name)
        self.m = float(m)
        self.ro = ro
        self.o_o = self.validate_orbiting(o_o)  
        self.r = r 
        self.population = 0
        
    def validate_orbiting(self, o_o):
        if type(o_o) in (list, tuple, set):
            return o_o
        else:
            raise TypeError('Orbiting Objects should be iterable!')
        
    def send_peeps_here(self, addnl):
        self.population = self.population + addnl
            
            
class Car(SpaceObject):
    def send_peeps_here(self, addnl):
        if self.population + addnl <= 0:
            self.population = 0
        elif self.population + addnl >= car_capacity:
            self.population = car_capacity
        elif self.population + addnl < car_capacity:
            self.population = self.population + addnl

class Star(SpaceObject):
    def send_peeps_here(self, addnl):
            self.population = 0
            
class Planet(SpaceObject):
    def __init__(self, name, m, ro, o_o, r, atm):
        super().__init__(name, m, ro, o_o, r)
        self.atm = atm
        