from datetime import date

class Owner:

    def __init__(self, id: int, first_name: str, last_name: str, 
                 dni: str, birth_date: date, address: str, email: str):

     self.__id = id
     self.__first_name = first_name
     self.__last_name = last_name
     self.__dni = dni
     self.__birth_date = birth_date
     self.__address = address
     self.__email = email

    def __str__(self) -> str:
        return (f"Id: {self.__id}\n"
                f"Nombre: {self.__first_name} {self.__last_name}\n"
                f"DNI: {self.__dni}\n"
                f"Email: {self.__email}")

    def get_id(self) -> int:
        return self.__id

    def get_first_name(self) -> str:
       return self.__first_name
    
    def get_last_name(self) -> str:
       return self.__last_name
    
    def get_dni(self) -> str:
       return self.__dni
    
    def get_birth_date(self) -> date:
       return self.__birth_date
    
    def get_address(self) -> str:
       return self.__address
    
    def get_email(self) -> str:
       return self.__email

    def set_id(self, id: int) -> None:
       self.__id = id

    def set_first_name(self, first_name: str) -> None:
       self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
       self.__last_name = last_name

    def set_dni(self, dni: str) -> None:
       self.__dni = dni

    def set_birth_date(self, birth_date: date) -> None:
       self.__birth_date = birth_date

    def set_address(self, address: str) -> None:
       self.__address = address

    def set_email(self, email: str) -> None:
       self.__email = email