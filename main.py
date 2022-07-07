from email.policy import default
import os

from numpy import spacing
from _main import *
from LogSystem import *

cwd = os.getcwd()
filename = cwd.split('\\')[-1]
OutputDataX = []
defaultList(OutputDataX, 0)
OutputDataY = []
defaultList(OutputDataY, 0)
# load CXX
CXX = ReadFile('CXX.DAT', os.path.basename(__file__))
## get Floor and Cross section
CandF = CXX.readline().split()
try :
    C = int(CandF[0])
    F = int(CandF[1])
except Exception as e:
    WriteEx()
    ExceptionExit('CXX Read File Error.')
for i in range(C):
    CXX.readline()
for i in range(F):
    CXX.readline()
for i in range(F):
    CXX.readline()
ALLCOLUMN = []
CXX_Data = CXX.readlines()
LineLen = len(CXX_Data)
Progress = 0
CaseCXX = 0
while CaseCXX < LineLen:
    ## set lines
    lines = []
    try :
        lines.append(CXX_Data[CaseCXX].split())
        lines.append(CXX_Data[CaseCXX + 1].split())
        lines.append(CXX_Data[CaseCXX + 2].split())
        lines.append(CXX_Data[CaseCXX + 3].split())
        lines.append(CXX_Data[CaseCXX + 4].split())
        lines.append(CXX_Data[CaseCXX + 5].split())
    except Exception as e:
        WriteEx()
        ExceptionExit('CXXData Out of range.')
    #floor and name
    try :
        if lines[0][0][-1] >= '0' and lines[0][0][-1] <= '9' or lines[0][0][-1] == 'F':
            floor = lines[0][0]
        else :
            floor = lines[0][0][:-1]
        name = floor + lines[0][2]
    except Exception as e:
        WriteEx()
        ExceptionExit('CXX: line 0 Out of range. Doing floor name.')
    ## BC HC type
    try :
        BC = float(lines[1][0])
        HC = float(lines[1][1])
    except Exception as e:
        WriteEx()
        ExceptionExit('CXX: line 1 Out of range. Doing BC HC.')
    if BC == 0 and HC == 0:
        CaseCXX = CaseCXX + 6
        continue
    ## No1
    try :
        No1 = lines[2][0]
    except Exception as e:
        WriteEx()
        ExceptionExit('CXX: line 2 Out of range. Doing No1 No2.')
    No1 = '#' + No1
    # No Numx Numy
    try :
        if lines[5][0] != lines[5][3]:
            ExceptionExit('Error in No. First Element diff with last Element in line 5.')
        No = '#' + lines[5][0]
        Numx = int(lines[4][3]) + 2
        Numy = int(lines[3][3]) + 2
        S = int(lines[5][1])
        SM = int(lines[5][2])
        steel1 = int(lines[3][0])
        steel2 = int(lines[4][0])
    except Exception as e:
        WriteEx()
        ExceptionExit('CXX: line 4 or 5 Out of range. Doing No Numxy S.')
    whichFloor = floor
    ALLCOLUMN.append(COLUMN(name, BC, HC, No1, No, Numx, Numy, S, SM, whichFloor, steel1, steel2))
    CaseCXX = CaseCXX + 6
    ## progress bar
    # if float(CaseCXX / LineLen) * 10.0 > Progress:
    #     Progress = Progress + 1
    #     print("\r", end = '')
    #     print('[', end = '')
    #     for i in range(Progress):
    #         print('|', end = '')
    #     for i in range(10 - Progress):
    #         print(' ', end = '')
    #     print(']', end = '')
    #     time.sleep(0.05)
    ## progress bar
#load beam data
Beam = ReadFile('A6B103C.dat', os.path.basename(__file__))
#load useless data
KeepRead  = True
while KeepRead:
    line = Beam.readline()
    if line.find('BEAM') != -1:
        KeepRead = False
KeepRead  = True
while KeepRead:
    line = Beam.readline()
    if line != '\n':
        KeepRead = False
ALLBEAM = []
BEAM_Data = [line]
for line in Beam.readlines():
    if line != '\n' and line.find('BEAM') == -1:
        BEAM_Data.append(line)
