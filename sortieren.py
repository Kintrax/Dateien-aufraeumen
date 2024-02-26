import os
import shutil

def sortieren(unordentlich):
    exe = False
    # Dateiendungen erkennen und Zielverzeichnis zuweisen
    for i in os.listdir(unordentlich):
        if i.endswith((".png", ".jpg")):
            dst_dir = f"{desktop}IMG/"
        elif i.endswith(".pdf"):
            dst_dir = f"{desktop}PDF/"
        elif i.endswith((".stl", ".3mf")):
            dst_dir = f"{desktop}3D_Dateien/"
        elif i.endswith((".lnk", ".exe", ".url")):
            dst_dir = f"{desktop}EXE/"
            exe = True
        else:
            continue
        
        # prüfen ob Datei im Zielverzeichnis bereits vorhanden ist
        # wenn ja ein 1 etc. an den Dateinamen anhängen
        count = 1
        if os.path.exists(dst_dir + i):
            if exe:
                # doppelte exe Dateien werden gelöscht statt umbennant
                os.remove(unordentlich + i)
                print("gelöscht")
            else:
                while True:
                    test = i.split(".")
                    new_name = "".join((test[0], str(count), ".", test[-1]))
                    if os.path.exists(dst_dir + new_name):
                        count += 1
                    else:
                        shutil.move(unordentlich + i, dst_dir + new_name)
                        break
        else:
            shutil.move(unordentlich + i, dst_dir)

# Hier muss der korrekte Pfad zu deinem Desktop und Download Verzeichnis zugewiesen werden
desktop = "C:/Users/deinUsername/Desktop/"
download = "C:/Users/deinUsername/Downloads/"

# Der Public Ordner muss nicht angepasst werden
desktop_public = "C:/Users/Public/Desktop/"


verzeichnis_liste = [desktop, download, desktop_public]

for verzeichnis in verzeichnis_liste:
    sortieren(verzeichnis)
