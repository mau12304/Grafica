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
        self.label_radio = QLabel("Rx", self)
        self.label_radio.setGeometry(930, 140, 60, 30)
        self.input_radio = QLineEdit(self)
        self.input_radio.setGeometry(970, 140, 60, 30)
        # Radio 2
        self.label_radio2 = QLabel("Ry", self)
        self.label_radio2.setGeometry(1040, 140, 60, 30)
        self.input_radio2 = QLineEdit(self)
        self.input_radio2.setGeometry(1080, 140, 60, 30)

        self.parametro_lb = QLabel("Parametro", self)
        self.parametro_lb.setGeometry(990, 425, 100, 30)
        self.parametro_lb.setStyleSheet("background-color: white; color: black; font-size: 12px; padding: 10px")

        self.primer_cuadrante = QLabel("Cuadrante 1\n ( X, Y )", self)
        self.primer_cuadrante.setGeometry(1130, 420, 100, 40)
        self.primer_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 12px; padding: 2px")

        self.segundo_cuadrante = QLabel("Cuadrante 2\n( X, Y )", self)
        self.segundo_cuadrante.setGeometry(1020, 178,100,40)
        self.segundo_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 12px; padding: 2px")


        self.tercer_cuadrante = QLabel("Cuadrante 3\n( X, Y )", self)
        self.tercer_cuadrante.setGeometry(1200, 180,100,40)
        self.tercer_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 12px; padding: 2px")


        self.cuarto_cuadrante = QLabel("Cuadrante 4\n( X, Y )", self)
        self.cuarto_cuadrante.setGeometry(1380, 180,100,40)
        self.cuarto_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 12px; padding: 2px")



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

        # Crear QLabel para mostrar las coordenadas
        self.segundo_cuadrante = QLabel(f"X, Y \n", self)
        self.segundo_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.segundo_cuadrante.setWordWrap(True)  # Permite que el texto se divida en varias líneas
        # Crear QLabel para mostrar las coordenadas
        self.tercer_cuadrante = QLabel(f"X, Y \n",self)
        self.tercer_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.tercer_cuadrante.setWordWrap(True)  # Permite que el texto se divida en varias líneas
        # Crear QLabel para mostrar las coordenadas
        self.cuarto_cuadrante = QLabel(f"X, Y \n",self)
        self.cuarto_cuadrante.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.cuarto_cuadrante.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear QScrollArea para contener el QLabel y permitir desplazamiento
        self.segundo_ca = QScrollArea()
        self.segundo_ca.setWidgetResizable(True)  # Permite que el QLabel se adapte
        self.segundo_ca.setWidget(self.segundo_cuadrante)  # Agregar QLabel al área de scroll
        self.segundo_ca.setFixedSize(150, 200)  # Mantiene un tamaño fijo sin expandirse
        # Agregar widgets al layout
        self.layout.addWidget(self.segundo_ca)  # Agrega el QLabel dentro del ScrollArea
        self.layout.setContentsMargins(980, 190, 0, 0)  # Posiciona el QLabel en la ventana
        self.setLayout(self.layout)

        self.tercer_ca = QScrollArea()
        self.tercer_ca.setWidgetResizable(True)  
        self.tercer_ca.setWidget(self.tercer_cuadrante)  
        self.tercer_ca.setFixedSize(150, 200)  

        self.layout.addWidget(self.tercer_ca)  

        self.cuarto_ca = QScrollArea()
        self.cuarto_ca.setWidgetResizable(True)  
        self.cuarto_ca.setWidget(self.cuarto_cuadrante)  
        self.cuarto_ca.setFixedSize(150, 200)  

        self.layout.addWidget(self.cuarto_ca)  

        # Layout horizontal para las coordenadas
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.segundo_ca)
        self.horizontal_layout.addWidget(self.tercer_ca)
        self.horizontal_layout.addWidget(self.cuarto_ca)

        # Agregar el layout horizontal al layout principal
        self.layout.addLayout(self.horizontal_layout)
         # Crear QLabel para mostrar las coordenadas
        self.parametro = QLabel(self)
        self.parametro.setGeometry(980, 510, 300, 50)  # Ajustar la posición y el tamaño según sea necesario
        self.parametro.setStyleSheet("background-color: white; color: black; font-size: 15px; padding-left: 25px;")
        self.parametro.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear un QScrollArea para el QLabel
        self.scroll_parametro = QScrollArea(self)
        self.scroll_parametro.setWidgetResizable(True)
        self.scroll_parametro.setGeometry(930, 190, 400, 300)  # Ajustar posición y tamaño
        self.scroll_parametro.setFixedSize(400, 300)  # Establecer un tamaño fijo para el QScrollArea
        self.scroll_parametro.setStyleSheet("background-color: lightblue;")

        # Establecer el QLabel en el QScrollArea
        self.scroll_parametro.setWidget(self.parametro)

        # Agregar el QScrollArea al layout principal
        self.layout.addWidget(self.scroll_parametro)
        self.parametro.setStyleSheet("background-color: white; color: black; font-size: 15px; padding-left: 25px;")
        self.parametro.setWordWrap(True)  # Permite que el texto se divida en varias líneas
        self.btn_trazar.clicked.connect(self.on_trazar_clicked)
        self.btn_limpiar.clicked.connect(self.limpiar_escena)

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
            r1 = int(self.input_radio.text())
            r2 = int(self.input_radio2.text())
            self.dibujar_elipse(xc, yc, r1, r2)
        except ValueError:
            pass
        
    def dibujar_elipse(self, xc, yc, rx, ry):
        Xk_1 = []
        Yk_1 = []
        Parametro = []
        regiones = []

        # Región 1: Primera parte de la elipse
        x = 0
        y = ry        
        Pk = (ry**2) - (rx**2) * ry + 0.25 * (rx**2)  # Parámetro inicial
        
        i = 0
        while 2*(ry**2) * x <= 2*(rx**2) * y:
            i +=1
            if Pk < 0:
                x += 1
                Xk_1.append(x)
                Yk_1.append(y)
                Parametro.append(f"R1 {round(Pk,2)}")
                regiones.append(f"R1 [ {x + xc}, {y + yc}]")
                Pk += 2 * (ry**2) * x + (ry**2)  
            else:
                x +=1
                y -= 1
                Xk_1.append(x)
                Yk_1.append(y)
                Parametro.append(f"R1 {round(Pk,2)}")
                regiones.append(f"R1 [ {x + xc}, {y + yc}]")
                Pk += 2 * (ry**2) * x - 2 * (rx**2) * y + (ry**2)
    
       
        # Región 2: Segunda parte de la elipse
        P2k = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2) * (ry**2)

        while y > 0:  # Cambiar la condición para detenerse cuando y == 0
            if P2k > 0:
                y -= 1
                Xk_1.append(x)
                Yk_1.append(y)
                Parametro.append(f"R2 {round(P2k,2)}")
                regiones.append(f"R2 [ {x + xc}, {y + yc}]")
                P2k = P2k - 2 * (rx**2) * y + (rx**2)
            else:
                x += 1
                y -= 1
                Xk_1.append(x)
                Yk_1.append(y)
                Parametro.append(f"R2 {round(P2k,2)}")
                regiones.append(f"R2 [ {x + xc}, {y + yc}]")
                P2k += 2 * (ry**2) * x - 2 * (rx**2) * y + (rx**2)
                 # Mostrar puntos calculados
            
            
        self.parametro.setText(
                "\n" + "\n".join([f"PK: {p}, : {region}" for p, region in zip(Parametro, regiones)]))
        self.dibujar_puntos_circulo(xc, yc, Xk_1, Yk_1)

    def dibujar_puntos_circulo(self, xc, yc, xk, yk):
        # Dibujar los 8 puntos de simetría del círculo
        ancho, altura = 800, 500
        margen = 50
        Xk_1 = []
        Yk_1 = []
        centro_x =  margen + ancho / 2 
        centro_y = margen + altura / 2 
        # puntos_rellenar = []
        # scale = min(ancho, altura) / 1000
        
        # Dibujar cada punto en la escena
        pen = QPen(Qt.GlobalColor.red, 0.5)
        for x, y in zip(xk, yk):
            for iteracion in range(4):
                if iteracion == 0:
                    px = xc + x
                    py = yc + y
                elif iteracion == 1:
                    px = xc + x
                    py = yc - y
                    self.segundo_cuadrante.setText(
                        self.segundo_cuadrante.text() + f"\n{px}, {py}"
                    )
                elif iteracion == 2:
                    px = xc - x
                    py = yc - y
                    self.tercer_cuadrante.setText(
                        self.tercer_cuadrante.text() + f"\n{px}, {py}"
                    )
                elif iteracion == 3:
                    px = xc - x
                    py = yc + y
                    self.cuarto_cuadrante.setText(
                        self.cuarto_cuadrante.text() + f"\n{px}, {py}"
                    )
                    
                # Calcular las posiciones en la escena
                px_scene = centro_x + (px * ancho/ 1000)
                py_scene = centro_y - (py * altura / 1000)  # Ajuste aquí para el eje Y
                self.scene.addEllipse(px_scene, py_scene, 2, 2, pen)
                Xk_1.append(px)
                Yk_1.append(py)
                
        self.rellenar_elipse(xc, yc, Xk_1, Yk_1)
    

    def rellenar_elipse(self, xc, yc, x, y):
        # Convertir coordenadas de usuario a coordenadas de escena
        ancho, altura = 800, 500
        margen = 50
        centro_x =  margen + ancho / 2
        centro_y = margen + altura / 2

        # Convertir el centro a coordenadas de escena
        

        # Dibujar líneas desde el centro a cada punto
        pen = QPen(Qt.GlobalColor.red, 0.5, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        for px, py in zip(x, y):
            xc_scene = centro_x + (px * ancho/ 1000)
            yc_scene = centro_y - (py * altura / 1000)
            px_scene = centro_x + (xc * ancho/1000)
            py_scene = centro_y - (yc * altura/1000)
            self.scene.addLine(px_scene, py_scene, xc_scene, yc_scene, pen)

    def limpiar_escena(self):
        self.scene.clear()
        self.dibujar_grafica()
        self.parametro.clear()
        self.input_radio.clear()
        self.input_xc.clear()
        self.input_yc.clear()
        self.input_radio2.clear()
        self.segundo_cuadrante.clear()
        self.tercer_cuadrante.clear()
        self.cuarto_cuadrante.clear()





if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()