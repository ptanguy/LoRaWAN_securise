# Notes Arthur

## LoRa 

Le **lora** est un protocol de communication sans fil que nous devons mettre en oeuvre au cour de ce projet. Nous devrons s'ecuriser :
- Le *noeud* qui se composera d'un ùC sur une carte de dev' STM32"" 
- La *passerelle* qui serra sur une Raspberry ( la raspberry hébergera aussi le serveur d'application)
- Transmission des paquets (pas la partie communication entre le noeud et la passerelle)

## Sécurisation du Noeud

### Attaques possibles :
#### Materiel 
- attaque par ecoute du bus entre le CPU et la mémoire

- modification de la mémoire (memory tempering)
    - injection aléatoire de donnée dans a mem' (Spoofing)
    - echange des données dans la mémoire (permutation)  (Splicing)
    - renvois d'un code d'instruction (replay)

- Injection de fautes
    - glitch
- Modèle de consomation 
    - SPA Simple power Analysis
    - DPA Differential power Analysis
- Analyse electromagnétique

- Modification du code source si pas de condanation du bootloader

## Sécurisation de la passerelle
La passerelle sera donc une Raspberry PI, nous utiliserons donc un OS
### Attaques possibles : 
*Toutes les  attques matérielles presentes dans la partie sur le noeud*

+

- Il faut empecher d'autre utilisteur de récuperer les valeurs de la communication.
- Empecher d'envoyer de fausses informations au serveur d'application.
- Empecher de booter sur un autre OS que celui que nous allons créer  

## Sécurisation des paquets:
