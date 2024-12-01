from collections import deque

def isPalindrome(word):
    que = deque(word)
    while len(que) > 1:
        s1 = que.pop()
        s2 = que.popleft()
        if s1 == s2:
            return True
    return False

print(isPalindrome("jajko"))

