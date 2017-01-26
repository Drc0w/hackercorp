Title: Serveur Minecraft
Author: JeKo
Date: 2015-03-29 19:00
Category: Tutoriels
lang: fr
traduction: false
tags: tutoriels, minecraft

<center><img style="border: 2px solid black" alt="Minecraft" src="/images/minecraft-02-700x393.jpg"></center>

Dans ce tutoriel je vais vous montrer la procédure à suivre afin d'installer un serveur Minecraft sur son ordinateur (ou serveur perso) tournant sous Linux. Pour ma part, mon serveur tourne sous la distribution Debian Wheezy 7.8. Mon serveur est en réalité une petite "board" (type Raspberry Pi) disposant d'un processeur ARMv7 de 4 cœurs @ 1,3GHz ainsi que de 2Go de RAM. Toutes les données sont stockées sur un disque dur SDD de 20Go. 
J'utilise donc un serveur loin d'avoir toute la puissance d'un serveur "classique", il a néanmoins l'avantage d'avoir une faible consommation électrique et un encombrement minime.<br />
Suivez le guide pour la suite de la procédure :-)


#Spigot
###Installation de Java
Vous devez d'abord télécharger cette version de Java `jdk-8u33-linux-arm-vfp-hflt.tar.gz`, elle disponible à l'adressse suivante : http://www.oracle.com/technetwork/java/javase/downloads/jdk8-arm-downloads-2187472.html

Pour extraire et installer le paquet Java :

    tar zxvf jdk-8u33-linux-arm-vfp-hflt.tar.gz -C /opt

Lorsque vous installez Java manuellement comme l'on vient de le faire, il faut à chaque fois passer par le chemin d'accès de Java pour lancer un programme. Ainsi si je voulais par exemple voir la version de Java, je serai obligé de faire la commande suivante :

    /opt/jdk1.8.0_33/bin/java -version
    java version "1.8.0_33"

On va donc mettre à jour les correspondances pour qu'on puisse par la suite utiliser la commande `java` depuis n'importe quel dossier :

    update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_33/bin/java 100
    update-alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_33/bin/javac 100

A présent, je vérifie que la commande `java` fonctionne bien. Exemple : 

    java -version
    java version "1.8.0_33"
    Java(TM) SE Runtime Environment (build 1.8.0_33-b05)
    Java HotSpot(TM) Client VM (build 25.33-b05, mixed mode)

###Installation de Spigot
La suite du tutoriel va porter seulement sur l'installation de Spigot. Je vous propose de créer un dossier qui contiendra tous les fichiers nécessaires à son bon fonctionnement.

    mkdir Spigot
    cd Spigot

Il faut savoir qu'actuellement la distribution de serveurs alternatifs au serveur officiel est interdite. Pour installer Spigot nous allons donc d'abord devoir le compiler à l'aide d'un utilitaire qu'ils fournissent :

    wget -O BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar

On configure aussi Git que vous devez avoir préalablement installé

    root@server:~/Spigot# git config --global --unset core.autocrlf
    
 Pour compiler Spigot, il faut simplement lancer le programme `BuildTools.jar`. Je précise que cette étape peut prendre jusqu'à 30 minutes en fonction de la velocité de votre machine.

    root@server:~/Spigot# java -jar BuildTools.jar

Qui vous donne à la fin deux programmes compilés :

    Success! Everything compiled successfully. Copying final .jar files now.
    Copying craftbukkit-1.8-R0.1-SNAPSHOT.jar to /root/Spigot/.
      - Saved as craftbukkit-1.8.jar
        Copying spigot-1.8-R0.1-SNAPSHOT.jar to /root/Spigot/.
      - Saved as spigot-1.8.jar

Vous devriez avoir un dossier similaire à ça théoriquement :

    root@server:~/Spigot# ls
    BuildData  BuildTools.jar  BuildTools.log.txt  Bukkit  CraftBukkit  Spigot  apache-maven-3.2.3  craftbukkit-1.8.jar  spigot-1.8.jar  work

On va créer un script de lancement du programme :

    nano start.sh

Et on colle le code suivant :

    #!/bin/sh
    java -Xms512M -Xmx1024M -jar spigot-1.8.jar nogui

On enregistre le tout et on lance le script :

    ./start.sh

Il faut accepter les conditions d'utilisation du serveur en modifiant un fichier :

    nano eula.txt
    false -> true

On relance le serveur et cette fois il commence à générer la map et affiche un message une fois que tout est ok :

    ./start.sh
    [...]
    [16:00:00 INFO]: Done (312.152s)! For help, type "help" or "?"

Dernière chose pour que le serveur ne se coupe dès que vous fermez putty, il faut lancer le programme avec `screen`

    screen ./start.sh
    

Pour détacher le serveur de la console faire [ctrl + a] et ensuite appuyer sur [d].
Pour retourner sur le serveur, c'est :

    screen -r

Finito !
Prochainement je vous présenterai des plugins sympas pour votre serveur Spigot.

