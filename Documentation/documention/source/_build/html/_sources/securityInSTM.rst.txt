************************************************
La sécurité dans le micro controleur STM32L072CZ
************************************************

La plus part des micros controleurs STM incorporent des technologies de sécurité [#]_ , nous allons nous concentrer sur le composant *STM32L072CZ* car c'est le microcontroleur utiliser pour notre noeud.

Fonctions de sécurité dans le STM32L072CZ
#########################################

Tout les micros controleur n'ont pas les mêmes fonctions de sécurité intégrer. Ici nous allons lister celles présantes dans le *STM32L072CZ*

- RDP (Read Out Protection) : Protection de la mémoire Flash qui empêche la copie du code. Cette fonction prévient donc du reverse ingineering fait à l'aide des outils de debugage.

- WRP (Write Protection) : Sert à prottéger une partie de la mémoire Flash d'un effacement ou d'une mise à jour.

- PCROP (Execute Only Firmware) : Permet de configurer certaines partie de la memoire flash pour qu'elles soient uniquement accéssible accéssible par le bus d'instruction du CPU.

- Firewall : Le parfeu est un composant physique qui controle les accés à trois parties de la mémoire, la zone du code (mémoire flash), les donées volatile (SRAM) et les donnés non volatile (Flash).

- MPU (Memory Protection Unit) : Mecanisme de protection qui permet de définir des droits d'accès à certaines zone de la mémoire.

- Anti temper : Détection d'une intrusion au niveau physique, permet de prendre les mesure adéquates comme éfaccer la mémoire par example.

- IWDG ( Independant watchdog) : Watchdog Independant permettant de lever des flags si une tache prend plus de temps que celui qui lui est attribué.

Premier cas d'étude, attaque par les ports de debugage
######################################################

Dans un premier temps nous allons nous concentrer sur la sécurisation vis à vis d'un dump memoire via l'outil ST Link.
Pour celà nous allons utiliser la fonction de sécurité *RDP*.

La *RDP* offre différents niveaux de protection 0, 1, 2.

- Le niveau 0, équivaut à aucune protection la memoire flash et complètement lisible, peut importe le mode de démarrage du controleur (par la RAM, par la flash, par le debuger ...). Ce mode doit être utilisé uniquement pour la phase de développement.

- Le niveau 1, empèche l'accès à la mémoire flash et à la mémoire SRAM2 par le debuger. Cepandant lorsque le programme démarra à partir de la mémoire flash celui-ci à accées à la mémoire flash et la SRAM2.

- Le niveau 2, ce niveau empêche tout les accès aux mémoire depuis l'extérieur. **Attention après l'avoir activer on ne peut plus revenir en arrière**.

Second cas d'étude, attaque par une faille dans le code
#######################################################

Il faut faire très attention lors de l'utilisation de la *RDP* car dés que l'on utilise une protection de niveau <= 1, on ne peut plus mettre de programme dans la carte via le bootloader.
Pour mettre à jour le programme il faut utiliser une *SFU* (Secure Firmware Update).

Dans un second temps nous pouvons nous attarder sur protéger nos clès vias à vis d'une faille exploité dans notre code. Pour celà nous devrons utiliser en plus les sécurité suivante *PCROP*, *Firewall* et *TrustZone*

Ordre d'implémentation des fonctions de sécurité
################################################

Nous venons de voir les fonctions à mettre en oeuvre pour notre scénario, comme ce sont des fonctions de sécurité une fois implémentée elles vont restreindrent les capacité de débogage du code.


.. rubric:: Footnotes

.. [#] Vous pouvez trouver plus d'information à cette adresse : https://www.st.com/content/ccc/resource/technical/document/application_note/group1/9f/0b/e4/b6/75/15/4f/e2/DM00493651/files/DM00493651.pdf/jcr:content/translations/en.DM00493651.pdf
