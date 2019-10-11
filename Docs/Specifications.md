 # Specification
Le travail de sécurisation à fournir pour la fin de ce projet vise 2 parties du réseau, la *passerelle* et le *noeud* nous ne nous occuperons pas de la sécurisation de la communiction en **LoRa**.
Le LoRaWAN est un protocole de communication à longue distance et faible consomation d'energie. Il est composé de 3 services. Les *noeuds*, les *passerelles* et le *serveur d'applications*. 

![fonctionnement_lora](Schema_techniques/Schema_LoRaWAN.png)

Le protocole LoRa n'est pas fait pour envoyer de grandes quantités d'information très rapidement. On ne peut envoyer que quelques KiloOctets par intervalle de quelques minutes.

Dans sa version 1.0 le LoRaWAN specifie déjà plusieurs directives à suivre pour le sécuriser.
Il y a une clef de ***AES 128bits*** à fournir pour sécuriser la commuication depuis le *noeud* jusqu'au *serveur d'application*.
- **AppKey** Clés AES principale elle doit être connue *du noeud* et *du network manager*. Elle sert ensuite à déterminer les 2 clefs suivantes.
- **NwkSKey** Network Session key : chiffre la communication entre le *noeud* et *le network server*. Elle sert à détecter une eventuelle perte d'information dans le message.
- **AppSKey** Application Session key : chiffre le message en tr *le noeud* et *le network server*, sans cette clées il est impossible de lire le message.

Les clés **NwkSKey** et **AppSKey** sont actualisées à chaque nouvelle connexion d'un appareil, elles sont unique à chaques *noeuds* du réseau.

Le LoRaWAN utilise des *frame counter* à fin déviter les attaques par répétition.
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
-  Les clés **NwkSKey** et **AppSkey** et de la clef AES **AppKey**

## La passerelle
La *passerelle* sert de traducteur entre le protocole *LoRa* et un autre protocole de communication. Elle sera hébergé sur un micro-ordinateur.

## Network Server
Le *Network server* est le cerveau du réseau LoRaWAN, il génére les clés et authentifie les noeuds. Il déchiffre aussi une partie des trames du réseau.

Surface d'attaque :
- Enregistrement clé AES
- Création des clefs **NwkSKey** et **AppSKey**

Secrets à protéger
- La valeur des clefs **NwkSKey**, **AppSKey** et **AppKey**

## Application Server
Le *Application server* est le service qui va traiter l'information du capteur, il va déchiffrer la dernière partie du message.

Surface d'attaque :
- Réception de la clef **AppSKey**
- Gestion de la clé **AppSKey**

Secret à protéger :
- La valeur de la clef **AppSKey**

## Mise en place d'un banc de test

Pour la réalisation du banc de test nous allons créer un noeud LoRa WAN avec un kit de développement provenant de ST microelectronics. Ce noeud communiquera les informations prevenant d'un capteur toutes les 10min à Raspberry Pi equipé d'un module LoRaWAN. La Raspberry aura plusieurs service qui communiquerons en interne *gateway*,*networkserver*, *application server*.
L'application server pourra par exemple enregistrer la valeur du capteur dans un fichier et l'afficher sur un therminal.


## Analyse des risques

Pour le cas d'usage, nous avons défini que les aspects de non-répudiation et de confidentialité ne sont pas les plus critiques car nous voulons transmettre uniquement la température et l'humidité.
Il faut cepandant éviter qu'une personne vienne altérer l'information envoyée. Nous devons être sûrs que le *noeud* qui envoie l'information est bien le *noeud* que nous avons créé et pas celui d'un éventuel attaquant (par exemple : *man in the middle*).


## Methodologie gestion de projet

Pour gérer le projet nous utilisons un outil de *versionning* appelé Github où on y met tout le code du projet, les sources ainsi que la documentation. Pour nous organiser tout au long de la période du projet nous avons créé un diagramme de GANTT. Nous le garderons à jour pandant toute la durée du projet. Pour avoir une gestion de projet plus précise (tâches à effectuer chaques semaines), nous utilisons l'onglet *Project* de notre *repository* Github. Dans cet onglet nous indiquons pour chaque semaine les différentes tâches à faire. Les tâches ont 3 états **A faire**, **En cours** et **Fini** nous déplaçons et nous ajoutons des tâches au cours de la semaine.

Pour la méthode de gestion de projet nous allons utiliser la methode en "spirale". En commençant par créer un réseau LoRaWAN basique, puis nous ajouterons des couches de sécurité au fur et à mesure.
