import numpy as np
import pygame
import pygame.color
import pygame.gfxdraw
import math
import os


#             ----- Force 3 -----

#Initialisation des modules de pygame
pygame.init()

#Variables
couleur = 0
grillePion = np.zeros([3, 3])
grilleCarres = np.zeros([3, 3])
magicNumber = 0
deplacement = 215
positions_carres_init = [(25, 25), (25+deplacement, 25), (25+2*deplacement, 25), (25, 25+deplacement), (25+2*deplacement, 25+2*deplacement),
                         (25+2*deplacement, 25+deplacement), (25, 25+2*deplacement), (25+deplacement, 25+2*deplacement)]  # Position départ carrés
positions_pion_init = [(750, 50), (750, 50+deplacement), (750, 50+2*deplacement),
                       (850, 50), (850, 50+deplacement), (850, 50+2*deplacement)]  # Position départ Pions
dimSelect = (0, 0)
limit = [0, 2, 0, 2]
continuer = 1
loop = True

#Création fenêtre
fenetre = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
fond = pygame.image.load("Image/background.jpg").convert()
fond = pygame.transform.scale(fond, (1000, 800))
# Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)
fenetre.blit(fond, (0, 0))


#Affichage grille
grid = pygame.image.load("Image/grille.png")
# Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
grid.set_colorkey((255, 255, 255))
grid = pygame.transform.scale(grid, (650, 650))
fenetre.blit(grid, (0, 0))

#Affichage logo
#Carre
logoCarre = pygame.image.load("Image/carre.png")
# Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
logoCarre.set_colorkey((255, 255, 255))
logoCarre_rezise = pygame.transform.scale(logoCarre, (50, 50))

#Pions
logoPion = pygame.image.load("Image/pawnwhite.png")
# Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
logoPion.set_colorkey((255, 255, 255))
logoPion_rezise = pygame.transform.scale(logoPion, (50, 50))


#Classes
class Tablier:

    def __init__(self):
        self.grilleCarres = grilleCarres
        self.grillePion = grillePion

    def occuperCarre(self, i, j):
        if grilleCarres[i, j] == 1:
            return True
        else:
            return False

    def occuperPion(self, i, j):
        if grillePion[i, j] == 1:
            return True
        else:
            return False


class Pion:
    def __init__(self):

        self.imagePion = pygame.image.load("Image/pawnblack.png")
        self.imagePion.set_colorkey((255, 255, 255))
        self.Pion_rezise = pygame.transform.scale(self.imagePion, (75, 75))

        self.position_Pion = self.Pion_rezise.get_rect()
        self.coord = [0, 0]
        self.numero = 10
        self.color = 0
        self.posIni = 0

    @staticmethod
    def start(liste6Pion):
        z = 0
        for i in range(6):   # Mise en place des carrées ainsi que de leurs positions respectives
            liste6Pion[i].position_Pion = liste6Pion[i].position_Pion.move(
                positions_pion_init[i])
            if z > 2:
                z = 0
            liste6Pion[i].posIni = z
            z = z+1

    def couleur(self):
        if self.color == 1:
            self.imagePion = pygame.image.load("Image/pawnblack.png")
            self.imagePion.set_colorkey((255, 255, 255))
            self.Pion_rezise = pygame.transform.scale(self.imagePion, (75, 75))

        else:
            self.imagePion = pygame.image.load("Image/pawnwhite.png")
            self.Pion_rezise = pygame.transform.scale(self.imagePion, (75, 75))
            self.Pion_rezise.set_colorkey((255, 255, 255))

    #Déplacements
    def right(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperPion(i+1, j) == False and i < 2):
            self.coord = [i+1, j]
            grillePion[i][j] = 0
            grillePion[i+1][j] = 1
            self.position_Pion.move(deplacement, 0)

    def left(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperPion(i-1, j) == False and i > 0):
            self.coord = [i-1, j]
            grillePion[i][j] = 0
            grillePion[i-1][j] = 1
            self.position_Pion.move(-deplacement, 0)

    def up(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperPion(i, j+1) == False and j > 0):
            self.coord = [i, j+1]
            grillePion[i][j] = 0
            grillePion[i][j+1] = 1
            self.position_Pion.move(0, deplacement)

    def down(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperPion(i, j-1) == False and j < 2):
            self.coord = [i, j-1]
            grillePion[i][j] = 0
            grillePion[i][j-1] = 1
            self.position_Pion.move(0, -deplacement)


