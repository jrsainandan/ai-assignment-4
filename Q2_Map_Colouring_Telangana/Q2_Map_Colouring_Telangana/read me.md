# Telangana Map Coloring using CSP and Backtracking

This project solves the **Map Coloring Problem** for Telangana districts using a **Constraint Satisfaction Problem (CSP)** approach with **Backtracking**.

The goal is to assign colors to each district such that no two neighboring districts share the same color.

---

## Problem

Given:
- A set of districts (states)
- Adjacency relationships (edges)
- A set of colors

Objective:
- Assign one color to each district
- Ensure no neighboring districts have the same color

---

## States (Districts)

- Adilabad  
- KomaramBheem  
- Nirmal  
- Mancherial  
- Nizamabad  
- Kamareddy  
- Karimnagar  
- Peddapalli  
- Jagtial  
- RajannaSircilla  
- WarangalUrban  
- WarangalRural  
- Jangaon  
- Mahabubabad  
- BhadradriKothagudem  
- Khammam  
- Suryapet  
- Nalgonda  
- YadadriBhuvanagiri  
- MedchalMalkajgiri  
- Hyderabad  
- Rangareddy  
- Vikarabad  
- Sangareddy  
- Medak  
- Siddipet  
- JayashankarBhupalpally  
- Mulugu  
- Nagarkurnool  
- Wanaparthy  
- JogulambaGadwal  
- Narayanpet  
- Mahabubnagar  

---

## Colors

- Red  
- Green  
- Blue  
- Yellow  

---

## Input File (TelanganaMap.json)

The program reads input from a JSON file containing:
- `states` → list of districts  
- `edges` → neighboring relationships  
- `colours` → available colors  

---

## Approach

### Backtracking Algorithm
- Select an unassigned district  
- Try assigning a valid color  
- Recursively continue  
- Backtrack if constraints are violated  

### Constraint Checking
- Before assigning a color, check all neighbors  
- Reject assignment if any neighbor has the same color  


---

## Example Input
Enter state: Hyderabad
Enter color: Red


---

## Example Output
- Adilabad : Red
- KomaramBheem : Green
- Nirmal : Green
- Mancherial : Red
- Nizamabad : Red
- Kamareddy : Red
- Karimnagar : Red
- Peddapalli : Green
- Jagtial : Red
- RajannaSircilla : Red
- WarangalUrban : Red
- WarangalRural : Green
- Jangaon : Red
- Mahabubabad : Red
- BhadradriKothagudem : Red
- Khammam : Red
- Suryapet : Green
- Nalgonda : Red
- YadadriBhuvanagiri : Green
- MedchalMalkajgiri : Red
- Hyderabad : Red
- Rangareddy : Green
- Vikarabad : Red
- Sangareddy : Red
- Medak : Red
- Siddipet : Green
- JayashankarBhupalpally : Red
- Mulugu : Red
- Nagarkurnool : Red
- Wanaparthy : Green
- JogulambaGadwal : Red
- Narayanpet : Green
- Mahabubnagar : Red
---

## Key Concepts

- Constraint Satisfaction Problems (CSP)  
- Backtracking Search  
- Graph Coloring  
- Recursion  

---
Name: J.REDDY SAI NANDAN
