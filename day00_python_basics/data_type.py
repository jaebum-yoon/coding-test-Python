# 정수형 (Integer)
a = 1000 # 양의 정수
print(a)

b = -1000 # 음의 정수
print(b)

# ================================

# 실수형 (Float)
a = 1e9 # 1 x 10^9
print(a)

a = 0.3 + 0.6
print(a)


if a == 0.9:
    print(True)
else:
    print(False)


a = 0.3 + 0.6
print(round(a, 2)) # 소수점 2자리까지 반올림
# 부동 소수점으로 인해 발생하는 오차를 해결하기 위해 round() 함수를 사용하여 소수점 자리를 지정할 수 있습니다.

# ================================

# 리스트 자료형
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 빈 리스트 선언 방법 (1)
a = list() # list() 함수를 사용하여 빈 리스트를 생성할 수 있습니다.
print(a)

# 빈 리스트 선언 방법 (2)
a = [] # 대괄호 []를 사용하여 빈 리스트를 생성할 수 있습니다.
print(a)

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화 방법
n = 10
a = [0] * n
print(a)


# ================================

# 리스트 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 요소를 가져오기 위해서는 인덱스 -1을 사용합니다.
print(a[-1]) 

# 두 번째 원소부터 네 번째 원소까지 가져오기 위해서는 인덱스 1부터 3까지를 사용
print(a[1:4]) # 끝 인덱스는 포함되지 않으므로 4는 포함되지 않습니다.


# ================================
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트 컴프리헨션
array = [i for i in range(20) if i %2 == 1]
print(array)


# ================================
# 1부터 9까지의 자연수를 더하는 반복문
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

# 언더바 사용 예시 (단순히 "Hello World"를 5번 출력하는 반복문)
for _ in range(5):
    print("Hello World")


# ================================
# 리스트 관련 메서드 사용 예시

# 기본 리스트 정의
a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 특정한 값의 원소를 모두 제거하는 다른 방식(시간 복잡도 줄이기)
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)


# ================================

# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 사전 자료형 관련 함수
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
value_list = data.values()

print(key_list)
print(value_list)

# ================================

# 집합 자료형
# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)


