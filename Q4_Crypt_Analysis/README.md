# Cryptarithmetic Solver

This project solves **Cryptarithmetic (Alphametic) puzzles**.

Each letter is assigned a unique digit (0–9), and all possible combinations are tested until a valid solution is found.

---

## Problem Description

Given:
- Two words representing numbers
- One result word

Objective:
WORD1 + WORD2 = RESULT

Example:
Input:
- Enter first word: send 
- Enter second word: more
- Enter result word: money

  Output:
- y : 2
- s : 9
- o : 0
- m : 1
- n : 6
- d : 7
- e : 5
- r : 8

  
---

## Approach (Brute Force)

- Extract all unique letters from the input
- Generate all possible digit permutations using `itertools.permutations`
- Assign digits to letters
- Convert words into numbers
- Check if:
  - Equation holds
  - Leading letters are not zero

---

## Constraints

- Each letter maps to a unique digit (0–9)
- Maximum 10 unique letters
- Leading letters cannot be `0`

---
Name :J.REDDY SAI NANDAN
