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
from PyQt6.QtCore import Qt, QPointF
import math
from PyQt6.QtGui import QPen, QPolygonF, QBrush

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


        #Xa 
        self.label_xa = QLabel("Xa:", self)
        self.label_xa.setGeometry(930, 100, 60, 30)  # x , y  , widht, hight (Ancho y altura)
        self.input_xa = QLineEdit(self)
        self.input_xa.setGeometry(970, 100, 60,30)

        #Ya
        self.label_ya = QLabel("Ya:", self)
        self.label_ya.setGeometry(1050, 100, 60, 30) 
        self.input_ya = QLineEdit(self)
        self.input_ya.setGeometry(1090, 100, 60, 30) 
        

        #Xb
        self.label_xb = QLabel("Xb:", self)
        self.label_xb.setGeometry(930,140,60,30)
        self.input_xb = QLineEdit(self)
        self.input_xb.setGeometry(970,140,60,30)

        #Yb
        self.label_yb = QLabel("Yb:", self)
        self.label_yb.setGeometry(1050, 140, 60, 30)
        self.input_yb = QLineEdit(self)
        self.input_yb.setGeometry(1090, 140, 60, 30)

        #Xc 
        self.label_xc = QLabel("Xc:", self)
        self.label_xc.setGeometry(930, 180, 60, 30)
        self.input_xc = QLineEdit(self)
        self.input_xc.setGeometry(970, 180, 60, 30)
        
        #Yc 
        self.label_yc = QLabel("Yc:", self)
        self.label_yc.setGeometry(1050, 180, 60, 30)
        self.input_yc = QLineEdit(self)
        self.input_yc.setGeometry(1090, 180, 60, 30)


        #  colores para los labels
        self.label_xa.setStyleSheet("color: blue;")
        self.label_ya.setStyleSheet("color: blue;")
        self.label_xb.setStyleSheet("color: red;")
        self.label_yb.setStyleSheet("color: red;")

        #  colores para los inputs
        self.input_xa.setStyleSheet("background-color: lightgreen;")
        self.input_ya.setStyleSheet("background-color: lightgreen;")
        self.input_xb.setStyleSheet("background-color: lightcoral;")
        self.input_yb.setStyleSheet("background-color: lightcoral;")
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


        #Etiqueta de si Xa > Xb
        self.Xa_Xb_txt = QLabel(self)
        self.Xa_Xb_txt.setGeometry(910, 220, 140, 30)
        self.Xa_Xb_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xa > Xb
        self.caso_A_B = QLabel(self)
        self.caso_A_B.setGeometry(1050, 220, 140, 30)
        self.caso_A_B.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xb > xc
        self.Xb_Xc_txt = QLabel(self)
        self.Xb_Xc_txt.setGeometry(910, 255, 140, 30)
        self.Xb_Xc_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xb > Xc
        self.caso_B_C = QLabel(self)
        self.caso_B_C.setGeometry(1050, 255, 140, 30)
        self.caso_B_C.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xa > Xb
        self.Xc_Xa_txt = QLabel(self)
        self.Xc_Xa_txt.setGeometry(910, 290, 140, 30)
        self.Xc_Xa_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xa > Xb
        self.caso_C_A = QLabel(self)
        self.caso_C_A.setGeometry(1050, 290, 140, 30)
        self.caso_C_A.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")


        #Etiqueta de la pendiente
        self.btn_pendiente_AB = QLabel("M (A, B): ", self)
        self.btn_pendiente_AB.setGeometry(1250, 95, 80, 30)
        self.btn_pendiente_AB.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 5px;")
        self.pendiente_AB = QLabel(self)
        self.pendiente_AB.setGeometry(1350,95,60,30)
        self.pendiente_AB.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        self.btn_pendiente_BC = QLabel("M (B, C): ", self)
        self.btn_pendiente_BC.setGeometry(1250, 127, 80, 30)
        self.btn_pendiente_BC.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 5px;")
        self.pendiente_BC = QLabel(self)
        self.pendiente_BC.setGeometry(1350,127,60,30)
        self.pendiente_BC.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        self.btn_pendiente_CA = QLabel("M (C, A): ", self)
        self.btn_pendiente_CA.setGeometry(1250, 160, 80, 30)
        self.btn_pendiente_CA.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 5px;")
        self.pendiente_CA = QLabel(self)
        self.pendiente_CA.setGeometry(1350,160,60,30)
        self.pendiente_CA.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")


        #etiqueta de caso
        self.caso_label = QLabel("Caso", self)
        self.caso_label.setGeometry(1250, 215, 80, 30)
        self.caso_label.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 10px;")
        self.caso_text = QLabel(self)
        self.caso_text.setGeometry(1350, 215, 170, 30)
        self.caso_text.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")

        #etiqueta de direccion 
        self.cumple_label = QLabel("Se cumple ", self)
        self.cumple_label.setGeometry(1250, 247, 80, 30)
        self.cumple_label.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 7px;")
        self.direccion_text = QLabel(self)
        self.direccion_text.setGeometry(1350, 247, 170, 30)
        self.direccion_text.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")

        #Etiqueta de Xk + 1
        self.xk_mas_uno = QLabel("Xk + 1/M ", self)
        self.xk_mas_uno.setGeometry(1250, 280, 80, 30)
        self.xk_mas_uno.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 7px;")
        self.xk_mas_uno_txt = QLabel(self)
        self.xk_mas_uno_txt.setGeometry(1350, 280, 170, 30)
        self.xk_mas_uno_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")


        # Etiqueta de las coordenadas generadas
        self.coordenadasAB = QLabel("A (Xa, Ya) B (Xb, Yb)", self)
        self.coordenadasAB.setGeometry(930, 330, 140, 30) # x , y  , widht, hight (Ancho y altura)
        self.coordenadasAB.setStyleSheet("background-color: rgb(216, 232, 219); color: black; font-size: 14px; padding: 5px;")
        # Etiqueta de las coordenadas generadas
        self.coordenadasBC = QLabel("B (Xb, Yb) C (Xc, Yc)", self)
        self.coordenadasBC.setGeometry(1135, 330, 140, 30) # x , y  , widht, hight (Ancho y altura)
        self.coordenadasBC.setStyleSheet("background-color: rgb(216, 232, 219); color: black; font-size: 14px; padding: 5px;")

        # Etiqueta de las coordenadas generadas
        self.coordenadasCA = QLabel("C (Xc, Yc) A (Xa, Ya)", self)
        self.coordenadasCA.setGeometry(1340, 330, 140, 30) # x , y  , widht, hight (Ancho y altura)
        self.coordenadasCA.setStyleSheet("background-color: rgb(216, 232, 219); color: black; font-size: 15px; padding: 5px;")
        
        
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
            xa = int(self.input_xa.text())
            ya = int(self.input_ya.text())
            xb = int(self.input_xb.text())
            yb = int(self.input_yb.text())
            xc = int(self.input_xc.text())
            yc = int(self.input_yc.text())
            self.trazar_linea(xb, yb, xc, yc)
            self.trazar_linea(xc, yc, xa, ya)
            self.trazar_linea(xa, ya, xb, yb)
            self.rellenar_triangulo(xa, ya, xb, yb, xc, yc)
            self.print_coordenadas(xa, ya, xb, yb, xc, yc)
        except ValueError:
            self.coordenadanas_A_B.setText("Error: Ingresa valores en el formato")
    
    
    def trazar_linea(self, xa, ya, xb, yb):
           
            # Convertir coordenadas de usuario a coordenadas de escena
            ancho, altura = 800, 500
            margen = 50
            centro_x = margen + ancho / 2
            centro_y = margen + altura / 2

            ax_scene = centro_x + xa * (ancho / 1000)
            ay_scene = centro_y - ya * (altura / 1000)
            bx_scene = centro_x + xb * (ancho / 1000)
            by_scene = centro_y - yb * (altura / 1000)

            # Dibujar la línea entre A y B
            line_pen = QPen(Qt.GlobalColor.red, 2, Qt.PenStyle.DashLine)  
            self.scene.addLine(ax_scene, ay_scene, bx_scene, by_scene, line_pen)
    
    def rellenar_triangulo(self, l_xa, l_ya, l_xb, l_yb, l_xc, l_yc):
        list_xa, list_ya =  self.generar_coordenadas(l_xa,l_ya, l_xb, l_yb)[5:7]
        ancho, altura = 800, 500
        margen = 50
        centro_x = margen + ancho / 2
        centro_y = margen + altura / 2

        # Dibujar la línea entre A y B
        line_pen = QPen(Qt.GlobalColor.red, 2)  
        for xa, ya in zip(list_xa, list_ya):
            ax_scene = centro_x + xa * (ancho / 1000)
            ay_scene = centro_y - ya * (altura / 1000)
            bx_scene = centro_x + l_xc * (ancho / 1000)
            by_scene = centro_y - l_yc * (altura / 1000)
            self.scene.addLine(ax_scene, ay_scene, bx_scene, by_scene, line_pen)
    
    def print_coordenadas(self, xa, ya, xb, yb, xc, yc):
            # Generar y mostrar las coordenadas intermediarias
        try:
            pendiente_AB = self.calcular_pendiente(xa, ya, xb, yb)
            pendiente_BC = self.calcular_pendiente(xb, yb, xc, yc)
            pendiente_CA = self.calcular_pendiente(xc, yc, xa, ya)

            direccion, xa_xb_mayor = self.determinar_caso(xa, xb)
            coordenadas_A_B, caso, xk, xa_xb, ya_yb_error, lis_xa, lis_ya = self.generar_coordenadas(xa, ya, xb, yb)
            xb_xc = self.generar_coordenadas(xb, yb, xc, yc)[3]
            xc_xa = self.generar_coordenadas(xb, yb, xc, yc)[3]
            coordenadas_B_C = self.generar_coordenadas(xb, yb, xc, yc)[0]
            coordenadas_C_A = self.generar_coordenadas(xc, yc, xa, ya)[0]
            

            if pendiente_AB is None:
                self.Xa_Xb_txt.setText(f"(A,B):{ya_yb_error}")
                self.caso_A_B.setText(xa_xb)
                self.caso_B_C.setText(xb_xc)
                self.caso_C_A.setText(xc_xa)
                self.pendiente_AB.setText("Error")
                self.caso_text.setText(caso)    
                self.direccion_text.setText(self.caso_error(ya, yb))
                self.pendiente_AB.setText(f"{pendiente_AB}")
                self.pendiente_BC.setText(f"{pendiente_BC}")
                self.pendiente_CA.setText(f"{pendiente_CA}")
                self.coordenadanas_A_B.setText("   X,     Y\n" + "\n".join(coordenadas_A_B))
                self.coordenadanas_B_C.setText("   X,     Y\n" + "\n".join(coordenadas_B_C))
                self.coordenadanas_C_A.setText("   X,     Y\n" + "\n".join(coordenadas_C_A))
            elif coordenadas_A_B:
                self.Xa_Xb_txt.setText(f"(A,B) Xa > Xb: {xa_xb_mayor}")
                self.Xb_Xc_txt.setText(f"(B,C)Xb > Xc: {self.determinar_caso(xb, xc)[1]}")
                self.Xc_Xa_txt.setText(f"(C,A)Xc > Xa: {self.determinar_caso(xc, xa)[1]}")
                self.caso_A_B.setText(xa_xb)
                self.caso_B_C.setText(xb_xc)
                self.caso_C_A.setText(xc_xa)
                self.pendiente_AB.setText(f"{pendiente_AB}")
                self.pendiente_BC.setText(f"{pendiente_BC}")
                self.pendiente_CA.setText(f"{pendiente_CA}")
                self.caso_text.setText(caso)
                self.direccion_text.setText(direccion)
                self.xk_mas_uno_txt.setText(str(xk))
                self.coordenadanas_A_B.setText("   X,     Y\n" + "\n".join(coordenadas_A_B))
                self.coordenadanas_B_C.setText("   X,     Y\n" + "\n".join(coordenadas_B_C))
                self.coordenadanas_C_A.setText("   X,     Y\n" + "\n".join(coordenadas_C_A))
            else:
                self.coordenadanas_A_B.setText("No se encontro ningun caso")
        except ValueError:
            self.coordenadanas_A_B.setText("Error: Ingresa valores en el formato")
    
    def determinar_caso(self, xa, xb):
        direccion = ""
        s_mayor = ""
        if xa > xb:
            direccion = "der --> izq, abajo | arrb" 
            s_mayor = "Si"
        else:
            direccion = "izq --> der, arrb | abajo"
            s_mayor = "No"
        return direccion, s_mayor
    
    def caso_error(self, ya, yb):
        if ya > yb:
            return "Arrib | abajo"
        else:
            return "Abajo | Arriba"

    def calcular_pendiente(self, xa, ya, xb, yb) -> float:
        try:
            m_pendiente: float = (yb - ya) / (xb - xa)
        except ZeroDivisionError:
            m_pendiente = None 

        return m_pendiente

    def generar_coordenadas(self, xa, ya, xb, yb):
        pendiente: float = self.calcular_pendiente(xa, ya, xb, yb)
        coordenadas = []
        lis_xa = []
        lis_ya = []
        caso = ""
        xa_xb = ""
        ya_yb_error = ""
        Xk = 0  # Initialize xk with a default value
        if pendiente == 1:  
            caso = "Especial M = 1"
            if xa > xb:#Si
                xa_xb = "X - 1 , Y - 1"
                while xa >= xb and ya >= yb: 
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    xa -= 1
                    ya -= 1
        
            else:#No
                xa_xb = "X + 1, Y + 1"
                while xa <= xb and ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    xa += 1
                    ya += 1

        elif pendiente == -1:
            caso = "Especial M = -1"
            if xa > xb:  # Si 
                xa_xb = "X - 1, Y + 1"
                while xa >= xb and ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [{xa}, {ya}]")
                    xa -= 1
                    ya += 1
            else:  # No
                xa_xb = "X + 1, Y - 1"
                while xa <= xb and ya >= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya) 
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    xa += 1
                    ya -= 1 

        elif pendiente == 0: 
            caso = "Especial M = 0"
            if xa > xb: # Si
                xa_xb = "X - 1, Y = Y"
                while xa >= xb and ya == yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    xa -= 1
            else: #No
                xa_xb = "X + 1, Y = Y"
                while xa <= xb and ya == yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    xa += 1
        elif pendiente is None: 
            caso = "Especial M = Error"
            if ya > yb:#Si
                xa_xb = "X = X, Y - 1"
                ya_yb_error = "ya > yb= Si"
                while ya >= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    ya -= 1
            else:#No
                xa_xb = "X = X, Y + 1"
                ya_yb_error = "ya > yb= No"
                while ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {ya} ]")
                    ya += 1

        elif pendiente > 0 and pendiente < 1: 
            caso = "Positivo cuando +M < 1"
            if xa > xb: # Si 
                xa_xb = "X - 1, Y - M"
                while xa >= xb and ya >= yb: 
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {xa}, {round(ya, 2)} ]")
                    xa -= 1 
                    ya -= pendiente
            else: #NO
                xa_xb = "X + 1, Y + M"
                while xa <= xb and ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya) 
                    coordenadas.append(f" [ {xa}, {round(ya, 2)}]")
                    xa += 1
                    ya += pendiente
        elif pendiente > 1: 
            caso = "Positivo cuando +M > 1"
            Xk = 1 / pendiente
            if xa > xb : #Si
                xa_xb = "X - Xk+1/m, Y - 1" #First prueba 
                while xa >= xb and ya >= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {round(xa, 2)}, {ya}]")
                    xa -= Xk
                    ya -= 1
            else: # No
                while xa <= xb and ya <= yb:
                    xa_xb = "X + Xk+1/m, Y + 1"
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f" [ {round(xa, 2)}, {ya}]")
                    xa += Xk
                    ya += 1

        elif pendiente < 0 and pendiente > -1: 
            caso = "Negativo cuando -M < 1"
            if xa > xb: # Si
                xa_xb = "X - 1, Y + m"
                while xa >= xb  and ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f"[ {xa}, {round(ya, 2)} ]")
                    xa -= 1
                    ya = (ya - (pendiente))
            else: #No
                xa_xb = "X + 1, Y - m"
                while xa <= xb and ya >= yb: 
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f"[ {xa}, {round(ya, 2)} ]")
                    xa += 1
                    ya = (ya + (pendiente))
        elif pendiente < -1:
            caso = "Negativo cuando -M > 1"
            Xk = 1 / pendiente
            if xa > xb:#Si
                xa_xb = "X - Xk, Y + 1"
                while xa >= xb and ya <= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f"[ {round(xa, 2)}, {ya} ]")
                    xa = (xa + (Xk))
                    ya += 1
            else: #No
                xa_xb = "X + Xk, Y - 1"
                while xa <= xb and ya >= yb:
                    lis_xa.append(xa)
                    lis_ya.append(ya)
                    coordenadas.append(f"[ {round(xa, 2)}, {ya} ]")
                    xa = (xa - (Xk))
                    ya -= 1

        return coordenadas, caso, Xk, xa_xb, ya_yb_error, lis_xa, lis_ya
        
    def limpiar_escena(self):
        self.pendiente_AB.clear()
        self.scene.clear()
        self.dibujar_grafica()
        self.coordenadanas_B_C.clear()
        self.coordenadanas_C_A.clear()
        self.pendiente_BC.clear()
        self.pendiente_CA.clear()
        self.input_xc.clear()
        self.input_yc.clear()
        self.caso_A_B.clear()
        self.xk_mas_uno_txt.clear()
        self.caso_text.clear() 
        self.Xa_Xb_txt.clear()
        self.direccion_text.clear()
        self.input_xa.clear()
        self.input_ya.clear()
        self.input_xb.clear()
        self.input_yb.clear()
        self.coordenadanas_A_B.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()