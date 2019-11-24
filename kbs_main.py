from random import choice
from experta import *
import extract_bare
import matematika
from rules import *
from fact import *
import cv2

def main(path, update_function):
    # Getting Points, Angles, and Lengths
    contours = extract_bare.processImage(path)

    image = cv2.imread(path)

    cv2.drawContours(image, contours, -1, (0,255,0), 3)

    cv2.imwrite("result.png", image)

    points = extract_bare.getPoint(path)
    
    # Getting Initial Facts

    engine = ShapeRecognition()
    engine.reset()
    
    engine.declare(Point(list=points, count=len(points)))

    engine.run()
    print(engine.facts)
    print(engine.agenda)

    update_function("result.png", str(engine.facts), engine.get_activated_rules())


if __name__ == "__main__":
    main()