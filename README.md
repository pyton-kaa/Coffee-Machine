# Coffee-Machine
A coffee machine simulator run in terminal, with ascii animations

## User's Manual
To launch the program, execute `main.py`.  
The program simulates a coffe machine. You can order americano, cappuccino, or latte, by entering the full name of the coffee in the terminal.
Besides that there are two commands *for staff only* that you can type:
1. `off` turns the machine off and exits the program,
2. `report` checks the availability of resources and money already paid.
After chosing the coffee type, the machine checks availability of the resources and asks you to pay the price. You should enter the numbers of various coins you insert.
After brewing the coffee, the machine will ask you to choose another one.

### Resources
The coffee machine has 3 types of resources: *coffee*, *water* and *milk*. Each time you brew a coffee, depending on its type, the amount of resources left decreases.
If at least one of the resources is lacking, the machine will inform you and ask to choose another coffee type.

### Payment
The machine accepts coins:
- *quarters* ($0.25),
- *dimes* ($0.1),
- *nickles* ($0.05),
- *pennies* ($0.01).
When you type the numbers of all types of coins that you insert, it either gives you back your change, or informs that you didn't pay enough and starts a new payment.

## Skills
The project involves:
- loops and conditional instructions,
- defining own functions,
- importing data from external files,
- managing varius data types at input,
- creating simple animations in text mode.
