****************************
Utilisation de LoRaMac-node
****************************

Dans un premier temps, nous allons utiliser le projet LoRaMAc-node créé par Semtech pour utiliser notre carte B-L072Z-LRWAN1 comme nœud LoRaWAN.

Installation
############


Pour gagner du temps dans le développement du nœud, nous utilisons comme base un projet github [LoRaMAC-node]_ mettant en œuvre le LoRaWAN sur notre carte.
Nous développons le nœud à partir d'une distribution *Linux* basée sur *Arch Linux*, les dépendances requises sont : 

.. code-block:: bash

    cmake
    arm-none-eabi-gcc
    arm-none-eabi-newlibS221 : https://www.st.com/en/mems-and-sS221 : https://www.st.com/en/mems-and-sensors/hts221.html#overviewensors/hts221.html#overview
    openocd

Pour utiliser le projet LoRaMAC-node dans notre projet, nous avons téléchargé le .zip du projet de la branche master en **version 4.4.2**.
Installation de Stlink
----------------------

Le St-link est un programme permettant d'avoir accès au débuger des cartes conçues par STMicroelectronics, il permet, entre autres, de charger des programmes dans les cartes.
.. code-block:: bash

    git clone https://github.com/texane/stlink.git
    make release
    cd build/Release
    sudo make install
    sudo ldconfig

Installation de LoRaMAC-node
----------------------------

Après avoir extrait le zip téléchargé précédemment, placez-vous dans le dossier LoRaMac-node-master.
.. code-block:: bash

    mkdir build
    cd buid
    BOARD=B-L072Z-LRWAN1
    cmake -DCMAKE_TOOLCHAIN_FILE="cmake/toolchain-arm-none-eabi.cmake" -DBOARD="$BOARD" -DAPPLICATION="LoRaMac" -DCLASS="classA" -DACTIVEREGION="LORAMAC_REGION_EU868" ..
    make


.. [LoRaMAC-node] Projet permettant la mise en œuvre d'un Nœud LoRaWAN sur une carte *B-L072Z-LRWAN1* (https://github.com/Lora-net/LoRaMac-node/tree/master/Doc)


Charger un programme dans la carte
##################################

Pour charger le programme dans la carte nous utilisons St-Link, dans un premier temps brancher la carte à l'aide d'un câble USB à l'ordinateur.
Sur la carte, vous devez utiliser le port USB le plus éloigné de l'antenne.

.. code-block:: Bash

	st-info --probe	#Permet de verifier que la carte est recunnu par l'ordinateur
	#Placez-vous dans le dossier build créé précédement. 
	st-flash write build/src/apps/LoRaMac/LoRaMac-classA.bin 0x8000000

Pour lancer le programme, vous n'avez plus qu'a appuyer sur le bouton noir (RESET) de la carte.


Faciliter la compilation et éviter les erreurs
##############################################

Pour faciliter la compilation et le chargement du projet nous vous recommandons de faire un script dans le dossier build.

.. code-block:: Bash

	nano my-LoRa.sh
	#A l'intérieur écrivez les lignes suivantes
	BOARD=B-L072Z-LRWAN1
	cmake -DCMAKE_TOOLCHAIN_FILE="cmake/toolchain-arm-none-eabi.cmake" -DBOARD="$BOARD" -DAPPLICATION="LoRaMac" -DCLASS="classA" -DACTIVEREGION="LORAMAC_REGION_EU868" ..
	make

Maintenant pour mettre le programme sur la carte vous n'aurez plus qu'à la brancher et lancer la commande suivante.

.. code-block:: Bash

	./my-LoRa.sh


Configurer LoRaMAC-node
#######################

Nous vous recommandons d'utiliser dans un premier temps le programme *exemple* de LoRaMAC-node.
Pour cela, vous devrez utiliser les programmes se trouvant dans le dossier "LoRaWAN_securise/noeud/LoRaMac-node-master/src/apps/LoRaMac/classA/B-L072Z-LRWAN1/"

Le programme *main.c* est le programme principal, c'est dans celui-ci que vous aller créer votre programme personnel. Le fichier *Commissioning.h* contient les différentes variables nécessaire à une liaison LoRaWAN (DevEUI, AppKey ...).

Lorsque l'on commence un projet, vous devez configurer dans un premier temps le fichier *Commissioning.h*.

Dans nôtres cas nous utilisons une méthode de connexion APB donc nous devons configurer dans ce fichier, le mode de connexion, devAddr, AppSKey et NwkSKey.

Voici les valeurs que nous utilisons pour ces différentes clés :

* devAddr  =  0x00000000
* AppSkey  =  0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C 
* NwkSkey  =   0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C 

Pour configurer notre programme, cherchez les lignes suivantes et mettez les valeurs indiquées à la place des valeurs par défaut.

.. code-block:: C

	#define OVER_THE_AIR_ACTIVATION                            0
	// Définit le mode de connexion APB
	#define LORAWAN_DEVICE_ADDRESS                             ( uint32_t )0x00000000
	// DevAddr
	#define LORAWAN_NWK_S_ENC_KEY                              { 0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C }
	//NwkSKey
	#define LORAWAN_APP_S_KEY                                  { 0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C }
	//AppSKey


Enregistrez les modifications et lancer le programme à l'aide du script créé précédemment.