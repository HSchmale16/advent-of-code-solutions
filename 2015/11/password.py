from __future__ import print_function

def incre_password(pwd):
    pwd = list(pwd)
    def incre_letter(let):
        if ord(let) >= ord('z'):
            return True,'a'
        return False, chr(ord(let) + 1)
    result = True,None
    idx = -1
    while result[0]: 
        if idx == (-len(pwd) - 1):
            break
        result = incre_letter(pwd[idx])
        pwd[idx] = result[1]
        idx -= 1
    return ''.join(pwd)
        
def check_password_1(pwd):
    def req1():
        p = map(ord, pwd)
        for i in range(1, len(pwd) - 1):
            if p[i] - p[i-1] == p[i + 1] - p[i] == 1:
                return True
        return False
    def req2():
        if pwd.count('i') or pwd.count('o') or pwd.count('l'):
            return False
        return True
    def req3():
        pair_cnt = {chr(a)*2:0 for a in range(ord('a'), ord('z') + 1)}
        pwd_pairs = [ pwd[i-1:i+1] for i in range(1, len(pwd)) ]
        for pair in pwd_pairs:
            if pair in pair_cnt: pair_cnt[pair] += 1
        val = sum(map(lambda x: 0 if x == 0 else 1, pair_cnt.values()))
        return val >= 2
    return req1() and req2() and req3() 

password = 'vzbxkghb'
while not check_password_1(password):
    password = incre_password(password)
print(password)

password = incre_password(password)
while not check_password_1(password):
    password = incre_password(password)
print(password)
