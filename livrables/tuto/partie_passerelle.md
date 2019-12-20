3. Réalisation et Tests
       
3.3. Passerelle

3.3.1 Surface d'attaque de la \textit{Box LoRa}

Concernant la \textit{Box LoRa}, nous avons affaire aux problématiques suivantes : comment faire pour garantir une compartimentation parfaite et complète de tous les services proposés ? 

Notre \textit{Box LoRa} peut fournir plusieurs services. Le service initial minimum est la réception de données provenant du noeud, sa traduction et son utilisation (afficher une donnée sur un moniteur, faire actionner un moteur, etc). Mais on peut penser qu'un fournisseur voudrait proposer plusieurs services avec une telle box. Par exemple, pour une société qui voudrait utiliser les communications en LoRa pour relever des données de ses capteurs, mais également avec un service de messagerie (mails) en interne, ou bien une zone de dépot et partage de documents sur la \textit{Box LoRa}, alors apparaissent certaines contraintes, notamment de sécurité.

En effet, il faut garantir les contraintes CIAN (Confidentialité, Intégrité, Authenticité, Non-répudiation) pour les données envoyées et reçues.

On peut donc voir que si chaque service n'est pas bien isolé des autres, ces contraintes pourraient ne pas être respectées respectées. Par exemple, si le compte utilisé pour la messagerie est un \textit{super-utilisateur}, il peut avoir les droit pour aller modifier des fichiers de configuration importants, faire arrêter le système, modifier les données, etc.

Ainsi, nous devons apporter des solutions pour protéger notre \textit{Box LoRa}

