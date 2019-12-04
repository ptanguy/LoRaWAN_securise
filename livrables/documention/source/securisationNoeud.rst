******************************
Sécurisation du Noeud LoRaWAN
******************************

Dans l'architecture LoRaWAN le rle du noeud est de transmettre une information qui serra traité par l'application server.
Dans le cadre de notre scénario le campus connécté, nous transmetons une donnée publique qui est la température. Nous devons donc nous concentrer, sur l'authentification du noeud LoRaWAN et l'intégrité de la donnée.

Pour celà nous devons éviter que notre noeud soit remplacé par un autre noeud qui pourrais envoyer des informations erronnées.

Le protocole LoRaWAN permet à un noeud de ce connécter de 2 façons différentes, OTAA (Over The Air Activation), ABP (Activation by personalization). 

Fonctionnement activation OTAA
##############################

L'activation par OTAA met en jeux *DevEUI*, *AppEUI*, *AppKey*  pour ce connecter à la gateway puis utilise *AppSKey* et *NetSKey* pour chiffrés la comunication jusqu'à l'application server.
Le protocole LoRaWAN ne précise pas si les clés doivent être stocké en clair dans la mémoire ou doivent être chiffrés. Il faut *AppSKey* et *NetSKey* sont renouvelé à chaque 
Si un attaquant arrive à obtenir les 3 premières clés alors, il pourra usurpé l'identité de notre neud. S'il parvint à obtenir les 2 autres clès, il pourra uniquement déchiffrer l'information.

Fonctionnement activation ABP
#############################

L'activation par personnalisatioon met en oeuvre *DevAddr*, *NwkSKey* et *AppSKey* ces 2 dernière sont les clés permettants de chiffrer la communication ainsi, si un attanquant les récupères, il peut tout aussi bien usurper l'identité de notre noeud que lire les informations envoyés.


Analyse des risques
###################

Dans un premier temps on remarque que le protocole LoRaWAN ne stipule pas si les clés doivent être stocké en clair dans la mémoire ou bien chiffré. Celà veut dire que si un attaquant fait un dump de la mémoire, il va pouvoir trouver facilement les clès.
On remarque ensuite, que l'utilisation de l'activation par OTAA est plus sécurisé car elle utilise plus de clès et en renouvelle 2 à chaques connexions. La connexions par ABP est moins sécurisé car elle utilise uniquement 3 clès, dont 2 qui peuvent aussi permettre l'écoutes de la communication.

