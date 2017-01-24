Title: Hachage
Date: 2015-01-21 14:57
Author: Dr_c0w
Category: Cours
tags: chat, cours, algorithmes
lang: fr

##Hachage

Bonjour à tous,

Je vais vous faire un petit cours sur le principe du hachage. Mais tout d'abord
je vais faire un petit point pour vous expliquer où est-ce que l'on retrouve
l'utilité de ce type de fonction et pourquoi.

##Où sont utilisés ces fonctions de hachage ?

Sans le savoir, vous avez souvent recours à des fonctions de hachage. Elles 
permettent soit de créer un identifiant unique pour classer des données, comme 
c'est le cas pour la gestion des groupes dans ma [messagerie instantanée]({filename}chat.md),
soit pour vérifier la concordance de deux chaînes de caractères comme c'est 
le cas lors de l'envoi de mot de passe. Dans ce dernier cas, le client va 
envoyer le hash de son mot de passe et le serveur va vérifier que ce hash
correspond à celui qu'il a enregistré pour ce client.
Plusieurs fonctions de hachage sont bien connues comme le MD5, mais
j'ai choisi de refaire ma propre fonction de hachage. La raison ? 
La chaîne de caractères qui résulte d'un hachage par MD5 est trop longue 
pour être envoyée, du coup j'ai préféré refaire une fonction de hachage dont
le résultat contient 4 chiffres et une lettre.

##Faire sa propre fonction de hachage

La notion la plus importante pour une fonction de hachage, c'est que,
contrairement à une fonction de cryptage, elle doit dépendre de la
valeur des caractères. Ainsi, il existe plusieurs techniques et il est donc
possible de se baser seulement sur une partie des caractères, donc de les
extraire de la chaîne pour les traiter. J'ai personnellement préféré me 
baser sur tous les caractères de la chaîne, et appliquer des opérations 
mathématiques dessus. Le but n'étant pas de pouvoir récupérer la chaîne
d'origine à partir du hachage, bien au contraire, il faut compresser la donnée 
pour un résultat plus petit que l'original, ainsi la fonction suivante peut
être considérée comme une fonction de hachage:

```csharp
public string Hash(string data)
{
	string hash = "";
	// Dans la boucle qui suit, on calcule
	// la valeur modulo 1 0 du caractère à la position i
	// et on le met dans le hash
	for (int i = 0; i < data.Length; i++)
	{
		hash += (uint)data[i] % 10;
	}
	// On remet dans hash une chaîne
	// qui contient uniquement les 5 derniers
	// caractères du hash généré
	hash = hash.Substring(hash.Length - 6);
}
```

