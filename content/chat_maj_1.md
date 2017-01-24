Author: Dr_c0w
Date: 2015-01-23
Title: Chat v1.0.1
Category: Mises-à-jour
Tags: chat, mises-à-jour
lang: fr
Status: draft

##Version 1.0.1 de Chat

Bonjour à tous,

J'ai apporté quelques améliorations à mon projet [*Chat*]({filename}./chat.md) qui, je
rappelle est un programme de discussion instantanée développée dans le cadre
d'une messagerie interne pour la société 
[Agence Etoile](http://www.agence-etoile.com). 

J'ai tout d'abord corrigé quelques bogues au niveau de la confirmation
de la fermeture de fenêtres de discussion qui n'apparaissait tout le
temps, mais plus quelque chose comme une fois sur deux.

J'ai également apporté des modifications au niveau de la réception
des messages privés qui passaient une ligne de trop.

Mais la plus grosse partie de la mise à jour est au niveau de la 
notification lors de la réception de nouveau message. Ainsi qu'une
grosse mis-à-jour de sécurité avec la mise en place de mot de passe
comme l'entreprise concernée me l'a demandé.

##Les mots de passe

Les mots de passe fonctionnent de la façon suivante:

- L'administrateur crée un nouvel utilisateur. Il doit
donc ici rentrer le nom que devra utiliser l'utilisateur
ainsi que __son mot de passe__. A noter qu'il est aussi 
possible pour l'administrateur __uniquement__ de modifier
le mot de passe d'un utilisateur.

- Le mot de passe est ensuite enregistré, ou plutôt un *hash*
du mot de passe (voir [le cours sur le *hachage*]({filename}./hachage.md)).

- Lorsque l'utilisateur se connecte, il doit rentrer ce mot de passe. 
Le hash est ensuite calculé puis envoyé au serveur. Si les deux 
valeurs concordent, alors l'utilisateur sera authentifié et sera
donc bien connecté au serveur.


##Le système de notifications

Lorsque l'utilisateur reçoit un message, il n'avait pour l'instant
pas de moyen de savoir si il avait lu tous ses messages. La seule
façon était de regardé chacune de ses fenêtres de discussion régulièrement.

Maintenant, si la fenêtre de discussion n'est pas active, l'icône dans la
barre des tâches clignote (en théorie en orange) et une petite notification
apparaît sur la droite avec le message, et le nom de la personne qui l'envoie.
Si il s'agit d'un groupe, le nom du groupe sera affiché, sinon, ce sera le 
nom de l'utilisateur qui apparaîtra à nouveau en titre de notification.


Si le programme n'est pas disponible au téléchargement, c'est pour la simple
et bonne raison que le programme n'est pas encore officiellement terminé.

D'autant plus que je pense encore ajouté quelques petits outils pratiques
notamment côté administration avec une interface spéciale qui permet de se
connecter au serveur en tant qu'administrateur et de pouvoir modifier
la liste blanche, d'avoir accès aux utilisateurs connectés et de voir les
groupes qui ont été créés.

Je tiens à préciser __qu'il n'est pas possible d'accéder aux messages envoyés
que ce soit pour les administrateurs ou pour les autres utilisateurs__ !


Côté utilisateur, je compte également ajouté quelques nouveautés intéressantes 
et colorées. Je parle de l'affichage de smiley. C'est une fonctionnalité assez
simple à implémenter, et ça permet un joli rendu visuel pour les utilisateurs.


Vous aurez donc la chance de voir de nouveaux articles paraître au sujet de
cette messagerie instantanée, et il y a de fortes chances pour que je l'adapte
à un usage plus ouvert et plus général.

En attendant, je vous souhaite une bonne soirée, et une bonne fin de mois
de janvier.
