from Set import Set 

def main():
	SetA = Set([1,3,5,7,9,10,11,13,15,17,19])
	SetB = Set([2,4,6,8,10,12,14,16,18])

	print (SetA.Size())
	SetUnion = SetA|SetB
	SetInt = SetA & SetB

	for i in SetUnion:
		print(i)

	for i in SetInt:
		print(i)

main()