Title: JukeBox
Author: Dr_c0w
Date: 2015-01-18 15:00
Category: Projects
lang: en
traduction: true
tags: jukebox

##Presentation of JukeBox

JukeBox is a small software able to read audio files in MP3 or WAV format.
It has been made in C\# with Windows Form.

###Open File

There are three ways to open a file:

* using the menu on top:
	
	* using "Open a file" or "CTRL + O" to open only one file

	* using "Open a folder" or "CTRL + F" to open the content of one folder

	* using "Open subfolders" or "CTRL + SHIFT + F" to open the content of the 
	subfolders of a folder

* using drag and drop on a node of the treeview

The third options is very useful when the user wants to load a full discography
of an artist or a group of albums. The software will be able to get the file
to the right format in the subfolders of the folder selected. 

When the user selects a file, those will be put in the first node of the 
treeview, else a node will be created with the name of the fodler

##Reading

In order to read a file, a double-click on an **album** node will make JukeBox
play the musics of the album. This will also clear the playlist and then put
the musics of the album in the playlist. Whereas a double-click on a song will
play that song after adding it at the end of the playlist. 

In order to put the musics of an album at the end of the list, you have to do 
a right-click on the node. 

At this time, there are no contextmenu nor the possibility to see the current 
playlist but I will add this soon. I should also redo the user 
interface later as I developped JukeBox a year ago and I was not as experienced
with Windows Form as I am now.

While playing a song, the user can easily move into the song thanks to a
progressbar. There are also five buttons and a trackbar:

* a play/pause button

* a next track and a previous track buttons

* a loop/loop-on-track button

* a shuffle button

The shuffle button allows the player to shuffle the playlist thanks to a 
[home-made randomization algorithm]({filename}randomisation_en.md).

###Album Information Display

I have implemented some features, some are really useless but cool but some
others are useful (hopefully). 
In the cool features, there are some filters that
can be applied on the cover such as **pinkify**, **greyscale** and 
**binarization**.
In useful features, there are the display of the information of the song
such as the name of the song, the name of the album, the name of the artists
and the kind of music.


