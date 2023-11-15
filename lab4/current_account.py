from owner import Owner
from account import Account

class Current_account(Account):
    def __init__(self, id: int, account_id: str, balance: float, 
                 owner: Owner, cash: float, check_numb: int) -> None:
        super().__init__(id, account_id, balance, owner, cash)

        self.__check_numb = check_numb
    
    def issue_check(self, cash: float) -> None:
        if cash <= self._balance:
            self.__check_numb += 1
            self._balance -= cash
        
        else:
            raise ValueError("El cheque supera el saldo de tu cuenta")

    
    