class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,stock,cost):
        self.stock=stock#货物名称
        self.cost=cost#货物单价
        self.total=0#当前储货量
        self.balance=0#当前钱数
    def vend(self):
        if self.total==0 :
            return 'Inventory empty. Restocking required.'
        elif self.balance<self.cost:
            return f'You must add ${self.cost-self.balance} more funds.'
        elif self.balance==self.cost:
            self.balance=0
            self.total-=1
            return f'Here is your {self.stock}.'
        else: 
            tmp,self.balance=self.balance,0
            self.total-=1
            return f'Here is your {self.stock} and ${tmp-self.cost} change.'
    def restock(self,total):
        self.total+=total
        return f'Current {self.stock} stock: {self.total}'
    def add_funds(self,balance):
        if self.total==0:
            return f'Inventory empty. Restocking required. Here is your ${balance}.'
        else:
            self.balance+=balance
            return f'Current balance: ${self.balance}'
