from bank import Bank
bank = Bank('Saderat')

account_number_ali = bank.signup('Ali', 20)


sample_account = '3321'

if account_number_ali == sample_account:
    sample_account == '1122'

assert bank.transaction('0000', '3321', 48) == False

assert bank.transaction(account_number_ali, '3321', 12) == False # 3321 is not valid
assert bank.transaction('3321', account_number_ali, 12) == False # 3321 is not valid
assert len(bank.transaction_history()) == 0

assert bank.transaction('0000', account_number_ali, 40) == True

balance_of_ali_account = bank.balance_of(account_number_ali)
assert balance_of_ali_account == 40

account_number_hasan = bank.signup('hasan', 25)


hasan_balance = bank.balance_of(account_number_hasan)
assert hasan_balance == 0

assert bank.balance_of('0000') == -1

bank.save()

del bank

bank = Bank()
bank.load('Saderat')

assert len(bank.transaction_history()) == 1
assert bank.info() == ('Saderat', 1, 2)

