password = 'a123456'
p = 3
while True:
    pwd = input('請輸入密碼:')
    if pwd == password:
        print('登入成功')
        break
    else:
        p = p - 1
        print('密碼錯誤,還有', p, '次機會')
        if p == 0:
            print('密碼輸入失敗!')
            break
