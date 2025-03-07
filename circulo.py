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
        self.titulo = QLabel("Circulo Relleno", self)
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

        # Xc
        self.label_xc = QLabel("Xc:", self)
        self.label_xc.setGeometry(930, 100, 60, 30)
        self.input_xc = QLineEdit(self)
        self.input_xc.setGeometry(970, 100, 60, 30)

        # Yc
        self.label_yc = QLabel("Yc:", self)
        self.label_yc.setGeometry(1040, 100, 60, 30)
        self.input_yc = QLineEdit(self)
        self.input_yc.setGeometry(1080, 100, 60, 30)

        #Radio 
        self.label_radio = QLabel("Radio", self)
        self.label_radio.setGeometry(930, 140, 60, 30)
        self.input_radio = QLineEdit(self)
        self.input_radio.setGeometry(970, 140, 60, 30)

        # Establecer colores para los inputs
        self.input_xc.setStyleSheet("background-color: lightgreen; color: black;")
        self.input_yc.setStyleSheet("background-color: lightgreen; color: black;")
        self.input_radio.setStyleSheet("background-color: lightyellow; color: black;")
        # Establecer colores para los labels
        self.label_xc.setStyleSheet("color: red; font-weight: bold; ")
        self.label_yc.setStyleSheet("color: red; font-weight: bold;")
        self.label_radio.setStyleSheet("color: blue; font-weight: bold;")

        # btn_Trazar linea
        self.btn_trazar = QPushButton("Trazar Circulo", self)
        self.btn_trazar.setGeometry(1150, 100, 100, 30)
        self.btn_trazar.setStyleSheet("background-color: lightgray; color: black;")

        # btn_Limpiar
        self.btn_limpiar = QPushButton("Limpiar", self)
        self.btn_limpiar.setGeometry(1150, 140, 100, 30)
        self.btn_limpiar.setStyleSheet("background-color: lightgray; color: black;")
        # Establecer colores para los botones
        self.btn_trazar.setStyleSheet("background-color: lightblue; color: lightblack; font-weight: bold;")
        self.btn_limpiar.setStyleSheet("background-color: lightcoral; color: lightblack; font-weight: bold;")

        # Layout principal
        self.layout = QVBoxLayout()

        self.PK_label = QLabel("Parametro PK", self)
        self.PK_label.setGeometry(950, 190, 120, 30)
        self.PK_label.setStyleSheet("font-size: 15px;background-color: lightcoral;  color: black;padding: 5px;")
        # Crear QLabel para mostrar las coordenadas
        self.parametro = QLabel(self)
        self.parametro.setStyleSheet("background-color: white; color: black; font-size: 15px; padding-left: 10px;")
        self.parametro.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        self.puntos_siguientes_label = QLabel("Xk + 1, Yk -1", self)
        self.puntos_siguientes_label.setGeometry(1150, 190, 120, 30)
        self.puntos_siguientes_label.setStyleSheet("font-size: 15px;background-color: lightcoral; color: black;padding: 5px;")

        # Crear QLabel para mostrar las coordenadas
        self.puntos_siguientes = QLabel(self)
        self.puntos_siguientes.setStyleSheet("background-color: white;  color: black; font-size: 15px; padding-left: 15px;")
        self.puntos_siguientes.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        self.puntos_circulo_label = QLabel("Puntos Circulo", self)
        self.puntos_circulo_label.setGeometry(1345, 190, 120, 30)
        self.puntos_circulo_label.setStyleSheet("font-size: 15px;background-color: lightcoral; color: black; padding: 5px;")
        # Crear QLabel para mostrar las coordenadas
        self.puntos_circulo = QLabel(self)
        self.puntos_circulo.setStyleSheet("background-color: white;color: black; font-size: 15px; padding-left: 10px;")
        self.puntos_circulo.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear QScrollArea para contener el QLabel y permitir desplazamiento
        self.scroll_ps = QScrollArea()
        self.scroll_ps.setWidgetResizable(True)  # Permite que el QLabel se adapte
        self.scroll_ps.setWidget(self.puntos_siguientes)  # Agregar QLabel al área de scroll
        self.scroll_ps.setFixedSize(120, 350)  # Mantiene un tamaño fijo sin expandirse
        # Agregar widgets al layout
        self.layout.addWidget(self.scroll_ps)  # Agrega el QLabel dentro del ScrollArea
        self.layout.setContentsMargins(880, 10, 0, 0)  # Posiciona el QLabel en la ventana
        self.setLayout(self.layout)

        self.scroll_p = QScrollArea()
        self.scroll_p.setWidgetResizable(True)  
        self.scroll_p.setWidget(self.parametro)  
        self.scroll_p.setFixedSize(120, 350)  

        self.layout.addWidget(self.scroll_p)  

        self.scroll_pc = QScrollArea()
        self.scroll_pc.setWidgetResizable(True)  
        self.scroll_pc.setWidget(self.puntos_circulo)  
        self.scroll_pc.setFixedSize(120, 350)  

        self.layout.addWidget(self.scroll_pc)  


        # Layout horizontal para las coordenadas
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.scroll_p)
        self.horizontal_layout.addWidget(self.scroll_ps)
        self.horizontal_layout.addWidget(self.scroll_pc)

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
        altura_x = 300  # Altura en la que se traza el eje X
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
            r = int(self.input_radio.text())
            self.dibujar_circulo(xc, yc, r)
        except ValueError:
            self.puntos_siguientes.setText("Error: Ingresa valores válidos")

    def dibujar_circulo(self, xc, yc, r):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50
        centro_x = margen + ancho / 2
        centro_y = margen + altura / 2

        # Inicializar variables
        x = 0
        y = r
        p = 1 - r  # Parámetro de decisión inicial
        puntos = []
        # Lista para almacenar todos los puntos del círculo
        puntos_circulo = []
        parametro = []

        # Dibujar los puntos iniciales y guardarlos en la lista
        self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y, puntos_circulo)

        # Algoritmo de punto medio para el círculo
        while x < y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
            # Dibujar y guardar los puntos en cada iteración
            parametro.append(p)
            puntos.append((x, y))
            self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y, puntos_circulo)

        self.parametro.setText("\n" + "\n".join([f"[ {x} ]" for x in parametro]))
        self.puntos_siguientes.setText("\n" + "\n".join([f"[ {x}, {y} ]" for x, y in puntos]))
        # Mostrar los puntos en la QLabel
        self.mostrar_puntos_en_label(puntos_circulo)

    def dibujar_puntos_circulo(self, xc, yc, x, y, centro_x, centro_y, puntos_circulo):
        # Dibujar los 8 puntos de simetría del círculo
        ancho, altura = 800, 500
        puntos = [
            (xc + x, yc + y),  # Primer octante
            (xc - x, yc + y),  # Segundo octante
            (xc + x, yc - y),  # Tercer octante
            (xc - x, yc - y),  # Cuarto octante
            (xc + y, yc + x),  # Quinto octante
            (xc - y, yc + x),  # Sexto octante
            (xc + y, yc - x),  # Séptimo octante
            (xc - y, yc - x),  # Octavo octante
        ]

        # Agregar los puntos a la lista
        puntos_circulo.extend(puntos)

        # Dibujar cada punto en la escena
        pen = QPen(Qt.GlobalColor.red, 3, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        for px, py in puntos:
            px_scene = centro_x + px * (ancho / 1000)
            py_scene = centro_y - py * (altura / 1000)
            self.scene.addEllipse(px_scene, py_scene, 2, 2, pen)
            self.rellenar_circulo(xc, yc, puntos)
        
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
        pen = QPen(Qt.GlobalColor.red, 0.9, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)  # Lápiz para las líneas
        for px, py in puntos:
            px_scene = centro_x + px * (ancho / 1000)
            py_scene = centro_y - py * (altura / 1000)
            self.scene.addLine(xc_scene, yc_scene, px_scene, py_scene, pen)

    def mostrar_puntos_en_label(self, puntos_circulo):
        # Formatear la lista de puntos como una cadena de texto
        texto_puntos = "Puntos del círculo:\n"
        for punto in puntos_circulo:
            texto_puntos += f"[ {punto[0]}, {punto[1]} ]\n"

        # Mostrar los puntos en la QLabel
        self.puntos_circulo.setText(texto_puntos)

    def limpiar_escena(self):
        self.scene.clear()
        self.dibujar_grafica()
        self.parametro.clear()
        self.puntos_siguientes.clear()
        self.input_radio.clear()
        self.puntos_circulo.clear()
        self.input_xc.clear()
        self.input_yc.clear()
        self.puntos_siguientes.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()