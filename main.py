from email.policy import default
import os
from tkinter import ALL
from _main import *
from LogSystem import *
import time

cwd = os.getcwd()
filename = cwd.split('\\')[-1]
OutputData = []
OutputData.append('$Unit\n')
OutputData.append('KGF-CM\n')
OutputData.append('\n')
OutputData.append('$ RC Rectangle Section Definitions\n')
OutputData.append('$\tName\tRCMaterial\tWidth\tHeight\tCover\tSNo\tSpacing\tSpacingM\tAngle\n')
OutputData.append('\t\t\t\tcm\tcm\tcm')
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
NowC = 0
NowF = 0
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
            floor = lines[0][0] + 'F'
        else :
            floor = lines[0][0][:-1] + 'F'
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
    except Exception as e:
        WriteEx()
        ExceptionExit('CXX: line 4 or 5 Out of range. Doing No Numxy S.')
    whichFloor = floor
    ALLCOLUMN.append(Case(name, BC, HC, No1, No, Numx, Numy, S, SM, whichFloor))
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
for item in ALLCOLUMN :
    print(item.name)
output = open(filename + '.SECT', mode = 'w')
for line in OutputData :
    output.write(line)