# ANAGRAMARAMA

## Anagram program

This program has several functions:

### See a chart showing letter point values

This just prints out the values of various letters.  I used the point values assigned to them in Scrabble.

### Check if a word is in my dictionary

This lets a user enter a string and the program reports whether it's in the dictionary.  The program generates a 
dictionary from scrabble.txt, which is simply a wordlist from the Moby project at http://icon.shef.ac.uk/Moby/mwords.html.

### Find anagrams of a word or series of letters

This lets users enter a string and the program will list all of the anagrams using that set of letters.

### Determine the score for a word.

Calculates the base score for a set of letters, using Scrabble point values.

### Play Anagramarama

See next section.

### Quit

Exits the program.

## Anagramarama

This is a simple anagram game.  They player is presented with a set of letters from which to create a word.  When 
a valid word is played, the letters used are replaced with new ones from a tile bag.  The game ends when
there are no valid plays and the tile bag is empty.  Alternatively, the user can "play" the letter x (an obvious 
nonword) to exit the game.

## Future development

Implement scoring.  Create Human and Computer children of Player object, so the player can see what the highest possible
score was for their game.  Possibly develop a GUI interface using tile-like objects.