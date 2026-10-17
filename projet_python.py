
import tkinter as tk
import json
from tkinter import messagebox


class Quiz:
    def __init__(self, fenetre):

        self.fenetre = fenetre
        self.fenetre.title("Mon Quiz Python")
        self.fenetre.geometry("600x400")

        # Charger les données du fichier JSON
        with open( r"C:\Users\hp\Documents\FORMATION\projet_final\questions.json",
    "r",
    encoding="utf-8") as fichier:
            self.donnees = json.load(fichier)

        self.questions = self.donnees["questions"]

        # Initialiser les variables
        self.score = 0
        self.num = 0
        self.nbr = len(self.questions)

        self.reponse_choisie = tk.StringVar(value="")
        self.reponse_verifiee = False

        # Étape 4 : créer les éléments de l'interface
        self.label_question = tk.Label(
            fenetre,
            text="",
            font=("Arial", 12),
            wraplength=550
        )
        self.label_question.pack(pady=20)

        self.label_options = tk.Frame(fenetre)
        self.label_options.pack()

        self.label_resultat = tk.Label(
            fenetre,
            text="",
            font=("Arial", 11)
        )
        self.label_resultat.pack(pady=10)

        self.bouton_verifier = tk.Button(
            fenetre,
            text="Vérifier la réponse",
            command=self.verifier_reponse
        )
        self.bouton_verifier.pack(pady=5)

        self.bouton_suivant = tk.Button(
            fenetre,
            text="Question suivante",
            command=self.question_suivante,
            state="disabled"
        )
        self.bouton_suivant.pack(pady=5)

        # Afficher la première question
        self.afficher_question()

    # Étape 5 : afficher la question et ses options
    def afficher_question(self):
        question = self.questions[self.num]
        print(question)
        print(question.keys())

        self.reponse_choisie.set("")
        self.reponse_verifiee = False
        self.label_resultat.config(text="")

        self.label_question.config(
            text=f"Question {self.num + 1}/{self.nbr}\n\n"
                 + question["question"].strip()
        )

        # Supprimer les anciennes options
        for widget in self.label_options.winfo_children():
            widget.destroy()

        # Afficher les options sous forme de boutons radio
        for option in question["options"]:
            bouton = tk.Radiobutton(
                self.label_options,
                text=option.strip(),
                variable=self.reponse_choisie,
                value=option.strip(),
                font=("Arial", 10)
            )
            bouton.pack(anchor="w", pady=3)

        self.bouton_verifier.config(state="normal")
        self.bouton_suivant.config(state="disabled")

    # Étape 6 : vérifier la réponse sélectionnée
    def verifier_reponse(self):
        if self.reponse_verifiee:
            return

        choix = self.reponse_choisie.get()

        if choix == "":
            messagebox.showwarning(
                "Attention",
                "Veuillez sélectionner une réponse."
            )
            return

        question = self.questions[self.num]
        bonne_reponse = question["reponse"].strip()

        if choix == bonne_reponse:
            self.score += 1
            self.label_resultat.config(
                text="Bonne réponse !",
                fg="green"
            )
        else:
            self.label_resultat.config(
                text=f"Mauvaise réponse ! Bonne réponse : {bonne_reponse}",
                fg="red"
            )

        self.reponse_verifiee = True
        self.bouton_verifier.config(state="disabled")
        self.bouton_suivant.config(state="normal")

    # Passer à la question suivante
    def question_suivante(self):
        self.num += 1

        if self.num < self.nbr:
            self.afficher_question()
        else:
            messagebox.showinfo(
                "Résultat final",
                f"Quiz terminé !\n\n"
                f"Bonnes réponses : {self.score}\n"
                f"Mauvaises réponses : {self.nbr - self.score}\n"
                f"Score : {self.score}/{self.nbr}"
            )
            self.fenetre.destroy()


# Lancer l'application
fenetre = tk.Tk()
quiz = Quiz(fenetre)
fenetre.mainloop()
