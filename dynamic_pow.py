import timeit

def remainder_when_divided_by_power(num1, num2):
	return num1 - ((num1 // num2) * num2)

def special_insert(index, data, arr):
	while index > len(arr):
		if own_pow_calc(len(arr), arr) not in arr:
			arr.append(own_pow_calc(len(arr), arr))

	arr.append(data)
	

def own_pow_calc(b, arr):
	
	if b in range(len(arr)):
		
		return arr[b]

	elif b not in range(len(arr)):
		bolum = remainder_when_divided_by_power(b, (len(arr) - 1))

		result = arr[bolum] * own_pow_calc(b - bolum, arr)
		
		special_insert(b, result, arr)
		
		return result

arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
arrf = [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625]


for i in range(1,50000):
	own_pow_calc(i, arrf)

while True:
	c = int(input("c = "))

	print(f"2 ^ {c} = {own_pow_calc(c, arrf)}", timeit.timeit(lambda: own_pow_calc(c, arrf), number=10000))

