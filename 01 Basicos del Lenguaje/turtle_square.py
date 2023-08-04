import turtle


tortuga=turtle.Turtle()
window=turtle.Screen()
tortuga.fillcolor('red')
tortuga.begin_fill()

""""
#Cuadrado
for i in range(4):
    tortuga.forward(50)
    tortuga.left(90)
"""

""""
#Estrella
for i in range(5):
    tortuga.forward(100)
    tortuga.right(144)
"""

#Pentagono
tortuga.Screen().bgcolor('black')
tortuga.speed(0)
color = ('green','blue','yellow','red','white')
for i in range (102):
	tortuga.color(color[i%5])
	tortuga.left(144)
	tortuga.forward(i*2)
	tortuga.rt(72)
	
tortuga.end_fill()
window.mainloop()
