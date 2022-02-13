import string

def solution(s, n):
    answer = []
    Upper = list(string.ascii_uppercase)
    Lower = list(string.ascii_lowercase)
    
    s = list(s)
    print(s)
    for i in range(len(s)):
        if s[i] in Upper: 
            Upper_Re = Upper.index(s[i]) 
            Upper_cnt = Upper_Re+n
            if Upper_cnt <= len(Upper):
                answer.append(Upper[Upper_cnt-1])
            else:
                Upper_cnt = Upper_cnt - len(Upper) 
                answer.append(Upper[Upper_cnt-1])
            
        elif s[i] in Lower:
            Lower_Re = Lower.index(s[i]) # Lower_Re(z의 위치) = 23 , if z
            Lower_cnt = Lower_Re+n +1 # Lower_cnt(z의 변경 위치) = 24 , len(Lower) =24
            if Lower_cnt <=  len(Lower): # 변경위치가 총 길이와 같거나 작을때
                answer.append(Lower[Lower_cnt-1])
            else:
                Lower_cnt = Lower_cnt - len(Lower) 
                answer.append(Lower[Lower_cnt-1])
        else:
            answer.append(" ")
    answer = "".join(answer)
    answer = ",".join(answer)
    print(answer)
    return str(answer)

print(solution("z",1))