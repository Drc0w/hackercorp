Title: Découverte du C++
Author: Dr_c0w
Date: 2015-02-02 00:51
Category: Projets
Tags: découvertes, projets, cours
lang: fr
status: draft

#Introduction

Bien le bonjour à tous,

Cet article est un peu particulier dans la mesure où il va regrouper fiche de 
cours et présentation de projet. Je pense qu'il y aura d'autres articles un peu
dans le même style, donc j'opterai probablement pour l'archivage dans une autre 
catégorie. 

Comme je le disais, je vais profiter de cette article pour vous présenter ce que
j'ai appris très récemment sur le C++ avec un projet que nous avons appelé 
[*MyFirstRPG*](https://github.com/Drc0w/FirstRPG). 
Nous réalisons ce projet ensemble JeKo et [moi-même](pages/dr_c0w.html). 
Nous en sommes d'autant plus fier que c'est notre premier vrai projet commun, 
même si nous nous sommes toujours entraidés dans nos projets personnels.

Donc voilà aujourd'hui nous réalisons ensemble un projet C++, principalement
pour nous familiariser avec la notion de classe pour JeKo et avec la notion
de classe en C++ pour ma part, connaissant déjà le principe des classes avec 
le C\#.

Le principe de ce projet est un RPG comme son nom l'indique, mais un peu
particulier dans la mesure où nous voulons simplement apprendre des notions
de code et que nous ne voulions pas faire d'interface graphique vu que 
ce n'était pas le but que nous recherchions, nous l'avons donc réalisé
façon console. 

A ce stade du développement, j'ai déjà bien appris sur le développement en
C++ et sur les classes, en tout cas bien assez pour pouvoir rédiger un petit
article à ce sujet. Cependant, cet article étant assez particulier, il va
se découper en deux parties: une présentation du projet comme nous
l'imaginons à ce stade du développement, et dans une deuxième partie,
je zoomerai un peu plus sur les fonctionnalités du C++ que j'ai découvertes.

#Présentation du projet

Comme dit plus haut, il s'agit d'un projet console en C++, pour la simple
et bonne raison qu'il constitue un entraînement à la gestion des classes.
Et pour cela quoi de mieux qu'un petit jeu où il faut gérer des évènements,
et pour lequel il faut coder une petite intelligence artificielle pas trop
complexe mais assez réaliste. Celle-ci devant être capable de se défendre
et d'attaquer. De gérer également une génération d'ennemis qui soit
suffisamment fort pour représenter une menace mais pas trop non plus
pour ne pas que le jeu soit impossible. Côté intelligence artificielle,
il faudrait également qu'il soit possible de générer un groupe d'ennemis
un peu moins puissant mais en plus grand nombre pour diversifier les méthodes
de combat.

Côté joueur maintenant, il faut pouvoir utiliser une arme, ou bien lancer
des sorts. Et pour ça nous voulons que le joueur puisse choisir entre deux 
classes: guerrier ou sorcier. Chacune a ses avantages et ses inconvénients.
Nous voulons donc bien évidemment faire un jeu qui sorte de l'ordinaire,
et qui le fait déjà par son interface, parce qu'un RPG console n'est pas
ce qu'il y a de plus répandu, et encore moins de plus joué. Pour en
revenir au principe du jeu, le joueur sera capable de récupérer des objets
lorsqu'il tue ses ennemis comme des livres de sorts à apprendre, ou
de nouvelles armes à utiliser.

Il sera également possible pour le joueur d'apprendre ces nouveaux sorts
ou de changer d'armes pendant la phase entre deux combats consécutifs sans
qu'il ne prenne de dégâts entre les deux.

Pour en revenir aux classes de personnage, les deux auront leurs avantages et leurs 
inconvénients, leurs points forts et leurs points faibles.

##Guerrier

Donc voilà, on a imaginé les guerriers comme des vrais bourrins sanguinaires
prêts à charger comme des bœufs pour tuer leurs ennemis. Donc bien évidemment
surtout des armes de corps-à-corps pour l'instant. Le point négatif du guerrier
est sa vulnérabilité à la magie...

##Sorcier

Côté sorcier, on a reproduit un peu le même schéma que le guerrier, un mage
qui utilise des sorts plus ou moins puissants. On pourrait également imaginer
des effets à ces sorts, mais on n'en est pas encore là côté développement.
Pour compenser, les sorciers sont plus vulnérables aux attaques au corps-à
-corps.


On a également pensé que ça pourrait être intéressant de pouvoir 
gérer deux personnages dans la même partie, mais encore une fois, nous 
sommes assez loin de cela au niveau du développement.

Donc j'ai parlé des ennemis, des personnages, des armes, mais je n'ai pas 
énoncé les potions.

##Les potions

Les potions, pour l'instant, permettent de redonner de la vie au joueur,
mais on peut leur imaginer d'autres effets comme la perte de point de vie
à celui qui en consomme. Bien évidemment, le joueur pourrait s'en servir
comme de poison par exemple sur ses armes.



Encore une fois, nous sommes assez loin du résultat que je décris. Je vais
encore plus m'en éloigner en parlant d'amélioration des armes et de la 
création de nouvelles, de même pour les sorts. Je précise juste qu'il faut
avoir un certain niveau pour pouvoir utiliser certaines armes, de même pour
les sorts.



Maintenant que vous connaissez le *pourquoi* et que vous avez une vision à
peu près globale du résultat que l'on attends pour ce jeu, je vais vous parler
du *comment*

#Programmation C++

Comme je l'ai déjà dit au moins trois fois, nous développons ce projet en
C++, langage de programmation dérivé du langage C qui a pour but de compléter
ce dernier. Il apporte la notion de classe et d'objets. Pour ma part, c'est la
première fois que je code en C++. Il est facile de trouver les bases de ce 
langage sur Internet donc je n'en parlerai pas vraiment ici. J'expliquerai
plus le fonctionnement des classes, je présenterai la notion de templates,
et tout ça avec un code joliment indenté et commenté. 

Je vais donc commencer par la définition des classes avec des exemples
basiques.

##Les Classes

*Les classes, c'est la classe !* 

C'est ce qu'il faut retenir pour la __Programmation Orientée Objet__, ou plus 
communément appelée __*POO*__. Elles permettent plein de choses. 
En réalité, dans une classe, on peut appeler des fonctions directement
qui prendront en compte l'objet à partir duquel elle est appelée.
C'est ici un gros avantage sur les structures du C, qui existent aussi en C++.
Pour les structures, on est obligé de faire la fonction et de passer en paramètre
la structure que l'on a faite, sinon impossible de savoir ce qui doit être modifié.
Avec les classes, ce n'est pas nécessaire, on appelle directement la fonction
depuis l'objet.

```cpp
personnage.ChangeWeapon(weapon);
```

ou

```cpp
personnage->ChangeWeapon(weapon)
```

Ici, j'appelle la méthode *ChangeWeapon* qui prends en paramètre *weapon* qui
est en réalité une __instanciation__ de la classe *Weapon*. Je reviendrai sur cette notion
plus loin. La seule chose qu'il faut constater ici, c'est que je n'ai pas besoin 
de préciser quel personnage va changer d'arme. Pour ce qui est du point ou de la
flèche, j'y reviendrai un peu plus loin.


###Déclaration d'une classe

Comme pour les structures, il faut une définition pour cet objet. ce qu'il est
important de remarquer, c'est que les classes ont deux types de classement
de données: __*public*__ et __*private*__, en réalité il y en a un troisième 
appelé __*protected*__ mais dont je parlerai sûrement dans un autre article.
Je ne vais donc m'intéresser qu'à ces deux premiers dans cet article.

Pour faire simple, tout ce qui est dans la partie *private* ne sera pas
accessible en dehors de la classe, et tout ce qui est en *public* peut
être utilisé et appelé partout où la classe est définie. Pour être
plus clair, je vais décrire la définition d'une classe:

```cpp
class Voiture
{
	public:
	Voiture(Couleur couleur);
	void Rouler();
	void Stop();

	private:
	Couleur couleur;
};
```

Donc voilà, rien de plus simple qu'une petite voiture pour commencer.
Voici le prototype de ma classe, à mettre dans *voiture.h*. Dans
ce prototype, on voir qu'il y a des attributs *public* et des attributs
*private*. Ici, on a la méthode *Voiture()* qui ne retourne rien, on l'appelle
__*constructeur*__, et deux méthodes *Rouler()* et *Stop()*. Ces deux dernières
méthodes pourront être utilisées partout où la classe est définie. Ensuite,
vous pouvez observer que dans les attributs *private*, on a une *Couleur* qui
n'est pas un type de base, et qui est également une classe. C'est juste à titre
d'exemple et pour montrer que l'on peut utiliser une classe dans une autre, mais
aussi des pointeurs et des structures. Dans les exemples suivant utilisant la
classe voiture, je remplacerai la classe *Couleur* par une *string* qui n'est
autre qu'une classe de base du C++, et une sorte de version avancée des *char\**
du langage C.

Si je refaisais mon fichier *voiture.h* en prenant en compte cette modification,
cela donnerait ceci:

```cpp
#ifndef VOITURE_H_
#define VOITURE_H_

class Voiture
{
	public:
	Voiture(std::string couleur);
	void Rouler();
	void Stop();

	private:
	std::string Couleur;
};

#endif
```

Vous avez ici l'ensemble de mon ficher *voiture.h* qui comprend aussi une
protection contre les inclusions multiples dans votre projet (le *ifndef*).

La raison de la présence de *std::* devant le type *string* est que, dans un
ficher *.h*, il n'est pas possible de se placer dans un *namespace*. Le type
*string* est donc indéfini ici, et je précise donc au compilateur où le chercher.

__Voilà donc faire le prototype, c'est bien utile, mais pouvoir coder
la classe et ses fonctions, c'est encore plus classe...__ bon ok je vais
essayer d'arrêter avec ce jeu de mot...

Nous allons donc passer à la partie qui suit: la création de *voiture.cpp*

```cpp
#include "voiture.h"
#include <cstdlib>
#include <iostream>

using namespace std;

Voiture::Voiture(const string couleur)
{
	Couleur = couleur;
}

void Voiture::Rouler()
{
	//Affichage d'un message dans la console
	cout << "La voiture roule !" << endl;
}

void Voiture::Stop()
{
	cout << "Arrêt de la voiture !" << endl;
}
```

Donc voilà à quoi ressemble notre *voiture.cpp*. Le prototype de la classe
est donc contenu dans le *voiture.h* que j'ai écrit plus haut.

Donc pour commencer, sans surprise, le constructeur n'a toujours pas de type 
de retour, il va permettre d'initialiser notre voiture à partir d'une couleur.
La couleur passée en paramètre a l'attribut *const* dans la simple mesure où 
je ne modifie pas sa valeur et donc que je n'ai pas besoin
d'avoir accès à son écriture, et je le fais donc savoir à l'utilisateur et
sutout au compilateur avec ce mot-clef.

Voilà en ce qui concerne la classe voiture. Lorsque vous appellerez les méthodes
*Rouler()* et *Stop()*, des messages s'afficheront à l'écran.

En ce qui concerne la déclaration des méthodes, la présence de *Voiture::* 
précise que l'on définit les méthodes de la classe *Voiture*. Il faut les
mettre, c'est obligatoire, sinon le compilateur ne comprendra pas de quoi
il s'agit et surtout, il ne saura pas où chercher vos définitions pour
la classe en question.

Je vais aller un peu plus loin dans la notion de classe avec la notion
de __*getters*__ et de __*setters*__. Les *getters* permettent d'accéder à un
attribut de la classe sans le modifier, mais de simplement connaître
sa valeur, et les *setters* permettent de modifier sa valeur.

On va donc ajouter deux méthodes à notre classe *Voiture*: 

- Une pour obtenir la couleur de la voiture

- Une autre pour changer la couleur de la voiture

```cpp
class Voiture
{
	public:
	Voiture(std::string couleur);
	void Rouler();
	void Stop();
	std::string GetCouleur() const;
	void SetCouleur(const std::string nouvelle_couleur);

	private:
	std::string Couleur;
};

```

Et en ce qui concerne la modification de la définition de la classe,
il suffit d'ajouter ces deux méthodes:

```cpp
string Voiture::GetCouleur() const
{
	return Couleur;
}

void Voiture::SetCouleur(const string nouvelle_couleur)
{
	Couleur = nouvelle_couleur;
}
```

Ici le mot-clef *const* après *GetCouleur()* signifie que la valeur
retournée est en lecture seule et ne pourra être modifiée.
Et celui situé pour le passage en paramètre de la nouvelle couleur
signifie qu'il ne sera pas modifié dans ma fonction.


Je vais mettre un peu en pause ces définitions de classe pour
vous montrer maintenant comment utiliser la classe nouvellement
créer. Il est donc temps de faire notre *main.cpp*

```cpp
#include "voiture.h"
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	string couleur = "rouge";
	Voiture voiture(couleur);
	voiture.Rouler();
	voiture.Stop();
	cout << "Changement de couleur" << endl;
	string couleur_bis = "orange";
	voiture.SetCouleur(couleur_bis);
	cout << "La voiture est de couleur: " << voiture.GetCouleur() << endl;
	return 0;
}
```

Voilà, donc pour initialiser notre voiture, il suffit de faire comme pour les 
autres types. j'aurai également pu écrire:

```cpp
Voiture voiture = Voiture(couleur)
```

Cela fonctione aussi bien, et a le même effet.

Maintenant je vais attirer votre curiosié sur la flèche (*->*) que j'ai
utilisé au début de cette partie pour accéder aux méthodes de la classe.
Elle est utilisée dans le cas où on utilise un pointeur pour
accéder à la classe:

```cpp
int main()
{
	string couleur = "rouge";
	//Déclaration d'un pointeur sur la voiture
	Voiture *voiture = new Voiture(couleur);
	voiture->Rouler();
	voiture->Stop();
	cout << "Changement de couleur" << endl;
	string couleur_bis = "orange";
	voiture->SetCouleur(couleur_bis);
	cout << "La voiture est de couleur: " << voiture->GetCouleur() << endl;
	delete voiture;
	return 0;
}
```

Voilà ce que cela donne si l'on passe par un pointeur. Il faut utiliser
le mot-clef *new* pour la déclaration et l'initialisation, on utilise la
flèche *->* pour accéder aux méthodes de la classe, et on pense bien
à libérer la mémoire avec le mot-clef *delete* une fois que l'on n'a plus
besoin de la variable.

Maintenant, admettons que l'on veuille que notre garagiste, donc ici le 
constructeur de notre classe, fasse notre voiture non plus à partir d'une
couleur mais à partir de la voiture de quelqu'un d'autre. Il suffit de
faire un second constructeur qui prends un autre argument.

```cpp
Voiture(const Voiture &src);
```

Cette définition est pour notre *voiture.h*, il suffit
simplement de l'ajouter.

Passons maintenant à la méthode dans *voiture.cpp*

```cpp
Voiture::Voiture(const Voiture &src)
{
	Couleur = src.GetCouleur();
}
```

Le symbole *&* devant *src* précise que l'on veut directement un
accès à la valeur de l'objet, et donc que l'on ne souhaite pas
passer par un pointeur. Et *src* est simplement une abréviation
pour *source*.

Bien évidemment, ici ce n'est pas très intéressant puisque de dire
à votre constructeur que l'on veut une voiture *orange* ou bien que
l'on veut une voiture qui soit comme la voiture de votre voisin qui
est *orange* revient très exactement au même. Cela deviendrait
plus intéressant si l'on rajoutait des attributs comme une marque et un
modèle par exemple. Vous voulez qu'on essaie ?

Reprenons notre *voiture.h* et modifions la définition de la classe:

```cpp
class Voiture
{
	public:
	Voiture(const std::string constructeur, const std::string modele, const std::string couleur);
	Voiture(const Voiture &src);
	std::string GetConstructeur() const;
	std::string GetModele() const;
	std::string GetCouleur() const;
	void Rouler();
	void Stop();

	private:
	std::string couleur;
	std::string modele;
	std::string constructeur;
};
```

Vous pouvez donc voir que l'on a maintenant deux constructeurs:

- Le premier qui prends trois paramètres:
 
	1. un nom de fabriquant automobile
 
	2. un nom de modèle
 
	3. une couleur

- Le second qui prends simplement une voiture *à copier*

Nous allons donc implémenter ces deux constructeurs de classe, puisque
nous n'allons pas redéfinir les méthodes *Rouler()* et *Stop()*.

```cpp
Voiture::Voiture(const string constructeur, const string modele, const string couleur)
{
	this.constructeur = constructeur;
	this.modele = modele;
	this.couleur = couleur;
}

Voiture::Voiture(const Voiture &src)
{
	constructeur = src.GetConstructeur();
	modele = src.GetModele();
	couleur = src.GetCouleur();
}
```

J'ai dû rajouté deux *getters* pour pouvoir faire ma copie de voiture 
correctement: 

- Le premier sur la marque de la voiture

- Le second sur le nom du modèle

Voilà, maintenant amusons nous un peu avec le *main*

```cpp
int main()
{
	Voiture voituredemarc = Voiture("Renault", "Mégane", "Bleue");
	Voiture voituredepierre = Voiture(voituredemarc);
	cout << "Voiture de Pierre:" << endl;
	cout << "Constructeur: " << voituredepierre.GetConstructeur() << endl;
	cout << "Modèle :" << voituredepierre.GetModele() << endl;
	cout << "Couleur: " << voituredepierre.GetCouleur() << endl;
	return 0;
}
```

Lorsque l'on observe la sortie console, on voit donc que la voiture
de Pierre a les mêmes attributs que la voiture de Marc. Et en même temps,
heureusement, puisque c'est le résultat que nous voulions.

Nous avons donc vu qu'il était possible de faire deux constructeurs différents
qui prennent des paramètres différents, mais c'est aussi possible avec les méthodes
de la classe. Par exemle, en changeant notre méthode *Rouler()* par:

```cpp
void Rouler(const int kilometres);
void Rouler(const int kilometres, const string nomderoute);
```

Nous avons maintenant deux prototypes pour la méthode *Rouler* qui
prennent des arguments différents, implémentons-les:

```cpp
void Rouler(const int kilometres)
{
	cout << "La voiture roule pendant << kilometres << " km"<<endl;
}

void Rouler(const int kilometres, const string nomderoute)
{
	cout << "La voiture roule sur la route " << nomderoute;
	cout << " pendant " << kilometres << " km" << endl;
}
```

J'ai simplement changé de ligne dans la deuxième méthode pour éviter d'avoir
une ligne trop longue, mais cela n'aura aucun effet sur l'affichage du texte.
Je n'écrirai pas la fonction *main* qui correspond, je pense que l'exemple parle
de lui-même.

Il est donc possible de faire aussi bien plusieurs constructeurs différents que
de méthodes publiques différentes. Après il faut le faire que si c'est nécessaire,
c'est inutile de faire deux méthodes qui ont le même nom, des paramètres différents
si les deux font quelque chose dont le résultat n'a rien à voir. 


Maintenant que nous avons des voitures fonctionnels, nous allons comparer les 
voitures que nous crééons. Ainsi, je vais poser le problème:

Marc et Pierre (oui, ils sont toujours là) ont deux voitures, et veulent
les comparer et savoir si ils ont la même.

Vous l'aurez compris, l'opération est très simple:

- Les deux voitures sont pareil si:

	1. Elles viennent du même fabriquant

	2. Elles sont du même modèle

	3. Elles ont la même couleur

- Les deux voitures sont diférentes dans les cas contraires

Nous pouvons donc écrire une condition comme celle-ci:

```cpp
if (voituredepierre.GetConstructeur() == voituredemarc.GetConstructeur()
	&& voituredepierre.GetModele() == voituredemarc.GetModele()
	&& voituredepierre.GetCouleur() == voituredemarc.GetCouleur())
```

Le défaut, c'est que nous devrons utiliser __à chaque fois__ cette condition.
Heureusement, le C++ offre la possibilité de redéfinir les opérateurs de base,
et quand je dis *opérateurs de base*, je veux dire:

- +

- -

- \*

- \\

- %

- +=

- -=

- \*=

- \\=

- %=

- ==

- !=

- etc...

Bien évidemment, ça n'aurait aucun sens ici d'additionner, ou de soustraire
des voitures ensemble. en revanche nous pouvons utiliser les opérateurs *==* et
*!=* sont plus intéressants puisqu'ils nous permettent de comparer deux voitures...
__oh eh bah ça tombe bien dis donc !__

Pour cela, nous allons inclure cette ligne dans le fichier *voiture.h*:

```cpp
class Voiture
{
	// Détail de la classe
};

bool operator== (Voiture voiture1, Voiture voiture2);
bool operator!= (Voiture voiture1, Voiture voiture2);
```

J'ai replacé le prototype de la classe pour montrer que le prototype 
pour la surcharge d'opérateur se fait en dehors.

Nous allons donc modifier notre *voiture.cpp*:

```cpp
bool operator== (Voiture voiture1, Voiture voiture2)
{
	return voiture1.GetConstructeur() == voiture2.GetConstructeur()
		&& voiture1.GetModele() == voiture2.GetModele()
		&& voiture1.GetCouleur() == voiture2.GetCouleur();
}

bool operator!= (Voiture voiture1, Voiture voiture2)
{
	// Comme on a la définition pour l'opérateur ==,
	// il suffit d'en retourner la négation
	return !(voiture1 == voiture2);
}
```

Grâce à ces deux opérateurs, il suffit donc d'écrire:

```cpp
//
if (voituredepierre == voituredemarc)
{
	//Les deux voitures sont identiques
}
else if (voituredepierre != voituredemarc)
{
	//Les deux voitures sont différentes
}
```

En parlant des opérateurs de base, les opérateurs *<*, *>*,
*<=* et *>=* en font également partie, mais pareil que pour
l'addition ou la soustraction, ça n'aurait aucun sens de
les appliquer à des voitures.
