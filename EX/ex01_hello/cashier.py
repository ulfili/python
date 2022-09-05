"""Cha-ching."""

amount = int(input("Enter a sum: "))                                                 # enter a sum
coin_50 = int(amount // 50)                                                          # how many times does coin_50 fit inside amount
num50 = int(amount % 50)                                                             # rest money
coin_20 = int(num50 // 20)                                                           # how many times does coin_20 fit inside num50
num20 = int(num50 % 20)                                                              # rest money
coin_10 = int(num20 // 10)                                                           # how many times does coin_10 fit inside num20
num10 = int(num20 % 10)                                                              # rest money
coin_5 = int(num10 // 5)                                                             # how many times does coin_5 fit inside num10
num5 = int(num10 % 5)                                                                # rest money
coin_1 = int(num5 // 1)                                                              # how many times does coin_1 fit inside num5
print("Amount of coins needed:", coin_50 + coin_20 + coin_10 + coin_5 + coin_1)      # amount of coins needed
