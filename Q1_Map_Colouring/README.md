# Map Coloring using CSP and Backtracking

This project implements the **Map Coloring Problem** using a **Constraint Satisfaction Problem (CSP)** approach with **Backtracking**.

The goal is to assign colors to regions (states) such that no two neighboring states share the same color.

---

## Problem Description

Given:
- A set of states (regions)
- A list of neighboring states
- A set of colors

Objective:
- Assign a color to each state
- Ensure no adjacent states have the same color

---

## States
- WA 
- NT
- Q
- SA
- NSW
- V
- T

  
---

## Colors

- Red
- Green
- Blue

---

## Constraints

- Neighboring states must not have the same color.
- Each state must be assigned exactly one color.

---

## Approach

This solution uses:

### 1. Backtracking Algorithm
- Assign colors recursively
- If a conflict occurs, undo the assignment (backtrack)
- Try the next possible color

### 2. Validity Check
- Before assigning a color, check if any neighbor already has the same color

---


---

## Example Input
Enter state: WA
Enter color: Red

---

## Example Output
WA : Red
NT : Green
Q : Red
SA : Blue
NSW : Green
V : Red
T : Red

---

## Key Concepts

- Constraint Satisfaction Problems (CSP)
- Backtracking Search
- Recursive Algorithms
- Graph Coloring

---

Name: J.REDDY SAI NANDAN
