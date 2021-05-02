import heapq
heap = []

while True:
	try:
		command = input()
		if command[0] == "+":
			if len(heap) < 15000:
				heapq.heappush(heap, -int(command[1:]))
		if command[0] == "-":
			if len(heap) == 0: continue
			best = heap[0]
			while len(heap) > 0 and heap[0] == best:
				heapq.heappop(heap)

	except EOFError:
		break

values = list(set(heap))
values.sort()
print(len(values))
for x in values:
	print(-x)
