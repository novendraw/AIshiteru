from experta import *
import matematika
from fact import *
from utils import *

class ShapeRecognition(KnowledgeEngine):
    """ Determine the shape """

    def __init__(self):
        super().__init__()

        self.activated_rules = []

    def get_activated_rules(self):
        return '\n'.join(self.activated_rules)

    @Rule(AS.point << Point(count=3))
    def segitiga(self, point):
        angles = matematika.checkAngle(point["list"])
        print()
        self.declare(Angle(
            equal=countModus(angles), 
            obtuse=findObtuse(angles), 
            supple=existSupple(angles)))
        print("segitiga")
        self.activated_rules.append("segitiga")
        self.facts

    @Rule(AS.point << Point(count=4))
    def segiempat(self, point):
        angles = matematika.checkAngle(point["list"])
        self.declare(Angle(
            equal=countModus(angles), 
            parallel=countParallel(angles), 
            twinAngle=countTwinAngle(angles), 
            all90=all90(angles), 
            samakaki=trapesiumSamaKaki(angles),
            ratakanan=rataKanan(angles),
            ratakiri=rataKiri(angles)))

        print("segiempat")
        self.activated_rules.append("segiempat")
        self.facts

    @Rule(AS.point << Point(count=5))
    def segilima(self, point):
        length = matematika.checkLength(point["list"])
        self.declare(Length(beraturan=samasisi(length)))
        print("segilima")
        
        self.facts

    @Rule(AS.point << Point(count=6))
    def segienam(self,point):
        length = matematika.checkLength(point["list"])
        self.declare(Length(beraturan=samasisi(length)))

        print("segienam")
        self.activated_rules.append("segienam")
        self.facts

    """ Specific Triangle """

    """ Segitiga samasisi """
    @Rule(Angle(equal=3))
    def samasisi(self):
        print("segitiga sama sisi")
        self.activated_rules.append("segitiga sama sisi")
        self.facts
    
    """ Segitiga siku-siku """
    @Rule(Angle(supple=True))
    def sikusiku(self):
        print("segitiga siku-siku")
        self.activated_rules.append("Segitiga siku-siku")
        self.facts
    
    """ Segitiga sama kaki """
    @Rule(Angle(equal=2, obtuse=True))
    def samakakitumpul(self):
        print("segitiga sama sisi tumpul")
        self.activated_rules.append("Segitiga tumpul")
        self.facts
    
    @Rule(Angle(equal=2, obtuse=False))
    def samakakilancip(self):
        print("segitiga sama sisi lancip")
        self.activated_rules.append("Segitiga lancip")
        self.facts
    
    @Rule(Angle(equal=2, supple=True))
    def samakakisikusiku(self):
        print("segitiga sama kaki siku-siku")
        self.activated_rules.append("Segitiga sama kaki dan siku-siku")
        self.facts

    """ Specific Rectangle """

    """ Jajaran genjang """
    @Rule(Angle(parallel=4))
    def jajarangenjang(self):
        print("jajaran genjang")
        self.activated_rules.append("jajaran genjang")
        self.facts
    
    @Rule(Angle(twinAngle=4, parallel=4))
    def segiempatberaturan(self):
        print("segiempat beraturan")
        self.activated_rules.append("Segiempat beraturan")
        self.facts

    @Rule(Angle(twinAngle=2, parallel=0))
    def layanglayang(self):
        print("layang-layang")
        self.activated_rules.append("Segiempat berbentuk layang-layang")
        self.facts
    
    """ Trapesium """
    @Rule(Angle(parallel=2))
    def trapesium(self):
        print("trapesium")
        self.activated_rules.append("trapesium")
        self.facts
    
    @Rule(Angle(parallel=2, samakaki=True))
    def trapesiumsamakaki(self):
        print("trapesium sama kaki")
        self.activated_rules.append("Trapezium sama kaki")
        self.facts
    
    @Rule(Angle(parallel=2, ratakanan=True))
    def trapesiumratakanan(self):
        print("trapesium rata kanan")
        self.activated_rules.append("Trapezium rata kanan")
        self.facts

    @Rule(Angle(parallel=2, ratakiri=True))
    def trapesiumratakiri(self):
        print("trapesium rata kiri")
        self.activated_rules.append("Trapezium rata kiri")
        self.facts
    
    """ Specific Pentagon """

    @Rule(Length(beraturan=True))
    def segilimaberaturan(self):
        print("segilima beraturan")
        self.activated_rules.append("Segi lima sama sisi")

    """ Specific Hexagon """

    @Rule(Length(beraturan=True))
    def segienamberaturan(self):
        print("segienam beraturan")
        self.activated_rules.append("Segi enam sama sisi")