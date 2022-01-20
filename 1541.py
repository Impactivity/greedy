# 주어진 식을 괄호쳐서 합이 최소값으로 만드는 문제 ( +, - 만을 포함하는  )
import sys
read = sys.stdin.readline

# #solution 1 )
# # 이 해결의 핵심 아이디어는 - 가 나오기 전까지 모든 수를 더하고 _sum1에 저장한다음
# # -가 나오는 순간부터 _sum2에 저장하여 최종적으로 _sum1 - sum2 를 해준다.
# # 즉, - 가 나온 다음부터 음수의 최댓값을 만든다면 정답에서 요구하는 최솟값이 될 것이다.

# arr = read().strip()
# st = ''
# arr2 = []
#
# #주어진 식을 연산자와 숫자로 분리한다.
# for i in arr:
#     if i != '+' and i != '-':
#         st += i
#     else:
#         arr2.append(int(st))
#         arr2.append(i)
#         st = ''
# arr2.append(int(st))
#
# n = len(arr2)
#
# _sum = 0
# _sum2 = 0
#
# # -가 나오기 전은 is_True가 True값이 된다.
#
# is_True = True
# if '-' in arr2:
#     for i in range(0,n):
#         if is_True == True:
#             if arr2[i] == '-':
#                 is_True = False
#             elif arr2[i] != '+' :
#                 _sum += arr2[i]
#         else:
#             if arr2[i] != '-' and arr2[i] != '+':
#                 _sum2 += arr2[i]
#     print(_sum - _sum2)
# # -가 없는 식은 모두 더하면된다.
# else :
#     for num in range(0,n):
#         if arr2[num] != '-' and arr2[num] != '+':
#             _sum += arr2[num]
#     print(_sum)


# solution 2
# - 구분자로 제거해주고 최초 - 기준으로 앞에 있는대상의 합과 뒤에 있는 대상들의 합의 차를 구한다
# solution 1 과 비슷한 아이디어인데 배열 슬라이스, split을 이용하여 코드를 간결하게 작성

arr = read().split('-') # 처음에 -로 구분해주는게 핵심 포인트임
arr[-1] = arr[-1][0:-1] #뒤에 개행문자 제거
_sum = 0
for i in arr[0].split('+'):
    _sum += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        _sum -= int(j)

print(_sum)
