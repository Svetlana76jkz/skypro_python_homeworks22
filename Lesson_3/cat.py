import turtle

# Настройки для рисования собаки
t = turtle.Turtle())
t.speed(0)  # Устанавливаем максимальную скорость
t.pensize(3)

# Тело собаки
t.fillcolor("brown")
t.begin_fill()
t.circle(50)
t.end_fill()

# Голова собаки
t.fillcolor("brown")
t.begin_fill()
t.circle(30)
t.end_fill()

# Уши собаки
t.penup()
t.goto(30, 60)
t.pendown()
t.setheading(60)
t.fillcolor("brown")
t.begin_fill()
t.circle(20, 120)
t.end_fill()

t.penup()
t.goto(-30, 60)
t.pendown()
t.setheading(120)
t.fillcolor("brown")
t.begin_fill()
t.circle(20, -120)
t.end_fill()

# Глаза собаки
t.penup()
t.goto(-15, 80)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

t.penup()
t.goto(15, 80)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

# Нос собаки
t.penup()
t.goto(0, 70)
t.pendown()
t.dot(10)

# Хвост собаки
t.penup()
t.goto(-50, -5)
t.pendown()
t.setheading(-45)
t.forward(20)

# Закрытие окна после завершения рисования
turtle.done()



