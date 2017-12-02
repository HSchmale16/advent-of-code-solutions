from hashlib import md5

def check_hash(hsh):
    return hsh.digest().encode('hex')[:6] == '000000'

salt = 'yzbqklnj'
i = 0
while True:
    m = md5(salt + str(i))
    if check_hash(m):
        break
    i += 1

print(i)
