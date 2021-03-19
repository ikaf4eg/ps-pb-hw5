class Product:
    def __init__(self, title, calorific, cost):
        if type(title) is str and len(title) > 0:
            if Product.check_calor(calorific) and Product.check_cost(cost):
                self.__title = title
                self.__calorific = calorific
                self.__cost = cost
            else:
                raise ValueError
        else:
            raise ValueError
    def __str__(self):
        #return f'{self.title} {self.calorific} {self.cost}'
        return [self.title,self.calorific,self.cost]
    @staticmethod
    def check_calor(calorific):
        return calorific > 0
    @staticmethod
    def check_cost(cost):
        return cost > 0
    @property
    def title(self):
        return self.__title
    @property
    def calorific(self):
        return self.__calorific
    @property
    def cost(self):
        return self.__cost    
        
class Ingredient(Product):
    def __init__(self, title, calorific, cost, weight):
        super().__init__(title, calorific, cost)
        if Ingredient.check_weight(weight):
            self.__weight = weight
        else:
            raise ValueError
    def __str__(self):
        return f'{self.title} ({self.calorific}), цена - {self.cost} за {self.weight}г'
    def selfcost(self):
        return self.weight / 100 * self.cost
    def calories(self):
        return self.weight / 100 * self.calorific
    @property
    def weight(self):
        return self.__weight
    @staticmethod
    def check_weight(weight):
        return weight > 0

class Pizza:
    def __init__(self, title, ingredients=[]):
        if type(title) is str and len(title) > 0:
            self.__title = title
            self.ingredients = ingredients
        else:
            raise ValueError
    def summ_calories(self):
        sum_cal = 0
        for calor in self.ingredients:
            sum_cal += calor.calories()
        return sum_cal
    def price(self):
        summ = 0
        for price in self.ingredients:
            summ += price.selfcost()
        return summ
    def __str__(self):
        return f'{self.title} ({self.summ_calories()}) цена: {self.price()}'
    @property
    def title(self):
        return self.__title

dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

product_list = [[dough_product.title,dough_product.calorific,dough_product.cost],[tomato_product.title,tomato_product.calorific,tomato_product.cost],[cheese_product.title,cheese_product.calorific,cheese_product.cost]]

print('Ингридиенты:')
for i in product_list:
    print(*i)

dough_ingredient = Ingredient(*product_list[0], 100)
tomato_ingredient = Ingredient(*product_list[1], 100)
cheese_ingredient = Ingredient(*product_list[2], 100)

ingredient_list = [[dough_ingredient.title,dough_ingredient.calorific,dough_ingredient.cost,dough_ingredient.weight],[tomato_ingredient.title,tomato_ingredient.calorific,tomato_ingredient.cost,tomato_ingredient.weight],[cheese_ingredient.title,cheese_ingredient.calorific,cheese_ingredient.cost,cheese_ingredient.weight]]

print('Продукты:')
for i in ingredient_list:
    print(*i)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита',[dough_ingredient, tomato_ingredient, cheese_ingredient])

print(pizza_margarita)