# DATA-4000-01-Assignment5

# POS System & Inventory/API Spot Check

This repository contains two Python command-line programs:

- **Exercise 1:** Point-of-Sale (POS) System  
- **Exercise 2:** Inventory Manager with API Spot Check  

---

## Requirements

Python 3.x is required.

Install the required dependency before running Exercise 2:

```bash
pip3 install requests
```

---

# Exercise 1 – POS System

## Description

A command-line POS system that:

- Generates a numeric seed from a student key
- Accepts multiple item entries
- Applies:
  - 10% discount if:
    - Total units ≥ 10 **OR**
    - Subtotal ≥ $100
  - $3.00 perk discount if seed is odd
- Displays formatted receipt summary

## How to Run

```bash
python3 exercise1.py
```

## Example Run

```
Student key: abc

--- POS System Started (Type 'DONE' for item name to exit) ---

Item name: Apple
Unit price: 2
Quantity: 5

Item name: Bread
Unit price: 3
Quantity: 4

Item name: DONE

====================
Seed: 294
Units: 9
Subtotal: $22.00
Discount: 0%
Perk applied: NO
Total: $22.00
====================
```

---

# Exercise 2 – Inventory Manager + API Spot Check

## Description

This program has two parts:

### Part A – Inventory Entry

- Generates seed from student key
- Determines reorder threshold based on seed % 3
- Accepts SKU entries
- Flags items for reorder if below threshold

### Part B – API Spot Check

- Uses the `requests` library
- Queries the iTunes Search API
- Search term:
  - `"weezer"` if seed is even
  - `"drake"` if seed is odd
- Returns:
  - Number of songs found
  - API status (OK / FAILED / INVALID_RESPONSE)

## How to Run

```bash
python3 exercise2.py
```

## Example Run

```
Student key: abc

SKU (or 'DONE'): A100
On hand for A100: 5
Status for A100: REORDER

SKU (or 'DONE'): B200
On hand for B200: 20
Status for B200: OK

SKU (or 'DONE'): DONE

------------------------------
Seed: 294
Threshold: 15
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
------------------------------
```

---

## Summary

This repository demonstrates:

- Input validation with loops and exception handling
- Conditional business logic
- Modular function design
- API integration using `requests`
- JSON parsing and error handling

```
