# Text Encoder

This is a little project to practice object-oriented coding as well as unittesting and hosting on git.

## How does it work?

The encoder can encode and decode texts (strings). It does so by following these steps:

1. A Seed for the Random Number Generator (RNG) is chosen. This could be without a password (the exact ms time will be chosen and converted into a number), or with a password (each password symbol will be translated into a number). For more information about the RNG used here, see below.
2. Based on the random number generator, all available characters are shuffled. The output is a string where the original characters have been replaced with the suffled ones.
3. Decoding is done by using the reverse. If the same seed is chosen, the shuffle is reversed to te original characters.


## The RNG
For this project, I am using an RNG based on `numpy.random` (https://numpy.org/devdocs/reference/random/index.html)
