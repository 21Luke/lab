from pytest import *
from account import *
class Test:
    def setup_method(self):
        self.account_1 = Account('john')



    def teardown_method(self):
        del self.account_1


    def test__init__(self):
        assert self.account_1.get_name() == 'john'
        assert self.account_1.get_balance() == 0




    def test_deposit(self):
        assert self.account_1.deposit(-10) is False
        assert self.account_1.get_balance() == 0
        assert self.account_1.deposit(10.5) is True
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)
        assert self.account_1.deposit(0) is False
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)
        assert self.account_1.deposit(-2.5) is False
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)

    def test_withdraw(self):
        assert self.account_1.withdraw(10.5) is True
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)
        assert self.account_1.withdraw(0) is False
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)
        assert self.account_1.withdraw(-2.5) is False
        assert self.account_1.get_balance() == approx(10.5, abs=0.00001)