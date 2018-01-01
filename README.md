# moe° Bot

moe° bot is an application of ``illustration2vec (i2v)`` on telegram platform.  
It can calculate the degrees of moe from your pictures.

# About characteristic of moe

"Moe" (萌え, pronounced as "Mo-Eh", derived from a Japanese word that means "budding, to sprout/bloom"), is an ill-defined otaku term that means, amongst other things, "cute", "huggable", or "endearing".  
A common definition is that Moe is the ability of a character to instill in the audience an irrational desire to adore them, hug them, protect them, comfort them, etc.  
  
Retrieved January 1, 2018, from [*tvtropes/Moe*](http://tvtropes.org/pmwiki/pmwiki.php/Main/Moe)

# Installation

```
$ git clone --recursive https://github.com/Yuessiah/moe-degree-bot.git  
$ mv moe-degree-bot/
$ pip install -r requirements.txt  
$ ./illustration2vec/get_models.sh  
```
manually install caffe library http://caffe.berkeleyvision.org/installation.html ,  
and follow the issue https://github.com/rezoo/illustration2vec/issues/6 to fix some wrong in code.   

# Usage

create a bot in telegram, https://core.telegram.org/bots  
replace `<token>` in app.py code by your token of bot.  
then `$ ./app.py`
