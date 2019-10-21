Introduction
============

Projet M1 CSSE *mise en oeuvre d'un réseauLoRaWAN sécurisé* 2019-2020

Ceci est la documentation de notre projet de sécurisation d'une communication LoRaWAN.

Contexte :

L’Internet des objets (IoT, en anglais) est un paradigme dont les premiers dé-
ploiements ont quelques années (voire plus, si l’on parle de réseau de capteurs).
D’un point de vue sécurité, l’IoT a une surface d’attaque très importante, du
fait du nombre de technologies, de protocoles, du type de déploiement et du
nombre d’acteurs différents.
Ce projet s’applique aux réseaux d’objets connectés longue porté du type Lo-
RaWAN (Long Range Wide Area Network).

Mission :

Dans ce contexte, il nous est demandé de mettre en place un réseau LoRaWAN.
Le premier et principal objectif est de créer un banc de test dans lequel un ré-
seau LoRaWAN complet, mais simple doit fonctionner, dont les éléments de sécu-
rité côté noeud et passerelle seront correctement mis en oeuvre. Un cas d’usage
(à définir) devra être mis en place et les aspects de sécurité devront être bien
maîtrisés. Le deuxième objectif consiste à discuter de la surface d’attaque de notre
système. Un aspect analyse est donc demandé en prenant en compte les dif-
férentes versions du LoRaWAN, chacun des éléments du système etc.

Rappel des points d’action :

• Mise en place d’un réseau LoRaWAN sécurisé
• Sécurisation de la passerelle, du Network serveur et de l’Application serveur
• Sécurisation des noeuds LoRaWAN en utilisant les blocs matériels pour le chiffrement ainsi que pour la gestion des clés.
• Analyse et discussion de la sécurité du système (éventuellement Pentest)


Schéma simplifié 
================

![fonctionnement_simple](../docs/schemas/Schema_LoRaWAN.png)



Répartition des tâches 
======================

Pour faire ce travail, nous sommes deux personnels travaillant à plein temps. 
Nous devons donc nous répartir équitablement les tâches