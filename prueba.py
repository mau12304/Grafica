# from PyQt6.QtWidgets import (
#     QApplication,
#     QWidget,
#     QGraphicsView,
#     QGraphicsScene,
#     QGraphicsLineItem,
#     QGraphicsTextItem,
#     QVBoxLayout,
#     QPushButton,
#     QLineEdit,
#     QLabel,
#     QHBoxLayout,
#     QScrollArea,
# )

# class HojaCalculo(QWidget):
#     def __init__(self):
#         super().__init__()

#         ancho_v = 1450
#         altura_v = 750
#         porsicion_x = 50  # izquierda y derecha
#         porsicion_y = 50  # arriba y abajo
#         self.setWindowTitle("PyQt6 Grafica Con Axes")  # Título de la ventana
#         self.setGeometry(porsicion_x, porsicion_y, ancho_v, altura_v)
#         self.setStyleSheet("background-color: rgb(176, 208, 228);")
#         self.dibujarHoja()
    
#     def dibujarHoja(self):

#         self.extendida =  QLabel("Extendida", self)
#         self.extendida.setGeometry(530, 100, 60, 30)
#         self.input_extendida  = QLineEdit(self)
#         self.input_extendida.setGeometry(600, 100, 60, 30)
#         self.setStyleSheet("background-color: lightcoral;")



# if __name__ == "__main__":
#     app = QApplication([])
#     window = HojaCalculo()
#     window.show()
#     app.exec()
xc , x, yc, y = 10, 3, 15, 4



puntos = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ]


completo = []
for px, py in puntos:
    completo.append(f"[ {px}, {py} ]")

print(completo)