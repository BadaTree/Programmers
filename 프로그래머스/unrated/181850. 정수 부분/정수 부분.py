def solution(flo):
    answer = 0
    if flo >= 0 and flo <= 100:
        answer = int(flo)
        print(f'{flo}의 정수 부분은 {answer}입니다.')
    return answer
