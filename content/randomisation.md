Title: Randomisation
Author: Dr_c0w
Date: 2015-01-18 23:01
Category: Cours
Slug: randomization
lang: fr
translation: false
tags: jukebox, cours, algorithmes

##La Randomisation

Je voulais vous présenter un petit cours simple sur une notion plutôt utile:
cela s'appelle la *randomisation*. Le principe est donc, ici, de trier ses
données de façon aléatoire sans que la valeur aléatoire générée soit la source
unique du classement.

Je vais m'expliquer avec un petit exemple en C\#. Pas besoin d'avoir fait du C\#
pour comprendre.

```csharp
public List<T> Shuffle(List<T> list)
{
	List<T> newList = new List<T>(list.Count); 
	// On crée ici une nouvelle liste de T
	for (int i = 0; i < list.Count; i++)
	{
		int random = new Random().Next(list.Count); 
		// On génère un nombre aléatoire entre 0 et le nombre d'éléments dans la liste
		if (newList[random] == null)
		{
			newList[random] = list[i];
		}
		else
		{
			i--; 
			// Pour pouvoir générer un nouvel entier aléatoire
		}
	}
	return newList;
}
```
Une petite précision au niveau du code, j'utilise *new Random().Next(int max)*
pour générer un nombre aléatoire, j'ai souvent lu et on m'a souvent recommandé
de créer une variable de type *Random* que l'on va ici appeler *rand* et
de simplement appeler la méthode *rand.Next(int max)*.

Alors tout d'abord, ceci n'est pas de la *randomisation* pour la simple et
bonne raison qu'ici l'aléatoire a toute son importance sur le classement 
des données, c'est-à-dire trop. D'après mon expérience, il faut que l'
aléatoire ne joue qu'une faible proportion, bien sûr, il est inévitable
pour organiser ses données de façon aléatoire, il faut simplement être 
capable de minimiser son importance. 

Ensuite, le problème de ce code, c'est notamment le fait que si, en
particulier pour les dernières valeurs, vous ne tombez pas sur des valeurs
qui conviennent, vous allez pouvoir tourner un bon moment sans obtenir de
résultat. Je peux vous l'approuver, et si j'écris ce cours ici, c'est que
j'ai eu besoin de cette notion. La raison ? Il me fallait un algorithme pour
créer une liste de lecture aléatoire pour mon programme [*JukeBox*]({filename}jukebox.md).

Après avoir testé un code un peu similaire et m'être rendu compte que cela ne
pouvait pas marcher du tout sur le long terme, je me suis interessé au 
principe de la *randomisation*. C'est à partir de ça que ma lecture
aléatoire se fait. 

Le danger est de trop minimiser l'utilisation de l'aléatoire.

J'ai en effet produit un code à peu près similaire à celui-ci:

```csharp
public List<T> Shuffle(List<T> list)
{
	List<T> newList = new List<T>();
	int[] rand_array = new int[list.Count];
	for (int = 0; i < rand_array.Length; i++)
	{
		nrand_array[i] = new Random().Next(0, 100) % 2; 
		// Pour n'avoir que des 0 ou des 1
	}
	bool loop = true; 
	// Un booléen qui permettra de savoir si de continuer à boucler est nécessaire
	do
	{
		loop = false;
		for (int i = 0; i < list.Count; i++)
		{
			if (rand_array[i] == 0)
			{
				rand_array[i] = 2;
				newList.Add(list[i];
				break;
			}
			else if (rand_array[i] == 1)
			{
				rand_array[i] = new Random().Next(0, 100) % 2;
				loop = true;
			}
		}
	} while (loop);
	return newList;
}
```

Ici, on a bien une randomisation, en effet, la liste obtenue en sortie n'est 
pas le résultat direct de la génération aléatoire, même si elle est fortement
déterminée par celui-ci. En d'autres termes, la liste obtenue n'est pas le
résultat du hasard seul, mais d'un hasard *"contrôlé"*. 
Par contre, j'ai rencontré un problème qui s'avère majeur avec ce type de
randomisation: les valeurs sont globalement dans le même ordre que lorsqu'elles
sont entrés. Alors toutes les valeurs ne se suivent heureusement pas de la 
même façon mais on verra que ce sont souvent les mêmes qui apparaîssent en tête.

Ce qui amène à l'algorithme que j'utilise actuellement dans mon projet:

```csharp
public List<T> Shuffle(List<T> list)
{
	int[] array = new int[list.Count];
	//On crée tout d'abord un tableau ordonné d'index donc des int
	for (int i = 0; i < array.Length; i++)
	{
		array[i] = i;
	}
	int j = 0; // j sera utilisé dans la boucle qui suit pour les itérations
	Random r = new Random();
	while (j < array.Length)
	{
		int pos1 = r.Next(array.Length);
		int pos2;
		do
		{
			pos2 = r.Next(array.Length);
		} while (pos2 == pos1);
		int value = array[pos1];
		array[pos1] = array[pos2];
		array[pos2] = value;
		// On échange les valeurs dans le tableau de façon aléatoire
		j++;
	}
	List<T> newList = new List<T>();
	for (int i = 0; i < array.Length; i++)
	{
		newList.Add(list[array[i]]);
	}
	return newList;
}
```

Je vais maintenant vous expliquer pourquoi j'ai effectué cet algorithme de
cette façon:

1. Tout d'abord, la génération d'index est simple et fiable.

2. Ensuite, je limite les conséquences de la génération aléatoire, tout en
gardant un certain contrôle sur ce qu'il se passe.

3. Enfin, ce cette façon, je limite en particulier les chances que l'algorithme
fasse une boucle infinie, puisqu'il y a moins de chances de générer deux fois
le même nombre à la suite que de générer une seule fois plusieus nombres 
différents.


J'espère que ce cours vous aura été utile et que vous comprendrez maintenant 
cette notion de randomisation.
