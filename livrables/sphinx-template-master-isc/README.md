# README documentation Sphinx Master ISC UBS SSI
 
## Guide création documentation avec Sphinx

La création et la génération de documentation est un point important d'un projet
qu'il ne faut pas négliger.
La méthode employé pour générer de la documentation dépendera probablement de
l'environnement dans lequel vous êtes.
Ici nous vous proposons une très courte introduction à la génération de documentation à
l'aide de Sphinx.
Sphinx (http://www.sphinx-doc.org/en/master/index.html) est un outil qui permet de générer un document dans différents format
(html, pdf, ...) à partir de fichiers écrits dans un format
appelé ReStructuredText (format Mardown aussi possible).
L'avantage des fichiers textes pour écrire la documentation est qu'ils peuvent
être intégrer au système de gestion de version de votre projet.
Ainsi, selon votre flux de travail (workflow), vous pouvez livrer une version de
documentation suivant la version de la livraison de votre projet.
Vous pouvez donc aussi conserver et maintenir un historique. 


### Démarrez avec Sphinx

Sous Debian vous pouvez installer Sphinx en tapant dans un terminal:


```bash
$ sudo apt install python3-sphinx
```

Ou sinon en utilisant le gestionnaire de paquets Python PyPi:

```bash
$ pip install -I sphinx
```

### Partir de zéro

Pour configurer l'environnement de documentation

```bash
$ mkdir docs
$ sphinx-quickstart
```
Faites la configuration comme vous le souhaitez.
Le seul conseil que nous pouvons faire lors de la configuration est de séparer les répertoires
build et source.

### Partir d'un exemple fourni

Un exemple est disponible dans ce répertoire.
Pour tester vous pouvez faire dans un terminal:

```bash
$ make html
$ firefox build/html/index.html
```

