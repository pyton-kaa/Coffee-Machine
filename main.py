MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from espresso import espresso
from latte import latte
from cappuccino import cappuccino
from art import machine
import os
import platform
from time import sleep

art = {
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}

def clear_screen():
    if platform.system() in ["Linux", "Darwin"]:
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        print("I don't recognize your operating system.")
        comm = input("Please type its clear screen command: ")
        os.system(comm)

def brew(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
    clear_screen()
    print(art[coffee][0])
    print("Warming up", end=" ", flush=True)
    for time in range(20):
        print(".", end="", flush=True)
        sleep(0.2)
    sleep(1)
    print(" I'm ready!")
    sleep(1)
    for time in range(1, len(art[coffee])):
        clear_screen()
        print(art[coffee][time])
        sleep(1.5)
    print(f"Your {coffee} is ready!")
    input("Press 'Enter' to continue.")

def check_resources(drink):
    lack = []
    for ingredient in MENU[drink]['ingredients']:
        if resources[ingredient] < MENU[drink]['ingredients'][ingredient]:
            lack.append(ingredient)
    if len(lack) == 0:
        return("sufficient")
    elif len(lack) == 1:
        return(lack[0])
    else:
        lacks = lack[0]
        for index in range(1,len(lack) - 1):
            lacks += ", " + lacks[index]
        lacks += " and " + lack[-1]
        return(lacks)

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0

def payment(drink):
    again = "yes"
    while(again == "yes"):
        print(f"Please insert ${MENU[drink]['cost']}.")
        inserted = 0
        for coin in coins:
            amount = int(input(f"How many {coin} (${coins[coin]}) do you insert? "))
            inserted += coins[coin] * amount
            print(f"Your credit: ${round(inserted, 2)}.")
        if round(inserted, 2) < MENU[drink]['cost']:
            print("Sorry, that's not enough money. Money refunded.")
            again = input("Do you want to try again? (yes / no): ")
            if again == "no":
                return(0)
        elif round(inserted, 2) > MENU[drink]['cost']:
            print(f"Your change is ${round(inserted - MENU[drink]['cost'], 2)}.")
            return(1)
        else:
            print("Thank you!")
            return(1)


clear_screen()
print(machine[0])
print("Welcome to the coffe machine!")
print("Please make sure that the machine fits in the window!")
input("Press 'Enter' to continue.")

power = "on"
while power == "on":
    clear_screen()
    print(machine[0])
    drink = input("What would you like? (espresso / latte / cappuccino): ")
    if drink == "off":
        power = "off"
    elif drink == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${money}")
        input("Press 'Enter' to continue.")
    elif drink in art:
        print(f"I'm checking the resources", end = "", flush = True)
        for time in range(1,10):
            print(".", end = "", flush = True)
            sleep(0.2)
        if check_resources(drink) != "sufficient":
            print(f"Sorry, there is not enough {check_resources(drink)}.")
            sleep(2)
        else:
            print(" Ok!")
            payment_done = payment(drink)
            if payment_done == 1:
                money += MENU[drink]['cost']
                input("Press 'Enter' to put a cup on the tray.")
                brew(drink)
            else:
                print("Payment aborted!")
                sleep(3)
    else:
        print("Oops! Something went wrong. Restarting the machine...")
        sleep(2)
        for time in range(0,5):
            clear_screen()
            print(machine[0])
            print("Restarting. Please wait until the POWER button stops blinking.")
            sleep(0.5)
            clear_screen()
            print(machine[1])
            print("Restarting. Please wait until the POWER button stops blinking.")
            sleep(0.5)

print("Turning off the machine...")
sleep(2)
for time in range(0,3):
    clear_screen()
    print(machine[1])
    print("Turning off. Please wait until the POWER button stops blinking.")
    sleep(0.5)
    clear_screen()
    print(machine[0])
    print("Turning off. Please wait until the POWER button stops blinking.")
    sleep(0.5)
clear_screen()
print(machine[1])
print("Thank you for using the machine. Have a nice day!")
