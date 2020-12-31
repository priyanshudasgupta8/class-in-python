class Atm(object):
    def __init__(self, cardNumber, pinNumber, amountOfWithDrawal, bankBranch):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.amountOfWithDrawal = amountOfWithDrawal
        self.bankBranch = bankBranch
    
    def cash_withdrawal(self, amountOfWithDrawal):
        print('Successfully withdrew', amountOfWithDrawal,'USD')

    def balance_enquiry(self):
        print('Fetching information required for enquiry...')

acc1 = Atm('123', '123456789', '20', 'SF')
print(acc1.bankBranch)
print(acc1.cash_withdrawal(50))