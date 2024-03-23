with open("jgknf","r+") as file:
    d = file
class Pizza():
    def __init__(self,name,sauces):
        self.name = name
        self.sauces = sauces
        self.cost = 100 * 4 + 40 * len(sauces)
        self.pizza ={"name":name,"sauces":sauces,"cost":self.cost}
    def print_pizza(self):
        print(f"название пиццы:{self.name}, соусы:{self.sauces}, цена:{self.cost}")

class User():
    def __init__(self,can_buy_pizza,username,password,wallet):
        self.__can_can_buy_pizza = can_buy_pizza
        self.__username = username
        self.__password = password
        self.wallet = wallet
        self.__list_of_shops =[{}]
        self.__cost_of_all_pizzas = 0
    def cost_of_all_pizzas1(self):
        a = str(input(f"вся корзина стоит {self.cost_of_all_pizzas} рублей, будете платить? "))
        if a == "да":
            if self.wallet >= self.cost_of_all_pizzas:
                print("вы успешно все оплатили")
            else:
                print("у вас не хватает денег")
        else:
            pass
    def buy_pizza(self, pizza_name,  cost):
        if pizza_name == "гавайская":
            print("мы не продаем пиццу психически больным")
            self.change_can_buy_pizza(False)
        elif self.can_can_buy_pizza == False:
            print("сначала зарегистрируйтесь / станьте нормальным человеком")
        else:
            a = str(input(f"ваша пицца стоит {cost}, будете покупать"))
            if a == "да":
                if self.wallet >= cost:
                    print("вы успешно купили пиццу")
                    self.wallet -= cost
                else:
                    print("вам не хватает денег")
                    self.cost_of_all_pizzas = self.cost_of_all_pizzas + cost

    def see_balance(self):
        print(f"{self.wallet} рублей")
    def change_balance(self,money):
        self.wallet = self.wallet + money
    def add_in_shop_list(self, pizza):
        self.list_of_shops.append(pizza.pizza)
    def change_can_buy_pizza(self,can_buy_pizza):
        self.can_can_buy_pizza = can_buy_pizza
    def del_obj_shop_list(self, obj):
        del self.list_of_shops[obj]
    def see_shop_list(self):
        print(self.list_of_shops)
    def clear_shoplist(self):
        self.cost_of_all_pizzas = 0
list_of_users ={"username":"bruh","password":"на горшке сидел король"}
username = str(input())
password = str(input())
if username == list_of_users["username"] and password == list_of_users["password"]:
    print("вы успешно зашли в аккаунт")
else:
    print("неправильное имя пользователя или пароль")
    quit()
with open('jgknf', 'r') as file:
    number_str = file.read()
    number = int(number_str)
user = User(True,username,password,number)

for_while = 0
while for_while!=1:
    choice = str(input())
    if choice == "купить пиццу":
        pizza_choice = str(input("Какую пиццу вы хотите "))
        sauces_choice = str(input("Какие соусы вы хотите?(пишите все через пробел) ")).split()
        pizza = Pizza(pizza_choice,sauces_choice)
        user.buy_pizza(pizza.name,pizza.cost)
    elif choice == "пополнить баланс":
        balance = int(input("на сколько вы хотите пополнить баланс "))
        user.change_balance(balance)
    elif choice == "посмотреть баланс":
        user.see_balance()
    elif choice =="оплатить корзину":
        user.cost_of_all_pizzas1()
    elif choice =="выход":
        with open('jgknf', 'w') as file:
            file.write(str(user.wallet))
        quit()
    elif choice =="очистить список покупок":
        user.clear_shoplist()
    else:
        print("Неизвестная команда")
