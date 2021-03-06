Title: EtoileMessenger
Author: Dr_c0w
Date: 2015-03-31 20:15
Category: Projects
Slug: chat
lang: en
tags: chat

##Presentation of EtoileMessenger

I just ended the debug session of EtoileMessenger which is a C\# program that I
made for a [real estate company](http://agence-etoile.com/en). I made this 
instant messaging program on a Client-Server base. I had already made a more
basic similar program with less possibilities: only one channel where all users
talk. In EtoileMessenger, I had to handle the creation of groups and the sending
of private messages. Those groups can be private or public. Hopefully, the first
program I made helped me to handle some bugs I had already fixed, mainly some
inter-thread operations such as the communication between the client threads
and the user interface. Eventough, I had some issues because sometimes I had
to create new windows from a thread which is not the main one. Thanks to the C\#
and its documentation, I could easily solve it.

As this is a presentation of a project I made, I will now introduce to you
my project as a user.

In the part of the server, things were more simple as I applied the notions
I saw while developping [JukeBox]({filename}jukebox_en.md), especially with
the user interface.

##User Interface
###The Server

For the server, nothing more simple than:

* a user interface easy-to-use with tabs that show informations like logs,
connecte users, whitelisted users, created groups.

* logs with main information concerning the server

* a whitelist to allow users to connect to the server. Whitelist can be
modified through the user interface

* the administrator can kick or ban anyone connected from the server.
But the groups are in read-only and cannot be modified through the interface

* the administrator has recently been granted the access to password change
and when an user is added to the whitelist, it will request a new password for
the session.

###The Client

The user interface I made for the client is more complicated. Indeed,
the UI is divided into 6 different types of windows:

* a login form that is able to store the last login informations used excepted
the password

* a main window where the user can see the connected users and the groups available

* as the user join a group, by double-clicking on the treeview or accepting an 
invitation, a new window pops up in which the user can talk to users in the 
group or even invite some others. It is also possible to change the font and 
the color of the text.

* when the user wants to invite another one in a group, he is able to see the
connected user and select one or more and send them an invite.

* private message window also exists and allow two users to talk to each other

* the last kind of window is the one to create groups. There the user is allowed
to enter the name of the group, to select if the group will be public or private
and then to send an invite to connected users.

##Group Management

The main obstacle I encountered while creating groups was the following: the
client and the server had to be able to identify the different groups even if
they had the same name (which can be possible for two private groups for example).
I finally found the answer by [hashing]({filename}jukebox_en.md) the name of the 
group to make an identifier. The other advantage of this identifier is the fact
that it is a 5 characters long string and is then the cost to send it is 
minimalized. So in order to send a message to a group, the client will send to
the server the identifier of the group.

###How do the groups work?

Firstly, the user creates a group through the window made for it, this will
send an instruction to the server that the group has been created. At this 
time, the identifier has not been created yet.

Then the server calculates the *hash* of the name of the group and will double-
hash it if it already exists.

The server is now telling the client that the operation has been successfully
made and the client can now open the window of that group. If some other users
were invited, they would receive the invitation at this time. If the group was
set as public, all other users would be able to see it in the treeview of the
main window.

Finally, when a user send a message to a group, the identifier is added at the
beginning of the group in order to make it easier for the server to deliver the
messages.

This is how the groups are managed

##Private Message Management

Private messages are based on the same pinciple of the group exept that instead
of the identifier of the group, the name of the sender and the name of the 
receiver are added at the beginning of the message and the server will be able
to deliver the message.

##Notifications

More recently I added a notification system for my project. I allowed the 
windows to flash in orange when a new message is received if they are hidden.
This happens only wen the window is hidden. In addition, there is a notification
at the bottom of the screen that appears with the sender, the name of the
conversation and the content of the message. This allows the user to have a
preview of what has been sent without having to go back to the discussion.

##Security Aspect

Obviously, without security, almost everybody knowing how to connect to the 
server would be able to get information about many things and would the be able
to see what happens almost everywhere. It would also be possible for the hacker
to set his identity as an allowed user.

In order to fix this, JeKo and I made our own security system for this software.
Obviously, it is far away from a professional one but still does the minimum
requirements.

Indeed, the encryption of the message are based on a home-made algorithm based
on a rotating on which a main key is applied which is send based on the same
algorithm but with another key when the user connects itself.

To login, it was not acceptable to send the password as it is entered. The
problem is that the hash algorithm that I made for the groups does not seem
to be reliable enough in order to be used for the checking of the passwords.
Indeed, I do not really know how to check how reliable my algorithm is, but
it cannot be as reliable as MD5. This is why I used this last one in order
to send passwords. The server has only to check if the MD5 registered in the
database is the same as the one received.

Soon, I will add the possibility to change the password, but I am stuck
on the way to do it. The problem is that changing a password is not that
complicated but make it possible for the owner of the account **only** is
more difficult. Currently, I do not really know how to check the ID of the
user.

##Command Handler

As I said in the previous paragraph, if the messages are sent without any 
security it would be possible for almost everybody having some knowledge
about my software to get access to them. They would then be able to send
commands to the server and would be able to make some discords on the server.

But those persons would not be able to send commands to other users. Indeed,
clients only communicate with the server and cannot communicate with other 
clients directly. But they would be able to send commands such as "join group"
or "create group", etc. 

##Recap

The client is a kind of stupid. Indeed, it can only communicates with the 
server and is not even able to interpret his own commands sended to the server.
He must receive a message from the server in order to do something, even when
sending a message.

##Conclusion

This project was a very interesting project and thanks to which I could learn
many things. I will do some improvements to this project so I will continue 
learning about some C\# features. I will probably do a more general version
of this project than the version I made for the 
[Agence Etoile](http://agence-etoile.com/en). 

As I wrote in this article, I already about Instant Massaging programming but
not as much far. I think that some features are still missing and I have the 
will to add some. But I first would like to fix some bugs.

##Future features

The following list is the list of some features I would like to implement:

* Smiley: really a cool feature.

* "is writing..." status in conversations when a user is writing.

* Allow the users to reset their passwords, working on it currently.

* Option menu: the main ones would be present in the main window after
login, the others would be present in the conversations' windows.
