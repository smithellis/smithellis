Title: ExpressionEngine Ugprader, EEupgrade
Date: 03/25/2015 7:00
Tags: eecms,ExpressionEngine,bash,hack

# Batteries Not Included

My biggest gripe about the ExpressionEngine CMS is that everything you need to manage a large site is *not included* with the core codebase.  You need plug-ins and add-ons to make the system robust for your users - and it turns out that most of them are not free.  In fact, most of them aren't even cheap.

The community around EE is very profit motivated.  I'm a developer, and a human, and kind of a capitalist pig - so I respect this.  But on the other hand, the product has a pretty steep cost just to get a license, then you feel a little nickle and dimed to death as you realize that you need stuff it doesn't have.  

Complaints without examples are just complaints, so here are some things I've ponied up for:  

+ Better caching
+ Simpler templating
+ Simpler choices for users
+ Simpler page management for users
+ Better SEO
+ More robust fieldtypes

Ok, so all that said - it's done.  We have spent our money, and it's a pretty cool offering after all that.  But then, lo and behold, it's time for me to do an upgrade of the system and here is the process:

+ Go log in to Ellislab.com
+ Download the new version zip file
+ Expand the zip file
+ Backup my existing system
+ Move folders over
+ Change a bunch of permissions (chmod)
+ Run the web based installer
+ Change a bunch of persmissions
+ Delete a folder
+ Blahblah

It seems to me that an improved update process would be table stakes on a product like this.  But I guess not.  In keeping with the nickel and dime aspect, you can pay for an updater plugin that does a lot of this work for you.

Assuming you aren't made of money, you can do other stuff...and maybe I can help you.

## I Wrote You This Script

I made a bash script to handle a bunch of the file moving and permissioning for you.  I'm guessing it will save you 20 minutes of work.  You still need to do your own database backups, but otherwise I think it's pretty solid.  You can grab [eeupgrade by clicking here and going to github][1].  It's at [https://github.com/smithellis/eeupgrade][1] if you prefer to type links.

Anyway, I like ExpressionEngine ok - for managing a huge site like the one I currently own, it's pretty robust.  But I have gripes about missing features and the pay-to-play model for functionality that should just plain be included.

[1]: https://github.com/smithellis/eeupgrade	"bash script to upgrade ee"
