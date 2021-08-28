def solution(price, money, count):
    answer = price * ((count * (count + 1)) // 2) - money
    return answer if answer > 0 else 0