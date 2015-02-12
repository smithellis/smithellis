Title: Linux Basics
Date: 02/11/2015 7:00
Tags: linux, bash, bash history, wget, tips

# Handy Linux Stuff

Linux is awesome.  I've been using some flavor of Linux for...a long time.  Right now on my personal machines, I'm mostly using [Mint][1].  It's just very clean and easy; if you don't feel like going configuration crazy, [Mint][1] might work for you.  I'm no longer a distro zealot - I've figured out that the right distro for you is the one you like.  So - enjoy!

I thought I'd take a second and tell you about some simple command line things that I've found to be incredibly useful.  One is bash history.  If you use a bash shell, you really should take a second to learn about it.  

At your command line, type:

    history

A giant list will sprawl before you of things you've typed in the shell.  If you just want to see the last ten or so, type:

    history 10

Each command has a number next to it.  If you want to rerun a command from your history, just type ! and the number.  So to rerun item 58:

    !58

Boom, it will run that command.  I find this handy if I've run some egregious one liner from the command line that I don't want to have to retype - a billion character piped nightmare of some type.

Another good use for bash history is when you forget to sudo.  If you try to run a comand and get the ole "Permission denied", instead of retyping the whole command over again with a sudo in front, just type:

    sudo !!

This equates to "sudo the last thing in my bash history".

Pretty good, eh?

Let's say you have something in your history that was a long time ago, and you need to search the history for it.  You could use grep:

    history | grep mycommand

Alternately, you could use CTRL-r - smack CTRL-r and type a few letters of what you are looking for.  It should show up and be ready for execution!  If not, you can scroll through multiple things that were found by hitting CTRL-r again. 

This is really just the beginning.  You can go way down the bash history rabbit hole.  One last example and I'll carry move on - let's say you botched some spelling in your last command:

    touch /etc/documentszd

Whoops!  That should say documents...good news, just type:

    ^documentszd^documents^

Boom goes the dynamite.  You are made whole.

I forget all the deeper features of bash history and have to find refreshers on the web - but maybe this brief introduction will help someone with the basics.  

# wget 

This is really an unrelated side note, but one I wanted to mention.  I've seen a few people not understanding what wget does, and using it the wrong way.  So I just wanted to share.  wget is a command line tool for retrieving files via HTTP,HTTPS and FTP.

People are using it to activate API calls:

    wget http://blahhlachaksdjlskjdf.com/mything.php

That works, but you are going to wind up downloading the output onto your filesystem.  If you must use wget instead of curl, be sure to pass it some flags to let it know you want the output sent to the garbage can (dev null).

    wget --quiet -O /dev/null http://baklhalsdhjflskdjalk.com/mything

That should work.

Have a great day.  :-) 

## UPDATE!

[Justin Ellingwood at DigitalOcean][2] has a much [much more detailed exposition on bash history here.][2].

[1]: http://www.linuxmint.com/	"Linux Mint"
[2]: https://www.digitalocean.com/community/tutorials/how-to-use-bash-history-commands-and-expansions-on-a-linux-vps "Bash History"
