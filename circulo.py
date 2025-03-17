from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsLineItem,
    QGraphicsTextItem,
    QStylePainter,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QScrollArea,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen
from PyQt6.QtGui import QPainter

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
        self.graphics_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graphics_view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.graphics_view.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.graphics_view.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.graphics_view.wheelEvent = self.wheelEvent
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

        # Crear 8 QLabel para los octantes
        self.octantes_labels = []
        for i in range(8):
            label = QLabel(f"Octante {i + 1}", self)
            label.setGeometry(930 + (i % 4) * 160, 200 + (i // 4) * 120, 200, 100)
            label.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 5px;")
            label.setWordWrap(True)  # Permitir que el texto se ajuste en varias líneas
            label.setFixedSize(150, 2500)  # Establecer un tamaño fijo para las etiquetas
            self.octantes_labels.append(label)
    

        # Crear un layout horizontal para los octantes
        self.octantes_layout = QHBoxLayout()
        for label in self.octantes_labels:
            self.octantes_layout.addWidget(label)

        # Agregar el layout de octantes al layout principal
        # Crear un QScrollArea para los octantes
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(930, 200, 440, 240)  # Ajustar el tamaño y la posición según sea necesario
        self.scroll_area.setStyleSheet("background-color: lightblue;")

        # Crear un widget contenedor para los octantes y establecer el layout
        self.octantes_widget = QWidget()
        self.octantes_widget.setLayout(self.octantes_layout)

        # Establecer el widget contenedor en el QScrollArea
        self.scroll_area.setWidget(self.octantes_widget)

        # Agregar el QScrollArea al layout principal
        self.layout.addWidget(self.scroll_area)


        # Conectar los botones a sus respectivas funciones
        self.btn_trazar.clicked.connect(self.on_trazar_clicked)
        self.btn_limpiar.clicked.connect(self.limpiar_escena)


        # Crear QLabel para mostrar las coordenadas
        self.parametro = QLabel(self)
        self.parametro.setGeometry(930, 450, 440, 100)  # Ajustar la posición y el tamaño según sea necesario
        self.parametro.setStyleSheet("background-color: white; color: black; font-size: 15px; padding-left: 25px;")
        self.parametro.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear un QScrollArea para el QLabel
        self.scroll_parametro = QScrollArea(self)
        self.scroll_parametro.setWidgetResizable(True)
        self.scroll_parametro.setGeometry(930, 450, 440, 200)  # Ajustar el tamaño y la posición según sea necesario
        self.scroll_parametro.setStyleSheet("background-color: lightblue;")

        # Establecer el QLabel en el QScrollArea
        self.scroll_parametro.setWidget(self.parametro)

        # Agregar el QScrollArea al layout principal
        self.layout.addWidget(self.scroll_parametro)
        self.parametro.setStyleSheet("background-color: white; color: black; font-size: 15px; padding-left: 25px;")
        self.parametro.setWordWrap(True)  # Permite que el texto se divida en varias líneas

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
            self.octantes_labels[0].setText("Error: Ingresa valores válidos")


    def dibujar_circulo(self, xc, yc, r):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800 , 500 
        margen = 50
        centro_x =  margen + ancho / 2 
        centro_y = margen + altura / 2 

        puntos = []
        parametro = []
        octantes = [[] for _ in range(8)]
        # Inicializar variables
        x = 0
        y = r
        p = 1 - r  # Parámetro de decisión inicial
        parametro.append(p)


        # Algoritmo de punto medio para el círculo
        while x <= y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * x + 1 - 2 * y
                
            # Dibujar y guardar los puntos en cada iteración
            parametro.append(p)
            puntos.append((x, y))
            

        self.dibujar_puntos_circulo(xc, yc,puntos, centro_x, centro_y, octantes)
        self.parametro.setText("\n" + "\n".join([f"PK: {p}, Puntos Siguientes: [ {x}, {y} ]" for p, (x, y) in zip(parametro, puntos)]))
        self.mostrar_puntos_octantes(octantes)

    def dibujar_puntos_circulo(self, xc, yc, puntos, centro_x, centro_y, octantes):
        # Dibujar los 8 puntos de simetría del círculo
        ancho, altura = 800, 500
        puntos_rellenar = []
        scale = min(ancho, altura) / 1000
        
        # Dibujar cada punto en la escena
        pen = QPen(Qt.GlobalColor.red, 1)
        for x, y in puntos:
            for iteracion in range(8):
                if iteracion == 0:
                    px = x + xc
                    py = y + yc
                elif iteracion == 1:
                    px = y + xc
                    py = x + yc
                elif iteracion == 2:
                    px = -y + xc
                    py = x + yc
                elif iteracion == 3:
                    px = -x + xc
                    py = y + yc
                elif iteracion == 4: 
                    px = -x + xc
                    py = -y + yc
                elif iteracion == 5:
                    px = -y + xc
                    py = -x + yc
                elif iteracion == 6:
                    px = y + xc
                    py = -x + yc
                elif iteracion == 7:
                    px = x + xc
                    py = -y + yc

                # Calcular las posiciones en la escena
                px_scene = centro_x + (px * scale)
                py_scene = centro_y - (py * scale)  # Ajuste aquí para el eje Y
                octantes[iteracion].append((px, py))
                puntos_rellenar.append((px, py))
                self.scene.addEllipse(px_scene, py_scene, 2, 2, pen)

        self.rellenar_circulo(xc, yc, puntos_rellenar)
        
    def rellenar_circulo(self, xc, yc, puntos):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50
        centro_x =  margen + ancho / 2
        centro_y = margen + altura / 2

        # Factor de escala uniforme basado en el mínimo entre ancho y altura
        scale = min(ancho, altura) / 1000

        # Convertir el centro a coordenadas de escena
        xc_scene = centro_x + xc * scale
        yc_scene = centro_y - yc * scale

        # Dibujar líneas desde el centro a cada punto
        pen = QPen(Qt.GlobalColor.red, 0.9, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        for px, py in puntos:
            px_scene = centro_x + px * scale
            py_scene = centro_y - py * scale
            self.scene.addLine(xc_scene, yc_scene, px_scene, py_scene, pen)


    def mostrar_puntos_octantes(self, octantes):
        # Mostrar los puntos en las etiquetas de los octantes
        for i in range(8):
            texto_puntos = f"Octante {i + 1}:\n"
            for punto in octantes[i]:
                texto_puntos += f"({punto[0]}, {punto[1]})\n"
            self.octantes_labels[i].setText(texto_puntos)


    def limpiar_escena(self):
        self.scene.clear()
        self.dibujar_grafica()
        self.parametro.clear()
        self.input_radio.clear()
        for label in self.octantes_labels:
            label.clear()
        self.input_xc.clear()
        self.input_yc.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()