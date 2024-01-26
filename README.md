# Text Encoder

This simple encoder programme is a little project to practice object-oriented coding as well as unittesting. Some features such as generating a random number are already implemented in the respective modules, but I thought it would be fun to code something like this myself. 

## How does it work?

The encoder can encode and decode texts (strings). It does so by following these steps:

1. A Seed for the Random Number Generator (RNG) is chosen. This could be without a password (the exact ms time will be chosen and converted into a number), or with a password (each password symbol will be translated into a number). For more information about the RNG used here, see below.
2. Based on the random number generator, all available characters are shuffled. The output is a string where the original characters have been replaced with the suffled ones.
3. Decoding is done by using the reverse. If the same seed is chosen, the shuffle is reversed to te original characters.


## The RNG

For this project, I am using an RNG based on `numpy.random` (https://numpy.org/devdocs/reference/random/index.html). The RNG produces deterministic sequences based on a seed (usually an integer number). Therefore, the encoder will encode a string in exactly the same way if the same seed is used. This additionally is used to decode the encoded text as well.

## Next steps

- Extend functionality to encode text files
- Add a 'Getting started' description and perhaps a 'try out file'
