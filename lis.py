import bisect

n = int(input())
a = list(map(int, input().split()))

lis = []
for x in a:
	if not len(lis) or lis[-1] < x:
		lis.append(x)
	else:
		index = bisect.bisect_left(lis, x)
		lis[index] = x

print(len(lis))
