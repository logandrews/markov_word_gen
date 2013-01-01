# Markov Chain Word Generator
Uses Markov Chains to generate lists of potentially new words from example word lists (which can be generated from example texts).

## Generating Word Lists From Texts
To generate a new word list, use the prepare script giving the name of a text file as a parameter. Two example texts from the public domain are provided: text_english and text_latin. The word lists are print to stdout and need to be redirected to a file.

## Generating New Words From Word Lists
To generate a new words, use the main script giving the name of a word list file as a parameter. Two example word lists, which are generated from the included public domain texts, are provided: words_english and words_latin.

### Example Output
```
$ ./main words_english
mccasin
ent
mate
placked
stricklant
ass
twohum
weetirries
cascap
cribber
vour
norititle
readachedrops
socialianshion
comed
blurkilbusicial
equesty
rydaying
ste
hydraultating
```

```
$ ./main words_latin 
copulchra
dis
exerxes
deferris
eraret
obserans
morem
inthiopiam
egres
comprecatur
fulgerunt
pens
ant
regiar
videret
memei
obsignares
hominatiam
viditudi
claudelia
```

## Limitations
Currently, the prepare script removes all non-latin characters. This is a cheap hack to remove punctuation, but prevents using it for languages that use non-Latin alphabets, such as Russian.

## License
TBD
