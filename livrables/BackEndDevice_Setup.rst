Mise en place du noeud LoRaWAN avec la carte *B-L072Z-LRWAN1*
=============================================================

Introduction
############

La finalité de la partie Noeud de notre projet est d'utiliser la carte *B-L072Z-LRWAN1* ainsi que le shield *Motion-MEMS*.
Nous devrons récupérer la valeure d'un des capteurs du shield *Motion-MEMS* et la transmettre à notre *BoxLoRa* (Passerelle + NetworkServer + Application Server).
Nous avons choisit de récupérer les valeur de la température.

D'un point de vue sécurité, comme nous avons préalablement chosit d'utiliser le mode d'appairage OTAA (Over The Air Activation) du protocal LoRaWAN pour notre noeud.
Nous devons cacher une clés maitre (AES 128bit) appelé **AppKey** fin déviter l'usurpation de notre Noeud. Nous devons aussi cacher la valeur d'un compteur de trame (Frame Counter) pour eviter les attaques par rejeu.

Installation des outils
***********************

Pour gagner du temps dans le dévelopement de noeud nous utilisons comme base un projet github [LoRaMAC-node]_ mettant en oeuvre le LoRaWAN sur notre carte.
Nous développons le Noeud à partir d'une distribution *Linux* basé sur *Arch Linux*, les dépendance requisent sont : 

..code-block:: bash

    cmake
    arm-none-eabi-gcc
    arm-none-eabi-newlibS221 : https://www.st.com/en/mems-and-sS221 : https://www.st.com/en/mems-and-sensors/hts221.html#overviewensors/hts221.html#overview
    openocd

Pour utiliser le projet LoRaMAC-node dans notre projet nous avons téléchargé le .zip du projet de la branche master en **version 4.4.2**.

Installation de Stlink
----------------------

Le St-link est un programme permettant d'avoir accés au debuger des cartes conçuent par St-microelectronics, il permet entre autre de charger des programmes dans les cartes.

.. code-block:: bash

    git clone https://github.com/texane/stlink.git
    make release
    cd build/Release
    sudo make install
    sudo ldconfig

Installation de LoRaMAC-node
----------------------------

Après avoir extrait le zip téléchargé précédement placez-vous dans le dossier LoRaMac-node-master.

.. code-block:: bash

    mkdir build
    cd buid
    BOARD=B-L072Z-LRWAN1
    cmake -DCMAKE_TOOLCHAIN_FILE="cmake/toolchain-arm-none-eabi.cmake" -DBOARD="$BOARD" -DAPPLICATION="LoRaMac" -DCLASS="classA" -DACTIVEREGION="LORAMAC_REGION_EU868" ..
    make


.. [LoRaMAC-node] Projet permettant la mise en oeuvre d'un Noeud LoRaWAN sur une carte *B-L072Z-LRWAN1* [lien](https://github.com/Lora-net/LoRaMac-node/tree/master/Doc)


Envoyer un programme sur la carte
*********************************

Pour développer un programme pour la carte il faut écrire le programme dans le fichier *src/apps/LoRaMac/classA/B-L072Z-LRWAN1/main.c*.

Dans un premier temps, branchez la carte en USB par le port **CN7**.
Ensuite placer vous dans le dossier *build*
compiler le programme en utilisant la commande :

.. code-block:: bash

    make

Pour envoyer un programme :


.. code-block:: bash

    st-info --probe #Doit retourné : Found 1 stlink programmers...
    st-flash write src/apps/LoRaMac/LoRaMac-classA.bin  0x8000000

Recupérer la valeur d'un capteur
********************************

Le shield de cateur que nous utilisons contient différents capteurs, nous utiliserons que le capteur de température (HTS221). En se rapportant à la documentation du shield [#]_ nous voyons que le capteur est relié au bus I2C.
Pour communiquer sur un bus I2C nous avons besoins d'un mettre et d'un esclave, le maitre sera notre carte *B-L072Z-LRWAN1* et l'esclave le capteur. Pour trouver l'addresse de notre capteur nous avons consulté la documentation de celui-ci [#]_ il est apparue que le capteur avait 2 addresses, une pour la lecture **BF** et une pour l'ecriture **BE**.



.. [#] Lien de la documentation du Shield MEMS : https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html
.. [#] Lien de la documentation du capteur HTS221 : https://www.st.com/en/mems-and-sensors/hts221.html#overview
