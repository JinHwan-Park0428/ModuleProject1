###필요한 모듈 불러오기
import pymysql
###회원 관련 클래스 설계
class Userinfo :
    def __init__(self, cursor):
        self.cursor = cursor
    ###회원 가입 관련 인스턴스 설계
    def Sign_up(self, userid, userpwd, username):
        self.userid = userid
        self.userpwd = userpwd
        self.username = username
        insertSql = """INSERT INTO userinfo(userid, userpwd, username, reg_date) VALUES(%s, %s, %s, NOW())"""
        try :
            self.cursor.execute(insertSql, (self.userid, self.userpwd, self.username))
        except Exception :
            print("\n오류가 발생했습니다. 다시 시도해주세요.")
        else :
            connectdb.commit()
            print("\n회원 가입이 완료 됐습니다.")
    ###회원 로그인 관련 인스턴스 설계
    def User_login(self, userid, userpwd, userpass):
        self.userid = userid
        self.userpwd = userpwd
        check_id = '''SELECT * FROM userinfo WHERE userid=%s AND userpwd=%s'''
        self.cursor.execute(check_id, (self.userid, self.userpwd))
        data = self.cursor.fetchone()
        if data != None :
            print("\n로그인 되었습니다.")
            userpass = 1
            return userpass 
        else : 
            print("\n계정 정보를 다시 확인해주세요.")
            userpass = 0
            return userpass 
    ###회원 정보 변경 관련 인스턴스 설계
    def Change_user_info(self, userid, userpwd, changepwd, changename):
        self.userid = userid
        self.userpwd = userpwd
        self.changepwd = changepwd
        self.changename = changename
        updatename = """UPDATE userinfo SET username = %s WHERE userid = %s"""
        updatepwd = """UPDATE userinfo SET userpwd = %s WHERE userid = %s"""
        try :
            self.cursor.execute(updatename, (self.changename, self.userid))
            self.cursor.execute(updatepwd, (self.changepwd, self.userid))
        except Exception :
            print("\n오류가 발생했습니다. 다시 시도해주세요.")
        else :
            connectdb.commit()
            print("\n이름과 비밀번호가 변경되었습니다.")
    ###회원 탈퇴 관련 인스턴스 설계
    def Delete_user_info(self, userid, userpwd):
        self.userid = userid
        self.userpwd = userpwd
        check_id = 'SELECT * FROM userinfo WHERE userid=%s AND userpwd=%s'
        self.cursor.execute(check_id, (self.userid, self.userpwd))       
        data = self.cursor.fetchone()
        if data != None :       
            deleteinfo = '''DELETE FROM userinfo WHERE userid = %s'''
            try :
                self.cursor.execute(deleteinfo, (self.userid, ))
            except Exception :
                print("\n오류가 발생했습니다. 다시 시도해주세요.")
            else :
                connectdb.commit()
                print("\n회원 탈퇴가 완료되었습니다. 이용해주셔서 감사합니다.") 
                return 0  
        else : 
            print("\n비밀번호를 다시 확인해주세요.")
            return 1       
