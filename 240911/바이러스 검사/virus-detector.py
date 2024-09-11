n = int(input())
c = list(map(int, input().split()))
maxB, maxW = map(int, input().split())

def required_mem_num(customer_num):
    if customer_num <= 0:
        return 0

    if customer_num % maxW == 0:
        return customer_num // maxW
    else:
        return (customer_num//maxW) +1

ans = 0

for customer_num in c:
    ans += 1

    ans += required_mem_num(customer_num - maxB)

print(ans)