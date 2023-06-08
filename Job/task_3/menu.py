from Job.task_3.bank_machine import Bank_machine

class Menu():

    def __init__(self, bank_machine: Bank_machine):
        self.bank_machine = bank_machine

    def menu_bank_card(self):
        print("Здраствуйте, вы попали в личное меню для управления вашими денежными средствами!\n")
        print("веберите пункт для дальнейших действий")
        while True:
            print("1. Узнать баланс!")
            print("2. Пополнить лицевой счёт!")
            print("3. Снять наличные!")
            print("4. Закончить сеанс!")
            print("5. Пункт для сотрудника инкосации!")
            point = input("")
            if point == "1":
                print(self.bank_machine.balance_user_card())
            elif point == "2":
                self.bank_machine.add_many_in_card()
            elif point == "3":
                self.bank_machine.remove_many()
            elif point == "4":
                print("Спасибо что воспользовались нашими услугами, всего доброго!")
                self.bank_machine.end_session()
            elif point == "5":
                print("остаток наличных вбанкомате!")
                print(self.bank_machine.get_balance_bank_machine())
            else:
                print("вы выбрали не верный пункт! попробуйте снова")