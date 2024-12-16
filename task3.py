class Base1:
    def __init__(self) -> None:
        self.str1 = "Base1"
        print("Init of Base1 activated")

class Base2:
    def __init__(self) -> None:
        self.str2 = "Base2"
        print("Init of Base2 activated")

class Derived(Base1, Base2):
    def __init__(self) -> None:
        Base1.__init__(self)  
        Base2.__init__(self)
        print("Init of derived activated")

obj = Derived()