def on_trazar_clicked(self):
        try:
            xc = int(self.input_xc.text())
            yc = int(self.input_yc.text())
            r = 100  # Puedes ajustar el radio o pedirlo como entrada
            self.dibujar_circulo(xc, yc, r)
        except ValueError:
            self.coordenadanas_A_B.setText("Error: Ingresa valores válidos")

# def dibujar_circulo(self, xc, yc, r):
#         # Convertir coordenadas de usuario a coordenadas de escena
#         ancho, altura = 800, 500
#         margen = 50
#         centro_x = margen + ancho / 2
#         centro_y = margen + altura / 2

#         # Inicializar variables
#         x = 0
#         y = r
#         p = 1 - r  # Parámetro de decisión inicial

#         # Dibujar los puntos iniciales
#         self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y)

#         # Algoritmo de punto medio para el círculo
#         while x < y:
#             x += 1
#             if p < 0:
#                 p += 2 * x + 1
#             else:
#                 y -= 1
#                 p += 2 * (x - y) + 1
#             self.dibujar_puntos_circulo(xc, yc, x, y, centro_x, centro_y)

#     def dibujar_puntos_circulo(self, xc, yc, x, y, centro_x, centro_y):
#         # Convertir coordenadas de usuario a coordenadas de escena
#         ancho, altura = 800, 500
#         margen = 50

#         # Dibujar los 8 puntos de simetría del círculo
#         puntos = [
#             (xc + x, yc + y),
#             (xc - x, yc + y),
#             (xc + x, yc - y),
#             (xc - x, yc - y),
#             (xc + y, yc + x),
#             (xc - y, yc + x),
#             (xc + y, yc - x),
#             (xc - y, yc - x),
#         ]

#         # Dibujar cada punto en la escena
#         pen = QPen(Qt.GlobalColor.blue, 2)
#         for px, py in puntos:
#             px_scene = centro_x + px * (ancho / 1000)
#             py_scene = centro_y - py * (altura / 1000)
#             self.scene.addEllipse(px_scene, py_scene, 2, 2, pen)