###상품 관련 클래스 설계
class Merchandiseinfo : 
    def __init__(self, cursor):
        self.cursor = cursor  
    ###상품 목록 조회 관련 인스턴스 설계
    def Showmerchandise(self):
        show_mer = '''SELECT * FROM merchandiseinfo'''
        self.cursor.execute(show_mer)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호 : "+ str(data[0]) + " 상품 태그 : " + str(data[1]) + " 상품 종류 : " + str(data[2]) + " 상품 이름 : " + str(data[3]) + " 상품 가격 : " + str(data[4]) + " 상품 재고 : " + str(data[5]) + " 유통기한 : " + str(data[6]))
                data = self.cursor.fetchone()
        else : print("\n상품이 존재하지 않습니다.")
    ###상품 목록 태그로 조회 관련 인스턴스 설계
    def Showmerchandisetag(self, tag):
        self.tag = tag
        show_mer = '''SELECT * FROM merchandiseinfo WHERE tag=%s'''
        self.cursor.execute(show_mer, (self.tag, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호 : "+ str(data[0]) + " 상품 태그 : " + str(data[1]) + " 상품 종류 : " + str(data[2]) + " 상품 이름 : " + str(data[3]) + " 상품 가격 : " + str(data[4]) + " 상품 재고 : " + str(data[5]) + " 유통기한 : " + str(data[6]))
                data = self.cursor.fetchone()
        else : print("\n해당 상품은 존재하지 않습니다.")
    ###상품 목록 타입으로 조회 관련 인스턴스 설계
    def Showmerchandisetype(self, type):
        self.type = type
        show_mer = '''SELECT * FROM merchandiseinfo WHERE type=%s'''
        self.cursor.execute(show_mer, (self.type, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호 : "+ str(data[0]) + " 상품 태그 : " + str(data[1]) + " 상품 종류 : " + str(data[2]) + " 상품 이름 : " + str(data[3]) + " 상품 가격 : " + str(data[4]) + " 상품 재고 : " + str(data[5]) + " 유통기한 : " + str(data[6]))
                data = self.cursor.fetchone()
        else : print("\n해당 상품은 존재하지 않습니다.")
    ###상품 목록 이름으로 조회 관련 인스턴스 설계
    def Showmerchandisename(self, name):
        self.name = name
        show_mer = '''SELECT * FROM merchandiseinfo WHERE name=%s'''
        self.cursor.execute(show_mer, (self.name, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호 : "+ str(data[0]) + " 상품 태그 : " + str(data[1]) + " 상품 종류 : " + str(data[2]) + " 상품 이름 : " + str(data[3]) + " 상품 가격 : " + str(data[4]) + " 상품 재고 : " + str(data[5]) + " 유통기한 : " + str(data[6]))
                data = self.cursor.fetchone()
        else : print("\n해당 상품은 존재하지 않습니다.")
    ###구매하려는 상품 확인 관련 인스턴스 설계
    def Showmerchandiseid(self, id, num):
        self.id = id
        self.num = num
        show_mer = '''SELECT * FROM merchandiseinfo WHERE id=%s'''
        self.cursor.execute(show_mer, (self.id, ))
        data = self.cursor.fetchone()
        if data != None :
            print("\n구매하고자 하는 상품은 {}입니다.".format(str(data[3])))
            self.num = 1
            return self.num
        else :            
            print("\n해당 상품은 존재하지 않습니다.")
            self.num = 0
            return self.num
    ###상품 구매 관련 인스턴스 설계
    def Buymerchandise(self, id, quantity, userid):
        self.id = id
        self.quantity = quantity
        self.userid = userid
        if self.quantity == 0 :
            print("\n0개는 구매하실 수 없습니다.")
        else :
            show_mer = '''SELECT * FROM merchandiseinfo WHERE id=%s'''
            self.cursor.execute(show_mer, (self.id, ))
            data = self.cursor.fetchone()
            temp_quantity = str(int(data[5]) - int(self.quantity))
            if int(temp_quantity) < 0 :
                print("\n재고를 초과하여 구매하실 수 없습니다.")
            else : 
                update_mer = '''UPDATE merchandiseinfo SET quantity = %s WHERE id = %s'''
                insert_buy = '''INSERT INTO buyinfo(userid, id, name, total_price, quantity, buy_date) VALUES(%s, %s, %s, %s, %s, NOW())'''
                try :
                    self.cursor.execute(update_mer, (temp_quantity, self.id))
                    total_price = str(int(data[4]) * int(self.quantity))
                    self.cursor.execute(insert_buy, (self.userid, self.id, str(data[3]), total_price, self.quantity))
                except Exception :
                    print("\n오류가 발생했습니다. 다시 시도해주세요.")
                else : 
                    connectdb.commit()
                    print("\n상품 구매를 완료했습니다. 감사합니다.")
    ###구매한 상품 목록 조회
    def Buylog(self, userid) :
        self.userid = userid
        show_log = '''SELECT * FROM buyinfo WHERE userid=%s'''
        self.cursor.execute(show_log, (self.userid, ))
        data = self.cursor.fetchone()
        if data != None :
            print("\n구매하신 상품 목록입니다.")
            while data :
                print("\n고유번호: {}, 상품명: {}, 최종 가격: {}, 수량: {}".format(str(data[1]), str(data[2]), str(data[3]), str(data[4])))
                data = self.cursor.fetchone()
        else : print("\n상품이 존재하지 않습니다.")
###관리자 관련 클래스 설계
class Admininfo :
    def __init__(self, cursor):
        self.cursor = cursor
    ###관리자 로그인 관련 인스턴스 설계
    def Admin_login(self, adminid, adminpwd, adminpass):
        self.adminid = adminid
        self.adminpwd = adminpwd
        check_id = 'SELECT * FROM admininfo WHERE id=%s AND pwd=%s'
        self.cursor.execute(check_id, (self.adminid, self.adminpwd))
        data = self.cursor.fetchone()
        if data != None :   
            print("\n로그인 되었습니다.")
            adminpass = 1              
            return adminpass 
        else : 
            print("\n계정 정보를 다시 확인해주세요.")
            adminpass = 0               
            return adminpass 
    ###회원 전체 목록 조회 관련 인스턴스 설계
    def Look_users(self) :
        show_user = '''SELECT * FROM userinfo'''
        self.cursor.execute(show_user)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n회원 아이디: {0}, 회원 이름: {1}, 가입 날짜: {2}".format(str(data[0]), str(data[2]), str(data[3])))
                data = self.cursor.fetchone()
        else : print("\n회원이 존재하지 않습니다.")
    ###전체 구매 내역 조회 관련 인스턴스 설계
    def Buylogall(self) :
        show_log = '''SELECT * FROM buyinfo'''
        self.cursor.execute(show_log)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n구매한 회원: {}, 상품 고유 번호: {}, 상품명: {}, 총 가격: {}, 수량: {}, 구매일시: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5])))
                data = self.cursor.fetchone()
        else : print("\n구매내역이 존재하지 않습니다.")
    ###고유 번호로 구매 내역 조회 관련 인스턴스 설계
    def Buylogid(self, buyid) :
        self.buyid = buyid
        show_log = '''SELECT * FROM buyinfo WHERE id=%s'''
        self.cursor.execute(show_log, (self.buyid, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n구매한 회원: {}, 상품 고유 번호: {}, 상품명: {}, 총 가격: {}, 수량: {}, 구매일시: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5])))
                data = self.cursor.fetchone()
        else : print("\n해당 고유 번호에 관련된 주문 목록이 존재하지 않습니다.")
    ###회원 아이디로 구매 내역 조회 관련 인스턴스 설계
    def Buyloguserid(self, buyuserid) :
        self.buyuserid = buyuserid
        show_log = '''SELECT * FROM buyinfo WHERE userid=%s'''
        self.cursor.execute(show_log, (self.buyuserid, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n구매한 회원: {}, 상품 고유 번호: {}, 상품명: {}, 총 가격: {}, 수량: {}, 구매일시: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5])))
                data = self.cursor.fetchone()
        else : print("\n해당 회원에 관련된 주문 목록이 존재하지 않습니다.")
    ###상품 목록 전체 조회 관련 인스턴스 설계
    def Showmerchandiseall(self) :
        show_log = '''SELECT * FROM merchandiseinfo'''
        self.cursor.execute(show_log)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호: {}, 상품 태그: {}, 상품 타입: {}, 상품명: {}, 상품 단가: {}, 상품 재고:{}, 유통기한: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6])))
                data = self.cursor.fetchone()
        else : print("\n상품내역이 존재하지 않습니다.")
    ###비어있는 재고 조회 관련 인스턴스 설계
    def Showmerchandiseempty(self) :
        show_log = '''SELECT * FROM merchandiseinfo WHERE quantity='0' '''
        self.cursor.execute(show_log)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호: {}, 상품 태그: {}, 상품 타입: {}, 상품명: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3])))
                data = self.cursor.fetchone()
        else : print("\n비어있는 상품이 없습니다.")
    ###유통기한이 다된 상품 목록 조회 관련 인스턴스 설계
    def Showmerchandiseexpired(self) :
        show_log = '''SELECT * FROM merchandiseinfo WHERE expiration_date < NOW() '''
        self.cursor.execute(show_log)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호: {}, 상품 태그: {}, 상품 타입: {}, 상품명: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3])))
                data = self.cursor.fetchone()
        else : print("\n유통기한이 지난 상품이 없습니다.")
    ###조건에 맞는 상품 목록 조회 관련 인스턴스 설계
    def Showmerchandisecondition(self, quantity) :
        self.quantity = quantity
        show_log = '''SELECT * FROM merchandiseinfo WHERE quantity < %s '''
        self.cursor.execute(show_log, (self.quantity, ))
        data = self.cursor.fetchone()
        if data != None :
            while data :
                print("\n고유 번호: {}, 상품 태그: {}, 상품 타입: {}, 상품명: {}, 상품 재고: {}".format(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[5])))
                data = self.cursor.fetchone()
        else : print("\n조건에 맞는 상품이 없습니다.")
    ###상품 재고 추가 관련 인스턴스 설계
    def Addmerchandise(self ,add_id, add_quantity) :
        self.add_id = add_id
        self.add_quantity = add_quantity
        show_log = '''SELECT * FROM merchandiseinfo WHERE id=%s '''
        self.cursor.execute(show_log, (self.add_id, ))
        data = self.cursor.fetchone()
        addquan = str(int(data[5]) + int(self.add_quantity))
        if data != None :
            add_merchandise = '''UPDATE merchandiseinfo SET quantity=%s WHERE id=%s'''
            try :
                self.cursor.execute(add_merchandise, (addquan, self.add_id))
            except Exception :
                print("\n오류가 발생했습니다. 다시 시도해주세요.")
            else : 
                connectdb.commit()     
        else : print("\n상품내역이 존재하지 않습니다.")
    ###유통기한 변경 관련 인스턴스 설계
    def Changedate(self, change_id, change_date) :
        self.change_id = change_id
        self.chage_date = change_date
        show_log = '''SELECT * FROM merchandiseinfo WHERE id=%s '''
        self.cursor.execute(show_log, (self.change_id, ))
        data = self.cursor.fetchone()
        if data != None :
            change_merchandise = '''UPDATE merchandiseinfo SET expiration_date=%s WHERE id=%s'''
            try :
                self.cursor.execute(change_merchandise, (self.chage_date, self.change_id))
            except Exception :
                print("형식이 틀렸습니다.")
            else:
                connectdb.commit() 
                print("\n유통기한이 변경되었습니다.")   
        else : print("\n상품내역이 존재하지 않습니다.")
    ###재고 줄이기 관련 인스턴스 설계
    def Downquantity(self, down_id, down_quantity) :
        self.down_id = down_id
        self.down_quantity = down_quantity
        show_log = '''SELECT * FROM merchandiseinfo WHERE id=%s '''
        self.cursor.execute(show_log, (self.down_id, ))
        data = self.cursor.fetchone()
        if data != None :
            if int(data[5]) > int(self.down_quantity) :
                downquan = str(int(data[5]) - int(self.down_quantity))
                down_merchandise = '''UPDATE merchandiseinfo SET quantity=%s WHERE id=%s'''
                try :
                    self.cursor.execute(down_merchandise, (downquan, self.down_id))
                except Exception :
                    print("\n오류가 발생했습니다. 다시 확인해주세요.")
                else:
                    connectdb.commit()     
            else : print("\n남아있는 재고보다 많은 양을 줄일 순 없습니다.")
        else : print("\n상품내역이 존재하지 않습니다.")
    ###상품 목록 추가 관련 인스턴스 설계
    def Updatemerchandise(self, update_id, update_tag, update_type, update_name, update_price, update_quantity, update_expirate) :
        self.update_id = update_id
        self.update_tag = update_tag
        self.update_type = update_type
        self.update_name = update_name
        self.update_price = update_price
        self.update_quantity = update_quantity
        self.update_expirate = update_expirate
        update_merchandise = '''INSERT INTO merchandiseinfo(id, tag, type, name, price, quantity, expiration_date) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        try :
            self.cursor.execute(update_merchandise, (self.update_id, self.update_tag, self.update_type, self.update_name, self.update_price, self.update_quantity, self.update_expirate))
        except Exception :
            print("\n오류가 발생했습니다. 다시 시도해주세요.")
        else :
            connectdb.commit()
            print("\n상품 목록 추가가 완료됐습니다.") 
    ###상품 목록 제거 관련 인스턴스 설계
    def Deletemerchandise(self, delete_id) :
        self.delete_id = delete_id
        show_log = '''SELECT * FROM merchandiseinfo WHERE id=%s '''
        self.cursor.execute(show_log, (self.delete_id, ))
        data = self.cursor.fetchone()
        if data != None :
            delete_merchandise = '''DELETE FROM merchandiseinfo WHERE id=%s'''
            try :
                self.cursor.execute(delete_merchandise, (self.delete_id, ))
            except Exception :
                print("\n오류가 발생했습니다. 다시 확인해주세요.")
            else:
                connectdb.commit()
                print("\n상품을 제거했습니다.")     
        else : print("\n상품내역이 존재하지 않습니다.")
    ###월별 최고 금액 구매자 조회 관련 인스턴스 설계
    def Monthbestuser(self, month_num) :
        self.month_num = month_num
        userlist = []
        bestuser = dict()
        show_name = '''SELECT userid FROM userinfo'''
        self.cursor.execute(show_name)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                userlist.append(data[0])
                data = self.cursor.fetchone()
        else : print("\n회원이 존재하지 않습니다.")
        for user in userlist :
            total_price = 0
            bestuser[user] = 0
            show_log = '''SELECT * FROM buyinfo WHERE userid=%s AND MONTH(buy_date)=%s'''
            self.cursor.execute(show_log, (user, self.month_num))
            pdata = self.cursor.fetchone()
            if pdata != None :
                while pdata :
                    total_price += int(pdata[3])
                    pdata = self.cursor.fetchone()
                bestuser[user] = total_price
        buy_max = max(bestuser.keys(), key = lambda k : bestuser[k])
        if bestuser[buy_max] != 0 :
            print("\n가장 많이 구매한 회원 : {}, 금액 : {}원".format(str(buy_max), bestuser[buy_max]))
        else : print("\n구매 내역이 존재하지 않습니다.")
    ###월별 가장 많이 팔린 상품 조회 관련 인스턴스 설계
    def Monthbestmerchandise(self, month_num) :
        self.month_num = month_num
        merchanlist = []
        bestmerchan = dict()
        show_name = '''SELECT id FROM merchandiseinfo'''
        self.cursor.execute(show_name)
        data = self.cursor.fetchone()
        if data != None :
            while data :
                merchanlist.append(data)
                data = self.cursor.fetchone()
        else : print("\n상품이 존재하지 않습니다.")
        for merchan in merchanlist :
            total_quantity = 0
            bestmerchan[merchan] = 0
            show_log = '''SELECT * FROM buyinfo WHERE id=%s AND MONTH(buy_date)=%s'''
            self.cursor.execute(show_log, (merchan, self.month_num))
            pdata = self.cursor.fetchone()
            if pdata != None :
                while pdata :
                    total_quantity += int(pdata[4])
                    pdata = self.cursor.fetchone()
                bestmerchan[merchan] = total_quantity
        buy_max = max(bestmerchan.keys(), key = lambda k : bestmerchan[k])
        if bestmerchan[buy_max] != 0 :
            print("\n가장 많이 구매한 상품의 고유 번호 : {}, 갯수 : {}개".format(list(buy_max)[0], bestmerchan[buy_max]))
        else : print("\n구매 내역이 존재하지 않습니다.")
###mysql 연동 단계
connectdb = pymysql.connect(host='172.17.0.2', user='root', password='', port=3306, db='mydb', charset='utf8')
cursor = connectdb.cursor()
usercur = Userinfo(cursor)
merchandisecur = Merchandiseinfo(cursor)
admincur = Admininfo(cursor)
###메인메뉴 UI단계
while True :
    userid = ''
    userpwd = ''
    username = ''
    adminid = ''
    adminpwd =''
    exitstr = ''
    tempstr = ''
    passnum = 0
    print()
    print("%40s" % "메인 메뉴")
    print()
    print("#" * 80)
    print("%40s" % "1. 회원가입")
    print()
    print("%40s" % "2. 회원 로그인")
    print()
    print("%40s" % "3. 관리자 로그인")
    print()
    print("%40s" % "4. 종료")
    print("#" * 80)
    print()
    try:
        input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
    except Exception :
        print("\n숫자를 입력해주세요.")
        continue
    if not input_menu_num in range(1, 5) :
        print("\n잘못된 번호를 입력하셨습니다.")
        continue
    ###메인 메뉴 - 회원가입 단계
    if input_menu_num == 1 :
        print()
        print("%40s" % "회원가입")
        print()
        print("#" * 80)
        print("%40s" % "환영합니다!!!")
        print()
        print("%40s" % "당신의 정보를 입력해주세요.")
        print("#" * 80)
        print()
        while True:
            if tempstr == 'y' :
                break
            exitstr = input("회원가입을 진행하려면 y을 입력해주세요. 돌아갈려면 n을 입력해주세요 ").lower()
            if exitstr == 'n' :
                break
            elif exitstr == 'y' :
                userid = input("아이디(10자리 이하로 입력하세요) ")
                if len(userid) > 10 :
                    print("\n10자리를 넘겼습니다. 다시 입력해주세요")
                    continue
                while True :
                    userpwd = input("비밀번호(10자리 이하로 입력하세요) ")
                    if len(userpwd) > 10 :
                        print("\n10자리를 넘겼습니다. 다시 입력해주세요")
                        continue 
                    userpwdagain = input("비밀번호를 한번 더 입력해주세요 ")
                    if userpwd == userpwdagain :   
                        username = input("이름(5자리 이하로 입력하세요) ")
                        if len(username) > 20 :
                            print("\n5자리를 넘겼습니다. 다시 입력해주세요")
                            continue  
                        print("\n입력 감사합니다.\n\n당신의 아이디는 : {0}, 비밀번호는 : {1}, 이름은 : {2}입니다.\n".format(userid, userpwd, username))
                        while True :
                            tempstr = input("회원가입을 진행하려면 y, 다시 입력하려면 n을 입력하세요 ").lower()    
                            if tempstr == 'n' : break
                            elif tempstr == 'y' :  
                                usercur.Sign_up(userid, userpwd, username)
                                break   
                            else : 
                                print("\n잘못 입력하셨습니다.") 
                                continue    
                    else : 
                        print("\n입력하신 비밀번호가 다릅니다.")
                        continue
                    break         
            else : 
                print("\n잘못 입력하셨습니다.")
                continue      
    ### 메인 메뉴 - 회원 로그인 단계
    elif input_menu_num == 2:
        while True:
            if exitstr == 'n' :
                break
            userpass = 0
            passnum = 0
            print()
            print("%40s" % "회원 로그인")
            print()
            print("#" * 80)
            print("%40s" % "반갑습니다.")
            print()
            print("%40s" % "아이디와 비밀번호를 입력해주세요.")
            print("#" * 80)
            print()
            while True :
                exitstr = input("로그인을 진행하려면 y, 돌아갈려면 n을 입력하세요 ").lower()
                if exitstr == 'n' :
                    break
                elif exitstr == 'y' :    
                    while True :  
                        userid = input("아이디를 입력해주세요 ")
                        userpwd = input("비밀번호를 입력해주세요 ")            
                        passnum = usercur.User_login(userid, userpwd, userpass)
                        if passnum == 0 : break
                        else : break 
                else :
                    print("\n잘못 입력하셨습니다.")   
                break                
        ###메인 메뉴 - 로그인 - 회원 선택 메뉴 단계
            if passnum == 1 :
                while True:
                    if passnum == 0 : break
                    print()
                    print("%40s" % "회원 선택 메뉴")
                    print()
                    print("#" * 80)
                    print("%40s" % "1. 회원 정보 수정 혹은 삭제")
                    print()
                    print("%40s" % "2. 상품 조회 및 구매")
                    print()
                    print("%40s" % "3. 구매 상품 조회")
                    print()
                    print("%40s" % "4. 로그아웃")
                    print("#" * 80)
                    print()
                    try:
                        input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                    except Exception :
                        print("\n숫자를 입력해주세요.")
                        continue
                    if not input_menu_num in range(1, 5) :
                        print("\n잘못된 번호를 입력하셨습니다.")
                        continue
                    ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 단계
                    if input_menu_num == 1 :
                        while True :
                            print()
                            print("%40s" % "회원 정보 수정 메뉴")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 회원 정보 수정")
                            print()
                            print("%40s" % "2. 회원 탈퇴")
                            print()
                            print("%40s" % "3. 돌아가기")
                            print()
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 4) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 - 회원 정보 수정 단계
                            if input_menu_num == 1 :
                                print()
                                print("%40s" % "회원 정보 수정")
                                print()
                                print("#" * 80)
                                print("%40s" % "1. 정보 수정")
                                print()
                                print("%40s" % "2. 돌아가기")
                                print("#" * 80)
                                print()
                                try:
                                    input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                                except Exception :
                                    print("\n숫자를 입력해주세요.")
                                    continue
                                if not input_menu_num in range(1, 3) :
                                    print("\n잘못된 번호를 입력하셨습니다.")
                                    continue
                                ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 - 회원 정보 수정 - 정보 수정 단계
                                if input_menu_num == 1 :
                                    print()
                                    print("%40s" % "정보 수정")
                                    print()
                                    print("#" * 80)
                                    print("%40s" % "변경할 비밀번호, 이름을 입력하세요.")
                                    print("#" * 80)
                                    print()
                                    while True:
                                        changename = input("변경할 이름을 입력하세요(5글자 이하를 입력하세요) ")
                                        if len(changename) > 5 :
                                            print("\n5자리를 넘겼습니다 다시 입력해주세요.")
                                            continue 
                                        changepwd = input("변경할 비밀번호(10글자 이하를 입력하세요) ")
                                        if len(changepwd) > 10 :
                                            print("\n10자리를 넘겼습니다 다시 입력해주세요.")
                                            continue
                                        changepwdagain = input("비밀번호를 한번 더 입력하세요 ")
                                        if changepwd == changepwdagain :
                                            usercur.Change_user_info(userid, userpwd, changepwd, changename)
                                            break
                                        else : 
                                            print("\n비밀번호가 일치하지 않습니다.")
                                            continue
                                ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 - 회원 정보 수정 - 돌아가기 단계
                                else : break
                            ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 - 회원 탈퇴 단계    
                            elif input_menu_num == 2 :
                                print()
                                print("%40s" % "회원 탈퇴")
                                print()
                                print("#" * 80)
                                print("%40s" % "현재 계정의 비밀번호를 입력하세요. (비밀번호를 틀리면 자동으로 탈출 합니다.)")
                                print("#" * 80)
                                print()
                                while True:
                                    deletepwd = input("비밀번호 ")
                                    deletepwdagain = input("비밀번호를 한번 더 입력하세요 ")
                                    if deletepwd == deletepwdagain :
                                        passnum = usercur.Delete_user_info(userid, deletepwd)
                                        break
                                    else : 
                                        print("\n비밀번호가 일치하지 않습니다.")
                                        break
                            ###메인 메뉴 - 회원 로그인 - 회원 정보 수정 메뉴 - 돌아가기 단계
                            else : break   
                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 단계
                    elif input_menu_num == 2 :
                        while True :
                            print()
                            print("%40s" % "상품 조회 및 구매 메뉴")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 상품 조회")
                            print()
                            print("%40s" % "2. 상품 구매")
                            print()
                            print("%40s" % "3. 돌아가기")
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 4) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 단계
                            if input_menu_num == 1 :
                                while True :
                                    print()
                                    print("%40s" % "상품 조회 메뉴")
                                    print()
                                    print("#" * 80)
                                    print("%40s" % "1. 전체 상품 조회")
                                    print()
                                    print("%40s" % "2. 특정 상품 조회")
                                    print()
                                    print("%40s" % "3. 돌아가기")
                                    print()
                                    print("#" * 80)
                                    print()
                                    try:
                                        input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                                    except Exception :
                                        print("\n숫자를 입력해주세요.")
                                        continue
                                    if not input_menu_num in range(1, 4) :
                                        print("\n잘못된 번호를 입력하셨습니다.")
                                        continue
                                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 -전체 상품 조회 단계
                                    if input_menu_num == 1 :
                                        print()
                                        print("#" * 80)
                                        print("%40s" % "전체 상품 조회를 시작합니다.")
                                        print("#" * 80)
                                        print()
                                        merchandisecur.Showmerchandise()                               
                                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 특정 상품 조회 단계
                                    elif input_menu_num == 2 :
                                        print()
                                        print("%40s" % "특정 상품 조회")
                                        print()
                                        print("#" * 80)
                                        print("%40s" % "1. 태그 검색")
                                        print()
                                        print("%40s" % "2. 종류 검색")
                                        print()
                                        print("%40s" % "3. 이름 검색")
                                        print()
                                        print("%40s" % "4. 돌아가기")
                                        print()
                                        print("#" * 80)
                                        print()
                                        try:
                                            input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                                        except Exception :
                                            print("\n숫자를 입력해주세요.")
                                            continue
                                        if not input_menu_num in range(1, 5) :
                                            print("\n잘못된 번호를 입력하셨습니다.")
                                            continue
                                        ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 특정 상품 조회 - 태그 검색 단계
                                        if input_menu_num == 1 :
                                            search_tag = input("검색하고자 하는 태그를 입력하세요 ")
                                            merchandisecur.Showmerchandisetag(search_tag)
                                        ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 특정 상품 조회 - 종류 검색 단계
                                        elif input_menu_num == 2 :
                                            search_type = input("검색하고자 하는 종류를 입력하세요 ")
                                            merchandisecur.Showmerchandisetype(search_type)
                                        ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 특정 상품 조회 - 이름 검색 단계
                                        elif input_menu_num == 3 :
                                            search_name = input("검색하고자 하는 이름을 입력하세요 ")
                                            merchandisecur.Showmerchandisename(search_name)
                                        ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 특정 상품 조회 - 돌아가기 단계 
                                        else : break
                                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 조회 메뉴 - 돌아가기 단계
                                    else :break
                            ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 구매 메뉴 단계
                            elif input_menu_num == 2 :
                                while True :
                                    print()
                                    print("%40s" % "상품 구매 메뉴")
                                    print()
                                    print("#" * 80)
                                    print("%40s" % "1. 상품 구매")
                                    print()
                                    print("%40s" % "2. 돌아가기")
                                    print("#" * 80)
                                    print()
                                    try:
                                        input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                                    except Exception :
                                        print("\n숫자를 입력해주세요.")
                                        continue
                                    if not input_menu_num in range(1, 3) :
                                        print("\n잘못된 번호를 입력하셨습니다.")
                                        continue
                                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 구매 메뉴 - 상품 구매 단계
                                    if input_menu_num == 1 :
                                        while True:
                                            buy_num = 0
                                            buy_id = input("구매하고자 하는 상품의 고유 번호를 입력하세요. 구매를 취소하고자 하면 n을 입력해주세요. ")
                                            if buy_id == 'n' :
                                                break
                                            if type(int(buy_id)) == int :
                                                temp_num = merchandisecur.Showmerchandiseid(buy_id, buy_num)
                                                if temp_num == 1 :
                                                    while True :
                                                        agree = input("구매를 원하시면 y, 아니면 n을 입력해주세요. ").lower()
                                                        if agree == 'y' : 
                                                            buy_quantity = input("구매하고자 하는 상품의 수량을 적어주세요. ")
                                                            merchandisecur.Buymerchandise(buy_id, buy_quantity, userid)
                                                            break
                                                        elif agree == 'n' : break
                                                        else : 
                                                            print("\n잘못 입력하셨습니다.")
                                                            continue
                                            else : 
                                                print("\n잘못 입력하셨습니다.")
                                                continue          
                                    ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 상품 구매 메뉴 - 돌아가기 단계
                                    else : break
                            ###메인 메뉴 - 회원 로그인 - 상품 조회 및 구매 메뉴 - 돌아가기 단계
                            else : break                        
                    ###메인 메뉴 - 회원 로그인 - 구매 상품 조회 메뉴 단계
                    elif input_menu_num == 3 :
                        print()
                        print("%40s" % "구매 상품 조회")
                        print()
                        print("#" * 80)
                        print("%40s" % "고객님이 구매하신 상품을 조회 하겠습니다.")
                        print("#" * 80)
                        print()
                        merchandisecur.Buylog(userid)
                    ###메인 메뉴 - 회원 로그인 - 로그아웃 단계
                    else :
                        print("로그아웃 했습니다.")
                        break
                break
    ### 메인메뉴 - 관리자 로그인 단계
    elif input_menu_num == 3:
        while True:
            if exitstr == 'n' :
                break
            adminpass = 0
            passnum = 0
            print()
            print("%40s" % "관리자 로그인")
            print()
            print("#" * 80)
            print("%40s" % "반갑습니다.")
            print()
            print("%40s" % "아이디와 비밀번호를 입력해주세요.")
            print("#" * 80)
            print()
            while True :  
                exitstr = input("로그인을 진행하려면 y, 돌아가려면 n을 입력하세요. ").lower()
                if exitstr == 'n' :
                    break
                elif exitstr == 'y' :
                    while True :
                        adminid = input("아이디를 입력해주세요 ")
                        adminpwd = input("비밀번호를 입력해주세요 ")         
                        passnum = admincur.Admin_login(adminid, adminpwd, adminpass) 
                        if passnum == 0 : break
                        else :  break
                else :
                    print("\n잘못 입력하셨습니다.")
                break
            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 단계
            if passnum == 1 :
                while True:
                    print()
                    print("%40s" % "관리자 선택 메뉴")
                    print()
                    print("#" * 80)
                    print("%40s" % "1. 전체 회원 목록 조회")
                    print()
                    print("%40s" % "2. 주문 목록 조회")
                    print()
                    print("%40s" % "3. 상품 목록 조회")
                    print()
                    print("%40s" % "4. 상품 재고 변경")
                    print()
                    print("%40s" % "5. 랭킹")
                    print()
                    print("%40s" % "6. 로그아웃")
                    print("#" * 80)
                    print()
                    try:
                        input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                    except Exception :
                        print("\n숫자를 입력해주세요.")
                        continue
                    if not input_menu_num in range(1, 7) :
                        print("\n잘못된 번호를 입력하셨습니다.")
                        continue
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 전체 회원 목록 조회 단계
                    if input_menu_num == 1 :
                        print("#" * 80)
                        print("%40s" % "전체 회원을 조회하겠습니다.")
                        print("#" * 80)
                        print()
                        admincur.Look_users()
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 주문 목록 조회 단계
                    elif input_menu_num == 2 :
                        while True:
                            print()
                            print("%40s" % "주문 목록 조회")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 전체 주문 목록 조회")
                            print()
                            print("%40s" % "2. 고유 번호 별 조회")
                            print()
                            print("%40s" % "3. 회원 별 조회")
                            print()
                            print("%40s" % "4. 돌아가기")
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 5) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 주문 목록 조회 - 전체 주문 목록 조회 단계
                            if input_menu_num == 1 :
                                print("#" * 80)
                                print("%40s" % "전체 주문 목록을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                admincur.Buylogall()
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 주문 목록 조회 - 고유 번호 별 조회 단계
                            elif input_menu_num == 2 :
                                print("#" * 80)
                                print("%40s" % "고유 번호로 주문 목록을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                buy_logid = input("상품 고유 번호를 입력하세요 ")
                                admincur.Buylogid(buy_logid)
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 주문 목록 조회 - 회원 별 조회 단계
                            elif input_menu_num == 3 :
                                print("#" * 80)
                                print("%40s" % "회원 별로 주문 목록을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                buy_loguserid = input("회원 아이디를 입력하세요 ")
                                admincur.Buyloguserid(buy_loguserid)
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 주문 목록 조회 - 돌아가기 단계
                            else : break
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 단계
                    elif input_menu_num == 3 :
                        while True:
                            print()
                            print("%40s" % "상품 목록 조회")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 전체 상품 목록 조회")
                            print()
                            print("%40s" % "2. 빈 재고 목록 조회")
                            print()
                            print("%40s" % "3. 유통기한 지난 상품 조회")
                            print()
                            print("%40s" % "4. 상품 목록 재고로 조회")
                            print()
                            print("%40s" % "5. 돌아가기")
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 6) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 - 전체 상품 목록 조회 단계
                            if input_menu_num == 1 :
                                print("#" * 80)
                                print("%40s" % "전체 상품 목록을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                admincur.Showmerchandiseall()
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 - 빈 재고 목록 조회 단계
                            elif input_menu_num == 2 :
                                print("#" * 80)
                                print("%40s" % "재고가 비어있는 상품을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                admincur.Showmerchandiseempty()
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 - 유통기한 지난 상품 조회 단계    
                            elif input_menu_num == 3 :
                                print("#" * 80)
                                print("%40s" % "유통기한이 지난 상품을 조회하겠습니다.")
                                print("#" * 80)
                                print()
                                admincur.Showmerchandiseexpired()
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 - 상품 목록 재고로 조회 단계 
                            elif input_menu_num == 4 :
                                while True:
                                    print("#" * 80)
                                    print("%40s" % "조건에 맞는 재고보다 적은 상품을 조회하겠습니다.")
                                    print("#" * 80)
                                    print()
                                    quantity = input("재고 조건을 입력하세요 ")
                                    if type(int(quantity)) == int :
                                        admincur.Showmerchandisecondition(quantity)
                                        break
                                    else : 
                                        print("\n조건을 잘못 입력했습니다.")
                                        continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 목록 조회 = 돌아가기 단계
                            else : break
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 단계
                    elif input_menu_num == 4 :
                        while True:
                            print()
                            print("%40s" % "상품 재고 변경")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 상품 재고 추가")
                            print()
                            print("%40s" % "2. 유통기한 변경")
                            print()
                            print("%40s" % "3. 상품 재고 제거")
                            print()
                            print("%40s" % "4. 목록 추가")
                            print()
                            print("%40s" % "5. 목록 삭제")
                            print()
                            print("%40s" % "6. 돌아가기")
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 7) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 상품 재고 추가 단계
                            if input_menu_num == 1:
                                print("#" * 80)
                                print("%40s" % "상품 재고를 추가합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    add_id = input("재고를 추가할 상품의 고유 번호를 입력하세요 ")
                                    add_quantity = input("얼마만큼 추가하시겠습니까? ")
                                    if type(int(add_id)) == int and type(int(add_quantity)) == int :
                                        admincur.Addmerchandise(add_id, add_quantity)
                                        break
                                    else :
                                        print("\n다시 시도해주세요.")
                                        continue                                
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 유통기한 변경 단계
                            elif input_menu_num == 2:
                                print("#" * 80)
                                print("%40s" % "상품의 유통기한을 변경합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    change_id = input("유통기한을 변경할 상품의 고유 번호를 입력하세요 ")
                                    change_date = input("기한을 입력해주세요(yyyy-mm-dd)형식을 지켜주세요 ")
                                    if type(int(change_id)) == int and len(change_date) == 10 :
                                        admincur.Changedate(change_id, change_date)
                                        break
                                    else :
                                        print("\n다시 시도해주세요.")
                                        continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 상품 재고 제거 단계
                            elif input_menu_num == 3:
                                print("#" * 80)
                                print("%40s" % "상품의 재고를 제거합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    down_id = input("재고를 제거할 상품의 고유 번호를 입력하세요 ")
                                    down_quantity = input("얼만큼 제거하시겠습니까? ")
                                    if type(int(down_id)) == int and type(int(down_quantity)) == int :
                                        admincur.Downquantity(down_id, down_quantity)
                                        break
                                    else :
                                        print("\n다시 시도해주세요.")
                                        continue     
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 목록 추가 단계
                            elif input_menu_num == 4:
                                print("#" * 80)
                                print("%40s" % "상품 목록을 추가합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    update_id = input("목록을 추가할 상품의 고유 번호를 입력하세요 ")
                                    update_tag = input("목록을 추가할 상품의 태그를 입력하세요 ")
                                    update_type = input("목록을 추가할 상품의 타입을 입력하세요 ")
                                    update_name = input("목록을 추가할 상품의 이름을 입력하세요 ")
                                    update_price = input("목록을 추가할 상품의 가격을 입력하세요 ")
                                    update_quantity = input("목록을 추가할 상품의 수량을 입력하세요 ")
                                    update_expirate = input("목록을 추가할 상품의 유통기한 입력하세요 ")
                                    if type(int(update_id)) == int and type(int(update_price)) == int and type(int(update_quantity)) == int and len(update_expirate) == 10 :
                                        admincur.Updatemerchandise(update_id, update_tag, update_type, update_name, update_price, update_quantity, update_expirate)
                                        break
                                    else :
                                        print("\n다시 시도해주세요.")
                                        continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 목록 삭제 단계
                            elif input_menu_num == 5:
                                print("#" * 80)
                                print("%40s" % "상품 목록을 제거합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    delete_id = input("목록을 제거할 상품의 고유 번호를 입력하세요 ")
                                    if type(int(delete_id)) == int :
                                        admincur.Deletemerchandise(delete_id)
                                        break
                                    else :
                                        print("\n다시 시도해주세요.")
                                        continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 상품 재고 변경 - 돌아가기
                            else : break
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 랭킹 단계
                    elif input_menu_num == 5 :
                        while True:
                            print()
                            print("%40s" % "월별 랭킹")
                            print()
                            print("#" * 80)
                            print("%40s" % "1. 월별 최고 주문 금액 회원")
                            print()
                            print("%40s" % "2. 월별 가장 많이 주문된 상품")
                            print()
                            print("%40s" % "3. 돌아가기")
                            print("#" * 80)
                            print()
                            try:
                                input_menu_num = int(input("원하시는 메뉴의 숫자를 입력해주세요 "))
                            except Exception :
                                print("\n숫자를 입력해주세요.")
                                continue
                            if not input_menu_num in range(1, 4) :
                                print("\n잘못된 번호를 입력하셨습니다.")
                                continue
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 랭킹 - 월별 최고 주문 금액 회원 단계
                            if input_menu_num == 1:
                                print("#" * 80)
                                print("%40s" % "월별 최고 주문 금액 회원을 조회합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    try:
                                        month_num = int(input("원하시는 월을 입력해주세요 "))
                                    except Exception :
                                        print("\n숫자를 입력해주세요.")
                                        continue                                   
                                    if not month_num in range(1, 13) :
                                        print("\n잘못된 월을 입력하셨습니다.")
                                        continue
                                    else :
                                        admincur.Monthbestuser(month_num)
                                        break
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 랭킹 - 월별 가장 많이 주문된 상품 단계
                            elif input_menu_num == 2:
                                print("#" * 80)
                                print("%40s" % "월별 가장 많이 주문된 상품을 조회합니다.")
                                print("#" * 80)
                                print()
                                while True :
                                    try:
                                        month_num = int(input("원하시는 월을 입력해주세요 "))
                                    except Exception :
                                        print("\n숫자를 입력해주세요.")
                                        continue                                   
                                    if not month_num in range(1, 13) :
                                        print("\n잘못된 월을 입력하셨습니다.")
                                        continue
                                    else :
                                        admincur.Monthbestmerchandise(month_num)
                                        break
                            ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 랭킹 - 돌아가기 단계
                            else : break
                    ### 메인메뉴 - 관리자 로그인 - 관리자 선택 메뉴 - 로그아웃 단계
                    else : break
                break
    ### 메인메뉴 - 종료 단계
    else :
        print("\n프로그램을 종료하겠습니다.\n")
        cursor.close()
        connectdb.close()
        break