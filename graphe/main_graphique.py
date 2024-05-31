import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt

import map
import parcours

class CaseWidget(QWidget):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.has_article = False
        self.is_in_path = False

    def set_article(self, has_article):
        self.has_article = has_article
        self.update()

    def set_in_path(self, is_in_path):
        self.is_in_path = is_in_path
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.is_in_path:
            painter.setBrush(QColor(0, 255, 0))  # Green for path
        elif self.has_article:
            painter.setBrush(QColor(255, 0, 0))  # Red for articles
        else:
            painter.setBrush(QColor(255, 255, 255))  # White for empty
        painter.drawRect(0, 0, self.width(), self.height())

class MainWindow(QMainWindow):
    def __init__(self, supermarche, chemin_optimal):
        super().__init__()

        self.supermarche = supermarche
        self.chemin_optimal = chemin_optimal

        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()
        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

        max_x = max([x for x, y in self.supermarche.get_parcours().keys()])
        max_y = max([y for x, y in self.supermarche.get_parcours().keys()])

        self.cells = {}
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                cell = CaseWidget(x, y)
                grid_layout.addWidget(cell, y, x)
                self.cells[(x, y)] = cell

        for (x, y), case in self.supermarche.cellules.items():
            if case.articles:
                self.cells[(x, y)].set_article(True)

        for (x, y) in self.chemin_optimal:
            self.cells[(x, y)].set_in_path(True)

        self.setWindowTitle('Supermarché')
        self.show()

def main():
    app = QApplication(sys.argv)

    supermarche = map.mapping("supermarche.json", "articles.json")

    points_interet = [(0, 5), (3, 2)]
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()

    chemin_optimal = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)

    main_window = MainWindow(supermarche, chemin_optimal)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
