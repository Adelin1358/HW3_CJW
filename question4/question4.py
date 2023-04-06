def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    for i in range(0, 15, 2):
        result = factorial(i)
        print(f"{i} 의 계승은 {result} 입니다.")
