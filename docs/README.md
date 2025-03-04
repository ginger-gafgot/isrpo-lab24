# Общее описание
В проекте на языке Python реализованы функции элементарного подсчёта площади и периметра геометрических фигур: 
1. Окружность (circle.py)
2. Прямоугольник (rectangle.py)
3. Квадрат (square.py) 
4. Треугольник (triangle.py) 

# Реализация функций
## Реализвация функций окружности в circle.py
- area(r)
```Python
def area(r):
	''' Принимает вещественное число r; возвращает площадь окружности с радиусом r '''
	
	return math.pi * r * r
```
1. Принцип работы функции - подсчёт площади окружности через математическую формулу S = πR²
В реализации функции: S - площадь, является возвращаемым значением функции; π - число пи, представлено константой math.pi; R² - алгебраический квадрат радиуса окружности, представлен в виде r * r

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргумента r:
``` Python
print(area(5))
print(area(7.8))
print(area(12347))
print(area(0))
```
Результат работы программы будет следующим:
```
78.53981633974483
191.13449704440302
478930801.76585215
0.0
```

- perimeter(r)
```Python
def perimeter(r):
	''' Принимает вещественное число r; возвращает периметр окружности с радиусом r '''

	return 2 * math.pi * r

```
1. Принцип работы функции - подсчёт длины окружности через математическую формулу P = 2πR
В реализации функции: P - периметр, является возвращаемым значением функции; π - число пи, представлено константой math.pi; R - радиус окружности, представлен в виде r

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргумента r:
``` Python
print(perimeter(5))
print(perimeter(7.8))
print(perimeter(12347))
print(perimeter(0))
```
Результат работы программы будет следующим:
```
31.41592653589793
49.00884539600077
77578.48898774636
0.0
```

## Реализвация функций прямоугольника в rectangle.py
- area(a, b)
```Python
def area(a,b):
	''' Принимает вещественные числа a, b; возвращает площадь прмоугольника со сторонами a, b '''

	return a*b
```
1. Принцип работы функции - подсчёт площади прямоугольника через математическую формулу S = ab
В реализации функции: S - площадь, является возвращаемым значением функции; a, b - стороны прямоугольника,  ab = a*b

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргументов a, b:
``` Python
print(area(9,6))
print(area(6,9))
print(area(3,6))
print(area(74.1,100))
print(area(5,0))
```
Результат работы программы будет следующим:
```
54
54
18
7409.999999999999
0
```

- perimeter(a, b)
```Python
def perimeter (a,b):
	''' Принимает вещественные числа a, b; возвращает периметр прмоугольника со сторонами a, b '''

	return (a + b) * 2

```
1. Принцип работы функции - подсчёт периметра прямоугольника через математическую формулу P = 2(a + b)
В реализации функции: P - периметр, является возвращаемым значением функции; a, b - стороны прямоугольника, 2(a+b) = (a + b) * 2

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргументов a, b:
``` Python
print(perimeter(9,6))
print(perimeter(6,9))
print(perimeter(3,6))
print(perimeter(74.1,100))
print(perimeter(5,0))
```
Результат работы программы будет следующим:
```
30
30
18
348.2
10
```
## Реализвация функций квадрата в square.py
- area(a)
```Python
def area(a):
	''' Принимает вещественное число a; возвращает площадь квадрата со стороной a '''
	
	return a * a
```
1. Принцип работы функции - подсчёт площади квадрата через математическую формулу S = a²
В реализации функции: S - площадь, является возвращаемым значением функции; a² - алгебраический квадрат стороны квадрата, представлен в виде a * a

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргумента a:
``` Python
print(area(4))
print(area(5.3))
print(area(0.99))
print(area(0))
```
Результат работы программы будет следующим:
```
16
28.09
0.9801
0
```

- perimeter(a)
```Python
def perimeter(a):
	''' Принимает вещественное число a; возвращает периметр квадрата со стороной a '''

	return 4 * a

```
1. Принцип работы функции - подсчёт периметра квадрата через математическую формулу P = 4a
В реализации функции: P - периметр, является возвращаемым значением функции; a - сторонa квадрата, 4a = 4 * a
2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргумента a:
``` Python
print(perimeter(4))
print(perimeter(5.3))
print(perimeter(0.99))
print(perimeter(0))
```
Результат работы программы будет следующим:
```
16
21.2
3.96
0
```
## Реализвация функций треугольника в triangle.py
- area(a,h)
```Python
def area(a,h):
	''' Принимает вещественные числа a, h; возвращает площадь треугольника со стороной a и проведенной к нему высотой h''' 

	return a * h / 2
```
1. Принцип работы функции - подсчёт площади треугольника через математическую формулу S = ah/2
В реализации функции: S - площадь, является возвращаемым значением функции; a - сторона треугольника, h - высота, проведенная к данной стороне, ah/2 = a * h / 2 

2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргументов a, h:
``` Python
print(area(4,19))
print(area(19,4))
print(area(0.99,15))
print(area(443, 3))
print(area(0, 7))
```
Результат работы программы будет следующим:
```
38.0
38.0
7.425
664.5
0.0
```

- perimeter(a,b,c)
```Python
def perimeter(a,b,c):
	''' Принимает вещественные числа a, b, c; возвращает периметр треугольника со сторонами a, b, c '''

	return a + b +c
```
1. Принцип работы функции - подсчёт периметра треугольника через математическую формулу P = a + b + c
В реализации функции: P - периметр, является возвращаемым значением функции; a, b, c - стороны треугольника
2. Напишем простую программу, чтобы проверить вывод функции при разных значениях аргументов a, b, c:
``` Python
print(perimeter(4,19, 4))
print(perimeter(1, 2.1 , 3))
print(perimeter(20, 13, 32))
print(perimeter(3, 4, 5))
print(perimeter(2, 8, 9))
print(perimeter(0, 7, 8))
```
Результат работы программы будет следующим:
```
27
6.1
65
12
19
15
```
# История изменения проекта
1. Копирование репозитория [geometry_lib](https://github.com/smartiqaorg/geometric_lib)
2. Разработка и добавление файла rectangle.py 
```
 commit c82a21c7abe9a26e5339723e9f4ff7319bf1b1b7
Author: ginger-gafgot <465333@niuitmo.ru>
Date:   Sat Sep 21 22:36:47 2024 +0300

    Rectangle added

 ```

3. Разработка и добавление файла triangle.py
```
commit f3904910058cfd098e3bb091146e9adf61d99c8c
Author: ginger-gafgot <465333@niuitmo.ru>
Date:   Sat Sep 21 22:38:16 2024 +0300

    Triangle added

```
4. Исправлена ошибка в функции подсчёта периметра прямоугольника
```
commit a93f395bbc13b018b73fcaf75c1149178b6a7588 (origin/new_features_465333, origin/HEAD)
Author: ginger-gafgot <465333@niuitmo.ru>
Date:   Sat Sep 21 22:38:57 2024 +0300

    Rectangle's perimeter fixed

``` 