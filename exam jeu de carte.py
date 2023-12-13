class Carte:
    def __init__(self, nom, mana, description):
        self.__nom = nom
        self.__mana = mana
        self.__description = description

    def getNom (self):
        return self.__nom
    def getMana (self):
        return self.__mana
    def getDescription (self):
        return self.__description
    

class Mage:
    def __init__(self, nom, pv, totalMana, actuelleMana):
        self.__nom = nom
        self.__pv = pv
        self.__totalMana = totalMana
        self.__actuelleMana = actuelleMana
        self.__main = ["cristal", "creature", "blast"]
        self.__zoneJeu = []
        self.__defausse = []

    def getNom (self):
        return self.__nom
    def getPv (self):
        return self.__pv
    def getTotalMana (self):
        return self.__totalMana
    def getActuelleMana (self):
        return self.__actuelleMana
    def getMain (self):
        return self.__main
    def getZoneJeu (self):
        return self.__zoneJeu
    def getDefausse (self):
        return self.__defausse
    
    def jouerCarte (self):
        self.__actuelleMana -= Carte.getMana()
        Carte.getNom.append(self.__zoneJeu)
    #egalement supprimer la carte de la main mais je ne connais plus la formule pour y parvenir
    
    #def recupereMana(self):
        #il faudrait un self.__passeTour ?

    def attaquer(self, cible):
        cible.__pv -= self.__atkCreature


class Cristal (Carte):
    def __init__ (self,valeur, nom, mana, description):
        Carte.__init__(self, nom, mana, description)
        self.__valeur = valeur
        self.__mana = 0
    def getValeur(self):
        return self.__valeur
    def getMana(self):
        return self.__mana
    
    def jouer(self):
        # Mage.getZoneJeu.append(self.__nom)
        Mage.getTotalMana -= self.__valeur

class Creature (Carte):
    def __init__(self,pv, atkCreature, nom, mana, description):
        Carte.__init__(self, nom, mana, description)
        self.__pv = pv
        self.__atkCreature = atkCreature

    def getPv (self):
        return self.__pv
    def getAtkCreature (self):
        return self.__atkCreature
    
    def jouer (self):
        # Mage.getZoneJeu.append(self.__nom)
        Mage.getActuelleMana -= self.__mana

    def attaquer(self, cible, atkCreature):
        cible.__pv -= atkCreature

    def  perdPv (self, cible):
        if (self.__pv <= 0):
            print ("Votre Creature est morte")
        else:
            self.__pv -= cible.__atkCreature


class Blast (Carte):
    def __init__(self,valeur, nom, mana, description):
        Carte.__init__(self, nom, mana, description)
        self.__valeur = valeur

    def getValeur(self):
        return self.__valeur
    
    def lancer (self, cible):
        cible.__pv -= self.__valeur
        Mage.getDefausse.append(self.__nom)


nom1 = str(input("Mage 1, comment vous appelez vous ?"))
nom2 = str(input("Mage 2, comment vous appelez vous ?"))

mage1 = Mage(nom1, 20, 30, 15,)
mage2 = Mage(nom2, 20, 30, 15,)

cristal = Cristal(4, "cristal", 2, "C'est un cristal magique fait de magie")
creature = Creature(20, 5, "creature", 6, "C'est une creature enchanté...enchanté de vous voir")
blast = Blast(2, "blast", 2, "C'est un blast... qu'est ce qu'un blast ? On ne sait pas")

while (mage1.getPv() > 0 and mage2.getPv() >0):
    choix1 = str(input(f"{mage1.getNom()}, vous avez des cartes dans votre main : {mage1.getMain()}, que voulez vous utiliser ?"))

    if (choix1 == "cristal"):
        cristal.jouer()
        print(f"Vous avez jouer un cristal, désormais vous avez {mage1.getTotalMana()} points de mana maximum")
        # print (f"Vous avez désormais dans votre zone de jeu: {mage1.getZoneJeu()}")
        #problème: "append" ne se fait pas

    elif (choix1 == "creature"):
        # creature.jouer()
        creature.attaquer(mage2, creature.getAtkCreature)
        print (f"Vous avez jouer votre creature, il vous reste {mage1.getActuelleMana} point de mana")
        print (f"Votre creature a attaquer le mage adverse, il lui reste {mage2.__pv} point de vie")

    elif (choix1 == "blast"):
        blast.lancer(mage2)
        print(f"Votre blast à été lancé sur le mage, il perd {mage2.getPv}")

    else:
        print("Cet objet n'est pas dans votre main")
    



    choix2 = str(input(f"{mage2.getNom()}, vous avez des cartes dans votre main : {mage2.getMain()}, que voulez vous utiliser ?"))

    if (choix2 == "cristal"):
        cristal.jouer()
        print(f"Vous avez jouer un cristal, désormais vous avez {mage2.getTotalMana()} points de mana maximum")
        # print (f"Vous avez désormais dans votre zone de jeu: {mage1.getZoneJeu()}")
        #problème: "append" ne se fait pas

    elif (choix2 == "creature"):
        # creature.jouer()
        creature.attaquer(mage1, creature.getAtkCreature)
        print (f"Vous avez jouer votre creature, il vous reste {mage2.getActuelleMana} point de mana")
        print (f"Votre creature a attaquer le mage adverse, il lui reste {mage1.__pv} point de vie")

    elif (choix2 == "blast"):
        blast.lancer(mage1)
        print(f"Votre blast à été lancé sur le mage, il perd {mage1.getPv}")

    else:
        print("Cet objet n'est pas dans votre main")


#Mon code ne marche pas, les objets ne se defaussent pas et ne vont pas dans les tableaux