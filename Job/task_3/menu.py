from Job.task_3.bank_machine import Bank_machine

class Menu():

    def __init__(self, bank_machine: Bank_machine):
        self.bank_machine = bank_machine

    def menu_bank_card(self):
        print("Здраствуйте, вы попали в личное меню для управления вашими денежными средствами!\n")
        print("✔Начальная сумма равна нулю")
        print("✔Допустимые действия: пополнить, снять, выйти")
        print("✔Сумма пополнения и снятия кратны 50 у.е.")
        print("✔Нельзя снять больше, чем на счёте")
        print("✔После каждой третей операции пополнения или снятия начисляются проценты - 3%")
        print("✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.")
        print("✔При превышении суммы в 5 млн, вычитать налог на богатство 10%\n")
        print("веберите пункт для дальнейших действий")
        while True:
            print("1. Узнать баланс!")
            print("2. Пополнить лицевой счёт!")
            print("3. Снять наличные!")
            print("4. Закончить сеанс!")
            print("5. Пункт для сотрудника инкосации!")
            point = input("")
            if point == "1":
                print("Ваш баланс равен", self.bank_machine.balance_user_card())
            elif point == "2":
                self.bank_machine.add_many_in_card()
            elif point == "3":
                self.bank_machine.remove_many()
            elif point == "4":
                print("Спасибо что воспользовались нашими услугами, всего доброго!")
                self.bank_machine.end_session()
            elif point == "5":
                print("остаток наличных в банкомате!")
                print(self.bank_machine.get_balance_bank_machine())
            else:
                print("вы выбрали не верный пункт! попробуйте снова")