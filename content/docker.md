Title: Docker on Ubuntu
Date: 12/07/2014 20:00
Tags: Docker,Containers

Docker is a tool that lets you develop and run applications in consistent environment.  It's different from a VM (or something like Vagrant) in that it doesn't include the full OS stack.  When you think of a VM, you are thinkin about a full guest OS running in a container on your computer - Docker is a container that only holds your application and its dependencies.  Small and fast!

On ubuntu, it's pretty easy to get up and running if you pay attention - the package is called "docker.io"...not "docker".

So, fire up the command line and go nuts:

    sudo apt-get update
    sudo apt-get install docker.io

Shampow - you now have it installed.  Using Docker is beyond the scope of my write up here - but an example from the documentation goes something like this:

    sudo docker run ubuntu:14.04 /bin/echo 'Hellow world'
    Hello world

This bit of code calls the docker binary and tells it we want to run a container; specifically, we want to run an Ubuntu 14.04 image and in that image execute the /bin/echo command to print "Hello world".  Pretty cool.  When the command was executed, the container was used, and then the container was closed.

Play around and have fun.  Check out the [Docker docs](http://docs.docker.com) for more/better information.  

