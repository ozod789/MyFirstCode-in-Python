import turtle

# Ekranni sozlash
window = turtle.Screen()
window.bgcolor("white")

# Ot (yoki oddiy shakl) yaratish uchun funksiyalar

def draw_body():
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.circle(50)

def draw_legs():
    for i in range(4):
        turtle.penup()
        turtle.goto(-70 + i * 30, -50)
        turtle.pendown()
        turtle.setheading(-90)
        turtle.forward(30)

def move_horse():
    for _ in range(100):
        turtle.clear()
        draw_body()
        draw_legs()
        turtle.forward(10)  # Harakatni oldinga 10 birlikka siljitish
        turtle.delay(50)

# Otni chizish
move_horse()

# Oynani yopilmasligi uchun kutish
window.mainloop()
