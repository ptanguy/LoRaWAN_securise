************************************************************************************
Tutoriel pour ajouter une layer SELinux à notre OS chirpstack-gateway-os via Yocto :
************************************************************************************

Connexion au serveur de compilation
###################################

Pour se connecter au serveur de compilation : 

.. code-block:: Bash

    numeroetudiant@m1-isc-os
    motdepasse

choisir un shell bash

.. code-block:: Bash

    bash


Problèmes rentrés
#################

Problème de téléchargement qui ne marche pas:

    Ajoutez le proxy: export http_proxy=http://ocytohe.univ-ubs.fr:3128

Problème Git et proxy

    git config --global http.proxy http://ocytohe.univ-ubs.fr:3128

Générer l'OS
############

Cloner le répertoire : 

    git clone https://github.com/brocaar/chirpstack-gateway-os



On se met dans notre répertoire > ~/projet/os/chirpstack-gateway-os/


On active l'environnement de build en faisant 

.. code-block:: Bash

    source oe-init-build-env


renvoit : 

    "You had no conf/local.conf file. This configuration file has therefore been created for you with some default values.
    You may wish to edit it, for example, select a different machine (target hardware). See conf/local.conf for more information as common configuration options are commented.

    You had no conf/bblayers.conf file. This configuration file has therefore been created for you with some default values. 
    To add additional metadata layers into your configuration please add entries to conf/bblayers.conf."


On se retrouve dans le dossier build

Ajouter la layer meta-selinux, dans le dossier source

.. code-block:: Bash

    git clone https://git.yoctoproject.org/git/meta-selinux

Aller éditer manuellement le fichier bblayers.conf dans le dossier build, pour l'ajouter

.. code-block:: Bash

    vim bblayers.conf
    i (entrer en mode insertion)

Ajouter à la fin du fichier, dans les guillemets : 


.. code-block:: Bash

    /home/numeroetudiant/projet/os/chirpstack-gateway-os/meta-selinux \
    echap
    :wq


Maintenant, on cherche à compiler nôtre image, avec la commande

.. code-block:: Bash

    bitbake core-image-minimal

Cependant, nous ne pouvons pas effectuer cette comande, car les modules dont dépend le projet chirpstack-gateway-os ne peuvent pas téléchargés, et bitbake en fait partie.

Le protocole ssh est bloqué par le seveur de compilation. Certains utilisent le protocole git qui lui aussi utilise le protocole ssh.
on a donc remplacé les url git par des url https qui n'utilisent pas le protocole ssh pour les télécharger.

On suit le cheminement du makefile : 

.. code-block:: Bash

    make submodules

Cependant, nous avons oublié de modifier également le fichier 

.. code-block:: Bash

    git submodule init
    git submodule => nous montre toutes les layers .git/modules/layers

On finit par tout télécharger à la main
On peut relancer la compilation

.. code-block:: Bash

    bitbake core-image-minimal

On obtient une erreur : 

    "Layer selinux is not compatible with the core layer which only supports these series: thud (layer is compatible with zeus)"

On va donc copier notre répertoire ailleurs pour faire des essais et essayer de changer de version de yocto : nous étions sur rocko et nous passons à zeus : 

.. code-block:: Bash

    git checkout -b zeus origin/zeus

Cependant erreur, nous travaillons sur le git du projet chirpstack-gateway-os donc incompatible pour les commandes avec la version zeus.


on passe tout le monde sur warrior (avant dernière version disponible et fonctionnelle)

On doit changer thud dans le fichier .gitmodules

exemple : 

    [submodule "layers/bsp/meta-raspberrypi"]
	path = layers/bsp/meta-raspberrypi
	url = git://git.yoctoproject.org/meta-raspberrypi
	branch = thud

On passe sur la branche warrior

.. code-block:: Bash

    branch = warrior

Rappatrier l'image sur la machine hôte

.. code-block:: Bash

    scp -r numeroetudiant@m1-isc-os:/<source>/ ./<cible>/

Flasher l'image sur carte SD

.. code-block:: Bash

    dd if=<source> of=<cible> bs=<taille des blocs> skip= seek= conv=<conversion>

Prêt à être utilisé sur la box LoRa. Les commandes d'administration peuvent s'effectuer via un terminal directement sur la box LoRa.