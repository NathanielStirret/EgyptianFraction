# Egyptian Fraction Decomposition

## Description

This program implements Egyptian Fraction Decomposition. This algorithm takes any fraction and expresses it as a sum of unit fractions (1/den). It does this by repeatedly subtracting and storing the largest unit fraction that is less than the remainder of the initial fraction.

## Greedy
This algorithm does not need to sort anything because we simply take the largest unit fraction that is still less than the remaining value. To compute the denominator of this unit fraction, I take the ceiling of the denominator divided by the numerator. Then I subtract the reciprocal of this number from the remainder and store it. After that, I simplify the fraction and repeat the process.

### Video

https://www.youtube.com/watch?v=aVUUbNbQkbQ

### Wikipedia Page

https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions


## Program

This program takes a user inputted Numirator and denominator, then it calcualtes the Egyptian Fraction Decomposition

### Running it

#### prerequisites 
Python 3.14.3

Although Python 3 *should* come with these libraries pre installed, if they don't here are the ones I used so one can pip them

- Math

