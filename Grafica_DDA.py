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
        self.label_xb.setGeometry(930,150,60,30)
        self.input_xb = QLineEdit(self)
        self.input_xb.setGeometry(970,150,60,30)

        #Yb
        self.label_yb = QLabel("Yb:", self)
        self.label_yb.setGeometry(1050, 150, 60, 30)
        self.input_yb = QLineEdit(self)
        self.input_yb.setGeometry(1090, 150, 60, 30)

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

        #btn_Trazar linea
        self.btn_trazar = QPushButton("Trazar Línea", self)
        self.btn_trazar.setGeometry(1200, 100, 120, 30)
        self.btn_trazar.setStyleSheet("background-color: lightgray; color: black;")

        #btn_Limpiar
        self.btn_limpiar = QPushButton("Limpiar", self)
        self.btn_limpiar.setGeometry(1200, 150, 120, 30)
        self.btn_limpiar.setStyleSheet("background-color: lightgray; color: black;")

        #Etiqueta de la pendiente
        self.pendiente_label = QLabel("Valor de M: ", self)
        self.pendiente_label.setGeometry(1200, 250, 80, 30)
        self.pendiente_label.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 5px;")
        self.pendiente_text = QLabel(self)
        self.pendiente_text.setGeometry(1290,250,60,30)
        self.pendiente_text.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xa > Xb
        self.Xa_Xb_txt = QLabel(self)
        self.Xa_Xb_txt.setGeometry(1200, 200, 120, 30)
        self.Xa_Xb_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #Etiqueta de si Xa > Xb
        self.caso_xa_xb = QLabel(self)
        self.caso_xa_xb.setGeometry(1300, 200, 120, 30)
        self.caso_xa_xb.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 7px;")

        #etiqueta de caso
        self.caso_label = QLabel("Caso", self)
        self.caso_label.setGeometry(1200, 300, 80, 30)
        self.caso_label.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 10px;")
        self.caso_text = QLabel(self)
        self.caso_text.setGeometry(1290, 300, 170, 30)
        self.caso_text.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")

        #etiqueta de direccion 
        self.cumple_label = QLabel("Se cumple ", self)
        self.cumple_label.setGeometry(1200, 350, 80, 30)
        self.cumple_label.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 7px;")
        self.direccion_text = QLabel(self)
        self.direccion_text.setGeometry(1290, 350, 170, 30)
        self.direccion_text.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")

        #Etiqueta de Xk + 1
        self.xk_mas_uno = QLabel("Xk + 1/M ", self)
        self.xk_mas_uno.setGeometry(1200, 390, 80, 30)
        self.xk_mas_uno.setStyleSheet("background-color: lightgray; color: black; font-size: 13px; padding: 7px;")
        self.xk_mas_uno_txt = QLabel(self)
        self.xk_mas_uno_txt.setGeometry(1290, 390, 170, 30)
        self.xk_mas_uno_txt.setStyleSheet("background-color: white; color: black; font-size: 13px; padding: 5px;")


        # Etiqueta de las coordenadas generadas
        self.coordenadas_label = QLabel("Coordenadas generadas en la pendiente:", self)
        self.coordenadas_label.setGeometry(950, 250, 230, 30) # x , y  , widht, hight (Ancho y altura)
        # Subrayar la etiqueta de coordenadas
        self.coordenadas_label.setStyleSheet("background-color: lightgray; color: black; font-size: 12px; padding: 5px;")
        
        
        # Layout principal
        self.layout = QVBoxLayout()

        # Crear QLabel para mostrar las coordenadas
        self.coordenadas_text = QLabel(self)
        self.coordenadas_text.setStyleSheet("background-color: white; color: black; font-size: 14px; padding: 15px;")
        self.coordenadas_text.setWordWrap(True)  # Permite que el texto se divida en varias líneas

        # Crear QScrollArea para contener el QLabel y permitir desplazamiento
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Permite que el QLabel se adapte
        self.scroll_area.setWidget(self.coordenadas_text)  # Agregar QLabel al área de scroll
        self.scroll_area.setFixedSize(180, 350)  # Mantiene un tamaño fijo sin expandirse
        # Agregar widgets al layout
        self.layout.addWidget(self.scroll_area)  # Agrega el QLabel dentro del ScrollArea
        self.layout.setContentsMargins(980, 160, 0, 0)  # Posiciona el QLabel en la ventana
        self.setLayout(self.layout)


        # Conectar los botones a sus respectivas funciones
        self.btn_trazar.clicked.connect(self.trazar_linea)
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


    def calcular_pendiente(self, xa, ya, xb, yb) -> float:
        try:
            m_pendiente: float = (yb - ya) / (xb - xa)
        except ZeroDivisionError:
            m_pendiente = None 

        return m_pendiente


    def generar_coordenadas(self, xa, ya, xb, yb):
        pendiente: float = self.calcular_pendiente(xa, ya, xb, yb)
        coordenadas = []
        caso = ""
        xa_xb = ""
        
        Xk = 0  # Initialize xk with a default value
        if pendiente == 1:  
            caso = "Especial M = 1"
            if xa > xb:#Si
                xa_xb = "X - 1 , Y - 1"
                while xa >= xb and ya >= yb: 
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa -= 1
                    ya -= 1
        
            else:#No
                xa_xb = "X + 1, Y + 1"
                while xa <= xb and ya <= yb:
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa += 1
                    ya += 1

        elif pendiente == -1:
            caso = "Especial M = -1"
            if xa > xb:  # Si 
                xa_xb = "X - 1, Y + 1"
                while xa >= xb and ya <= yb:
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa -= 1
                    ya += 1
            else:  # No
                xa_xb = "X + 1, Y - 1"
                while xa <= xb and ya >= yb: 
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa += 1
                    ya -= 1 

        elif pendiente == 0: 
            caso = "Especial M = 0"
            if xa > xb: # Si
                xa_xb = "X - 1, Y = Y"
                while xa >= xb and ya == yb:
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa -= 1
            else: #No
                xa_xb = "X + 1, Y = Y"
                while xa <= xb and ya == yb:
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    xa += 1
        elif pendiente is None: 
            caso = "Especial M = Error"
            if ya > yb:#Si
                xa_xb = "X = X, Y - 1"
                while ya >= yb: 
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    ya -= 1
            else:#No
                xa_xb = "X = X, Y + 1"
                while ya <= yb:
                    coordenadas.append(f"   [ {xa}, {ya} ]")
                    ya += 1

        elif pendiente > 0 and pendiente < 1: 
            caso = "Positivo cuando +M < 1"
            if xa > xb: # Si 
                xa_xb = "X - 1, Y - M"
                while xa >= xb and ya >= yb: 
                    coordenadas.append(f"   [ {xa}, {round(ya, 4)} ]")
                    xa -= 1 
                    ya -= pendiente
            else: #NO
                xa_xb = "X + 1, Y + M"
                while xa <= xb and ya <= yb: 
                    coordenadas.append(f"   [ {xa}, {round(ya, 4)}]")
                    xa += 1
                    ya += pendiente
        elif pendiente > 1: 
            caso = "Positivo cuando +M > 1"
            Xk = 1 / pendiente
            if xa > xb : #Si
                xa_xb = "X - Xk+1/m, Y + 1"
                while xa >= xb and ya >= yb:
                    coordenadas.append(f"   [ {round(xa, 4)}, {ya}]")
                    xa -= Xk
                    ya -= 1
            else: # No
                while xa <= xb and ya <= yb:
                    xa_xb = "X + Xk+1/m, Y + 1"
                    coordenadas.append(f"   [ {round(xa, 4)}, {ya}]")
                    xa += Xk
                    ya += 1

        elif pendiente < 0 and pendiente > -1: 
            caso = "Negativo cuando -M < 1"
            if xa > xb: # Si
                xa_xb = "X - 1, Y + m"
                while xa >= xb  and ya <= yb:
                    coordenadas.append(f"[ {xa}, {round(ya, 4)} ]")
                    xa -= 1
                    ya = (ya - (pendiente))
            else: #No
                xa_xb = "X + 1, Y - m"
                while xa <= xb and ya >= yb: 
                    coordenadas.append(f"[ {xa}, {round(ya, 4)} ]")
                    xa += 1
                    ya = (ya + (pendiente))
        elif pendiente < -1:
            caso = "Negativo cuando -M > 1"
            Xk = 1 / pendiente
            if xa > xb:#Si
                xa_xb = "X - Xk, Y + 1"
                while xa >= xb and ya <= yb:
                    coordenadas.append(f"[ {round(xa, 4)}, {ya} ]")
                    xa = (xa + (Xk))
                    ya += 1
            else: #No
                xa_xb = "X + Xk, Y - 1"
                while xa <= xb and ya >= yb:
                    coordenadas.append(f"[ {round(xa, 4)}, {ya} ]")
                    xa = (xa - (Xk))
                    ya -= 1

        return coordenadas, caso, Xk, xa_xb

    def trazar_linea(self):
        
            # Obtener las coordenadas de los puntos A y B
            xa = int(self.input_xa.text())
            ya = int(self.input_ya.text())
            xb = int(self.input_xb.text()) 
            yb = int(self.input_yb.text())
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
            self.caso_coordenadas(xa, ya, xb, yb)

    def caso_coordenadas(self, xa, ya, xb, yb):
            # Generar y mostrar las coordenadas intermediarias
        try:
            pendiente = self.calcular_pendiente(xa, ya, xb, yb)
            coordenadas, caso, xk, xa_xb = self.generar_coordenadas(xa, ya, xb, yb)
            direccion, xa_xb_mayor = self.determinar_caso(xa, xb)

            if pendiente is None:
                self.pendiente_text.setText("Error")
                self.caso_text.setText(caso)    
                self.direccion_text.setText(self.caso_error(ya, yb))
                self.coordenadas_text.setText("\n".join(coordenadas))
            elif coordenadas:
                self.Xa_Xb_txt.setText(f"Xa > Xb: {xa_xb_mayor}")
                self.caso_xa_xb.setText(xa_xb)
                self.pendiente_text.setText(f"{pendiente}")
                self.caso_text.setText(caso)
                self.direccion_text.setText(direccion)
                self.xk_mas_uno_txt.setText(str(xk))
                self.coordenadas_text.setText("   X,      Y\n" + "\n".join(coordenadas))
            else:
                self.coordenadas_text.setText("No se encontro ningun caso")
        except ValueError:
            self.coordenadas_text.setText("Error: Ingresa valores en el formato")

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
    
        
    def limpiar_escena(self):
        self.pendiente_text.clear()
        self.scene.clear()
        self.dibujar_grafica()
        self.caso_xa_xb.clear()
        self.xk_mas_uno_txt.clear()
        self.caso_text.clear() 
        self.Xa_Xb_txt.clear()
        self.direccion_text.clear()
        self.input_xa.clear()
        self.input_ya.clear()
        self.input_xb.clear()
        self.input_yb.clear()
        self.coordenadas_text.clear()





if __name__ == "__main__":
    app = QApplication([])
    window = MyGraphic()
    window.show()
    app.exec()