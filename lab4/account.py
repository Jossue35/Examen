from owner import Owner

class Account:

    def __init__(self, id: int, account_id: str, balance: float,
                  owner: Owner, cash: float) -> None:
        
        self.__id = id
        self.__account_id = account_id
        self.__owner: Owner = owner
        self.__cash = cash
        
        if not isinstance(self.__owner, Owner):
            raise ValueError("Ingresa un OWNER")
        
        if (balance >= 0):
            self._balance = balance
        else:
            raise("Tu balance es negativo")
        
             
    def __str__(self) -> str:
        return (f"Id cuenta: {self.__account_id}"
                f"Saldo: {self._balance}")
    
    

#Gets

    def get_id(self) -> int:
        return self.__id
    
    def get_account_id(self) -> str:
        return self.__account_id
    
    def get_balance(self) -> str:
        return self._balance
    
    def get_owner(self) -> Owner:
        return self.__owner
    
    def set_id(self, id: int) -> None:
        self.__id = id
#Sets

    def set_account_id(self, account_id: str) -> None:
        self.__account_id = account_id

    def set_balance(self, balance: float) -> None:
        self._balance = balance
        if (balance >= 0):
            self._balance = balance
        else:
            raise("Tu balance es negativo")
        
    def set_owner(self, owner: Owner) -> None:
        self.__owner: Owner = owner

        if not isinstance(self.__owner, Owner):
            raise ValueError("Has ingresado otro dato, ingresa un OWNER")
        
    def deposit(self, cash: float) -> None:
        if (cash > 0):
            self._balance += cash
        else:
            raise ValueError("No podemos depositar valores negativos")
        
    def withdraw(self, cash: float) -> None:
        if (cash > 0 and cash <= self._balance):
            self._balance -= cash
        else:
            raise ValueError("No puedes retirar valores negativos de tu cuenta")
    