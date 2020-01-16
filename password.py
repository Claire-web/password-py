p = 0
while True:
    p < 3
    password = input('請輸入密碼')
    if password == 'a123456': 
        print('登入成功')
        break
    elif p == 0:
    	print('密碼錯誤! 還有2次機會')
    	p = p + 1
    	p < 3
    elif p == 1:
    	print('密碼錯誤! 還有1次機會')
    	p = p + 1
    	p < 3
    else:
    	print('登入失敗')
    	break