bank = Bank('Saderat')

bank.transaction('0000', '3321', 48)

bank.transaction('3321', '1123', 40)
money_3321 = bank.check('3321')
assert money_3321 == 8

bank.transaction('3321', '1123', 12) # print error

money_1123 = bank.check('1123')
assert money_1123 == 40

bank.history('3321') # print all transactions
bank.info() # bank: Saderat, accounts, transactions number



0000 --> 3321: 10$
0000 --> 3321: 5$
0000 --> 3321: 1$
0000 --> 3321: 12$
3321 --> 1123: 18$
1123 --> 9121: 20$ x


class Bank:
    def __init__(self,name):
        self.name = name
        
    
    def transaction():
        
    def history():
        
    def info():
        