# Hoffman algorithm

## Description

This program implements Huffman Coding, an algorithm that has been used for data compression. The general idea is to represent more common characters with fewer bits.

The program asks the user for a string, counts how often each character appears, builds a Huffman tree, and then prints the binary code for each character.

## Greedy
This algorithm sorts by frequency lowest to highest. By pushing nodes down it guarantees that the rarest nodes are at the bottom and the most common are at the top. Then when you traverse the tree to decode it the path you take to the node determines the assignment, right is one left is zero.

### Video

https://www.youtube.com/watch?v=iEm1NRyEe5c

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

