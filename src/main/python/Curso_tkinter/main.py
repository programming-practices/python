from tkinter import *
import math

# https://www.youtube.com/watch?v=Cq5tpTwfJJY

root = Tk()
root.title("Postroenie grafika funccii y = sin(x)")
root.geometry("1020x620")

canavas = Canvas(root, width=1020, height=620, bg='#002')

# Linii setku po vertikali
for y in range(21):
    k = 50 * y
    canavas.create_line(10+k, 610, 10+k, 10, width=1, fill='#191938')

# Linii setku po gorizontali
for y in range(13):
    k = 50 * y
    canavas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#191938')

# Linii coordenat x i y
canavas.create_line(10, 10, 10, 610, width=1, arrow=FIRST, fill='white') # os y
canavas.create_line(0, 310, 1010, 310, width=1, arrow=LAST, fill='white') # os x

w = 0.0209      # ciklicheskaia chistota
# w = 0.020      # ciklicheskaia chistota
phi = 10        # smewchenie grafika po XCargarDatos
# phi = 5        # smewchenie grafika po X
A = 200         # amplityda
# A = 100         # amplityda
# dy = 310        # smewchenie grafika po Y
dy = 110        # smewchenie grafika po Y

xy = []
for x in range(1000):
    y = math.sin(x * w)
    xy.append(x + phi)
    xy.append(y * A + dy)

sin_line = canavas.create_line(xy, fill='blue')

canavas.pack()
root.mainloop()