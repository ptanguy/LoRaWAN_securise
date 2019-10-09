 # Specification
Le travail de sécurisation à fournir pour la fin de ce projet vise 2 parties du réseau, la *passerelle* et le *noeud* nous ne nous occuperons pas de la sécurisation de la communiction en **LoRa**.
Le LoRaWAN est un protocole de communication à longue distance et faible consomation d'energie. Il est composé de 3 services. Les *noeuds*, les *passerelles* et le *serveur d'applications*. 
![fonctionnement_lora](Schema_techniques/Schema_LoRaWAN.png)

Le protocole LoRa n'est pas fait pour envoyer de grandes quantités d'information très rapidement. On ne peut envoyer que quelques KiloOctets par intervalle de quelques minutes.

Dans sa version 1.0 le LoRaWAN specifie déjà plusieurs directives à suivre pour le sécuriser.
Il y a plusieurs clés de ***AES 128bits*** à fournir pour sécuriser la commuication depuis le *noeud* jusqu'au *serveur d'application*.
- **NwkSKey** Network Session key 
- **AppSKey** Application Session key : chiffre le message, sans cette clées il est impossible de lire le message

Les clés **NwkSKey** et **AppSKey** sont actualisées à chaque nouvelle connexion d'un appareil, elles sont unique à chaques appareil du réseau.

Le LoRaWAN utilise des frame Counter à fin déviter les attaque par répétition.
2 conteurs sont initialisés lorsqu'un nouvel appareil est connécté.
Le Noeud incrément le compteur **FCntUP** à chaque fois que qu'il envoit une information sur le *UpLink*. Le Network serveur lui incrémente le compteur **FCntDown** à chaque fois qu'il écrit sur le *DownLink*. Pour chaque trame du réseau la valeure des compteurs est envoyé avec. Le recepteur de la trame va comparer la valeur des compteurs à l'intérieure de la trame avec ses propres compteurs et si la valeurs des compteurs de la trame est inferieur aux copteur du recepteur ce dernier va ignorer le message.


## Le noeud
Le *noeud* sera composé d'un microcontroleur, d'un capteur (ou plusieurs) et d'un module permettant la communication en LoRa. Pour le noeud nous allons utiliser un kit de développement provenant de STmicroelectronics.

Surface d'attaque : 
-  Gestion des Clés AES
-  Modification du code source
-  Interception des données directement sur le capteur
-  SPA
-  DPA
-  Analyse EM
-  Memory tempering
-  Valeur des Frame Counters

Les secrets à protéger sont :
-  La valeur du capteur
-  Les clés AES **NwkSey** et **AppSkey**

## La passerelle
La *passerelle* sert de traducteur entre le protocole *LoRa* et un autre protocol de communication. Elle sera hebergé sur un micro-ordinateur.

## Network Server
Le *Networkmanager* est le cerveau du réseau LoRaWAN il génére les clées et authentifie les noeuds. Il déchiffre aussi une partie des trame du réseau.

Surface d'attaque :
- Enregistrement clé AES
- Création clé AES
- Valeur des Frame Counters
  
## Application Server
Le *Application server* est le service qui va traiter l'information du capteur, il va déchiffrer la dernière partie du message.

Surface d'attaque :
- Gestion clé AES
- Création clés AES

Secret à protéger :
- La valeur de la clés AES