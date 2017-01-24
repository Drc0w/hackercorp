Title: SSH & Git
Author: Dr_c0w
Date: 2016-01-31 12:59
Category: Cours
tags: ssh, git, cours
lang: fr
Status: draft

<center>
  <img style="border: 2px solid black" alt="Git" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/2000px-Git-logo.svg.png">
</center>

##Introduction

Bonjour à tous,

Je vais vous faire un cours sur SSH et Git. Dans ce cours, nous allons voir
comment se servir de SSH, et son intégration au logiciel de versionnement Git.

Ce cours réunit SSH et Git, qui sont deux notions bien distinctes, pour une
raison simple : il est possible d'utiliser Git via des accès SSH.

##SSH

###Configuration partie client

Pour générer une bonne clef SSH, vous pouvez utiliser la commande suivante:

```
ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_key
```

Les  options utilisées:

- __-t__ permet de préciser le type de clef que l'on veut générer, en
  l'occurence, on génère une clef du type RSA
- __-b__ permet de spécifier le nombre de bits dans la clef, on choisit donc de
  générer une clef de __4096__ bits
- __-f__ permet de préciser le nom, et le répertoire, pour enregistrer la clef.
  En l'occurence, notre clef s'appellera **my_key** et situera dans le dossier
  __.ssh__ dans le répertoire __home__ de l'utilisateur.

Une fois la ligne de commande lancée, __ssh-keygen__ vous demande de taper une
*passphrase*. Cette *passphrase* vous permet de sécuriser l'utilisation de
votre clef. À chaque fois que vous voudrez utiliser votre clef SSH, vous devrez
retaper cette *passphrase*. Ce procédé permet de sécuriser vos connexions SSH
directement sur la clef.

Pour utiliser votre clef, vous devez modifier, ou créer si il n'existe pas, le
fichier __.ssh/config__ :

```
Host ssh.hackercorp.eu
User Dr_c0w
IdentityFile ~/.ssh/my_key
```

Grâce à ce fichier, vous pouvez préciser la clef à utiliser lors d'un accès à
l'hôte. Une fois votre configuration faite, vous devez vous assurer que votre
clef est dans le fichier __authorized_keys__ côté serveur.

###Configuration partie serveur

Du côté du serveur, de base sur les distributions classiques, SSH est configuré
pour des accès avec le nom de l'utilisateur et le mot de passe du compte. Il
est cependant possible de modifier les paramètres de SSH pour que les accès se
fassent via des clefs pré-configuré. Ainsi, il vous suffira de taper la
commande suivante pour vous connecter directement à un serveur :
```
ssh ssh.hackercorp.eu
```

Comme nous avons SSH pour accéder au compte __*Dr\_c0w*__, il est inutile de le
préciser dans la commande.

Pour configurer le serveur pour ne recevoir que des connexions de clef connus,
et ne pas passer par le nom de compte et le mot de passe associé, il suffit de
modifier les lignes suivantes dans le fichier __*/etc/ssh/sshd_config*__
```
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile %h/.ssh/authorized_keys
PasswordAuthentication no
```

Il faut être __sudo__ pour effectuer cette opération. Une fois cette opération
terminée, il vous suffit d'ajouter votre __clef publique__ dans le fichier
*~/.ssh/authorized_keys*.

Et voilà, vous pouvez maintenant vous connecter à votre session directement
grâce à votre clef SSH.

##Git

Dans la prochaine partie, nous allons voir comment configurer les gestionnaires
GitHub ou BitBucket avec votre clef SSH plutôt qu'avec votre compte. Nous
verrons également comment gérer un _repository_ Git et les différentes
commandes liées à Git.

###Configuration de GitHub pour utiliser une clef SSH

###Configuration de BitBucket pour utiliser une clef SSH

###Gérer proprement son Git

####Configurer son Git

Nous verrons dans un premier toutes commandes disponibles sous Git que vous
serez amené à utiliser régulièrement. Enfin, nous verrons comment les utiliser
_correctement_ avec différentes stratégies de gestion de Git.

####Pull

La commande _pull_ permet de récupérer les dernières modifications disponibles
sur le _repository_ distant. Cela permet de se maintenir à jour sur la version
locale. Il existe plusieurs façons de l'utiliser :
```
git pull
git pull remote branch
git pull --rebase remote branch
git pull -r remote branch
git pull --tags remote branch
```

Dans l'ordre:

- On exécute un _pull_ classique, à savoir récupérer les modifications sur la
  _remote_ principale et la branche courante

- On exécute un _pull_ classique mais cette fois en précisant la _remote_ et la
  branche que l'on veut mettre à jour. Si la branche préciser n'est pas la
  branche courante, Git affichera une erreur.

- On exécute un pull, cependant si la version de la _remote_ est plus à jour,
  il n'y aura pas de conflit, cela permet d'appliquer les commits manquant sur
  la branche en cours en limitant le risque de conflit.

- Même chose qu'au dessus.

- Cette commande permet de mettre à jour les tags qui ont été mis. La notion de
  tag sera expliqué plus tard dans le cours.

Ainsi, il est possible d'utiliser plusieurs syntaxes pour la commande _pull_,
il est préférable d'utiliser la 3ème ou la 4ème pour limiter les risques de
conflits et les _merge_ inutile. De même, la notion de _merge_ sera expliquée
plus tard.

####Add

La commande _add_ permet d'ajouter un fichier au _repository_. Cela permet
aussi d'ajouter des modifications qui pourront ensuite être appliquées. Ainsi,
si un utilisateur du _repository_ modifie ou ajoute un fichier dans le dossier
courant ou dans un sous-dossier du _repository_, lancer la commande _add_
permet d'archiver ses modifications. Il pourra ensuite les _commit_.

Utilisation :
```
git add file
git add file1 file2 ...
```

####Remove

La commande _add_ ne serait rien sans sa paire _remove_. En effet, il est
possible de supprimer un fichier du _repository_. Chose qui peut paraître
étrange, mais cette modification doit être suivie d'un commit.

Utilisation :
```
git rm file
git rm file1 file2 ...
```

####Move

De même que _remove_, la commande _move_ est utilisée pour déplacer des
fichiers dans un répertoire. Elle doit être, elle aussi, suivie d'un commit
pour que le changement soit appliquée.

Utilisation :
```
git mv file1 file2
git mv file1 dir/
```

Cette commande s'utilise de la même façon que la commande _mv_ sous Linux.

####Status

La commande _status_ permet de voir les modifications qui ont été effectuées
sur la branche courante.

Il existe plusieurs status:

- ___To be committed___ : Le fichier a été modifié ou ajouté, et déjà ajouté au
  _repository_

- ___Modified___ : Le fichier était déjà dans le _repository_ et suivi par Git,
  mais a été modifié sans avoir été _commit_ pour le moment.

- ___Untracked___ : Le fichier concerné n'a jamais été inclus dans le
  _repository_.

Utilisation :
```
git status
```

####Diff

####Commit

####Push

####Tag

####Remote

####Init

####Branch

####Checkout

####Rebase

####Merge

####Delete a branch

####Logs
