class data:
    __member: dict
    __file:str
    __group: str
    __pt:str
    __product: str
    __init_temp: float
    __slope: float


    @property
    def f(self):
        return self.__file
    @f.setter
    def f(self,file):
        self.__file = file

    @property
    def pt(self):
         return self.__pt

    @pt.setter
    def pt(self, pt):
         self.__pt = pt

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product

    @property
    def init_temp(self):
         return self.init_temp

    @init_temp.setter
    def init_temp(self,init_temp):
        self.__init_temp = init_temp

    @property
    def slope(self):
        return self.__slope

    @slope.setter
    def slope(self,slope):
         self.__slope = slope




    def __str__(self):
     return f"{self.__file},{self.__group}, {self.__product}, {self.__pt},{self.__init_temp},{self.__slope}"