A partir de cette fonction, on va donc récupérer un hash du paramètre *data*,
basé sur la valeur ASCII de ses caractères modulo 10 (*modulo* signifiant le
plus petit reste strictement inférieur à la valeur spécifiée, ici 10, que l'on
obtiendra suite à des divisions successives d'un certain nombre, ici la valeur
du caractère). La fonction *Substring* permet ici de récupérer les caractères
de la fin d'une chaîne de caractères à partir d'une position donnée (*Note: 
j'aurai pu parcourir ma chaîne passée en paramètre seulement sur ces 5 derniers
caractères, et j'aurai eu le même résultat*). Ici j'ai donc effectué une 
extraction puisque je me base seulement sur un certain nombre de caractères,
et non sur tous.


J'en viens donc aux défauts de certaines fonctions de hachage: les *collisions*.
On dit qu'il y a *collision* lorsque l'on obtient deux hash similaires pour deux
valeurs différentes. Par exemple, si vous utiliser la fonction précédente pour
calculer le hash des mots "contacter" et "rétracter", le hash sera similaire
pour les deux mots. En effet, comme la fonction ne se base que sur les 5 derniers
caractères, on obtiendra un hash similaire pour tout mot qui contient les mêmes
5 derniers caractères. Après, cela dépends de la fonction de hachage qui est
utilisée. 

Ces collisions peuvent poser de très gros problèmes notammment de 
sécurité. Si vous reprenez la fonction de hachage qui sert d'exemple, et
que l'on admet que votre banque utilise cette fonction de hachage pour 
vérifier votre mot de passe (personnellement je changerai de banque),
alors si le hacker essaie de rentrer un mot de passe dont les 5 derniers
caractères sont similaires à ceux de votre mot de passe, il peut avoir
accès à votre compte banquaire et effectuer un virement de votre compte 
vers le sien.

En réalité, il existe plusieurs façons de faire sa fonction de hachage,
j'aurai aussi bien pu traiter un caractère sur deux par exemple, ou alors
tous les caractères qui sont situés à un emplacement qui serait un nombre
premier (un nombre premier étant un nombre qui n'est divisible que par 1 et
lui-même). Il suffirait simplement de calculer les nombres premiers 
inférieurs strictement à la taille de la chaîne de caractères et extraire
seulement les lettres à ces postions. On extrairait donc encore une fois
des caractères à un emplacement fixe, mais il y a de plus en plus d'espace
entre les caractères extraits. Ce serait donc un bon point par exemple pour
les chaînes longues, mais un gros point négatif pour les chaînes de petite
taille. Il est aussi possible de traiter tous les caractères et d'appliquer
des fonctions mathématiques pour *réduire* ensuite la chaîne, en changeant
par exemple de modulo et en ajoutant des symboles, ou des lettres pour
continuer à ne générer qu'un seul caractère quelque soit sa valeur.

Vous comprendrez donc que la réalisation d'une fonction de hachage
est une tâche qui a des contraintes si on veut la réaliser correctement.
Pour être sûr de ne pas avoir de problèmes avec votre fonction, il faut
vérifier qu'elle soit bien injective pour toutes les valeurs qu'on lui donne.
Pour informations, il existe des collisions sur le MD5, mais ce dernier reste
tout de même une des plus sécurisées et surtout l'une des plus utilisées

##Ma fonction de hachage

Comme je l'ai dit en introduction, j'ai eu recours à une fonction de hachage
pour pouvoir générer un identifiant unique pour mes groupes, en sachant qu'il
me suffit de procéder à un double-hachage en cas de collision, c'est-à-dire
que je hash de nouveau le hash que j'ai obtenu.

J'ai fait ma fonction de hachage de la façon suivante:

```csharp
public string Hash(string name)
{
	// On crée d'abord deux tableaux
	// Le premier qui va contenir les caractères
	// Le second qui va recevoir les valeurs des caractères
	// auxquelles on applique certaines opérations
	// Les deux tableaux font la même taille
	char[] array = name.ToArray();
	uint[] result = new uint[array.Length];
	
	// Dans la boucle qui suit, on traite une première fois
	// chacun des caractères, on les mets dans le tableau
	for (int i = 0; i < array.Length; i++)
	{
		// On va se servir d'une deuxième boucle pour
		// modifier les valeurs.
		// Dans cette boucle, on part de 0, pour aller jusqu'à i
		for (int j = array.Length - 1; j >= i; j--)
		{
			//On ajoute d'abord leur position dans le tableau de caractères + 1
			result[i] += (uint)(array[j] * (i + 1));
			// On multiplie ensuite par une certaine expression mathématiques
			result[i] *= (uint)(((j + 1) * (i + 1)) + (j + i + 1));
		}
	}
	// On modifie les valeurs à partir de certaines opérations
	// prédéfinies
	for (int i = 0; i < result.Length; i++)
	{
		result[i] += (uint)(result.Length * (i + 10));
		result[i] *= 4;
		result[i] += '0';
		result[i] -= 'A';
		result[i] *= 25;
		result[i] *= 40;
	}
	// On calcule le total contenu dans le tableau
	uint total = 0;
	for (int i = 0; i < result.Length; i++)
	{
		total += result[i];
	}
	// On définit une lettre en utilisant le résultat 
	// et en prenant son modulo par 26
	char letter = (char)(total % 26 + 'A');
	// On récupère ensuite le hash en parcourant la valeur
	// totale à laquelle on applique des opérations 
	// une fois encore.
	string hash = "";
	for (int i = 0; i < 4; i++)
	{
		hash += total % 9;
		total /= 9;
	}
	// On ajoute la lettre calculée au hash
	hash += letter;
	return hash;
}
```

A partir de cette fonction, j'obtiens donc un identifiant qui sera unique et
qui, dans le cadre de ma messagerie instantanée, permettra au serveur de créer
et d'identifier un groupe, et au client de spécifier simplement à quel groupe
le message doit être envoyé.

##Conclusion

Le hachage est donc une méthode très utile pour vérifier la concordance de 
certaines données comme je l'ai expliqué avec le système de vérification 
de mot de passe ou encore pour identifier une donnée, avec par exemple 
l'identification des groupes. En réalité, j'utilise aussi mon identifiant
pour classer et regrouper mes données. Elles sont rangées dans une liste
spéciale en C\# qui s'appelle un *Dictionnary* et qui stocke deux valeur:
ma valeur de hash et mon groupe, ou plus précisément un lien vers l'interface
graphique du groupe. La valeur de hash sert ici de clef pour accéder directement
à l'interface du groupe.
