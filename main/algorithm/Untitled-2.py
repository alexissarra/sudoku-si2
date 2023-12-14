

grille_des_chiffres = [[1], [2], [3], [4], [5], [6], [7], [8]]

for region in grille_des_chiffres:
    if grille_des_chiffres.index(region) % 3 == 0:
        print(0)
    elif grille_des_chiffres.index(region) % 3 == 1:
        print(1)
    else:
        print(2)
   




# region = [0, 0, 1, 0, 0, 6, 0, 8, 0]
# def test(region):
#     grille_temporaire = []
#     for number in region: # pour un élément dans une région
#             if number == 0:
#                 for element in grille_des_chiffres : # je parcours la grille des chiffres
#                     if element not in region:      
#                                 try:
#                                     boolean = region[region.index(number) - 1] != element
#                                     try:
#                                         boolean = region[region.index(number) + 1] != element
#                                         if boolean is True : grille_temporaire.append(element)
#                                     except IndexError:
#                                         grille_temporaire.append(element)
#                                 except IndexError:
#                                     try:
#                                         boolean = region[region.index(number) + 1] != element
#                                         if boolean is True : grille_temporaire.append(element)
#                                     except:
#                                         pass
#                 break
#     return grille_temporaire



                


# print(test(region))
# print(grille_des_chiffres.index(2))