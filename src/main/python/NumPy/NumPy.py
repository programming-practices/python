import numpy

# Простой пример широковещания
a = numpy.array([1.0, 2.0, 3.0])
b = 2.0
c = a * b
# возвращает [ 2.  4.  6.] - скаляр b автоматически продвигается / широковещается и применяется к вектору для создания c
print(c)

# 2-d (матрица с рангом 2) индексирование в NumPy – распространяется и на тензоры - т.e. ранг > 2
y = numpy.arange(35).reshape(5, 7)
print(y)
# array([[ 0,  1,  2,  3,  4,  5,  6],
#        [ 7,  8,  9, 10, 11, 12, 13],
#        [14, 15, 16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25, 26, 27],
#        [28, 29, 30, 31, 32, 33, 34]])

# доступ к отдельной ячейке – нотация в построчном порядке, возвращает 0
print(y[0, 0])
# возвращает всю строку 4: array([28, 29, 30, 31, 32, 33, 34])
print(y[4, ])
# возвращает весь столбец 2: array([ 2,  9, 16, 23, 30])
print(y[:, 2])
