http://genelaix.free.fr/IMG/pdf/presentation_lora_lorawan.pdf

Sigfox est prévu pour envoyer 140 messages de 12 octets à 300 bauds par jour et recevoir 4 messages par jour. 

LoRa envoie des messages plus longs (5KO) et sans limitation.

LoRa optimise dynamiquement le lien entre l’objet (node) et la passerelle (gateway) ce qui permet des portées plus grandes ( plus de 15Km en plaine)

Le protocole LoRa est sous licence Semtech mais s’appuie sur un réseau « libre »

Sigfox utilise les réseaux privés des opérateur téléphoniques

LoRa et Sigfox utilisent en Europe la bande des 868MHz


------------

Dans un premier temps et pour faire nos tests, on va travailler sur un capteur de température simple. On prendra bien le temps de sécuriser notre réseau.

Dans un second temps, si on a le temps, on peut imaginer un réseau de capteurs. Par exemple un capteur classe A (cf site web) qui envoit la luminosité, un traitement par l'application server en fonction d'un seuil, et un autre capteur en classe B ou C qui serait un actionneur sur un volet roulant ou autre. Bien sécuriser toutes les communications.