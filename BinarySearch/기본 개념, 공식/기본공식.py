이분 탐색 문제 유형은 두가지이다. 그냥 아래 코드만 알면 된다.

어떤 함수 bool f(x)가 있을 때,
경우 1. f(x)가 참이 되는 최솟값 x 구하기
경우 2. f(x)가 참이 되는 최댓값 x 구하기
-> f(x)는 x가 문제의 조건을 만족시키는 지 구하는 함수

예시)  "백준 2110번: 공유기 설치"
      이 문제의 경우 조건을 만족시키는 최댓값을 구하라고 하니
      f(x) = { 공유기 사이 간격이 최소 x가 되도록 c개를 설치할 수 있으면 return True }로 놓고 경우2 코드를 쓰면 된다.

// 탐색 범위 = [mn, mx]
// 만약 불가능한 경우가 없다면 (최소 하나의 해가 [mn, mx]사이에 있다는 게 보장된다면)
// 경우 1, 2 전부 lo = mn, hi = mx로 통일해도 됨


// 경우 1 -> [lo, hi) 구간에서 이분 탐색

lo, hi = mn, mx + 1
while lo != hi:
    int mid = (lo + hi) >> 1
    if f(mid):
        hi = mid
    else:<br>
        lo = mid + 1
        
if lo == mx + 1:
    IMPOSSIBLE   // 가능한 해가 없음
else:
    answer = lo
            
            
// 경우 2 -> (lo, hi] 구간에서 이분 탐색
lo, hi = mn - 1, mx
while lo != hi:
    int mid = (lo + hi + 1) >> 1
    if f(mid):
        lo = mid
    else:<br>
        hi = mid - 1
        
if lo == mn - 1:
    IMPOSSIBLE
else:<br>
    answer = lo