class Carres:
    def __init__(self):

        self.imageCarre = pygame.image.load("Image/carre.png")
        self.carre_rezise = pygame.transform.scale(self.imageCarre, (170, 170))
        self.position_carre = self.carre_rezise.get_rect()
        self.coord = [0, 0]

    @staticmethod
    def start(liste8carre):
        h = 0
        k = 0
        for i in range(8):   # Mise en place des carrées ainsi que de leurs positions respectives
            liste8carre[i].position_carre = liste8carre[i].position_carre.move(
                positions_carres_init[i])
            if k > 2:
                k = 0
                h = h+1
            if k != 1 or h != 1:
                liste8carre[i].coord = [k, h]
            else:
                liste8carre[i].coord = [2, 2]
            print(liste8carre[i].coord)
            k = k+1

        for i in range(3):  # Remplissage grilleCarres (on met des 1 la ou sont placés les carrées dans la matrice des carrés)
            for j in range(3):
                if i != 1 or j != 1:
                    grilleCarres[i][j] = 1
        print(grilleCarres)
        print("position initiale bien definie")

    #Déplacements
    def right(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperCarre(i+1, j) == False and i < 2):
            self.coord = [i+1, j]
            grilleCarres[i][j] = 0
            grilleCarres[i+1][j] = 1
            self.position_carre.move(deplacement, 0)

    def left(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperCarre(i-1, j) == False and i > 0):
            self.coord = [i-1, j]
            grilleCarres[i][j] = 0
            grilleCarres[i-1][j] = 1
            self.position_carre.move(-deplacement, 0)

    def up(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperCarre(i, j+1) == False and j > 0):
            self.coord = [i, j+1]
            grilleCarres[i][j] = 0
            grilleCarres[i][j+1] = 1
            self.position_carre.move(0, deplacement)

    def down(self, tablier):
        i = self.coord[0]
        j = self.coord[1]
        if (tablier.occuperCarre(i, j-1) == False and j < 2):
            self.coord = [i, j-1]
            grilleCarres[i][j] = 0
            grilleCarres[i][j-1] = 1
            self.position_carre.move(0, -deplacement)


class Selecteur:
    def __init__(self):
        self.posPion_select = 0
        self.posPion = [1, 1, 1]
        self.imageSelect = pygame.image.load("Image/selecteur.png")
        self.Select_rezise = pygame.transform.scale(
            self.imageSelect, (220, 220))
        # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
        self.Select_rezise.set_colorkey((255, 255, 255))
        self.position_Select = self.Select_rezise.get_rect()
        #self.position_Select = self.position_Select.move(0,25)
        self.coord = [0, 0]
        self.limit = limit
        self.deplacement = deplacement
        self.InPawn = False
        self.Actif = False
        self.dimSelect = (220, 220)

    def selecteurActif(self):
        self.imageSelect = pygame.image.load("Image/selecteuractif.png")
        if self.InPawn == True:
            self.dimSelect = (75, 75)
            Position_Du_Pion = self.posPion_select
            while Position_Du_Pion > 0:
                self.down()
                Position_Du_Pion -= 1
        else:
            self.dimSelect = (220, 220)
        self.Select_rezise = pygame.transform.scale(
            self.imageSelect, self.dimSelect)
        # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
        self.Select_rezise.set_colorkey((255, 255, 255))
        self.Actif = True

    def selecteurpassif(self):
        self.imageSelect = pygame.image.load("Image/selecteur.png")
        if self.InPawn == True:
            self.dimSelect = (75, 75)
        else:
            self.dimSelect = (220, 220)
        self.Select_rezise = pygame.transform.scale(
            self.imageSelect, self.dimSelect)
        # Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
        self.Select_rezise.set_colorkey((255, 255, 255))
        self.Actif = False

    def selectionINITPion(self, joueur):
        self.coord = [0, 0]
        self.deplacement = 50
        self.limit = [0, 0, 0, 2]
        self.Select_rezise = pygame.transform.scale(self.imageSelect, (75, 75))
        self.Select_rezise.set_colorkey((255, 255, 255))
        if joueur.joueurCouleur == 0:
            self.position_Select[0] = 750
            self.position_Select[1] = 50
        else:
            self.position_Select[0] = 850
            self.position_Select[1] = 50
        self.InPawn = True

    def selectionCarre(self, joueur):
        self.coord = [0, 0]
        self.deplacement = 250
        self.limit = [0, 2, 0, 2]
        self.Select_rezise = pygame.transform.scale(
            self.imageSelect, (220, 220))
        self.Select_rezise.set_colorkey((255, 255, 255))
        self.position_Select[0] = 0
        self.position_Select[1] = 0
        self.InPawn = False

    #Déplacements

    def right(self):
        i = self.coord[0]
        j = self.coord[1]
        if i < self.limit[1]:
            self.coord = [i+1, j]
            self.position_Select = self.position_Select.move(deplacement, 0)

    def left(self):
        i = self.coord[0]
        j = self.coord[1]
        if i > self.limit[0]:
            self.coord = [i-1, j]
            self.position_Select = self.position_Select.move(-deplacement, 0)

    def up(self):
        i = self.coord[0]
        j = self.coord[1]
        print(j, "j")
        if j > self.limit[2]:
            if self.InPawn == True:
                self.coord = [i, j-1]
                self.position_Select = self.position_Select.move(
                    0, -deplacement)
                self.posPion_select = self.posPion_select-1
            else:
                self.coord = [i, j-1]
                self.position_Select = self.position_Select.move(
                    0, -deplacement)

    def down(self):
        i = self.coord[0]
        j = self.coord[1]
        if j < self.limit[3]:
            if self.InPawn == True:
                self.coord = [i, j+1]
                self.position_Select = self.position_Select.move(
                    0, deplacement)
                self.posPion_select = self.posPion_select+1
            else:
                self.coord = [i, j+1]
                self.position_Select = self.position_Select.move(
                    0, deplacement)


