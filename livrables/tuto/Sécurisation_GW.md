Tutoriel pour la sécurisation point à point de la passerelle.



se connecter au serveur de compilation : 

    numeroetudiant@m1-isc-os
    motdepasse

choisir un shell bash

    bash

Problème de téléchargement qui ne marche pas:

    Ajoutez le proxy: export http_proxy=http://ocytohe.univ-ubs.fr:3128

Problème Git et proxy

    git config --global http.proxy http://ocytohe.univ-ubs.fr:3128

cloner le répertoire : 

    git clone https://github.com/brocaar/chirpstack-gateway-os


/!\ penser à faire une doc sur comment créer un OS qu'on peut flasher sur carte SD pour le mettre dans la rasp
cf tp.pdf ex3 dans séquence de démarrage avec uboot


on se met dans > ~/projet/os/chirpstack-gateway-os/


on active l'environnement de build en faisant > source oe-init-build-env

renvoit : 

"
you had no conf/local.conf file. This configuration file has therefore been created for you with some default values.
You may wish to edit it, for example, select a different machine (target hardware). See conf/local.conf for more information as common configuration options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been created for you with some default values. 
To add additional metadata layers into your configuration please add entries to conf/bblayers.conf.
"

on se retrouve dans le dossier build

Ajouter la layer meta-selinux, dans le dossier source

    git clone https://git.yoctoproject.org/git/meta-selinux

Aller éditer manuellement le fichier bblayers.conf dans le dossier build, pour l'ajouter

    vim bblayers.conf
    i (entrer en mode insertion)
    ajouter à la fin du fichier, dans les guillemets : 
    /home/numeroetudiant/projet/os/chirpstack-gateway-os/meta-selinux \
    apuyer sur echap
    :wq


Maintenant, on cherche à compiler notra image, avec la commande

    bitbake core-image-minimal

Cependant, nous ne pouvons pas effectuer cette comande, car les modules dont dépend le projet chirpstack-gateway-os ne peuvent pas téléchargés, et bitbake en fait partie.

résolution : 

on a changé les sources dans le fichiers .gitmodules internet.
hypothèse 1 : ssh bloqué par le seveur de compilation
certains utilisent le protocoles github qui lui utilise le protocole ssh
on a donc remplacé les url git par des url https qui n'utilisent pas le protocole ssh pour les télécharger

on suit le cheminement du makefile : (détailler le contenu du fichier)

    make submodules

