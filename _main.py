class COLUMN :
    def __init__(self, name, BC, HC, No1, No, Numx, Numy, S, SM, whichFloor, steel1, steel2):
        self.name = name
        self.RCMaterial = name + '_CONC'
        if whichFloor[0] == 'R':
            self.FloorPtr = int(whichFloor[1:]) + 1000
        elif whichFloor[0] == 'B':
            self.FloorPtr = int(whichFloor[1:]) * -1
        elif IsInt(whichFloor) :
            self.FloorPtr = int(whichFloor)
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
        self.steel1 = steel1
        self.steel2 = steel2
class BEAM :
    def __init__(self, name, BC, HC, No, S, SM, whichFloor):
        self.name = name
        self.RCMaterial = name + '_CONC'
        if whichFloor[0] == 'R':
            if len(whichFloor) == 1:
                self.FloorPtr = 1000
            elif whichFloor[-1] >= '0' and whichFloor[-1] <= '9' :
                self.FloorPtr = int(whichFloor[1:]) + 1000
            else :
                self.FloorPtr = int(whichFloor[1:-1]) + 1000
        elif whichFloor[0] == 'B':
            self.FloorPtr = int(whichFloor[1:]) * -1
        elif IsInt(whichFloor) :
            self.FloorPtr = int(whichFloor)
        else :
            self.FloorPtr = -1000
        self.type = type  
        self.BC = BC  
        self.HC = HC  
        self.No = No  
        self.S = S
        self.SM = SM
        self.whichFloor = whichFloor
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def compare(case):
    return -case.FloorPtr
NodDic = {3 : 0.953, 
          4 : 1.27, 
          5 : 1.59, 
          6 : 1.91, 
          7 : 2.22, 
          8 : 2.54, 
          9 : 2.87, 
          10 : 3.22, 
          11 : 3.58,
          12 : 3.94,
          14 : 4.30,
          16 : 5.02,
          18 : 5.73}
def defaultList(InList, phase) :
    if phase == 0 :
        InList.append('$Unit\n')
        InList.append('KGF-CM\n')
        InList.append('\n')
        InList.append('$ RC Rectangle Section Definitions\n')
        InList.append('$\tName\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tAngle\n')
        InList.append('\t\t\t\tcm\tcm\tcm\n')
    elif phase == 1 :
        InList.append('\n$ End RC Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ RC Circle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tDiameter\tCover\tSNo\tSpacing\tSpacingM\tAngle\n')
        InList.append(' \t\t\tcm\t\tcm\t\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End RC Circle Section Definitions\n')
        InList.append('\n')
        InList.append('$ RC Hollow Rectangle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tth\ttw\tAngle\n')
        InList.append(' \t\t\tcm\tcm\tcm\tcm\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End RC Hollow Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ Composite A Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tth\tAngle\n')
        InList.append(' \t\t\tcm\tcm\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End Composite A Section Definitions\n')
        InList.append('\n')
        InList.append('$ Composite B Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tth\tAngle\n')
        InList.append(' \t\t\tcm\tcm\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End Composite B Section Definitions\n')
        InList.append('\n')
        InList.append('$ Composite Right Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tth\tAngle\n')
        InList.append(' \t\t\tcm\tcm\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End Composite Right Section Definitions\n')
        InList.append('\n')
        InList.append('$ SJS Retrofit Circle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tSMaterial\tDiameter\tCover\tSNo\tSpacing\tSpacingM\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\t\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End SJS Retrofit Circle Section Definitions\n')
        InList.append('\n')
        InList.append('$ SJS Retrofit Rectangle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tSMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End SJS Retrofit Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ SJR Retrofit Circle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tSMaterial\tDiameter\tCover\tSNo\tSpacing\tSpacingM\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\t\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End SJR Retrofit Circle Section Definitions\n')
        InList.append('\n')
        InList.append('$ SJR Retrofit Rectangle Section Definitions\n')
        InList.append('$ Name\tRCMaterial\tSMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End SJR Retrofit Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ CJS Retrofit Circle Section Definitions\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tDiameter\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\t\tcm\t\t\tcm\t\tcm\t\tcm\t\tcm\n')
        InList.append('\n')
        InList.append('$ End CJS Retrofit Circle Section Definitions\n')
        InList.append('\n')
        InList.append('$ CJS Retrofit Rectangle Section Definitions\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tWidth\tHeight\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\t\tcm\t\tcm\t\tcm\t\tcm\n')
        InList.append('\n')
        InList.append('$ End CJS Retrofit Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ CJR Retrofit Circle Section Definitions\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tDiameter\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\t\tcm\t\t\tcm\t\tcm\t\tcm\t\tcm\n')
        InList.append('\n')
        InList.append('$ End CJR Retrofit Circle Section Definitions\n')
        InList.append('\n')
        InList.append('$ CJR Retrofit Rectangle Section Definitions\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tWidth\tHeight\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tt\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\t\tcm\t\tcm\t\tcm\t\tcm\n')
        InList.append('\n')
        InList.append('$ End CJR Retrofit Rectangle Section Definitions\n')
        InList.append('\n')
        InList.append('$ WingWall A Section Definitons\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tWidth\tHeight\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tWL\tWR\tHU\tHB\tTSteel\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\t\t\tcm\tcm\t\tcm\t\tcm\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End WingWall A Section Definitions\n')
        InList.append('\n')
        InList.append('$ DUF A Section Definitons\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tWidth\tHeight\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tWR\tHU\tHB\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\t\t\tcm\tcm\t\tcm\t\tcm\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End DUF A Section Definitions\n')
        InList.append('\n')
        InList.append('$ DUF B Section Definitons\n')
        InList.append('$ Name\tRCMaterialA\tRCMaterialB\tWidth\tHeight\tCover\tSNoA\tSNoB\tSpacingA\tSpacingM\tSpacingB\tWL\tWR\tHU\tAngle\n')
        InList.append(' \t\t\t\t\tcm\tcm\tcm\t\t\t\tcm\tcm\t\tcm\t\tcm\tcm\tcm\tcm\n')
        InList.append('\n')
        InList.append('$ End DUF B Section Definitions\n\n')
        InList.append('$ Steels Location\n')
        InList.append('$\tName\t\tMaterial\t\tNo. X Y\n')