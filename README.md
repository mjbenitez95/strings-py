# Cracking the Coding Interview
This repo contains Python 2 implementations of string/list coding challenges
from the Cracking the Coding Interview book. Each program is intended to solve
a challenge, as indicated below. For each solution, I'm simplifying the string
to only lowercase letters, and performing the algorithm on those.

# 1.1: Is Unique
unique.py is for the following: Implement an algorithm to determine if a string
has all unique characters. What if you cannot use additional data structures?

# 1.2: Check Permutation
permutation.py is for the following: Given two strings, write a method 
to decide if one is a permutation of the other.

# 1.3: URLify
url.py is for: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the 
additional characters and that you are given the "true" length of the string.

# 1.4: Palindrome Permutation
palindrome.py is for the following: Given a string, write a function to check
if it is a permutation of a palindrome. A palindrome is a word or phrase that
is the same forwards and bakcwards. A permutation is a rearrangement of 
letters. The palindrome does not need to be limited to just dictionary words.

# 1.5: One Away
one_away.py is for the following: There are three types of edits that can be
performed on strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they are one edit
(or zero edits) away.

# 1.6 String Compression
compress.py is for the following: Implement a method to perform basic string
compression using the counts of repeated characters. For example, the string 
'aabcccccaaa' would be come 'a2b1c5a3'. If the "compressed" string would not 
become smaller than the original string, your method should return the original
string.