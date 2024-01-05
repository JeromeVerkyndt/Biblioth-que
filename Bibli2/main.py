class Bibliotheque:
    def __init__(self):
        self.listeLivres = []
        self.liste_livres()

    def liste_livres(self):
        try:
            with open('saveLivres.txt') as file:
                data = (file.readlines())
            file.close()
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')
        for x in data:
            x = x.strip('\n')
            liv = x.split(',')
            self.listeLivres.append(liv)

    def up(self):
        fichier = open('saveLivres.txt', 'w')
        for x in self.listeLivres:
            fichier.write(x[0] + ',' + x[1] + '\n')
        fichier.close()

    def ajouter_livre(self, livre):
        self.listeLivres.append([livre, "disponible"])
        self.up()
        print(f"Le livre '{livre}' a été ajouté à la bibliothèque.")

    def afficher_livres(self):
        if self.listeLivres:
            print("Liste des livres dans la bibliothèque :")
            for livre in self.listeLivres:
                print(f"-{livre[0]} est {livre[1]}.")
        else:
            print("Il n'y a pas de livres dans la bibliothèque.")

    def supprimer_livre(self, livre):
        nomLivres = []

        for x in self.listeLivres:
            nomLivres.append(x[0])

        if livre in nomLivres:
            position = nomLivres.index(livre)
            self.listeLivres.pop(position)
            print(f"Le livre '{livre}' a été supprimé de la bibliothèque.")
        else:
            print(f"Le livre '{livre}' n'est pas présent dans la bibliothèque.")

        self.up()

    def emprunter_livre(self, livre):
        nomLivres = []

        for x in self.listeLivres:
            nomLivres.append(x[0])

        position = nomLivres.index(livre)

        if (self.listeLivres[position][1]) == 'indisponible':
            print('Désolé mais ce livre est indisponible pour le moment')
        elif (self.listeLivres[position][1]) == 'disponible':
            self.listeLivres[position][1] = 'indisponible'
            self.up()
            print('Vous empruntez le livre : ' + self.listeLivres[position][0])

    def rendre_livre(self, livre):
        nomLivres = []

        for x in self.listeLivres:
            nomLivres.append(x[0])

        position = nomLivres.index(livre)

        if (self.listeLivres[position][1]) == 'disponible':
            print('Désolé mais ce livre est déja rendu disponible pour le moment')
        elif (self.listeLivres[position][1]) == 'indisponible':
            self.listeLivres[position][1] = 'disponible'
            self.up()
            print('Vous empruntez le livre : ' + self.listeLivres[position][0])



def main():
    biblio = Bibliotheque()

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Afficher les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Emprunter un livre")
        print("5. Rendre un livre")
        print("6. Quitter")

        choix = input("Entrez le numéro de votre choix (1/2/3/4/5/6) : ")

        if choix == '2':
            titre = input("Entrez le titre du livre à ajouter : ")
            biblio.ajouter_livre(titre)
        elif choix == '1':
            biblio.afficher_livres()
        elif choix == '3':
            titre = input("Entrez le titre du livre à supprimer : ")
            biblio.supprimer_livre(titre)
        elif choix == '4':
            titre = input("Entrez le titre du livre à emprunter : ")
            biblio.emprunter_livre(titre)
        elif choix == '5':
            titre = input("Entrez le titre du livre à rendre : ")
            biblio.rendre_livre(titre)
        elif choix == '6':
            print("Bibliothèque quitté")
            break
        else:
            print("Choix invalide. Veuillez entrer un choix valide (1/2/3/4/5/6).")


if __name__ == "__main__":
    main()