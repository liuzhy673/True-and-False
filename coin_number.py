coin_number = 1000  # 初始值

def decrease_coin(amount):
    global coin_number
    coin_number -= int(amount)
    return coin_number
def increase_coin(amount):
    global coin_number
    coin_number += int(amount)
    return coin_number

def get_coin():
    return coin_number