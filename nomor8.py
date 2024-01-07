# soal nomor 8.1
numbers = [1, 2, 3, 4, 5, 8, 9, 12, 15, 21, 27, 33, 39, 45]
div_by_3 = filter(lambda num: num % 3 == 0, numbers)
print(tuple(div_by_3))