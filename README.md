# Friendly Octo Telegram

This repository contains a simple calculator implemented with **PyQt6**. The calculator uses `sympy` for expression evaluation, `numpy` for numeric conversion, `Pillow` to generate an icon, and `pyperclip` for clipboard support. Calculation history is saved to `history.json`.

## Setup

Create a Python virtual environment and install the dependencies listed in `requirements.txt`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

After activating the virtual environment, start the GUI with:

```bash
python main.py
```

The application window provides buttons for digits and basic arithmetic operations. Use the **Copy** button to copy the current result to the clipboard.
