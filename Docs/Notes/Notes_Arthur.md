# Notes Arthur

## LoRa 

Le **lora** est un protocol de communication sans fil que nous devons mettre en oeuvre au cour de ce projet. Nous devrons s'ecuriser :
- Le *noeud* qui se composera d'un ùC sur une carte de dev' STM32"" 
- La *passerelle* qui serra sur une Raspberry ( la raspberry hébergera aussi le serveur d'application)
- Transmission des paquets (pas la partie communication entre le noeud et la passerelle)

## Protocol LoRa WAN 
Tant que l'on utilise 1 capteur et une passerelle on peut utiliser de P2P, mais si nous avons plusieurs capteurs il va falloir **utiliser un réseau** la technologie LoRaWAN implémante ...

## Clées LoRaWAN :

### NwkSKey:
Cette clé sert à calculer et à vérifier intégrité du message (**MIC** : Message Integrity Code) elle est utilisé par *le noeud* et *le Network Server* 

### AppSKey:
Cette clé set a chiffrer et à déchiffrer la *payload* d'un message d'une application. Elle est utilisé part *le noeud* et *le Network Server*

### AppKey:
Clé AES généré par le serveur d'application. Les 2 clées précédente sont dérivé de celle-ci


## Sécurisation du Noeud

### Attaques possibles :
#### Materiel 
- attaque par écoute du bus entre le CPU et la mémoire

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

- Il faut empécher d'autre utilisteur de récuperer les valeurs de la communication.
- Empecher d'envoyer de fausses informations au serveur d'application.
- Empecher de booter sur un autre OS que celui que nous allons créer  

## Sécurisation des paquets:
Nous n'avons pas à sécuriser la maniere dont communiquent le noeud et la passerelle. Mais il faut s'assurer que les messages ne soient pas alterés ou interceptés.
La comminication entre le *noeud* et la *passerelle*  doit pouvoir éviter :
- Man in the middle
- Les attaques en texte clair
- Le jamming
- Dos


## Analyse des risques

Dump memoire
capteurs
