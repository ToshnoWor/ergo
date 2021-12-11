class Factors:
    """Factors class"""
    code = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
            111, 112, 113, 201, 202, 250]
    name = [
        "Температура повітря на робочому місці в приміщенні, оС, теплий період",
        "Температура повітря на робочому місці в приміщенні, оС, холодний період",
        "Атмосферний тиск: перебільшення над нормою, атм",
        "Токсична речовина, кратність перебільшення  гранично допустимої концентрації (ГДК)",
        "Промисловий пил, кратність перебільшення, ГДК",
        "Вібрація, перебільшення гранично допустимого рівня (ГДР), дБ",
        "Промисловий шум, дБА",
        "Ультразвук, перебільшення ГДР, дБ",
        "Поверхнева щільність інфрачервоного (теплового) випромінювання, ккал/см2 *хвилину=6,978-103",
        "Освітленість РМ: рівень освітленості РМ при освітленості на рівні санітарних норм в залежності від розміру " +
        "об’єкта в мм",
        "Електромагнітне поле радіочастот (ГДР плюс кількість випромінювання, що перевищує норму): високочастотне",
        "Електромагнітне поле радіочастот (ГДР плюс кількість випромінювання, що перевищує норму):" +
        " ультрависокочастотне",
        "Електромагнітне поле радіочастот (ГДР плюс кількість випромінювання, що перевищує норму): зверхвисокочастотне",
        "Фізичне навантаження. Зовнішня механічна робота, загальна (з участю м’язів корпуса і ніг) Дж.*105",
        "Фізичне навантаження. Зовнішня механічна робота, регіональна (з участю плечового пояса),Дж*105",
        "Доля зосередженого спостереження від часу робочої зміни, %"
    ]
    categoryUT = [[1, 18.999], [19, 33.999], [34, 45.999], [46, 53.999], [54, 59], [59.001, 60]]
    norm = [20, 22, 1, 0.007, 0.005, 0.001, 80, 0.5, 0, 400, 0.001, 0.001, 0.001, 1, 0.5, 5]
    factorAssessment = [
        [
            [18, 20], [21, 22], [23, 28], [29, 32], [33, 35], [36, 50]
        ],
        [
            [20, 22], [17, 19], [15, 16], [7, 14], [4, 6], [0, 3]
        ],
        [
            [0, 0], [0.2, 0.6], [0.7, 1.2], [1.3, 1.8], [1.9, 3], [3.05, 5]
        ],
        [
            [0, 0], [0.001, 0.995], [1, 2.5], [2.6, 4], [4.05, 6], [6.01, 8]
        ],
        [
            [0, 0], [0.001, 0.995], [1, 5], [6, 10], [11, 30], [30.5, 40]
        ],
        [
            [0, 0], [0.001, 0.995], [1, 3], [4, 6], [7, 9], [9.5, 12]
        ],
        [
            [75, 80.995], [81, 81.001], [81.005, 85], [86, 90], [91, 110], [110.5, 120]
        ],
        [
            [0.005, 0.995], [1, 1.001], [1.005, 5], [6, 10], [11, 20], [20.5, 30]
        ],
        [
            [0, 0], [0.0001, 0.005], [0.006, 0.5], [0.6, 2], [2.001, 5], [5.001, 10]
        ],
        [
            [400, 500], [400, 500], [310, 395], [300, 300.1], [200, 300], [10, 199]
        ],
        [
            [0.001, 3], [3.001, 9.999], [10, 19], [20, 20.1], [21, 30], [31, 50]
        ],
        [
            [0.001, 2], [2.001, 4.999], [5, 9], [10, 10.1], [11, 20], [21, 50]
        ],
        [
            [0.001, 4], [4.001, 14.999], [15, 29], [30, 30.1], [31, 40], [41, 50]
        ],
        [
            [1, 4.2], [4.25, 8.3], [8.35, 12.5], [12.55, 17], [17.05, 20], [20.05, 30]
        ],
        [
            [0.5, 2.1], [2.15, 4.2], [4.25, 6.2], [6.25, 8.3], [8.35, 10.4], [10.45, 20]
        ],
        [
            [5, 25], [25.5, 50], [50.5, 75], [75.5, 90], [90.5, 95], [95.5, 99]
        ],
    ]

    def __init__(self, value):
        print('Create factors...')
        self.__score = [0] * len(self.code)
        self.__value = value
        self.__countFactors = 0
        self.__maxScore = 0
        self.__sumWithOutMax = 0
        self.__UT = 0
        self.__categoryUT = 0
        self.__y = 0
        self.__p = 0

    def change_value(self, code, value):
        index = self.code.index(code)
        self.__value[index] = value
        self.calc()

    def calc(self):
        self.calc_score()
        self.calc_count_factors()
        self.calc_max_score()
        self.calc_sum_with_out_max()
        self.calc_u_t()
        self.calc_category()
        self.calc_y()
        self.calc_p()

    def calc_category(self):
        cat = 1
        for (val1, val2) in self.categoryUT:
            if val1 <= self.__UT <= val2:
                self.__categoryUT = cat
            cat += 1

    def calc_score(self):
        # print('Calculate score...')
        index = 0
        for num in self.factorAssessment:
            j = 1
            for (val1, val2) in num:
                if val1 <= self.__value[index] <= val2:
                    self.__score[index] = j
                j += 1
            index += 1

    def calc_count_factors(self):
        # print('Calculate count factors...')
        self.__countFactors = 0
        for v in self.__score:
            if v != 0:
                self.__countFactors += 1
                
    def calc_max_score(self):
        self.__maxScore = max(self.__score)

    def calc_sum_with_out_max(self):
        # print('Calculate sum with out max...')
        self.__sumWithOutMax = sum(self.__score) - self.__maxScore
        
    def calc_u_t(self):
        # print('Calculate UT...')
        self.__UT = (self.__maxScore + (6 - self.__maxScore) / (
                6 * (self.__countFactors - 1)) * self.__sumWithOutMax) * 10

    def calc_y(self):
        self.__y = (self.__UT-15.6)/0.64

    def calc_p(self):
        self.__p = 100 - self.__y

    def get_u_t(self):
        return self.__UT

    def get_y(self):
        return self.__y

    def get_p(self):
        return self.__p

    def get_full_category(self):
        return self.__categoryUT

    def print_category(self):
        print(f'Category UT = {self.__categoryUT}')

    def print_u_t(self):
        print(f'UT = {self.__UT}')

    def print_score(self):
        print('Result calculate - score:')
        for number in range(len(self.code)):
            print(f'{self.code[number]} - {self.__score[number]} - {self.__value[number]}')

    def print_score_for_code(self, code):
        index = self.code.index(code)
        print(f'{self.code[index]} - {self.__score[index]}')

    def print_y(self):
        print(f'Y = {self.__y}')

    def print_p(self):
        print(f'P = {self.__p}')

    def print(self):
        self.print_score()
        self.print_u_t()
        self.print_category()
        self.print_y()
        self.print_p()
