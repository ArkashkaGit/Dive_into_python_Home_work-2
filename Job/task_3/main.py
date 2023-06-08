# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Нельзя снять больше, чем на счёте
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10%

# перед каждой операцией, даже ошибочной - НЕЛОГИЧНАЯ ФУНКЦИЯ (проинорировал)
# Любое действие выводит сумму денег - НЕЛОГИЧНАЯ ФУНКЦИЯ (проинорировал)

from Job.task_3.bank_machine import Bank_machine
from Job.task_3.card import Card
from Job.task_3.menu import Menu

# создал объект карты Ивана
card_ivan = Card("Ivan", 1234)

# Создал объект банкомата банка ROYAL,
# вставил карту Ивана, пароль карты - 1234
bank_royal = Bank_machine(card_ivan)

# Создал объект меню банкомата
menu = Menu(bank_royal)

# Запустил интерфейсное меню
menu.menu_bank_card()