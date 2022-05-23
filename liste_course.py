#Correction
import sys

liste = []
menu = """Choisissez parmi les 5 options suivantes : 
1 : Ajouter un élément à la liste.
2 : Retirer un élément de la liste.
3 : Afficher la liste.
4 : Vider la liste.
5 : Quitter
Votre choix : """
choix_menu=["1","2","3","4","5"]

while True:
    choix_utilisateur=input(menu)
    if choix_utilisateur not in choix_menu:
        print("Veuillez choisir une option valide..")
        continue
    if choix_utilisateur=="1":
        item=input("Entrez le nom d'un élément à ajouter à la liste.")
        liste.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
    elif choix_utilisateur=="2":
        item=input("Entrez le nom d'un élément à retirer de la liste.")
        if item in liste:
            liste.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif choix_utilisateur=="3":
        if liste:
            print("Voici le contenu de votre liste : ")
            for i,item in enumerate(liste,1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif choix_utilisateur=="4":
        liste.clear()
        print("La liste a été vidée de son contenu.")
    elif choix_utilisateur=="5":
        print("A bientôt")
        sys.exit() 
