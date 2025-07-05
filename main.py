import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QPixmap
from PIL import Image, ImageQt
import sympy as sp
import numpy as np
import pyperclip


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Calculator")
        self._create_icon()
        self.history = []
        self._read_history()

        self.display = QLineEdit()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display)
        self.buttons = QGridLayout()
        self._add_buttons()
        self.layout.addLayout(self.buttons)
        self.setLayout(self.layout)

    def _create_icon(self):
        # create a simple checkerboard icon using Pillow
        img = Image.new("RGBA", (32, 32), (255, 255, 255, 0))
        for i in range(32):
            for j in range(32):
                if (i + j) % 2 == 0:
                    img.putpixel((i, j), (0, 0, 0, 255))
        qt_img = ImageQt.ImageQt(img)
        pix = QPixmap.fromImage(qt_img)
        self.setWindowIcon(QIcon(pix))

    def _add_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('Copy', 4, 1, 1, 3)
        ]
        for spec in buttons:
            text, row, col = spec[0], spec[1], spec[2]
            rowspan = spec[3] if len(spec) > 3 else 1
            colspan = spec[4] if len(spec) > 4 else 1
            btn = QPushButton(text)
            btn.clicked.connect(self._on_clicked)
            self.buttons.addWidget(btn, row, col, rowspan, colspan)

    def _on_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == 'C':
            self.display.clear()
        elif text == '=':
            expr = self.display.text()
            try:
                # use sympy to safely evaluate the expression
                result = sp.sympify(expr).evalf()
                # convert to numpy float for demonstration
                result_np = np.float64(result)
                self.display.setText(str(result_np))
                self.history.append({'expr': expr, 'result': float(result_np)})
                self._write_history()
            except Exception:
                self.display.setText('Error')
        elif text == 'Copy':
            pyperclip.copy(self.display.text())
        else:
            self.display.insert(text)

    def _read_history(self):
        if os.path.exists('history.json'):
            try:
                with open('history.json', 'r') as fh:
                    self.history = json.load(fh)
            except Exception:
                self.history = []

    def _write_history(self):
        try:
            with open('history.json', 'w') as fh:
                json.dump(self.history, fh, indent=2)
        except Exception:
            pass


def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