LineLen = len(BEAM_Data)
Progress = 0
CaseBeam = 0
while CaseBeam < LineLen:
    ## set lines
    lines = []
    try :
        lines.append(BEAM_Data[CaseBeam])
        lines.append(BEAM_Data[CaseBeam + 1])
        lines.append(BEAM_Data[CaseBeam + 2])
        lines.append(BEAM_Data[CaseBeam + 3])
        lines.append(BEAM_Data[CaseBeam + 4])
        lines.append(BEAM_Data[CaseBeam + 5])
        lines.append(BEAM_Data[CaseBeam + 6])
        lines.append(BEAM_Data[CaseBeam + 7])
    except Exception as e:
        WriteEx()
        ExceptionExit('BEAMData Out of range.')
    ## get case num of these line
    Casenum = lines[0].count('*') - 1
    ## get name and BC, HC
    nameList = []
    BCList = []
    HCList = []
    SNoList = []
    SList = []
    SMList = []
    WFList = []
    #
    UUList = []
    UBList = []
    BUList = []
    BBList = []
    #
    tmp = lines[0].split('*')
    tmp2 = lines[2].replace('*', ' ').split()
    tmp3 = lines[3].replace('#', ' ').split()
    tmp4 = lines[4].replace('#', ' ').split()
    tmp5 = lines[5].replace('*', ' ').split()
    tmp6 = lines[6].split()
    UNo = tmp3[0]
    DNo = tmp4[0]
    UDcount = 1
    STIRcount = 2
    for i in range(1, 1 + Casenum) :
        tmp[i] = tmp[i].replace('(', ' ')
        tmp[i] = tmp[i].replace(')', ' ')
        tmp[i] = tmp[i].replace('x', ' ')
        tmp[i] = tmp[i].replace('/', ' ')
        data = tmp[i].split()
        nameList.append(data[0] + data[1])
        WFList.append(data[0])
        BCList.append(data[2])
        HCList.append(data[3])
        SNoList.append('#' + tmp6[STIRcount].split('#')[-1])
        SList.append(str(max(float(tmp6[STIRcount + 1]),float(tmp6[STIRcount + 3]))))
        SMList.append(tmp6[STIRcount + 2])
        # TOP
        if int(tmp2[UDcount]) + int(tmp3[UDcount]) < int(tmp2[UDcount + 2]) + int(tmp3[UDcount + 2]) :
            UUList.append(tmp2[UDcount])
            UBList.append(tmp3[UDcount])
        else :
            UUList.append(tmp2[UDcount + 2])
            UBList.append(tmp3[UDcount + 2])
        # BOT
        if int(tmp4[UDcount]) + int(tmp5[UDcount]) < int(tmp4[UDcount + 2]) + int(tmp5[UDcount + 2]) :
            BUList.append(tmp4[UDcount])
            BBList.append(tmp5[UDcount])
        else :
            BUList.append(tmp4[UDcount + 2])
            BBList.append(tmp5[UDcount + 2])
        UDcount = UDcount + 3
        STIRcount = STIRcount + 4
    for i in range(Casenum) :
        if nameList[i].find('P') == -1 and (BCList[i] != '0' or HCList[i] != '0'):
            ALLBEAM.append(BEAM(nameList[i], float(BCList[i]), float(HCList[i]), SNoList[i], UNo, DNo, SList[i], SMList[i], WFList[i], UUList[i], UBList[i], BUList[i], BBList[i]))
    CaseBeam = CaseBeam + 8
ALLCOLUMN.sort(key=compare)
ALLBEAM.sort(key=compare)
for column in ALLCOLUMN :
    OutputDataX.append(f'\t{column.name}\t{column.RCMaterial}\t{column.HC}\t{column.BC}\t5\t{column.No}\t{column.S}\t{column.SM}\t\t0\n')
    OutputDataY.append(f'\t{column.name}\t{column.RCMaterial}\t{column.BC}\t{column.HC}\t5\t{column.No}\t{column.S}\t{column.SM}\t\t0\n')
