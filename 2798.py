# 입력
n, m = list(map(int, input().split(" ")))
cards = list(map(int, input().split(" ")))

# 결과값의 초기값 정의
result = 0

# 반복문을 돌면서 cards 리스트 중 3개 선택
for i in range(0, len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            sum_result = cards[i] + cards[j] + cards[k]
            # sum_result가 m보다 작은 경우 sum_result와 result 중 큰 값을 갱신
            if sum_result <= m:
                result = max(result, sum_result)

print(result)
