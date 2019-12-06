-------------------

Cas classique : système DAC (propriétaire, groupe) de Linux
Cas avancé : SELinux, Apparmor, etc

Une fois compris le principe, voir comment l'intéger à ma distro Linux (LoRaserver.io) via Yocto pour la GW.


/!\ Deux challenges techniques : 
- savoir mettre en oeuvre le système de permission DAC et MAC.
- savoir ensuite appliquer la compétence précédente dans le cas de la passerelle LoRa avec Yocto.

Bonus : *travail sur le secure-boot*. Garantir que l'on n'essaye pas
d'usurper notre identité pour récupérer les trames reçues, ni pouvoir
envoyer des instructions aux noeuds.


Fermer les ports et services inutiles, réduire la surface d'attaque.
Faire un nmap pour voir ce qui est ouvert


















---------------
ANCIEN
---------------

[Cours complet](http://genelaix.free.fr/IMG/pdf/presentation_lora_lorawan.pdf)

Sigfox est prévu pour envoyer 140 messages de 12 octets à 300 bauds par jour et recevoir 4 messages par jour. 

LoRa envoie des messages plus longs (5KO) et sans limitation.

LoRa optimise dynamiquement le lien entre l’objet (node) et la passerelle (gateway) ce qui permet des portées plus grandes ( plus de 15Km en plaine)

Le protocole LoRa est sous licence Semtech mais s’appuie sur un réseau « libre »

Sigfox utilise les réseaux privés des opérateur téléphoniques

LoRa et Sigfox utilisent en Europe la bande des 868MHz


------------

Dans un premier temps et pour faire nos tests, on va travailler sur un capteur de température simple. On prendra bien le temps de sécuriser notre réseau.

Dans un second temps, si on a le temps, on peut imaginer un réseau de capteurs. Par exemple un capteur classe A (cf site web) qui envoit la luminosité, un traitement par l'application server en fonction d'un seuil, et un autre capteur en classe B ou C qui serait un actionneur sur un volet roulant ou autre. Bien sécuriser toutes les communications.

------------

Demander à la réunion : 

- Combien de clefs y a-t-il réellement (2 ou 3) ?
- Est-ce que on pourrait pas voir une vraie passerelle et un serveur network et d'application distincts plutôt que tout dans la raspberry ?
- Quand est la fin du projet ?

Réponses : 

- Il y en a bien 3
- Non, on met tout sur la rasp
- M. Tanguy va se renseigner...

-------------


Utilisation de la raspberry

> sudo raspi-config (puis autoriser le ssh)
> sudo apt update
> sudo apt upgrade (faire et installer les maj)

-------------

15 octobre 2019 -> prise en main IC880A

-------------------


Sécurisation de la passerelle : HTTP => HTTPS et modification MDP par défaut

-------------------

Pour le diapo, faire au début un rappel des termes et acronymes utilisés 
(ex : noeud = capteur + stm(ou fipy) + antenne, etc)

-------------------

