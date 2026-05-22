# CLAUDE.md

When Claude is started in this repo, it reads this file first to gain context.

## What this project is

A CLI program designed to assist people who are calculating the sales tax rates of items across the world. It takes in the price of an item or items, the location, and said location's sales tax rate, and uses it to output the precise amount of money one would need in order to purchase the item or items.

## Stack

- Python 3.10+
- pytest

## How to run things

```bash
# Run the app
python3 app.py


# Run all tests
pytest
```

## Conventions

- When generating code, be sure to keep it in the style of CLI--do not try and apply GUI elements.
- Always refer back to the original synopsis when creating new code.
- Avoid anything that could be confidential such as credit card information, addresses, names, etc.

## Working with Claude here

- Plan before implementing.
- Run `pytest` after each substantive change.
