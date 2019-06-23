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
    page=len(custlist)-1

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

def print_page(pg):
    if pg == -1:
        print('아직 입력된 정보가 없습니다!')
    else:
        print('PAGE : %d\n'% (pg+1))
        print(custlist[pg])
    
def prev_page(pg):
    if pg <= 0:
        print('첫번째 페이지 입니다.')
    else: pg-=1
    print('PAGE : %d\n'% (pg+1))
    print(custlist[pg])
    return pg

def next_page(pg):
    if pg >= len(custlist)-1:
        print('마지막 페이지 입니다.')
    else: pg+=1
    print('PAGE : %d\n'% (pg+1))
    print(custlist[pg])
    return pg



def del_cust(pg):
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
    pg=len(custlist)-1
    return pg

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
    ''').upper()
    if menu == 'I':
        Insert_cust()
    elif menu == 'C':
        print_page(page)
    elif menu == 'P':
        page=prev_page(page)
    elif menu == 'N':
        page=next_page(page)
    elif menu == 'U':
        print('고객 정보 수정')
        idx=-1
        demail = input('수정할 회원의 이메일을 입력해주세요 : ')
        for i in custlist:
            if i['email'] == demail:
                idx = custlist.index(i)
        if idx == -1:
            print('등록되어있지 않은 이메일입니다.')
            continue
        Edit_P = custlist[idx]
        while True:
            print('''           ===수정할 정보 선택===
            1. 이름 : {}
            2. 성별 : {}
            3. 이메일 : {}
            4. 출생년도 : {}
            (exit 입력시 종료)
            '''.format(Edit_P['name'], Edit_P['sex'], Edit_P['email'],Edit_P['birthyear']))
            ins = input('번호 입력 : ')
            if ins == '1':
                ch = cust_name()
                print('이름 : {} -> {}'.format(Edit_P['name'], ch))
                q= input('수정하시겠습니까? (Y/N) :')
                if q == 'Y':
                    Edit_P['name']=ch
                    continue
                else: continue
            elif ins == '2':
                ch = cust_sex()
                print('성별 : {} -> {}'.format(Edit_P['sex'], ch))
                q= input('수정하시겠습니까? (Y/N) :')
                if q == 'Y':
                    Edit_P['sex']=ch
                    continue
                else: continue
            elif ins == '3':
                ch = cust_email()
                print('이메일 : {} -> {}'.format(Edit_P['email'], ch))
                q= input('수정하시겠습니까? (Y/N) :')
                if q == 'Y':
                    Edit_P['email']=ch
                    continue
                else: continue
            elif ins == '4':
                ch = cust_birth()
                print('출생년도 : {} -> {}'.format(Edit_P['birthyear'], ch))
                q= input('수정하시겠습니까? (Y/N) :')
                if q == 'Y':
                    Edit_P['birthyear']=ch
                    continue
                else: continue
            elif ins == 'exit':
                break
            else :
                print('잘못 입력하셨습니다.\n')
    elif menu == 'D':
        page=del_cust(page)
    elif menu == 'Q':
        print('종료합니다.')
        break
    else :
        print('잘못 입력하셨습니다.\n')
        