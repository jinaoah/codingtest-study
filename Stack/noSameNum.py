# 프로그래머스 고득점 kit > 스택/큐 > 같은 숫자는 싫어
# 1. 내가 푼 풀이
def my_solution(arr):
    answer = []
#   1,1,1,3,3,0,1,1
#   0 1 2 3 4 5 6 7
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]: #첫번째 값과 다음 값이 같으면 for문으로
            continue #pass보다 continue가 더 빠름
        else: #앞의 값과 뒤의 값이 같지 않으면 앞의 값 추가
            answer.append(arr[i+1])
    # 근데 앞의 값을 추가하니까 맨 마지막 1을 넣지 못하는 문제가 발생!
    # 그래서 마지막 요소만 따로 꺼내서 추가해줌
    answer.append(arr.pop())
    return answer

#2. 다른 사람의 풀이
def another_solution(arr):
    answer = []
    for item in arr:
        if answer[-1:] == [item]: #빈 배열과 첫번째 값 1과 비교
            continue
        answer.append(item)
    
    return answer

arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]
print('입력값:',arr1)
print('실행 결과: ', my_solution(arr1))
print('실행 결과2: ', another_solution(arr2))