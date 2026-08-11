
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Doubling the numbers

d_nums = list(map(lambda x: x * 2, numbers))

print("result:", d_nums)


#Even Numbers

even_nums = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Reslut:", even_nums)
