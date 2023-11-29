import time


heure_actuelle = (0, 0, 0)
alarme = None

def afficher_heure(heure):
    global heure_actuelle
    heure_actuelle = heure
    print(f"Heure réglée sur : {heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def regler_alarme(heure):
    global alarme
    alarme = heure
    print(f"Alarme réglée sur : {heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")

def afficher_heure_actuelle():
    global heure_actuelle
    while True:
      
        heure = time.localtime()
        heure_actuelle = (heure.tm_hour, heure.tm_min, heure.tm_sec)
        
       
        print(f"\r{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}", end="")
        time.sleep(1)

        
        if alarme is not None and heure_actuelle == alarme:
            print("\nAlarme activée !")
            break
afficher_heure_actuelle()
