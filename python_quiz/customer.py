import re
custlist=[]
page=-1

def Insert_cust():
    customer={'name':'', 'sex':'','email':'','birthyear':''}
    customer['name']= cust_name()
    customer['sex']= cust_sex()
    customer['email']= cust_email()
    customer['birthyear']= cust_birth()
    custlist.append(customer)
    print(custlist)
    global page
    page+=1

def cust_name():
    name = input('이름 입력 : ')
    return name

def cust_sex():
    while True:
        sex= input('성별 입력 : ')
        sex = sex.upper()
        if sex == 'M' or sex == 'F':
            break
        else: print('다시 입력.')
    return sex

def cust_email():
    while True:
        email = input("이메일 입력 : ")
        check=0
        for i in custlist:
            if i['email']==email:
                check=1
            
        m = re.search('\w+@[a-z]+[.][a-z]{2}', email)
        if m == None:
            print('@를 포함하여 제대로 입력해주세요.')
        else:
            if check == 0:
                break
            print('중복되는 이메일입니다.')
    return email

def cust_birth():
    while True:
        birth = input('생년월일 입력 : ')
        if len(birth) == 4 and birth.isdigit(): #문자열 내의 내용이 숫자인지 확인
            break
        else : print('다시 입력.')
    return birth

while True:
    menu = input('''
    메뉴 선택:
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')
    if menu == 'I':
        Insert_cust()
    elif menu == 'C':
        print('PAGE : %d\n'% (page+1))
        print(custlist[page])
    elif menu == 'P':
        if page == 0:
            print('첫번째 페이지 입니다.')
        else: page-=1
        print('PAGE : %d\n'% (page+1))
        print(custlist[page])
    elif menu == 'N':
        if page == len(custlist)-1:
            print('마지막 페이지 입니다.')
        else: page+=1
        print('PAGE : %d\n'% (page+1))
        print(custlist[page])
    elif menu == 'U':
        print('고객 정보 수정')
    elif menu == 'D':
        print('고객 정보 삭제')
        delok=0
        demail = input('삭제할 회원의 이메일을 입력해주세요 : ')
        for i in custlist:
            if i['email'] == demail:
                index = custlist.index(i)
                print('삭제되었습니다.\n')
                del custlist[index]
                delok=1
        if delok==0:
            print('등록되어있지 않은 이메일입니다.')
        page=0
    elif menu == 'Q':
        print('종료합니다.')
        break
    else :
        print('잘못 입력하셨습니다.\n')
        