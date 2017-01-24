Title: JukeBox
Author: Dr_c0w
Date: 2015-01-18 15:00
Category: Projets
lang: fr
traduction: false
tags: jukebox

##Présentation de JukeBox

JukeBox est un petit programme capable de lire des fichiers audio encodés au
format MP3 ou WAV. Il est fait en Windows Form et est assez intuitif.

###Ouverture de fichier

Il y a plusieurs façons d'ouvrir un fichier: soit en utilisant
dans le menu déroulant "Ouvrir un fichier" ou l'association de touches
"CTRL + O", "Ouvir un dossier" ou "CTRL + F", ou encore "Ouvrir les sous dossiers"
ou "CTRL + SHIFT + F". Cette dernière option permet d'explorer l'arborescence 
du dossier d'un niveau inférieur pour y récupérer tous les fichiers que le
programme pourra lire. Cette fonctionnalité est assez pratique lorsque 
vous avez toute une discographie, ou une association de plusieurs albums
d'un artiste pour tous les ouvrir. Une fois l'ouverture terminée, le programme
va afficher chacun des dossiers qu'il a exploré avec le contenu exploitable
dans un arbre affiché à l'écran.

###Lecture

Pour lire un fichier, il suffit de double-cliquer sur un noeud "album".
Cela permet de lancer la lecture de tout l'album. Double-cliquer sur une 
chanson permet de l'ajouter à la fin de la liste. Tandis que lancer la
lecture sans avoir sélectionné de morceaux permet de tous les lancer à la
suite organisé par apparition dans l'arbre.

Pendant la lecture, il est possible de se déplacer dans le fichier grâce
à une barre de progression. 

Deux boutons permettent également de passer aisément d'une musique à la 
suivante ou la précédente.

Il est aussi possible de lire la liste en mode aléatoire. Pour ceux qui sont
intéressés par le principe algorithmique de mon algorithme, vous pouvez 
consulter [ce lien]({filename}randomisation.md).

###Affichage des informations de l'album

J'ai implémenté quelques features, dont certaines sont inutiles, lors de la
lecture de fichier. En effet, il est possible, grâce à l'interface "Album",
d'afficher la pochette de l'album, ainsi que certaines informations qui 
concernent le fichier en lecture. De même, quelques effets ont été implémentés
sur la pochette: plusieurs filtres peuvent être appliqués (*"pinkify"*, 
*"greyscale"*, *binarisation*).

##Remerciements

Pour ce projet, j'ai utilisé la bibliothèque [NAudio](naudi.codeplex.com), 
qui permet la lecture de fichier audio en C\#. Donc je remercie sincèrement 
l'auteur de cette bibliothèque ainsi que ses contributeurs.

J'ai également utilisé la bibliothèque [TagLib\#](https://github.com/mono/taglib-sharp/) pour la lecture de tags des
fichiers, notamment ID3. Donc une fois encore, je remercie les auteurs de cette
bibliothèque ainsi que les contributeurs.
