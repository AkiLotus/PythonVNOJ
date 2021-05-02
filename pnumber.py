a, b = map(int, input().split())
is_prime = [True for _ in range(b+1)]
is_prime[0] = is_prime[1] = False
for x in range(2, b+1):
    if not is_prime[x]: continue
    for y in range(x*x, b+1, x):
        is_prime[y] = False

for i in range(a, b+1):
    if is_prime[i]:
        print(i)
