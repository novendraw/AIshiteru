import cv2

def processImage(path):
    image = cv2.imread(path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    ret, tresh = cv2.threshold(blurred, 64, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    return contours

def getPoint(path):
    contours = processImage(path)

    approx = [cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True) for c in contours]

    lis = []

    for point in approx[0]:
        lis.append((point[0][0], point[0][1]))

    return lis