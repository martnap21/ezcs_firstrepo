"""
 * Martin Patterson
 * COP 3003
 * DUE: 01/22/2024
 */

# This program prompts a user to enter a tip percentage and returns adjusted bill total

import datetime  # time
import locale  # formatting currency

# set the locale for currency formatting
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


# horizontal line function declaration
def print_horizontal_line():
    """Prints a horizontal line."""
    print("=" * 50)


# message of the day function declaration
def print_motd():
    """Prints the message of the day."""

    messages = [
        "The only thing fishy here are picky eaters. Sunday apps are BOGO ALL day.",
        "Enjoy Fresh Fish everyday of the week and half off oysters on Mondays!",
        "Tuesday's are for the kids. BOGO Fish and Chips ALL day!",
        "The Lords day is also Wednesday. Sangria Pitchers in his name are just $12.99 after church!",
        "Thursday's are basically the weekend anyway right? BOGO Drinks from 3-9.",
        "Friday is here and so is our freshest catch. Lobster tails HALF off ALL day.",
        "Every hour on the hour we top off your pint. Happy Saturday!",
    ]

    # gets the current date
    current_date = datetime.datetime.now()
    day_of_week = current_date.weekday()  # Monday is 0, Sunday is 6

    # displays motd based on current date
    if 0 <= day_of_week < 7:
        print(f"{current_date.strftime('%m/%d/%Y').center(50)}")  # Center the date
        print(messages[day_of_week])
    else:
        print("ERROR")


# created a class so that I can easily access certain elements
class MenuItem:
    """Represents a menu item."""

    def __init__(self, name, price):
        """
        Initializes a MenuItem object.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.
        """
        self.name = name
        self.price = price


"""
 * In the future id like to make it more modular where pieces are broken down more.
 * better menu handling
 * more consistent formatting and i think i might be indenting weird or explaining things wrong
 * updated store info
 * my currency formatting is off
 * overall better flexibility
 * at the moment the outcome is great so who cares!
 """


def main():
    print_horizontal_line()

    """
     * I thought about adding a dynamic store array where you could just access a store information and call a store number
     * but i realized that was to much for what I had going on
     * will update later
     """
    print("\t\t     Fresh Fish Forever")
    print("884 Sailing Tilapia Ln, Spam, New Hampshire")
    print("\t\t     >>(207) 725-6667<<")

    print_motd()
    print_horizontal_line()

    # thank you mrcrabs very nice
    print("\nServer: MrCrabs")
    print("Table: 012\n")

    print_horizontal_line()

    # didn't feel like making up anything else on the menu
    # add full menu and easier access later
    # florida sales tax rate
    sales_tax_rate = 0.07

    # accessing menu array from MenuItem struct
    # i thought about making 2 arrays that work along side each other but the struct makes more sense especially for later
    menu = [
        MenuItem("\t[1]Original Fish and chips", 9.99),
        MenuItem("\t[2]Brazen Dozen Oysters", 14.99),
        MenuItem("\t[3]Slopped Tuna Sandwich", 5.99),
        MenuItem("\t[4]Honey Baked Salmon", 15.99),
        MenuItem("\t[5]Holy Clam Chowder", 8.99),
    ]

    # displaying a menu on a receipt?
    # sure why not, will use that
    print("\n[Menu:]\n")
    for i, item in enumerate(menu):
        print(f"{item.name:<30}: {locale.currency(item.price, grouping=True)}")

    # this guy sure does love horizontal lines i mean line breaks
    print("\n")
    print_horizontal_line()

    # prob a better way of doing this but made
    # each index in array an int and accessed that way
    fish_and_chips = 1
    dozen_oysters = 2
    tuna_sandwich = 3
    baked_salmon = 4
    clam_chowder = 5

    # access array through struct very nice
    # decided not to use typedef for struct
    print("Table: 012 | Order: 0694 | Items: 02\n")
    print(f"{menu[fish_and_chips - 1].name:<30} - {locale.currency(menu[fish_and_chips - 1].price, grouping=True)}")
    print(f"{menu[dozen_oysters - 1].name:<30} - {locale.currency(menu[dozen_oysters - 1].price, grouping=True)}")

    subtotal = menu[fish_and_chips - 1].price + menu[dozen_oysters - 1].price
    print(f"\n{'Subtotal:':>30} {locale.currency(subtotal, grouping=True)}")

    sales_tax = subtotal * sales_tax_rate
    print(f"{'Sales Tax:':>30} {locale.currency(sales_tax, grouping=True)}")

    total = subtotal + sales_tax
    print(f"{'Total:':>30} {locale.currency(total, grouping=True)}")

    print(
        "\nWould you like to tip?:  [1]10%  [2]20%  [3]30%  [4]Other  [5]No Tip\n"
    )

    while True:
        try:
            tip_option = int(input("\tSelect: "))
            if 1 <= tip_option <= 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    if tip_option == 4:
        while True:
            try:
                tip_percentage = float(input("Custom:\t")) / 100.0
                break
            except ValueError:
                print("Invalid input. Please enter a valid percentage.")
    elif tip_option == 1:
        tip_percentage = 0.10
    elif tip_option == 2:
        tip_percentage = 0.20
    elif tip_option == 3:
        tip_percentage = 0.30
    elif tip_option == 5:
        tip_percentage = 0.0
    else:
        print("Invalid choice. Exiting.")
        return

    # the only thing that was actually asked for in this
    tip = total * tip_percentage

    # got all confused with the different types of totals
    # realized that i needed to set precision of double
    # using library features for that
    print(f"\n{'Total:':>30} {locale.currency(total, grouping=True)}")
    print(f"{'Tip:':>30} {locale.currency(tip, grouping=True)}")
    grand_total = total + tip
    print(f"{'Grand Total:':>30} {locale.currency(grand_total, grouping=True)}")

    print_horizontal_line()

    print("   Thank you for dining at Fresh Fish Forever!")

    print_horizontal_line()


if __name__ == "__main__":
    main()
