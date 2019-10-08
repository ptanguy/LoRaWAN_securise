 # Specification
Le travail de sécurisation à fournir pour la fin de ce projet vise 2 parties du réseau, la *passerelle* et le *noeud* nous ne nous occuperons pas de la sécurisation de la communiction en **LoRa**.
Le LoRaWAN est un protocol de communication à longue distance et faible consomation d'energie. Il est composé de 3 services. Les *noeuds*, les *passerelles* et le *serveur d'applications*. 
![fonctionnement_lora](Schema_techniques\Schema_LoRaWAN.png)

Le protocol LoRa n'est pas fait pour envoyer de grandes quantitées d'information trés rapidement, on peut envoyer que quelques Kilobits par intervalle de quelques minutes.

Dans ça version 1.0 le LoRaWAN specifie déjà plusieurs directives à suivre pour le sécuriser.
Il y a plusieurs clés de ***AES 128bits*** à fournir pour sécuriser la commuication depuis le *noeud* jusqu'au *serveur d'application*.
- **NwkSKey** Network Session key
- **AppSKet** Application Session key
- **AppKey** Application key

Les clés **NwkSKey** **AppSKet** et sont actualisé à chaque nouvelle connexion d'un appareil, elles sont unique à chaques appareil du réseau.



## Le noeud
Le noeud sera composé d'un microcontroleur, d'un capteur (ou plusieurs) et d'un module permettant la communication en LoRa.

## La passerelle
La passerelle sera hébergé sur un micro-ordinateur qui aura un module pour la communication LoRa. Le micro-ordinateur hégergera par la même occasion un serveur d'application.

Pour maitriser aux mieux notre passerelle nous allons dévelloper notre propre OS