class Joueur:
    def __init__(self):
        self.couleur = 0

    def joueurCouleur(self, i):
        self.couleur = i


_tablier = Tablier()
selecteur = Selecteur()
selecteur2 = Selecteur()

#Création carrés
listecarres = []
for _i in range(8):
    cr = Carres()
    listecarres.append(cr)

#Créations Pions
listePion = []
for _i in range(6):
    if _i < 3:  # Pions blancs
        pi = Pion()
        pi.color = 0
        pi.couleur()
        listePion.append(pi)
    else:  # Pions noirs
        pi = Pion()
        pi.color = 1
        pi.couleur()
        listePion.append(pi)

player = Joueur()
player.joueurCouleur = 0
#Initialisation plateau de jeu carrés & pions

Carres.start(listecarres)
Pion.start(listePion)

Tour = 0
while loop:  # Boucle d'événements
    fenetre.blit(fond, (0, 0))
    fenetre.blit(grid, (0, 0))
    #Jeu

    for _i in range(8):
        fenetre.blit(listecarres[_i].carre_rezise,
                     listecarres[_i].position_carre)
    for _i in range(6):
        fenetre.blit(listePion[_i].Pion_rezise, listePion[_i].position_Pion)

    #Fermer fênetre
    for event in pygame.event.get():  # parcours de la liste des événements

        #Passer des carrés aux pions
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
            selecteur.selectionINITPion(player)
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_c):
            selecteur.selectionCarre(player)

        #Mouvement
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            selecteur.down()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            selecteur.up()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            selecteur.left()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            selecteur.right()

            #Selection Pions
        if selecteur.InPawn == True:
            data = selecteur.posPion_select
            selecteur2.selectionINITPion(player)
            selecteur2.posPion_select = data
            # K_RETURN pour touche entrée
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN)):

                selecteur2.selecteurActif()
                selecteur.selectionCarre(player)

        if selecteur2.Actif == True and selecteur.Actif == False:
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN)):
                for pion in listePion:
                    if pion.posIni == selecteur2.posPion_select and pion.color == Tour:
                        _i = selecteur.coord[0]
                        _j = selecteur.coord[1]
                        if tablier.occuperPion(_i, _j) == False:
                            grillePion[_i][_j] = 1
                            pion.position_Pion = selecteur.position_Select
                            pion.position_Pion.move(25, 25)
                            selecteur2.selecteurpassif()

        #Calcul Win
        if magicNumber != 30:
            magicNumber = 0

        # interrompt la boucle si nécessaire
        if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            loop = False
    #              ----  Affichage  ----

    #Selecteur
    if selecteur2.Actif == True:
        fenetre.blit(selecteur2.Select_rezise, selecteur2.position_Select)

    fenetre.blit(selecteur.Select_rezise, selecteur.position_Select)

    #Logo
    if selecteur.InPawn == True:
        fenetre.blit(logoPion_rezise, (0, 750))
    else:
        fenetre.blit(logoCarre_rezise, (0, 750))

    #Fenetre
    pygame.display.flip()
pygame.quit()
