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

Dump memoire (STM32) des clès
++ Canaux cachés (DPA,SPA ...)
Capteurs (non hackable )
Antenne ( Non)
Communication sans fil LoRa entre Noeud et passerelle ( Hackable mais non traité)
LoRaServer OS : Sécurisé ?? mais a adapter à notre cas d'usage (plusieurs utilisateurs, ouverture ports ...) 
Gérer les Maj (cf Mender ) / Gerer la Maintenance
++ Mise a jour l'ogiciel ne venant pas d'un trusted serveur
++ Usurpation d'identité d'un Noeud (Authenticitée)
++ execution d'un code malicieux sur la box LoRa
++ Dos attaque sur la box LoRA

### OS 

2 cas de figures 

1. Un os qui ne fais que passerelle, network serv', application serv
    - Administration SSH
    - VPN pour la connection ?
    - MAJ ... (à reflechir la sécuritée à ce propos)
    - Faire attention aux services inutiles 
2. Un os qui fais ce qui est dit au dessus  + peut avoir d'autres services donc il faut empécher les autres utilisateurs d'accéder aux information , il faut vérrouiller chaque partie du server en faisant attention qui y a accées...
Dans le premier cas nous devrons considérer la Box LoRa comme un **serv à sécuriser** alors que dans le second cas nous devrons le considérer plus comme **une sessions** sur une machine sur laquelle tourne plusieurs services.



### Contre mesures
Dump mémoire  -> Crypté / Caché la clef / Composant sécurisé autre projet M1
Capteur difficilement hackable mais on peut le mettre dans une boite ( dans notre cas on devra mettre tout le noeud dans la boite)
Antenne mettre en hauteur / boite 
Communication

A rechercher pour l'OS 

Sécuriser la com avec le serv de Maj avec un VPN

Secureboot pour éviter l'execution de code malicieu des les premiers moments du boot [lien secure boot debian](https://wiki.debian.org/SecureBoot)



## Comment cacher la clés dans le STM3é ?
Il faut eviter de cacher la clé dans le software, car elle serra directement lisible dans la mémoire.

Idée 1 :
Il faut la stocker en hardware...

Idée 2 :
Generer une clées aléatoire pour encrypter la RAM stocker à chaque execution du programme ainsi la mémoire est illisible. 


## Choisir OS ou en créer un ?

| Créer OS                                                             | Prendre LoRa Server                                                   |
|----------------------------------------------------------------------|-----------------------------------------------------------------------|
| ++ Parfaite connaissance des programmes fonctionnant sur le serveur  | ++ Rapidité de mise en place                                          |
| -- Recherche de recettes à mettre en oeuvre                          | -- Recherche des pogrammmes installé pour vérifier s'ils sont sécuisé |

Le choix ce porte sur LoRa Server car nous penssont gagner beaucoup de temps sur la mise oeuvre.

# Présentation du Projet Format Poupées Russes

- Mise en place d'un réseau LoRaWAN sécurisé
    - Mise en place d'un réseau LoRaWAN avec sécurité basique
        - Création d'un premier réseau (facile) entre des µC Fipy et capteur Pysense pour la partie Noeud et une Raspberry pour la partie box LoRa
        - Création d'un deuxième réseau pareil que le précédant mais en remplaçant le noeud par une carte STM32 équipé d'un Shield LoRaWAN
        - Construction des services de la Box LoRa
                - Création d'un OS Perso 
             - Utilsation d'un OS existant (LoRaServer IO)
                - OS Full  == Gateway + Network Server + Application Server
                - OS Base == Gateway
    - Tests :
        - Vérification que la valeur du capteur est correcte 
            - Afficher la valeur de celle-ci dans le terminal ecomparer avec la température ambiante
        - Vérifier que la valeur est émise
        - Vérifier que la valeur est arrivée 
        - Verifier que la valeur est bien transmise dans la box LoRA
    - Mise en place d'un réseau avec des couches de sécurité renforcé
        - Sécurisation du Noeud
            - Développer le software du Noeud LoRaWAN
                - Sécurisation du Noeud en cachant les clefs dans la mémoire
                - Sécurisation du Noeud en cachant les clefs dans un composant de sécurité
        - Sécurisation de la Box LoRa 
            - Points de vu 1 : La Box LoRa est le seul composant du serveur
                - Sécurisation vis à vis d'intrusion externe au systeme
                    - VPN 
                - Maintenance 
                    - Mise à jours
                    - SSH
                - Verification des services
            - Point de vu 2 :  La Box LoRa ne sert pas uniquement à au LoRa WAN
                - Sécurisation par rapport aux autres service présent et/ou utilisateurs 
                    - Vérifier les droits d'accées 
        