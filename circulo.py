from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsLineItem,
    QGraphicsTextItem,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QScrollArea,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen

class MyGraphic(QWidget):
    def __init__(self):

        super().__init__()
        # Dimensiones de la ventana (Vista en windows)
        ancho_v = 1450
        altura_v = 750
        porsicion_x = 50  # izquierda y derecha
        porsicion_y = 50  # arriba y abajo
        self.setWindowTitle("PyQt6 Grafica Con Axes")  # Título de la ventana
        self.setGeometry(porsicion_x, porsicion_y, ancho_v, altura_v)
        self.setStyleSheet("background-color: rgb(176, 208, 228);")
        self.dibujar_area_grafica()


    def dibujar_area_grafica(self):
        # Área gráfica (Escena grafica)
        # Título grande en la ventana
        self.titulo = QLabel("METODO DDA", self)
        self.titulo.setGeometry(600, 20, 300, 50)  # x, y, width, height
        self.titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: black;")
        ancho_e = 900
        altura_e = 600
        posicion_e_x = 10
        posicion_e_y = 95  # Más es menos y Menos es más
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setGeometry(posicion_e_x, posicion_e_y, ancho_e, altura_e)  # Posición y tamaño de la gráfica
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setStyleSheet("background-color: rgb(216, 232, 219);")


        #Xc 
        self.label_xc = QLabel("Xc:", self)
        self.label_xc.setGeometry(930, 100, 60, 30)
        self.input_xc = QLineEdit(self)
        self.input_xc.setGeometry(970, 100, 60, 30)
        
        #Yc 
        self.label_yc = QLabel("Yc:", self)
        self.label_yc.setGeometry(1040, 100, 60, 30)
        self.input_yc = QLineEdit(self)
        self.input_yc.setGeometry(1080, 100, 60, 30)
        
        self.input_xc.setStyleSheet("background-color: white;")
        self.input_yc.setStyleSheet("background-color: white;")

        #btn_Trazar linea
        self.btn_trazar = QPushButton("Trazar Triangulo", self)
        self.btn_trazar.setGeometry(1150, 100, 100, 30)
        self.btn_trazar.setStyleSheet("background-color: lightgray; color: black;")

        #btn_Limpiar
        self.btn_limpiar = QPushButton("Limpiar", self)
        self.btn_limpiar.setGeometry(1150, 140, 100, 30)
        self.btn_limpiar.setStyleSheet("background-color: lightgray; color: black;")
        
        # Layout principal
        self.layout = QVBoxLayout()

        # Crear QLabel para mostrar las coordenadas
        self.coordenadanas_A_B = QLabel(self)
        self.coordenadanas_A_B.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.coordenadanas_A_B.setWordWrap(True)  # Permite que el texto se divida en varias líneas
        # Crear QLabel para mostrar las coordenadas
        self.coordenadanas_B_C = QLabel(self)
        self.coordenadanas_B_C.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.coordenadanas_B_C.setWordWrap(True)  # Permite que el texto se divida en varias líneas
        # Crear QLabel para mostrar las coordenadas
        self.coordenadanas_C_A = QLabel(self)
        self.coordenadanas_C_A.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.coordenadanas_C_A.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear QScrollArea para contener el QLabel y permitir desplazamiento
        self.scroll_AB = QScrollArea()
        self.scroll_AB.setWidgetResizable(True)  # Permite que el QLabel se adapte
        self.scroll_AB.setWidget(self.coordenadanas_A_B)  # Agregar QLabel al área de scroll
        self.scroll_AB.setFixedSize(150, 350)  # Mantiene un tamaño fijo sin expandirse
        # Agregar widgets al layout
        self.layout.addWidget(self.scroll_AB)  # Agrega el QLabel dentro del ScrollArea
        self.layout.setContentsMargins(880, 290, 0, 0)  # Posiciona el QLabel en la ventana
        self.setLayout(self.layout)

        self.scroll_BC = QScrollArea()
        self.scroll_BC.setWidgetResizable(True)  
        self.scroll_BC.setWidget(self.coordenadanas_B_C)  
        self.scroll_BC.setFixedSize(150, 350)  

        self.layout.addWidget(self.scroll_BC)  

        self.scroll_CA = QScrollArea()
        self.scroll_CA.setWidgetResizable(True)  
        self.scroll_CA.setWidget(self.coordenadanas_C_A)  
        self.scroll_CA.setFixedSize(150, 350)  

        self.layout.addWidget(self.scroll_CA)  

        # Layout horizontal para las coordenadas
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.scroll_AB)
        self.horizontal_layout.addWidget(self.scroll_BC)
        self.horizontal_layout.addWidget(self.scroll_CA)

        # Agregar el layout horizontal al layout principal
        self.layout.addLayout(self.horizontal_layout)

        # Conectar los botones a sus respectivas funciones
        self.btn_trazar.clicked.connect(self.on_trazar_clicked)
        self.btn_limpiar.clicked.connect(self.limpiar_escena)

        # Dibujar los ejes
        self.dibujar_grafica()

    def dibujar_grafica(self):
        
        self.scene.clear()  # Limpia la escena antes de dibujar

        # Definir dimensiones del gráfico
        ancho, altura = 800, 500  # Tamaño del área del gráfico
        margen = 50  # Margen para separar el gráfico de los bordes

        # Dibujar el contorno del gráfico
        rect_pen = QPen(Qt.GlobalColor.black, 1)
        self.scene.addRect(margen, margen, ancho, altura, rect_pen)

        # Configuración de los ejes X e Y
        axis_pen = QPen(Qt.GlobalColor.black, 1.8)

        # Dibujar eje X
        inicio_x, fin_x = 50, 850  # Posición inicial y final en X
        altura_x = 300  # Altura qen la que se traza el eje X
        self.scene.addLine(inicio_x, altura_x, fin_x, altura_x, axis_pen)

        # Dibujar eje Y
        inicio_y, fin_y = 450, 550  # Posición inicial y final en Y
        margen_y_superior = 50  # Margen superior para el eje Y
        self.scene.addLine(inicio_y, margen_y_superior, inicio_y, fin_y, axis_pen)

        # Dibujar la cuadrícula
        grid_pen = QPen(Qt.GlobalColor.lightGray, 1, Qt.PenStyle.DotLine)
        num_lineas = 20  # Número de líneas de la cuadrícula

        for i in range(1, num_lineas):
            # Líneas verticales de la cuadrícula
            x = margen + i * (ancho / num_lineas)
            self.scene.addLine(x, margen, x, margen + altura, grid_pen)

            # Líneas horizontales de la cuadrícula
            y = margen + i * (altura / num_lineas)
            self.scene.addLine(margen, y, margen + ancho, y, grid_pen)

        # Agregar etiquetas a los ejes
        for i in range(-500, 600, 100):  # Rango de valores en los ejes
            # Etiquetas del eje X
            x_pos = inicio_y + i * (ancho / 1000)
            text_x = QGraphicsTextItem(f"{i}")
            text_x.setPos(x_pos - 12, altura_x - 5)
            self.scene.addItem(text_x)

            # Etiquetas del eje Y
            y_pos = altura_x - i * (altura / 1000)
            text_y = QGraphicsTextItem(f"{i}")
            text_y.setPos(inicio_y - 3, y_pos - 5)
            self.scene.addItem(text_y)
            text_x.setDefaultTextColor(Qt.GlobalColor.black)
            text_y.setDefaultTextColor(Qt.GlobalColor.black)

    def on_trazar_clicked(self):
        try:
            xc = int(self.input_xc.text())
            yc = int(self.input_yc.text())
            r = 100  # Puedes ajustar el radio o pedirlo como entrada
            self.dibujar_circulo(xc, yc, r)
        except ValueError:
            self.coordenadanas_A_B.setText("Error: Ingresa valores válidos")

    def dibujar_circulo(self, xc, yc, r):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50
        centro_x = margen + ancho / 2
        centro_y = margen + altura / 2
        puntos = []
        # Inicializar variables
        x = 0
        y = r
        p = 1 - r  # Parámetro de decisión inicial

        # Dibujar los puntos iniciales
        self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y)

        # Algoritmo de punto medio para el círculo
        while x < y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
            puntos.append((x, y))
            self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y)
            puntos_completos = self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y)
            self.coordenadanas_B_C.setText("\n" + "\n".join([f"({x}, {y})" for x, y in puntos_completos]))


        self.coordenadanas_A_B.setText("\n" + "\n".join([f"({x}, {y})" for x, y in puntos]))


    def dibujar_puntos_circulo(self, xc, yc, x, y, centro_x, centro_y):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50

        # Dibujar los 8 puntos de simetría del círculo
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

        # Dibujar cada punto en la escena
        pen = QPen(Qt.GlobalColor.blue, 3)
        for px, py in puntos:
            px_scene = centro_x + px * (ancho / 1000)
            py_scene = centro_y - py * (altura / 1000)
            self.scene.addEllipse(px_scene, py_scene, 2, 2, pen)
            self.rellenar_circulo(xc, yc, puntos)

        return puntos   

    def rellenar_circulo(self, xc, yc, puntos):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50
        centro_x = margen + ancho / 2
        centro_y = margen + altura / 2

        # Convertir el centro a coordenadas de escena
        xc_scene = centro_x + xc * (ancho / 1000)
        yc_scene = centro_y - yc * (altura / 1000)

        # Dibujar líneas desde el centro a cada punto
        pen = QPen(Qt.GlobalColor.red, 0.9)  # Lápiz para las líneas
        for px, py in puntos:
            px_scene = centro_x + px * (ancho / 1000)
            py_scene = centro_y - py * (altura / 1000)
            self.scene.addLine(xc_scene, yc_scene, px_scene, py_scene, pen)

    def limpiar_escena(self):
        self.scene.clear()
        self.dibujar_grafica()
        self.coordenadanas_B_C.clear()
        self.coordenadanas_C_A.clear()
        self.input_xc.clear()
        self.input_yc.clear()
        self.coordenadanas_A_B.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()






















    