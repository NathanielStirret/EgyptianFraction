# Egyptian Fraction Decomposition

## Description

This program implements Egyptian Fraction Decomposition, this algorith takes any fraction and expresses it as a sum of unit fractions (1/dem). It does this my repeatedly subtracting and storeing the largest unit fraction out of the remainder of the intial fraction.

## Greedy
This algorithm does not need to sort anything because we simply take the largest unit fraction that is still less than the remaining value. To compute the denominator of this unit fraction, I take the ceiling of the denominator divided by the numerator. Then I subtract the reciprocal of this number from the remainder and store it. After that, I simplify the fraction and repeat the process.

### Video

[https://www.youtube.com/watch?v=iEm1NRyEe5c](https://www.youtube.com/watch?v=aVUUbNbQkbQ)

### Wikipedia Page

https://en.wikipedia.org/wiki/Huffman_coding


## Program

This program takes a user inputted string and builds a hoffman tree and then uses it to build a code.

### Running it

#### prerequisites 
Python 3.14.3

Although Python 3 *should* come with these libraries pre installed, if they don't here are the ones I used so one can pip them

- heapq
- collections 

