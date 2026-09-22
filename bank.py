
class Bank:
    def __init__(self,name):
        self.name=name
        self.accounts={}
        
        self.transaction_history=[]

    def transaction(self,sender, receiver , money):

        if sender=="0000":
            self.accounts[receiver]=money

            result=[sender,receiver,money]
            self.transaction_history.append(result)
            return True

        if sender in self.accounts:

            if receiver not in self.accounts:
                self.accounts[receiver]=0
            if self.accounts[sender]>=money:
                self.accounts[sender]-=money
                self.accounts[receiver]+=money
                result=[sender,receiver,money]
                self.transaction_history.append(result)
                return True

            else:
                result=[sender,receiver,money]
                self.transaction_history.append(result)

                return False

        return False


    def history(self,account_number):

        tr_l=[]

        for transaction in self.transaction_history:

            if transaction[0]==account_number or transaction[1]==account_number:
                tr_l.append(transaction)

        return tr_l


    def check(self,account_number):

        if account_number=="0000":
            return -1

        else:
            return self.accounts[account_number]


    def info(self):

        return (self.name,len(self.accounts),len(self.transaction_history))



#bahtare ke dige kolan az print estefadeh nakonim va az return estefadeh konime
        
#history:تراکنش هاي يک حساب اينکه از کجا به کجا چند ريخته شده
#info: اظلاعات مربوط به بانک رو نشون بده اينکه چه بانکيه و چه تراکنش هايي داخلش انجام شده
#check : موجودي حساب