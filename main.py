import os
import shutil

def sortieren(unordentlich):
    exe = False
    # Dateiendungen erkennen und Zielverzeichnis zuweisen
    for i in os.listdir(unordentlich):
        if i.endswith((".png", ".jpg")):
            dst_dir = "C:/Users/troho/Desktop/IMG/"
        elif i.endswith(".pdf"):
            dst_dir = "C:/Users/troho/Desktop/PDF/"
        elif i.endswith((".stl", ".3mf")):
            dst_dir = "C:/Users/troho/Desktop/3D_Dateien/"
        elif i.endswith((".lnk", ".exe")):
            dst_dir = "C:/Users/troho/Desktop/EXE/"
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

desktop = "C:/Users/troho/Desktop/"
desktop_public = "C:/Users/Public/Desktop/"
download = "C:/Users/troho/Downloads/"


sortieren(desktop)
sortieren(desktop_public)
sortieren(download)