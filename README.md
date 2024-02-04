# GNU Cash Kassenstände Visualisieren

Dieses Python-Tool gibt der Finanzer:in die Möglichkeit Kassenstände aus GNU-Cash zu exportieren und über eine Zeitachse zu visualisieren.

## HOWTO: Export Running Balance

1. In GNU-Cash Reports -> Transaction Reports auswählen
2. Clicke auf Options
3. Unter Accounts entsprechenden Account auswählen
4. Unter Display wähle aus: Date, Num, Account Balance
5. Unter General stelle das Anfangsdatum korrekt ein.
6. Auf Exportieren drücken und an der entsprechenden Stelle abspeichern.

## Visualisieren

Vor dem Ausführen des Skriptes stelle sicher dass `python3` installiert ist und du dich im entsprechenden Virtual Environment befindest.

> Um eine Virtuelle Umgebung zu erstellen gib in der Konsole ein:
> ```
> python3 -m venv /path/to/new/virtual/environment
> ```
> (auf Windows ist `python3` meist nur als `python` installiert)
>
> Öffne die virtuelle Umgebung mit `source /venv path/bin/activate`
>
> [Dokumentation](https://docs.python.org/3/library/venv.html)

Dort müssen die Pakete `pandas`und `matplotlib`installiert sein.

> ```
> pip install <paket>
> ```

Das Script nimmt die aus GNU-Cash exportierten HTML-Dateien entgegen und liest diese zur Visualisierung automatisch ein.

```
python3 display_balance_history.py [path/to/report1] [path/to/report2] [path/to/report3] [...]
```

Das Script unterstützt hier eine beliebige Anzahl an Transaktions-Report Dateien, um die Entwicklung mehrerer Kassenstände gleichzeitig dar zu stellen.
