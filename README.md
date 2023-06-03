# PythonEindopdracht

## De werking/features

1. Modules.py

- Alle modules erven over van de parent Module klasse.
- De modules hebben een log en run functie. Bij de run functie wordt de module uitgevoerd en de log functie wordt gebruikt om te loggen naar het output bestand. Het zijn virtuele functies.
- Door deze 2 virtuele functies is het makkelijk om een module toe te voegen die makkelijk zal werken met script.py.
- self.logmessage bevat de boodschap die gelogd zal worden naar de output. Dit wordt gebruikt bij elke module.


2. Formaat van config bestand

- In het config bestand wordt een structuur gebruikt. 
- Het signaalwoord van signals.txt wordt gemapt met de parent label van config.yaml. 
- De child labels bevatten informatie over het  bestand, de klasse en de functie die moeten worden uitgevoerd. 
- Dit formaat maakt het makkelijk om nog een extra module toe te voegen.



3. script.py

- Eerst wordt er gekeken of er een nieuwe commit met signaalwoord is geweest in de afgelopen 120 seconden in signals.txt.
- Het signaalwoord uit signals.txt wordt gekoppeld via config.yaml aan de overeenkomstige module.
- Output van de log functie van de module wordt naar output.txt weggeschreven.
- output.txt wordt gepusht naar GitHub.



## moeilijkheden 
- Ik heb de keylogger niet kunnen uitvoeren/testen omdat mijn pc de module als een bedreiging zag. 
- De MailModule werkte maar ik heb bij username, password , sender en recipient example.@example.com geschreven anders moest ik mijn gegevens laten staan.

## problemen
Ik heb al de problemen kunnen oplossen 


