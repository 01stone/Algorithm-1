# 작성자: red-Pen9uin
# Data structure: stack
# 12605번: 단어순서 뒤집기
"""
스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라.
각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다.
각 행은 알파벳과 스페이스로만 이루어져 있다. 단어 사이에는 하나의 스페이스만 들어간다.

"""
import sys

def get_reversed_str(word: str) ->None:
    temp = word.rstrip('\n') # 개행문자 제거
    num = len(temp) # length of word
    end_index = num
    result = ""

    for i in reversed(range(0, num)):
        if temp[i] == ' ':
            result += temp[i:end_index]
            end_index = i

    if temp[0] != ' ':
        result += ' ' + temp[0:end_index]
    
    return result


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    for i in range(1, num+1):
        word = sys.stdin.readline()
        print( f'Case #{i}:{get_reversed_str(word)}')