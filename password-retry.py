password = 'a123456'
p = 3 # 剩餘機會
while p > 0:
    p = p - 1
    pwd = input('請輸入密碼: ')
    if pwd == password: 
        print('登入成功!')
        break # 逃出迴圈
    else:
        print('密碼錯誤!')
        if p > 0:
            print('還有' , p, '次機會')
        else:
            print('帳號已鎖')
        