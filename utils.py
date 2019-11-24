
def findObtuse(angles):
    for angle in angles:
        if angle > 90:
            return True
    return False

def existSupple(angles):
    for angle in angles:
        if  89 <= angle <= 91:
            return True
    return False


def countModus(list):
    maks = 0
    for elem in list:
        curr = 0
        for el in list:
            if el == elem:
                curr += 1
        if curr > maks:
            maks = curr
    return maks

def countParallel(angles):
    num = 0
    for i in range(-2, len(angles)-2):
        if  178 <= (angles[i+1]+angles[i+2]) <= 182:
            num += 1
    return num

def countTwinAngle(angles):
    num = 0
    for i in range(-2, len(angles)-2):
        if angles[i+2]-1 <= angles[i] <= angles[i+2]+1:
            num += 1
    return num

def all90(angles):
    for angle in angles:
        if ((angle > 91) & (angle < 89)):
            return False
    return True

def trapesiumSamaKaki(angles):
    return 178 <= angles[0] + angles[2] <= 182

def rataKiri(angles):
    for i in range(-1, len(angles)-1):
        if angles[i] > 91:
            return 89 <= angles[i-1] <= 91
        elif angles[i] < 89:
            return 89 <= angles[i+1] <= 91

def rataKanan(angles):
    for i in range(-1, len(angles)-1):
        if angles[i] < 89:
            return 89 <= angles[i-1] <= 91
        elif angles[i] > 91:
            return 89 <= angles[i+1] <= 91
def samasisi(lengths):
    for length in lengths:
        if length != lengths[0]:
            return False
    return True