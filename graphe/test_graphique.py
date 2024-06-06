import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt

import map
import parcours

#################################################################################
# Programme graphique permettant de visualiser les graphes dans un but de DEBUG
#################################################################################

class CaseWidget(QWidget):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.has_article = False
        self.is_in_path = False
        self.is_start = False
        self.is_end = False
        self.order_label = QLabel(self)  # qlabel pour indiquer l'ordre de apssage
        self.order_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.order_label.hide()  

    def set_article(self, has_article):
        self.has_article = has_article
        self.update()

    def set_in_path(self, is_in_path, order=None):
        self.is_in_path = is_in_path
        self.update()
        if order is not None:
            self.order_label.setText(str(order))
            self.order_label.show()
        else:
            self.order_label.hide()

    def set_start(self, is_start):
        self.is_start = is_start
        self.update()

    def set_end(self, is_end):
        self.is_end = is_end
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.is_start:
            painter.setBrush(QColor(255, 165, 0))  # point de départ orange
        elif self.is_end:
            painter.setBrush(QColor(0, 0, 255))  # point d'arrivé bleu
        elif self.is_in_path:
            painter.setBrush(QColor(0, 255, 0))  # vert pour le chemin
        elif self.has_article:
            painter.setBrush(QColor(255, 0, 0))  # rouge pour les articles
        else:
            painter.setBrush(QColor(255, 255, 255)) 
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

        depart = self.supermarche.get_depart()
        arrivee = self.supermarche.get_arrivee()

        self.cells[depart].set_start(True)
        self.cells[arrivee].set_end(True)

        for order, (x, y) in enumerate(self.chemin_optimal):
            self.cells[(x, y)].set_in_path(True, order + 1)

        self.setWindowTitle('Supermarché')
        self.showMaximized()

def main():
    app = QApplication(sys.argv)

    supermarche = map.mapping("supermarche.json", "articles.json")

    points_interet = [(0, 5), (3, 2)]
    depart = supermarche.get_depart()
    arrivee = supermarche.get_arrivee()

    print(parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet))
    chemin_optimal = parcours.parcours_opti(supermarche.get_parcours(), depart, arrivee, points_interet)

    main_window = MainWindow(supermarche, chemin_optimal)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
