class Case :
    def __init__(self, name, BC, HC, No1, No, Numx, Numy, S, SM, whichFloor):
        self.name = name
        tmp = whichFloor[:-1]
        if tmp[0] == 'R':
            self.FloorPtr = int(tmp[1:]) + 1000
        elif tmp[0] == 'B':
            self.FloorPtr = int(tmp[1:]) * -1
        elif IsInt(tmp) :
            self.FloorPtr = int(tmp)
        else :
            self.FloorPtr = -1000
        self.type = type  
        self.BC = BC  
        self.HC = HC  
        self.No1 = No1  
        self.No = No  
        self.Numx = Numx
        self.Numy = Numy
        self.S = S
        self.SM = SM
        self.whichFloor = whichFloor
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False