# Создаём класс Product с параметрами title - имя, 
# calorific - калорийность и cost - цена за 100 грамм.
class Product:
    def __init__(self, title, calorific, cost):
        # Проверяем title на заполнение
        if type(title) is str and len(title) > 0:
            # Проверяем calorific и cost, должны быть больше 0
            if Product.check_calor(calorific) and Product.check_cost(cost):
                self.title = title
                self.calorific = calorific
                self.cost = cost
            else:
                raise ValueError
        else:
            raise ValueError
    @staticmethod
    def check_calor(calorific):
        return calorific > 0
    @staticmethod
    def check_cost(cost):
        return cost > 0

# Создаём класс Ingredient из Product с параметрами title - имя, 
# calorific - калорийность, cost - цена за 100 грамм и weight - вес.
class Ingredient(Product):
    def __init__(self, title, calorific, cost, weight):
        super().__init__(title, calorific, cost)
        # Проверяем вес, должен быть больше 0.
        if Ingredient.check_weight(weight):
            self.weight = weight
        else:
            raise ValueError
    # Функции подсчёта цены и калорийности
    def selfcost(self):
        return self.weight / 100 * self.cost
    def calories(self):
        return self.weight / 100 * self.calorific
    @staticmethod
    def check_weight(weight):
        return weight > 0

# Создём класс Pizza с параметром title -имя и списком ingredients
class Pizza:
    def __init__(self, title, ingredients=[]):
        # Проверяем title на заполнение
        if type(title) is str and len(title) > 0:
            self.title = title
            self.ingredients = ingredients
        else:
            raise ValueError
    # Функции для подсчёта общей калорийности и себестоимости пиццы
    def calories(self):
        sum_cal = 0
        for calor in self.ingredients:
            sum_cal += calor.calories()
        return sum_cal
    def selfcost(self):
        summ = 0
        for price in self.ingredients:
            summ += price.selfcost()
        return summ
    def __str__(self):
        return f'{self.title} ({self.calories()}) цена: {self.selfcost()}'


# Создаём продукты
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Создаём ПРОСТОЙ список продуктов для упрощения обращения в дальнейшем
product_list = [[dough_product.title,dough_product.calorific,dough_product.cost],[tomato_product.title,tomato_product.calorific,tomato_product.cost],[cheese_product.title,cheese_product.calorific,cheese_product.cost]]

# Создаём ингридиенты из продуктов
dough_ingredient = Ingredient(*product_list[0], 100)
tomato_ingredient = Ingredient(*product_list[1], 100)
cheese_ingredient = Ingredient(*product_list[2], 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита',[dough_ingredient, tomato_ingredient, cheese_ingredient])

print(pizza_margarita)