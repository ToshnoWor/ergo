class Factors_u_t:
    """Class Factors_UT"""
    def __init__(self, code, values, factors):
        self.__ps = []
        self.__ys = []
        self.__category = []
        self.__code = code
        self.__values = values
        self.__UTs = []
        # self.generate_u_ts(factors)

    def generate_u_ts(self, factors):
        for value in self.__values:
            factors.change_value(self.__code, value)
            self.__UTs.append(factors.get_u_t())
            self.__ys.append(factors.get_ys())
            self.__ps.append(factors.get_ps())

    def generate_u_t(self, factors, value):
        factors.change_value(self.__code, value)
        self.__UTs.append(factors.get_u_t())
        self.__ys.append(factors.get_y())
        self.__ps.append(factors.get_p())
        self.__category.append(factors.get_full_category())

    def get_u_ts(self):
        return self.__UTs

    def get_ys(self):
        return self.__ys

    def get_ps(self):
        return self.__ps

    def get_values(self):
        return self.__values

    def get_code(self):
        return self.__code

    def get_category(self):
        return self.__category
