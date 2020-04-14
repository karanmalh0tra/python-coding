def stockSpan(price,n):
    stack = [0]
    Output = [0 for i in range(n)]
    Output[0] = 1
    for i in range(1,n):
        while(len(stack) > 0 and price[stack[-1]] < price[i]):
            stack.pop()
        Output[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])
        stack.append(i)
    return Output

n = int(input())
price = [int(ele) for ele in input().split()]
spans = stockSpan(price,n)
for ele in spans:
    print(ele,end= ' ')
