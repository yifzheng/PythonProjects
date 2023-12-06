import random

""" GLOBAL CONSTANTS"""
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

"""NUMBER OF SYMBOLS IN EACH COLUMN"""
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 4
}

""" VALUES FOR EACH SYMBOL """
SYMBOL_VALUES = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 4
}

"""GET SLOTH MACHINE SPIN"""
def get_slot_machine_spin(rows, cols, symbols):
    symbol_bank = []
    """ SLOT MACHINE """
    columns = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            symbol_bank.append(symbol)
    for _ in range(cols):
        column = []
        current_symbols = symbol_bank[:]
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)
    """ RETURN SLOT MACHINE """
    return columns

""" PRINT SLOT MACHINE """
def print_slot_machine(columns):
    print("<------->")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if (i != len(columns) - 1):
                print(column[row], end=" | ")
            else:
                print(column[row], end="") 
        print()
    print("<------->")
    
def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            current_symbol = column[line]
            if (symbol != current_symbol):
                break
        else:
            winnings += values[symbol] * bet
    return winnings

"""GET PLAYER DEPOSIT"""
def deposit():
   while True:
       amount = input("Please depost some money: $")
       if (amount.isdigit()):
           amount = int(amount)
           if (amount > 0):
               break
           else:
               print("Please enter an amount greater than 0!")
       else :
           print("Please input a number value!")
   return amount

"""GET NUMBER OF LINES FOR THE SLOT MACHINE"""
def get_num_of_lines():
    while True:
        lines = input("Please enter number of lines to be on (1-" + str(MAX_LINES) + ") ")
        if (lines.isdigit()):
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break
            else:
                print("Please enter a valid number of lines!")
        else :
            print("Please input a number value!")
    return lines

"""GET BET AMOUNT FROM PLAYER"""
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if (bet.isdigit()):
            bet = int(bet)
            if (MIN_BET <= bet <= MAX_BET):
                break
            else:
                print("Please enter a valid bet amount between " + str(MIN_BET) + " - " + str(MAX_BET))
        else :
            print("Please input a number value!")
    return bet

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if (total_bet > balance):
            print("You don't have enough balance for this bet. Current Balance: $" + str(balance))
        else: break
    print("You are betting $" + str(bet) + " on " + str(lines) + " lines. Total bet: $" + str(total_bet))
    
    """ GENERATE SLOT MACHINE """
    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, total_bet, SYMBOL_VALUES)
    print("You won $" + str(winnings))
    return winnings - total_bet
""" 
Main function
"""
def main():
    balance = deposit()
    while True:
        print("Current balance is $" + str(balance))
        spining = input("Press enter to spin slot machine (q t quit)")
        if (spining == "q"): break
        balance += spin(balance)
        if (balance == 0): break
    print("You are left with $" + str(balance))
    
main()