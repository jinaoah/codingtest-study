# 스택: LIFO(Last In First Out) -> 리스트로 구현
stack = []

stack.append(5)
stack.append(4)
stack.append(3)

print(stack)
print(stack[-1]) #3
print(stack.pop()) #3

if stack:
    print('스택 비어있지 않음')
    pass
else:
    pass #나중에 코드를 작성할 때 해당 블록의 내용을 추가하거나 구현할 때 유용합니다.
idx = 0
for item in stack:
    print('[{0}] : {1}'.format(idx, item))
    idx += 1