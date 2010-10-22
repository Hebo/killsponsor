killsponsor.py
=================

Introduction
------------
killsponsor.py is a script that will generate a list of binds that claim a random series of companies have sponsored your game performance.

Examples
-------
 * This kill brought to you by Umbrella Corporation!
 * This flawless frag paid for by 3M and Macy's!
 * This ownage courtesy of Amazon.com!

Usage
-----

Make sure you've installed [python 2.7](http://www.python.org/download/releases/2.7/)

1. Edit `companies-fictional.txt` and `companies-real.txt` as you like, or use the default lists
2. Edit `killsponsor.py` and choose how many binds you would like to generate (default is 80)
3. Run `killsponsor.py` to generate `binds.cfg`
4. Move `binds.cfg` to `<your TF2 folder>/cfg`
5. Add the following lines to `autoexec.cfg` in that folder:  
   `bind f4 sponsorSay`  
   `bind f5 sponsorSwitch`  
   `exec binds`
6. Ingame, press `F4` to say the sentence, and `F5` to rotate to the next one in the list