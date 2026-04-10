# Uppgift 2 Lagerhållning

## Projektstruktur
* features/stock.feature beskriver beteendet med Given, When, Then
* features/steps/stock_steps.py – innehåller stegdefinitioner i Python
* src/stock.py – innehåller funktionerna för lagerhanteringssystem

## Tester (BDD)
Testerna är skrivna enligt BDD och består av två delar:

### Feature-fil
Beteendet beskrivs i en .feature-fil med Gherkin-syntax:
* Given – startvärde
* When – handling (omvandling)
* Then – förväntat resultat

## Installation
* installerar beroenden:
```
pip install -r requirements.txt
```
## Kör tester
```
behave
```

## Konfigurationsfiler
* requirements.txt