# Kutai NFT Generator
Kutai NFT Generator is a Random Generative Engine for creating random generative artworks/collections using Python code. This project idea was inspired by Hashlips Art Engine. This project is trying to solve/add more features that do not exist in Hashlips Art Engine. I may add more functions/scripts like "rule" that have logic in it that is able to exclude some attributes for being chosen.  

Anyway, what I'm trying to do is to make it as simple as possible, so users with no programming background are able to use it.

## How to use it?
You can try it by running [test.py](test.py).
```terminal
python test.py
```
or you can try to create custom folder by executing the command line below
```terminal
python manage.py generate <n-output> <output-destination>
```
It will create a source folder including attributes.json, config.json, probability.json, and source.svg files in it. _Make sure the layers folder is not empty_.

All png files in the layers folder should be written in `index_trait-type_trait-name.png` format. Underscore ("\_") character will be the delimiter as it is being read by the scripts/functions.

## Make sure you install all the requirements
```terminal
pip install -r requirements.txt
```
