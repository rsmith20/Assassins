# Verbal Assasins

This is a script to assist running a variant on the game of Assasins.

In this game, every person has a target, and every person is targetted by someone else.

Your goal is to get your target to say a particular word, and to avoid saying the particular word
of whoever is targetting you. TO make it harder, you don't know who this is.

After you kill someone, you gain their target (presevers the ordering of the cycle). You also need a new
word.

The larger script will help setup the cycle and divy out initial words.
The smaller script will give a single word.

Both have internal details that should probably be modifiable via command line arguments,
but until then you'll have to modify code to make changes. To use, simply type 

```
python AssasinsScript.py
```

for the initial setup and 
```
python SingleWord.py
```
for a single word.


This has been tested using Windows 10 and Python 3.5.
