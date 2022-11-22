# coffee-machine
Python Coffee Machine
WHat can this coffee machine do?

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt shows every time action has completed, e.g. once the drink is
dispensed. The prompt shows again to serve the next customer.

2. Be turned off by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

3. Print report.
a. When the user enters “report” to the prompt, a report is generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g

4. Check if resources are sufficient.
a. When the user chooses a drink, the program checks if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It does
not continue to make the drink but print: “Sorry there is not enough water.”

5. Checks if transaction is successful.
a. Checks that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program returns “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
