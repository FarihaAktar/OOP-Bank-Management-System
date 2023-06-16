from abc import ABC, abstractmethod

class User:
    def __init__(self, name, address, phone, nid) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.nid = nid
        self.balance = 0
        self.isAdmin = False


class Admin(User):
    def __init__(self, name, address, phone, nid) -> None:
        super().__init__(name, address, phone, nid)
        self.isAdmin = True


