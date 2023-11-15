from account import Account
from owner import Owner

class Saving_account(Account):
    def __init__(self, id: int, account_id: str, balance: float, owner: Owner,
                 limit_transaction: float, cash: float,) -> None:
        super().__init__(id, account_id, balance, owner, cash)
    
        self.__limit_transaction = limit_transaction
    
    def __validate_limit(self, cash: float) -> bool:
        return cash <= self.__limit_transaction
   
#Definir retiro
    def withdraw(self, cash: float) -> float:
        if (self.__validate_limit(cash)):
           super().withdraw(cash)
        else:
           raise ValueError("No puedes reitrar esa cantidad porque\
                             has superado el limite")


    def get_limit_transaction(self) -> float:
        return self.__limit_transaction
    
    def set_limit_transaction(self, limit_transaction: float) -> None:
        self.__limit_transaction = limit_transaction
        
    
    