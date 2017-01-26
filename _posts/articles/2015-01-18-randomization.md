---
title: Randomization
layout: post
author: Dr_c0w
date: 2015-01-18 23:01
categories: articles
tags: ['jukebox', 'courses', 'algorithms']
---

## Randomization

This is a course about a useful notion: the randomization. The principle of
this is to sort datas randomly but whith the particularity that the random
value generated must not be the only source of the sort.

I will explain with a little algorithm in C\# but you do not need to know
C\# to understand.


```csharp
public List<T> Shuffle(List<T> list)
{
	List<T> newList = new List<T>(list.Count);
	// A new List of T is created
	for (int i = 0; i < list.Count; i++)
	{
		int random = new Random().Next(list.Count);
		//A random number between 0 and the number of elements in the list is generated
		//If no element is in the newList at the generated place, we put the ith there
		if (newList[random] == null)
		{
			newList[random] = list[i];
		}
		else //if there is already an element there
		{
			i--;
			// To generate a new random number
		}
	}
	return newList;
}
```

I need to precify only one thing in that code, I use
***new Random().Next(int max)*** method to generate a new random value. But
I should first initialize a new variable of type ***Random*** called *rand*
and then call its method ***rand.Next(int max)***.

First, this is **not** randomization because here random is too important
while sorting. The random variable must *not* be the only one to intervene
while shuffling, because, indeed, it must be present. Its importance should
be minimized but still there.

The second problem with this code is the fact that values do not match and
must be regenerated, and this would be a great problem in the end of the
shuffling because there would be only one index available and while the right
index is not generated, the for loop will continue. Indeed, as I am writing
this course in here about randomization, I did those mistakes or kind of
the same. I needed this notion for my project [JukeBox]({% post_url articles/2015-01-18-jukebox %})
in order to shuffle the playlist.

And this code is there because I tried something similar and I realized that
it was not reliable at all on long term and then I learnt the notion
of randomization. Thanks to this notion, I can shuffle the playlist.

But take care of minimizing too much the use of random as in the following code:

```csharp
public List<T> Shuffle(List<T> list)
{
	List<T> newList = new List<T>();
	// Initilizing a list of T
	int[] rand_array = new int[list.Count];
	// Initializing an array of integers
	for (int = 0; i < rand_array.Length; i++)
	{
		nrand_array[i] = new Random().Next(0, 100) % 2;
		// Only 0 and 1 thanks to the modulo 2 in the array
	}
	bool loop = true;
	// A boolean that will tell whether looping is necessary or not
	do
	{
		loop = false;
		for (int i = 0; i < list.Count; i++)
		{
			//if the value is 0, then the value is added to the list
			if (rand_array[i] == 0)
			{
				rand_array[i] = 2;
				newList.Add(list[i];
				break;
			}
			else if (rand_array[i] == 1) //else the value is regenerated
			{
				rand_array[i] = new Random().Next(0, 100) % 2;
				loop = true;
				// Just regenerate and continue looping
			}
		}
	} while (loop);
	// Looping while not all values are put in the list
	return newList;
}
```

This is a randomization because the list returned at the end is not the only
result of random. Indeed, the list returned is the result of a random that is
oriented the way it is needed. We use random to do something that is needed
and to do it our own way and get the result we need. Altough, there is an
issue with this code: the iteration are made in the order of the list. So
the result obtained is often sorted randomly but in the same order as the
list was initially and there are often the same in the first positions.

Which brings us to the algorithm un use in my project:


```csharp
public List<T> Shuffle(List<T> list)
{
	int[] array = new int[list.Count];
	// Initializing an array of int in which the value is the position
	for (int i = 0; i < array.Length; i++)
	{
		array[i] = i;
	}
	int j = 0; // j will be used in the loop for iterations
	Random r = new Random();
	// Then swapping values in the array randomly
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
		j++;
	}
	// The values in the array are used as index to get
	// the T in the list as parameter and add them to
	// the new list
	List<T> newList = new List<T>();
	for (int i = 0; i < array.Length; i++)
	{
		newList.Add(list[array[i]]);
	}
	return newList;
}
```

I did this algorithm in this way because:

1. The generation of index is simple and reliable

2. I minimize the consequences of random, while controlling what is happening

3. In this way, I minimize the possibility of endless loop. It is also easier
to generate two random numbers and having them different, this makes more
possibilites.

I hope this course was useful and that you understand this notion of
randomization now.