for beam in ALLBEAM:
    OutputDataX.append(f'\t{beam.name}\t{beam.RCMaterial}\t{beam.BC}\t{beam.HC}\t5\t{beam.No}\t{beam.S}\t{beam.SM}\t\t0\n')
    OutputDataY.append(f'\t{beam.name}\t{beam.RCMaterial}\t{beam.HC}\t{beam.BC}\t5\t{beam.No}\t{beam.S}\t{beam.SM}\t\t0\n')
###
defaultList(OutputDataX, 1)
defaultList(OutputDataY, 1)
###
for column in ALLCOLUMN :
    # column = COLUMN(column)
    No = int(column.No[1:])
    No1 = int(column.No1[1:])
    BasicLine = f'\t{column.name}\t\t{column.RCMaterial}' + '_fy\t\t' + f'{column.No1}*'
    X1 = float(5.0 + NodDic[No] + float(NodDic[No1] / 2))
    X1 = float("{:.2f}".format(float(X1)))
    X2 = float(column.HC) - X1
    YB = X1
    space = float((column.BC - 10.0 - 2 * NodDic[No] - NodDic[No1]) / (column.steel2 - 1))
    space = float("{:.2f}".format(float(space)))
    for i in range(column.steel2) :
        linex = BasicLine
        if i == 0 or i ==  column.steel2 - 1 :
            linex = linex + str(column.steel1)
        else :
            linex = linex + '2'
        Y = float("{:.2f}".format(float(YB - float(i * space))))
        OutputDataX.append(linex + f'({X1},{Y}-{X2},{Y})\n')
    ##
    X1 = float(5.0 + NodDic[No] + float(NodDic[No1] / 2))
    X1 = float("{:.2f}".format(float(X1)))
    X2 = float(column.HC) - X1
    YB = X1
    space = float((column.BC - 10.0 - 2 * NodDic[No] - NodDic[No1]) / (column.steel1 - 1))
    space = float("{:.2f}".format(float(space)))
    for i in range(column.steel1) :
        linex = BasicLine
        if i == 0 or i ==  column.steel1 - 1 :
            linex = linex + str(column.steel2)
        else :
            linex = linex + '2'
        Y = float("{:.2f}".format(float(YB - float(i * space))))
        OutputDataY.append(linex + f'({X1},{Y}-{X2},{Y})\n')
for beam in ALLBEAM :
    BasicLine = f'\t{beam.name}\t\t{beam.RCMaterial}' + '_fy\t\t#'
    UNo = int(beam.UNo)
    DNo = int(beam.DNo)
    No = int(beam.No[1:])
    for i in range(4) :
        if beam.AUB[i] != '0' :
            if i <= 1 :
                line = BasicLine + beam.UNo + '*' + beam.AUB[i]
                space = 3 + float(NodDic[UNo] / 2)
                space = float("{:.2f}".format(float(space)))
                X1 = float(5.0 + NodDic[No] + float(NodDic[UNo] / 2))
                X1 = float("{:.2f}".format(float(X1)))
                X2 = float(beam.BC) - X1
                Y = X1 + space * i
            else :
                line = BasicLine + beam.DNo + '*' + beam.AUB[i]
                space = 3 + float(NodDic[UNo] / 2)
                space = float("{:.2f}".format(float(space)))
                X1 = float(5.0 + NodDic[No] + float(NodDic[DNo] / 2))
                X1 = float("{:.2f}".format(float(X1)))
                X2 = float(beam.BC) - X1
                Y = float(beam.HC) - X1 -space * float(i-3)
            Y = float("{:.2f}".format(float(Y)))
            OutputDataX.append(f'{line}({str(X1)},{str(Y)}-{str(X2)},{str(Y)})\n')
            OutputDataY.append(f'{line}({str(X1)},{str(Y)}-{str(X2)},{str(Y)})\n')
##
defaultList(OutputDataX, 2)
defaultList(OutputDataY, 2)
outputX = open(filename + '+X.SECT', mode = 'w')
for line in OutputDataX :
    outputX.write(line)
outputY = open(filename + '+Y.SECT', mode = 'w')
for line in OutputDataY :
    outputY.write(line)