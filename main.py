import datetime
import locale

try:
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
except locale.Error:
    print("Warning: en_US.UTF-8 locale not available. Using default locale.")
    locale.setlocale(locale.LC_ALL, "")

def print_horizontal_line():
    print("=" * 50)


def print_motd():
    messages = [
        "The only thing fishy here are picky eaters. Sunday apps are BOGO ALL day.",
        "Enjoy Fresh Fish everyday of the week and half off oysters on Mondays!",
        "Tuesday's are for the kids. BOGO Fish and Chips ALL day!",
        "The Lords day is also Wednesday. "
        "Sangria Pitchers in his name are just $12.99 after church!",
        "Thursday's are basically the weekend anyway right? BOGO Drinks from 3-9.",
        "Friday is here and so is our freshest catch. Lobster tails HALF off ALL day.",
        "Every hour on the hour we top off your pint. Happy Saturday!",
    ]
    current_date = datetime.datetime.now()
    day_of_week = current_date.weekday()
    if 0 <= day_of_week < 7:
        print(f"{current_date.strftime('%m/%d/%Y').center(50)}")
        print(messages[day_of_week])
    else:
        print("ERROR: Invalid day of week.")


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def display_menu(menu):
    print("\n[Menu:]\n")
    for item in menu.values():
        print(f"{item.name:<30}: {locale.currency(item.price, grouping=True)}")


def get_tip_percentage():
    print("\nWould you like to tip?:  [1]10%  [2]20%  [3]30%  [4]Other  [5]No Tip\n")
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
                if 0 <= tip_percentage <= 1:
                    break
                else:
                    print("Invalid input. Percentage should be between 0 and 100")
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
        return None
    return tip_percentage


def calculate_bill(menu, order_items, sales_tax_rate):
    subtotal = sum(item.price for item in order_items)
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax
    return total


def print_bill(menu, order_items, total, tip):
    print("\n")
    print_horizontal_line()
    print("Table: 012 | Order: 0694 | Items: 02\n")
    for item in order_items:
        print(f"{item.name:<30} - {locale.currency(item.price, grouping=True)}")
    print(
        f"\n{'Subtotal:':>30} "
        f"{locale.currency(sum(item.price for item in order_items), grouping=True)}"
    )
    print(
        f"{'Sales Tax:':>30} "
        f"{locale.currency(total - sum(item.price for item in order_items), grouping=True)}"
    )
    print(f"{'Total:':>30} {locale.currency(total, grouping=True)}")
    if tip is not None:
        print(f"{'Tip:':>30} {locale.currency(tip, grouping=True)}")
        grand_total = total + tip
        print(f"{'Grand Total:':>30} {locale.currency(grand_total, grouping=True)}")
    print_horizontal_line()
    print("  Thank you for dining at Fresh Fish Forever!")
    print_horizontal_line()


def main():
    print_horizontal_line()
    print("\t\t  Fresh Fish Forever")
    print("884 Sailing Tilapia Ln, Spam, New Hampshire")
    print("\t\t  >>(207) 725-6667<<")
    print_motd()
    print_horizontal_line()
    print("\nServer: MrCrabs")
    print("Table: 012\n")
    print_horizontal_line()
    sales_tax_rate = 0.07
    menu = {
        1: MenuItem("Original Fish and chips", 9.99),
        2: MenuItem("Brazen Dozen Oysters", 14.99),
        3: MenuItem("Slopped Tuna Sandwich", 5.99),
        4: MenuItem("Honey Baked Salmon", 15.99),
        5: MenuItem("Holy Clam Chowder", 8.99),
    }
    display_menu(menu)
    order_items = [menu[1], menu[2]]
    total = calculate_bill(menu, order_items, sales_tax_rate)
    tip_percentage = get_tip_percentage()
    tip = total * tip_percentage if tip_percentage is not None else None
    print_bill(menu, order_items, total, tip)


if __name__ == "__main__":
    main()
