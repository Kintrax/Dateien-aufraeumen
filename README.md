# Dateisortierungsprogramm

Das Dateisortierungsprogramm ist eine Python-Anwendung, die es Benutzern ermöglicht, Dateien automatisch in entsprechende Zielverzeichnisse zu sortieren, basierend auf ihren Dateiendungen. Die App verwendet die `os`- und `shutil`-Module für die Dateiverwaltung.

## Wie funktioniert es?
Das Programm durchsucht ein angegebenes Verzeichnis nach Dateien und ordnet sie je nach Dateiendung in bestimmte Zielverzeichnisse. Die unterstützten Dateitypen und die zugehörigen Zielverzeichnisse sind wie folgt:
- **Bilder (.png, .jpg)** --> `C:/Users/deinUsername/Desktop/IMG/`
- **PDF-Dokumente (.pdf)** --> `C:/Users/deinUsername/Desktop/PDF/`
- **3D-Dateien (.stl, .3mf)** --> `C:/Users/deinUsername/Desktop/3D_Dateien/`
- **Verknüpfungen und ausführbare Dateien (.lnk, .exe, .url)** --> `C:/Users/deinUsername/Desktop/EXE/`

Doppelte Dateinamen werden durch Anhängen von Zahlen an den Dateinamen gelöst, und doppelte ausführbare Dateien werden gelöscht, um Konflikte zu vermeiden.

## Installation und Verwendung
1. Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
2. Laden Sie das Dateisortierungsprogramm herunter.
3. Öffnen Sie das Programm in einem Texteditor und passen Sie die Pfadvariablen `desktop` und `download` entsprechend Ihrem System an.
4. Führen Sie das Programm aus, um Ihre Dateien zu sortieren.

## Batch-Datei und Aufgabenplanerintegration
Die Datei `sortieren.bat` enthält Befehle zum Starten des Python-Interpreters und zur Ausführung des `sortieren.py`-Skripts. Um die Batch-Datei zum Windows-Aufgabenplaner hinzuzufügen, folgen Sie diesen Schritten:
1. Drücken Sie `Win + R`, um den Ausführen-Dialog zu öffnen, und geben Sie `taskschd.msc` ein, um den Aufgabenplaner zu öffnen.
2. Klicken Sie auf "Aufgabe erstellen..." im rechten Bereich.
3. Geben Sie einen Namen und eine Beschreibung für die Aufgabe ein.
4. Klicken Sie auf "Trigger" und "Neu...". Unter Aufgabe starten wählen Sie "Bei Anmeldung" als Trigger aus und bestätigen Sie mit "OK".
5. Klicken Sie auf "Aktionen" und "Neu...". Geben Sie den Pfad zur Batch-Datei in das Feld "Programm/Skript" ein oder navigieren Sie zu der Batch-Datei.
6. Klicken Sie auf "OK" und noch einmal auf "OK", um die Aufgabe zu erstellen.

## Hinweis
Das Programm wurde für den persönlichen Gebrauch entwickelt und kann je nach Bedarf angepasst und erweitert werden. Bitte beachten Sie, dass das Programm in seiner aktuellen Form möglicherweise nicht alle Dateitypen oder spezifischen Anforderungen abdeckt.
