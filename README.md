# ISM2411 — Python for Business

**Name:** Timothy Sonkin

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411 at the University of South Florida. Each code folder corresponds to a course module.

## Modules

- `week07/` — Functions: `calculate_tax`, `apply_discount`, and `final_price`, plus scope and debugging exercises.
- Module 8 — Git and GitHub setup, documented in this README, `.gitignore`, and the commit history.

## How to Run

Install Python 3, open a terminal in this repository, and run:

```bash
python3 week07/functions.py
```

The script prints examples of tax calculations, customer-tier discounts, final prices, variable scope, and sales totals. It requires no external packages.

## Reflection

### 1. What does my commit history show?

Output of `git log --oneline` before adding this reflection:

```text
2cb712c add README with module listing and run instructions
eee73ca add module 7 functions: calculate_tax, apply_discount, final_price
5b284ff add .gitignore for Python and OS files
3ab797a Initial commit
```

This history shows that the work was split into clear steps: setting up ignored files, adding the Python code, and documenting how to use it. If I were hiring someone, descriptive commits like these would help me understand their changes and see that they keep their work organized.

### 2. How should Git change the way I edit scripts?

I should make one focused change at a time, run the script to check it, and commit the working version with a clear message. Instead of overwriting a script and hoping I can undo everything later, I can compare versions and recover earlier work. I also need to push my commits so the version on GitHub matches the work on my laptop.

### 3. What else would I ignore?

I would add `.venv/` for a local Python virtual environment, and I included it in this repository's `.gitignore`. It contains installed packages and files specific to the local environment, which can be recreated and should not clutter the course repository.
