# Dispersion Calculator

Turned my math assignment into code. Calculates statistical measures (range, variance, std dev, IQR) from a dataset and makes a box plot.

## Background
Had a math assignment about price dispersion analysis (see `OriginalAssignment.pdf`). Instead of just doing the math manually, I wrote a Python script to do it. Figured it'd be good practice with classes and numpy.

## What it does
- Reads prices from `prices.txt`
- Calculates: range, mean, variance, standard deviation, IQR
- Generates a box plot visualization

## Setup
```bash
pip install numpy matplotlib
python main.py
```

## File structure
- `compute_dispersion.py` - Main class that does the calculations
- `main.py` - Runs everything
- `prices.txt` - Dataset (one price per line)
- `OriginalAssignment.pdf` - The original math assignment

## Why I made this
Wanted to practice:
- Object-oriented programming (classes)
- Working with numpy for stats
- Reading data from files
- Basic matplotlib plotting

Could've just used Excel but i could use this too so why not? ;)
