import turtle

# Configurar la ventana de dibujo
window = turtle.Screen()
window.bgcolor("#D7A9E3")  # Cambia el color de fondo a morado pastel
window.title("Soley Vida Mia")

# Crear un objeto Turtle para dibujar
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("yellow")
flower.speed(10)  # Ajusta la velocidad de dibujo

# Función para dibujar un pétalo
def draw_petal():
    flower.circle(160, 60)
    flower.left(120)
    flower.circle(160, 60)
    flower.left(120)

# Dibuja los pétalos de la flor
for _ in range(15):
    draw_petal()
    flower.left(360 / 15)  # Gira para el siguiente pétalo

# Mueve la pluma fuera del camino
flower.penup()
flower.goto(0, -200)
flower.pendown()

# Dibuja el círculo central de la flor sin relleno
flower.color("yellow")
flower.circle(200, extent=360)  # Cambia extent para dibujar un círculo completo sin relleno

# Escribe un mensaje encima del círculo central en fuente negrita
flower.penup()
flower.goto(0, 210)  # Ajusta la posición para el mensaje
flower.color("#FF9999")  # Cambia el color del texto
flower.write("Te amo", align="center", font=("Arial", 20, "bold italic"))
flower.hideturtle()

# Cierra la ventana haciendo clic en ella
window.exitonclick()
