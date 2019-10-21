Introduction
============

Projet M1 CSSE *mise en oeuvre d'un réseau LoRaWAN sécurisé* 2019-2020

Ceci est la documentation de notre projet de sécurisation d'une communication LoRaWAN.

**Contexte :**

L’Internet des objets (IoT, en anglais) est un paradigme dont les premiers déploiements ont quelques années (voire plus, si l’on parle de réseau de capteurs).
D’un point de vue sécurité, l’IoT a une surface d’attaque très importante, du fait du nombre de technologies, de protocoles, du type de déploiement et du nombre d’acteurs différents.
Ce projet s’applique aux réseaux d’objets connectés longue porté du type Lo-
RaWAN (Long Range Wide Area Network).

**Mission :**

Dans ce contexte, il nous est demandé de mettre en place un réseau LoRaWAN.
Le premier et principal objectif est de créer un banc de test dans lequel un réseau LoRaWAN complet, mais simple doit fonctionner, dont les éléments de sécurité côté noeud et passerelle seront correctement mis en oeuvre. Un cas d’usage (à définir) devra être mis en place et les aspects de sécurité devront être bien maîtrisés. Le deuxième objectif consiste à discuter de la surface d’attaque de notre système. 
Un aspect analyse est donc demandé en prenant en compte les différentes versions du LoRaWAN, chacun des éléments du système etc.

**Rappel des points d’action :**

- Mise en place d’un réseau LoRaWAN sécurisé
- Sécurisation de la passerelle, du Network serveur et de l’Application serveur
- Sécurisation des noeuds LoRaWAN en utilisant les blocs matériels pour le chiffrement ainsi que pour la gestion des clés.
- Analyse et discussion de la sécurité du système (éventuellement Pentest)


Schéma simplifié 
================

Le schéma ci-dessous est un schéma simplifié, permettant de comprendre le fonctionnement global de notre système.

Nous avons donc plusieurs noeuds, qui vont communiquer en LoRaWAN avec une passerelle. Cette passerelle va ensuite communiquer ce qu'elle a reçu des noeuds au serveur d'application, via un autre protocole de communication.

![fonctionnement_simple](../docs/schemas/Schema_LoRaWAN.png "Fonctionnement simple")



Répartition des tâches 
======================

Pour faire ce travail, nous sommes deux personnels travaillant à plein temps, Arthur et François.
Nous devons donc répartir équitablement les tâches.

Dans un premier temps, nous allons tous les deux travailler au déploiement du réseau LoRaWAN. 

François va ensuite se charger de la sécurisation de la passerelle, ainsi que des connections avec le network server et l'application server.

Arthur se chargera de travailler sur la sécurisation du noeud, et le transfert des informations vers la passerelle.

Tous les deux s'occuperont de rédiger constamment une documentation fournie ainsi que tous les documents livrables attendus.

Organisation
============

Nous avons choisi une approche en spirale pour notre organisation. En effet, sur les conseils de notre encadrant, ce modèle nous permet de tester les différentes couches de sécurisation une à une et de revenir aux étapes précédentes si besoin pour modifier et compléter le dispositif.

Le schéma ci-dessous montre simplement le fonctionnement d'une organisation en spirale.

![organisation_spirale](../docs/schemas/Schema_spirale.png "Organisation en spirale")


Contraintes
===========

