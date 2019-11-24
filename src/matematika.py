import math
import numpy as np

def getAngle(point1, point2, point3) :
    x1 = point1[0]
    x2 = point2[0]
    x3 = point3[0]
    y1 = point1[1]
    y2 = point2[1]
    y3 = point3[1]

    xA = abs(x2 - x1)
    xB = abs(x3 - x2)
    yA = abs(y2 - y1)
    yB = abs(y3 - y2)

    lengthA = math.sqrt(xA * xA + yA * yA)
    lengthB = math.sqrt(xB * xB + yB * yB)

    cosTheta = (xA * xB + yA * yB) / (lengthA * lengthB)

    return np.arccos(cosTheta) / (2 * np.pi) * 360

def getLength(point1, point2) :
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    return math.sqrt(x*x + y*y)

def checkAngle(listOfPoint) :
    listSudut = []
    for i in range(0, len(listOfPoint)) :
        if(i == 0) :
            listSudut.append(getAngle(listOfPoint[-1], listOfPoint[0], listOfPoint[1]))
        elif(i == len(listOfPoint)-1) :
            listSudut.append(getAngle(listOfPoint[i-1], listOfPoint[i], listOfPoint[0]))
        else :
            listSudut.append(getAngle(listOfPoint[i-1], listOfPoint[i], listOfPoint[i+1]))
        
        # print(i, listSudut)
    
    return listSudut

def checkLength(listOfPoint) :
    listPanjang = []
    for i in range(0, len(listOfPoint)) :
        if(i == len(listOfPoint)-1) :
            listPanjang.append(getLength(listOfPoint[i], listOfPoint[0]))
        else :
            listPanjang.append(getLength(listOfPoint[i], listOfPoint[i+1]))

    return listPanjang

def main() :
    listOfPoint = [[0, 0], [0, 4], [3, 4], [3, 0]]
    a = checkAngle(listOfPoint)
    b = checkLength(listOfPoint)
    print(a, b)

if __name__ == "__main__" :
    main()