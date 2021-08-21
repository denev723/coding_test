# 단순히 반복문을 돌면서 자리 수를 비교하는 문제라고 판단
a_list = list(map(int, input().split(" ")))

# ascending, descending 기본값을 설정
ascending = True
descending = True

# 반복문을 돌면서 해당 자리와 다음 자리의 수를 비교하여
# 차례대로 증가하는 경우 descending 값을 False로 차례대로 감소하는 경우
# ascending 값을 False로 둠
for i in range(len(a_list) - 1):
    if a_list[i] < a_list[i+1]:
        descending = False
    if a_list[i] > a_list[i+1]:
        ascending = False

# ascending이 True라면 "ascending"을 descending이 True라면 "descending"을
# 둘 다 False라면 "mixed"를 출력하게함
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
