import datetime
import time
import os
import sys
import subprocess

fichier = sys.argv[1]
date_debut = sys.argv[2]
heure_debut = sys.argv[3]
intervalle = sys.argv[4]
repetition = sys.argv[5]

# Variables pour les messages d'erreur
messages_erreur = {
    "chemin_inexistant": "Chemin d'accès inexistant",
    "date_invalide": "La date de lancement doit comporter 8 chiffres, format JJMMAAAA",
    "heure_invalide": "L'heure de lancement doit comporter 6 chiffres, format HHMMSS",
    "intervalle_invalide": "L'intervalle doit comporter 6 chiffres, format HHMMSS",
    "repetition_invalide": "Veuillez entrer seulement des chiffres"
}

# Variables pour les erreurs détectées
erreur_detectee = False
chemin_inexistant = False
date_invalide = False
heure_invalide = False
intervalle_invalide = False
repetition_invalide = False

#Input - Fichier
fichier = fichier.strip('"') #supprime les guillemets
if not os.path.exists(fichier):
    print(messages_erreur["chemin_inexistant"])
    erreur_detectee = True

#Input - Date de début
if len(date_debut) == 0 or date_debut == '""':
    date_debut = datetime.date.today()
else:
    if len(date_debut) != 8 or not date_debut.isdigit():
        print(messages_erreur["date_invalide"])
        erreur_detectee = True
    else:
        try:
            date_debut = datetime.datetime.strptime(date_debut, "%d%m%Y").date()
            if date_debut < datetime.date.today():
                date_debut = datetime.date.today()
        except ValueError:
            print(messages_erreur["date_invalide"])
            erreur_detectee = True

#Input - Heure de début
if len(heure_debut) == 0 or heure_debut == '""':
    heure_debut = datetime.datetime.now().time()
else:
    if len(heure_debut) != 6 or not heure_debut.isdigit():
        print(messages_erreur["heure_invalide"])
        erreur_detectee = True
    else:
        try:
            heure_debut = datetime.datetime.strptime(heure_debut, "%H%M%S").time()
            if heure_debut < datetime.datetime.now().time():
                heure_debut = datetime.datetime.now().time()
        except ValueError:
            print(messages_erreur["heure_invalide"])
            erreur_detectee = True

#Input - intervalle de lancement
if len(intervalle) != 6 or not intervalle.isdigit():
    print(messages_erreur["intervalle_invalide"])
    erreur_detectee = True

#Input - répétition
if not repetition.isdigit():
    print(messages_erreur["repetition_invalide"])
    erreur_detectee = True

# Afficher un message d'erreur global si une erreur a été détectée
if erreur_detectee:
    print("Des erreurs ont été détectées. Veuillez corriger les paramètres.")
else:
    print("Exécution en cours...")

    # Attendre l'heure de début
    while heure_debut > datetime.datetime.now().time():
        time.sleep(1)

    while date_debut > datetime.datetime.now().date():
        time.sleep(1)
        
    tempsattente = datetime.timedelta(hours=int(intervalle[0:2]), minutes=int(intervalle[2:4]), seconds=int(intervalle[4:6]))

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

def lancer_fichier(fichier):
    if fichier.endswith(".txt"):
        subprocess.Popen(["notepad++.exe", "-nosession", "-notabbar", fichier], startupinfo=startupinfo)
    elif fichier.endswith(".exe"):
        subprocess.Popen([fichier], startupinfo=startupinfo)
    else:
        # pour d'autres types de fichiers ou pour les utiliser avec leur programme associé
        subprocess.Popen(["cmd", "/c", fichier], startupinfo=startupinfo)

# Vérifiez si le script doit s'exécuter indéfiniment ou un certain nombre de fois
if repetition == "0" or repetition == "":
    while True:
        lancer_fichier(fichier)
        time.sleep(tempsattente.total_seconds())
else:
    for i in range(int(repetition)):
        lancer_fichier(fichier)
        time.sleep(tempsattente.total_seconds())
        if i == int(repetition) - 1:
            break

print("Traitement terminé")
