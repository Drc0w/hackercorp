Title: EtoileMessenger
Author: Dr_c0w
Date: 2015-03-31 09:29
Category: Projets
Slug: chat
Lang: fr
tags: chat


##Présentation du projet de chat

Je viens de finir de déboguer les derniers bogues que j'ai rencontré dans mon 
programme de tchat, projet que j'ai réalisé en C#. Le but était de mettre en 
place une messagerie instantanée pour une [entreprise](http://agence-etoile.com). 
J'ai basé le projet sur  une communication Client-Serveur, mais je ne vous 
cacherai pas que ce projet n'a pas été de tout repos, malgré le fait que 
j'avais déjà fait un système de messagerie instantanée, mais bien moins avancé 
que celui-ci. La particularité est qu'ici, il est possible de créer des groupes 
privés et des groupes publics mais également de créer des discussions privés, 
contrairement à ma première messagerie instantanée qui ne comportait qu'un 
seul et unique groupe sur lequel tout le monde se retrouvait. Cependant, même 
si ma première création restait très basique, certaines notions dont je me 
suis servi m'ont beaucoup aidé pour réaliser le projet au stade auquel il est 
arrivé, entre autre au niveau du travail sur les threads (j'ajouterai 
probablement un cours à ce sujet prochainement). Bien que certaines de ces 
notions m'ont également posés quelques soucis, comme les opérations entre 
thread justement bien que celles-ci soient fortement simplifiées en C#, 
peut-être même parfois trop, mais je ne rentrerai pas dans les détails 
dans cette présentation.

Au niveau du serveur, les choses ont été plus simples puisque j'ai pu appliqué 
les notions que j'avais rencontrées avec JukeBox notamment au niveau du travail 
sur les interfaces (et ça m'a d'ailleurs donné quelques petites idées d'
améliorations pour [JukeBox]({filename}jukebox.md).

##Interfaces
###Partie Serveur

Au niveau du serveur, rien de plus simple:

* une interface facile à utiliser qui fait ce qu'on lui demande comme afficher 
les informations principales (connexions, déconnexions, création de groupe, 
mais aussi utilisateurs connectés, accès à la liste blanche, et groupes créés)

* un système de logs pour pouvoir s'y retrouver et archiver les informations 
du serveur

* un système de liste blanche pour ne permettre que à certains utilisateurs 
de se connecter au serveur

* Il est possible de modifier la liste blanche depuis l'interface du serveur, 
mais aussi de kicker ou de bannir un utilisateur depuis la liste des 
utilisateurs. En revanche, il n'est pas possible de modifier les informations qui 
concernent les groupes.

* Il est possible pour l'administrateur de modifier les mots de passe des 
utilisateurs. De même, lors de l'ajout d'un utilisateur à la liste blanche,
le programme demande la définition d'un mot de passe.

###Partie Client

Au niveau du client, c'est un peu plus compliqué. En effet, l'interface se 
décompose en plusieurs fenêtres:

* une fenêtre de connexion qui enregistre et permet donc d'afficher la dernière 
configuration utilisée

* une fenêtre principale où apparaissent les utilisateurs connectés ainsi que 
les groupes qui sont accessibles par l'utilisateur

* lorsque l'utilisateur choisit de rejoindre un groupe, soit en double-cliquant 
dessus dans l'arbre affiché dans la fenêtre principale, soit en acceptant une 
invitation, une nouvelle fenêtre s'ouvre dans laquelle il est possible de 
tchater avec les autres membres du groupe et de voir les membres faisant partie 
de ce groupe. Il est possible d'inviter d'autres utilisateurs à rejoindre le 
groupe et de modifier la police et la couleur pour les deux boîtes de textes.

* il y a également les fenêtres pour inviter des nouveaux utilisateurs à 
rejoindre un groupe, dans laquelle on peut voir les utilisateurs connectés 
qui n'appartiennent pas au groupe.

* et bien évidemment une fenêtre pour créer un groupe, avec le nom, le type 
de groupe (public ou privé) et les membres à inviter

* et enfin les fenêtres de discussion privée sont similaires à celles des 
discussions de groupe, à la différence qu'il n'est pas possible d'inviter 
de nouveaux utilisateurs à la discussion.

##Gestion des groupes

Le principal obstacle rencontré lors de la création de groupes était le suivant: 
il fallait pouvoir créer plusieurs groupes pouvant avoir le même nom mais aussi 
être capable d'identifier les groupes. Après avoir cherché une solution pendant 
5 petites minutes, l'idée de procéder à un hachage 
([voir cours sur le hachage]({filename}hachage.md)) du nom m'a paru être une 
évidence. Ainsi, il suffit d'envoyer une seule fois le nom du groupe, ensuite 
tout se fait à partir de l'identifiant unique pour chaque groupe, d'autant 
plus que ma fonction de hachage permet la création d'identifiant à 5 caractères.

Bon tout ça c'est bien beau, mais je vais vous expliquer un peu comment 
fonctionne mon principe de groupes. Tout d'abord, l'utilisateur va créer un 
groupe, cela envoie une instruction au serveur comme quoi un groupe a été 
créé. A ce moment là, aucun identifiant n'a été calculé. Ensuite, le 
serveur envoie au client que son groupe a bien été créé, et lui permet 
ainsi d'ouvrir la fenêtre de discussion. Les membres qui ont été invités 
vont recevoir une invitation, et si le groupe est public, les autres clients 
connectés vont recevoir l'information et afficher ce groupe dans l'arbre 
principal.

Ensuite, lorsque chaque utilisateur envoie un message, l'identifiant est ajouté 
au message pour que le serveur sache à qui il doit être redistribué.

##Gestion des messages privés

Les messages privés sont encore une fois basé sur le même principe, à la 
différence que lors de l'envoi du message, au lieu d'un identifiant, le client 
ajoute l'expéditeur et le destinataire, cela permet au serveur de savoir à qui 
le message doit être distribué, et au client destinataire d'en connaître la 
provenance.

La seule particularité, qui peut paraître assez bizarre d'ailleurs, c'est que 
les clients ne sont pas autonomes, ainsi un message privé transitera par le 
serveur et sera achimené jusqu'au destinataire... mais aussi jusqu'à 
l'expéditeur. Le client dépends totalement du serveur. C'est pourquoi j'ai 
rencontré pas mal de difficultés notamment au niveau de la création des fenêtres.

##Notifications

J'ai récemment ajouté un système de notifications à mon projet. En effet,
lors de la réception d'un message lorsque la fenêtre n'est pas au premier
plan, elle se met à clignoter. La barre qui lui correspond dans la barre des
tâches clignote également.

De plus, j'ai ajouté un icône qui apparaît dans la barre des tâches et qui
se charge d'afficher le contenu du message avec le nom de l'expéditeur, le nom
de la conversation et le contenu du message. Cela permet à l'utilisateur
d'avoir un aperçu du message qu'il vient de recevoir sans avoir à changer de
fenêtres et sans arrêter ce qu'il est actuellement en train de faire.

##Sécurité

Evidemment, sans sécurité, toutes personnes sachant comment se connecter au 
serveur est capable de récupérer des informations publiques mais aussi 
d'envoyer des commandes au serveur pour pouvoir voir ce qu'il se passe un peu 
partout, et il serait même possible d'effectuer des actions à la place du vrai 
client, ce qui pourrait causer du tort. C'est pourquoi j'ai intégré mon propre 
système de sécurité à ce projet. Bien évidemment, mon système est loin d'être 
infaillible mais constitue une première défense. Il est basé sur le principe 
de la rotation selon une certaine valeur en fonction de la position de la lettre 
dans le message et de la longueur du message. J'applique en plus de cela une 
clef de sécurité déterminée lors du lancement du serveur. La clef est partagée 
lors de la connexion du client

Côté sécurité aussi il y a du nouveau. J'ai ajouté la gestion des mots de
passe pour éviter l'usurpation d'identité. Pour éviter l'envoi des mots de
passe en clair, j'utilise un algorithme de hachage (*oui, encore*). Cependant,
je n'ai pas utilisé celui que j'ai conçu pour la gestion des groupes étant
donné que je ne sais pas à quel point il est fiable au niveau des collisions.
J'ai préféré l'utilisation d'un MD5 pour l'authentification. Le client envoi
donc un hash du mot de passe qu'il a entré. Le serveur compare ensuite ce hash
à celui contenu dans sa base de donnée. Si les deux données concordent, alors
l'utilisateur est authentifié.

Je travaille actuellement sur les changements de mot de passe. Le principe est
simple. Il suffit d'envoyer le hash d'un nouveau mot de passe et de l'enregistrer.
Le problème encore une fois est qu'il ne faut pas que n'importe qui puisse changer
un mot de passe. Il y a donc encore une fois un problème basé sur l'identité que
je ne sais pas résoudre pour l'instant.

##Traitement des commandes

Comme je l'ai dit dans la partie sur la sécurité, si les messages sont envoyés 
en clair, il est possible pour tout utilisateur connaissant un minimum mon 
architecture de semer un peu la zizanie. En revanche, il lui sera impossible 
d'envoyer des commandes à exécuter à un client en particulier. En effet, il 
y a les commandes qui sont reconnus par le serveur, et celles qui sont reconnus 
par le client, en général conséquence l'une de l'autre. Par exemple, lorsque 
l'utilisateur créé un groupe, le serveur recevra une commande qui sera 
différente de celle qu'il enverra aux clients pour les informer de cet évènement.

##Conclusion

C'est un projet qui a été très intéressant et pendant lequel j'ai appris 
énormément de choses, et bien sûr je continuerai à en apprendre puisque je 
vais maintenir ce programme à jour et sans doute en faire une version plus 
générale que la version faite pour l'entreprise qui l'a commandé.

Comme je l'ai dit dans cet article, j'avais déjà touché à la programmation 
d'une messagerie instantanée mais pas de façon aussi avancée, aussi je trouve 
que certaines fonctions manquent encore, et je compte bien y remédier. J'ai 
déjà des idées plein la tête, mais je vais d'abord me concentrer sur la 
correction de bugs puisqu'il s'agit de la première version que je release, 
et par définition, il y aura forcément des éléments à améliorer, mais je le 
ferai avec plaisir et c'est un grand honneur pour moi d'avoir pu réaliser 
ce projet.

###Modifications prochaines

Voici une petite liste des quelques idées que j'ai en tête pour modifier mon
projet:

* Les changements de mot de passe

* Ajout de smileys

* Ajouter un statut *est en train d'écrire* lorsque qu'un utilisateur tape un
message

* Ajouter un menu d'options qui regrouperaient plusieurs options. Une majorité
seraient présentes dans la fenêtre principale, d'autres dans les conversations.
