from experta import *


class Point(Fact):
    """ List of known points """
    pass

class Angle(Fact):
    """ List of known angles """
    pass

class Length(Fact):
    """ List of known lines length """
    pass

class ParallelLines(Fact):
    """ The amount of known pair of parallel line """
    pass

class TwinAngle(Fact):
    """ The amount of known pair of angles that face each other and of the same magnitude """
    pass

class EqualAngleCount(Fact):
    """ The amount of known angles that have the same magnitude """
    pass

class EqualLengthCount(Fact):
    """ The amount of known line that have the same length """
    pass

class ObtuseAngleExisted(Fact):
    """ Existence of an obtuse angle """
    pass