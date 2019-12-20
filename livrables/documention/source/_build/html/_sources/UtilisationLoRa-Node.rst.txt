****************************
Utilisation de LoRaMac-node
****************************

Dans un premier temps nous allons utiliser le projet LoRaMAc-node créer par semtech pour utiliser notre carte B-L072Z-LRWAN1 comme noeud LoRaWAN.

Installation
############

Pour commencer, vous devez installer les dépendances nécessaires. Le nom des pacquet est sucéptible de varié en onctions de votre OS, dans nôtres cas nous utilisons ArchLinux

.. code-block:: Bash

	sudo pacman -Sy arm-none-eabi-gcc gdb-common cmake
	# Installation de St-Link version Open Sources
	git clone https://github.com/texane/stlink.git
	make release
	cd build/Release
	sudo make install
	sudo ldconfig


Ensuite il faut récupérer la branche master du projet sur github.

.. code-block:: Bash

	git clone https://github.com/Lora-net/LoRaMac-node.git
	cd LoRaMac-node-master
	mkdir build
	cd build 
	BOARD=B-L072Z-LRWAN1
	cmake -DCMAKE_TOOLCHAIN_FILE="cmake/toolchain-arm-none-eabi.cmake" -DBOARD="$BOARD" -DAPPLICATION="LoRaMac" -DCLASS="classA" -DACTIVEREGION="LORAMAC_REGION_EU868" ..
	make
	
Charger un programme dans la carte
##################################

Pour charger le programme dans la carte nous utilisons St-Link, dans un premier temps brancher la carte à l'aide d'un cable USB à l'ordinateur.
Sur la carte vous devez utiliser le port USB le plus éloigné de l'antenne.

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
Pour cela, vous devrez utiliser les programmes ce trouvant dans le dossier "LoRaWAN_securise/noeud/LoRaMac-node-master/src/apps/LoRaMac/classA/B-L072Z-LRWAN1/"

Le programme *main.c* est le programme principale c'est dans celui-ci que vous aller créer votre programme personnel. Le fichier *Commissioning.h* contient les différentes variables nécéssaire à une liaison LoRaWAN (DevEUI, AppKey ...).

Lorsque l'on commence un projet vous devez configurer dans un premier temps le fichier *Commissioning.h*.

Dans notres cas nous utilisons une méthode de connexion APB donc nous devons configurer dans ce fichier, le mode de connexion, devAddr, AppSKey et NwkSKey.

Voici les valeurs que nous utilisons pour ces différentes clés :

* devAddr  =  0x00000000
* AppSkey  =  0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C 
* NwkSkey  =   0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C 

Pour conigurer nôtre programme, cherchez les lignes suivante et métez les valeurs indiqué à la place des valeurs par défaut

.. code-block:: C

	#define OVER_THE_AIR_ACTIVATION                            0
	// Définit le mode de connexion APB
	#define LORAWAN_DEVICE_ADDRESS                             ( uint32_t )0x00000000
	// DevAddr
	#define LORAWAN_NWK_S_ENC_KEY                              { 0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C }
	//NwkSKey
	#define LORAWAN_APP_S_KEY                                  { 0x2B, 0x7E, 0x15, 0x16, 0x28, 0xAE, 0xD2, 0xA6, 0xAB, 0xF7, 0x15, 0x88, 0x09, 0xCF, 0x4F, 0x3C }
	//AppSKey


Enregistrez les modifications et lancer le programme à l'aide du script créé précédement.
