Title: Shady web crawlers and SSH attacks
Date: 12/09/2014 7:00
Tags: crawlers,attacks,spam,security

I get a ton of traffic from what appears to be a web crawler; it originates at semalt.com.  

From reading around the webs, it looks like a questionable company doing questionable work.  I can find no positive write ups about them except their own.  It has all the hallmarks of something malicious, but I can't figure out what their point is (other than url spamming analytics accounts, and generating posts like this that get them hits).

I guess that's a clever way to generate traffic, even if it is shady.  I mean, if you see the bulk of your traffic coming from a domain, you just might click there to find out what's going on.  I think that is part of the irritation that semalt is getting - it's not like they are linking to your site or helping you advertise or...anything.  They are just jamming up your site with crawl after crawl.

Side note: since I started using [Papertrailapp](http://www.papertrailapp), I have become exceedingly aware of just how many brute force attempts are being made against every port of my home server.  What in the world??  Is this common now?  A constant barrage of ssh attacks?  I did some manual iptables work to chill them out, and then implemented fail2ban; but I'm not seeing the results I'm after.

My router's firewall appears to be much less configurable than I'd hoped, as well.  I can't seem to have it block IPs on its own; I can, of course, turn off a bunch of ports.  But what ports I have open are opened for a reason, soo....hmm.

Anyway, not a big deal - they aren't getting in; and fail2ban slows things down on the brute force side.  But still - the amount of traffic against my ip is really amazing.

That's all I have for now.  Smith Ellis, bringing you the freshest news about stuff you don't care about.  ShamPOW.
