 # Specification
Le travail de sécurisation à fournir pour la fin de ce projet vise 2 parties du réseau, la *passerelle* et le *noeud* nous ne nous occuperons pas de la sécurisation de la communiction en **LoRa**.
Le LoRaWAN est un protocole de communication à longue distance et de faible consommation d'énergie. Il est composé de 3 services. Les *noeuds*, les *passerelles* et le *serveur d'applications*. 
![fonctionnement_lora](Schema_techniques\Schema_LoRaWAN.png)

Le protocole LoRa n'est pas fait pour envoyer de grandes quantités d'information très rapidement. On ne peut envoyer que quelques KiloOctets par intervalle de quelques minutes.

Dans sa version 1.0 le LoRaWAN specifie déjà plusieurs directives à suivre pour le sécuriser.
Il y a plusieurs clés de ***AES 128bits*** à fournir pour sécuriser la commuication depuis le *noeud* jusqu'au *serveur d'application*.
- **NwkSKey** Network Session key 
- **AppSKet** Application Session key : Encrypt le message, sans cette clé il est impossible de lire le message
- **AppKey** Application key

Les clés **NwkSKey** et **AppSKet** sont actualisées à chaque nouvelle connexion d'un appareil, elles sont unique à chaques appareil du réseau.




## Le noeud
Le noeud sera composé d'un microcontroleur, d'un capteur (ou plusieurs) et d'un module permettant la communication en LoRaWAN.

## La passerelle
La passerelle sera hébergée sur un micro-ordinateur qui aura un module pour la communication LoRa. Le micro-ordinateur hégergera par la même occasion un serveur d'application.

Pour maitriser aux mieux notre passerelle nous allons développer notre propre OS.
