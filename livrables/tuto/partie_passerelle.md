3. Réalisation et Tests
       
3.3. Passerelle

3.3.1. Surface d'attaque de la \textit{Box LoRa}

Concernant la \textit{Box LoRa}, nous avons affaire aux problématiques suivantes : comment faire pour garantir une compartimentation parfaite et complète de tous les services proposés ? 

Notre \textit{Box LoRa} peut fournir plusieurs services. Le service initial minimum est la réception de données provenant du noeud, sa traduction et son utilisation (afficher une donnée sur un moniteur, faire actionner un moteur, etc). Mais on peut penser qu'un fournisseur voudrait proposer plusieurs services avec une telle box. Par exemple, pour une société qui voudrait utiliser les communications en LoRa pour relever des données de ses capteurs, mais également avec un service de messagerie (mails) en interne, ou bien une zone de dépot et partage de documents sur la \textit{Box LoRa}, alors apparaissent certaines contraintes, notamment de sécurité.

En effet, il faut garantir les contraintes CIAN (Confidentialité, Intégrité, Authenticité, Non-répudiation) pour les données envoyées et reçues.

On peut donc voir que si chaque service n'est pas bien isolé des autres, ces contraintes pourraient ne pas être respectées respectées. Par exemple, si le compte utilisé pour la messagerie est un \textit{super-utilisateur}, il peut avoir les droit pour aller modifier des fichiers de configuration importants, faire arrêter le système, modifier les données, etc.

Ainsi, nous devons apporter des solutions pour protéger notre \textit{Box LoRa}

3.3.2. Solutions envisagées et solution retenue

Pour répondre à ces problématiques, nous avons étudié plusieurs solutions. 

Premièrement, nous avons considéré les modèles d'habilitation. Ces modèles d’habilitation permettent de garantir, au sein d’une entreprise par exemple, un contrôle d’accès performant sur les ressources et les services. Ils permettent également de rationaliser le processus de demande d’accès des utilisateurs.

Les principaux sont : 

    DAC (Discretionary Access Control)
    MAC (Mandatory Access Control)
    ABAC (Attribute Based Access Control)
    RBAC (Role Based Access Control).

Nous donnons ci-desssous une rapide description de leur fonctionnement : 

Dans le modèle DAC (ou Contrôle d’Accès Discrétionnaire), chaque personne est administrateur de ses ressources. Le fait de posséder un objet permet de modifier les droits d’accès sur celui-ci. 

Comme points positifs, on peut considérer : Facile à implémenter ;Offre une grande flexibilité ; Intégré à la plupart des systèmes d’exploitation.

Les points négatifs sont plus nombreux : Modèle inadapté à un système comportant un nombre important d’utilisateurs ; Ne reflète pas le flux réel de l’information dans un système, les informations autorisées pouvant être copiées d’un objet à un autre ; Aucune restriction ne s’applique à l’utilisation des informations lorsque l’utilisateur les a reçues ; Sujet à de nombreuses erreurs lors de l’attribution des autorisations par le propriétaire de l’objet.


Dans le modèle MAC, l’accès aux objets est restreint en fonction de la sensibilité des informations (classification) contenues dans les objets et du niveau d’autorisation de l’utilisateur de disposer d’informations d’une telle sensibilité. 
On aura par exemple : un technicien habilité niveau 3 ne pourra pas accéder à un dossier de niveau 5, mais il aura accès aux dossiers de niveau 1, 2 et 3.

Les niveaux proposés pour l'exemple sont les suivants : 

- Niveau 1 : néant
- Niveau 2 : Non classifié
- Niveau 3 : Confidentiel, non-classifié
- Niveau 4 : Secret, confidentiel, non-classifié
- Niveau 5 : Top secret, secret, confidentiel, non-classifié

Le principal point positif est que cette méthode offre un niveau hautement sécurisé d’administration aux sources d’information. En effet, une autorité centrale applique les décisions de contrôle d’accès, et non par le propriétaire individuel d’un objet (ressource). Et le propriétaire ne peut pas modifier les droits d’accès. 

Les points négatifs sont : Modèle très rigide. Il impose des restrictions sur l’accès des utilisateurs qui, conformément aux politiques de sécurité, ne permettent pas les modifications dynamiques. ; Inadapté aux systèmes repartis. ; Assez coûteux en étude, car il nécessite une planification prédéterminée pour être mis en oeuvre efficacement. ; Assez coûteux en exploitation. Après la mise en oeuvre, un mode de gestion complexe est nécessaire à cause de la mise à jour constante des étiquettes d’objet et de compte, pour collecter de nouvelles données.

Nous ne détaillerons pas les autres modèles d'habilitations.

Par rapport aux problématiques de sécurité définies plus haut, nous pensons que le modèle MAC est le plus adapté pour notre \textit{Box LoRa}. Nous choisissons donc ce modèle comme angle d'attaque.

Ainsi, nous pouvons proposer l'utilisation de deux modules intéressants qui semblent être adaptés : SELinux et AppArmor.
Ces deux logiciels - Linux Security Module (LSM), sont un moyen de mettre en oeuvre un système MAC. 

Concernant l'emploi de l'un ou l'autre, nous avons retenu les critères suivants : 

AppArmor n'est pas nativement installable sur Raspberry Pi, il faut faire de nombreuses modifications. SELinux est moins facile à configurer, mais à l'aide de nos cours de bases des OS, nous avons les connaissances pour ajouter un LSM au noyau de notre OS (cf. tutoriel en annexe). Suivant de nombreux conseils de collègues et de lectures sur Internet, nous choisissons de partir sur la solution SELinux.


