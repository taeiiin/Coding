T = int(input())
for test_case in range(1, T + 1):
	n = list(map(int, input().split()))
	print("#", test_case, " ", max(n), sep="")