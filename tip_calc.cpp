/*
 * Martin Patterson
 * COP 3003
 * DUE: 01/22/2024
 */

//This program prompts a user to enter a tip percentage and returns adjusted bill total

#include <iostream>//input and output
#include <ctime>//time
#include <iomanip>//setw

//horizontal line function declaration
void printHorizontalLine();

//message of the day function declaration
void printMotd();

//created a struct so that I can easily access certain elements and it just made sense to me
struct MenuItem {
    std::string name;
    double price;
};

/*
 * In the future id like to make it more modular where pieces are broken down more.
 * better menu handeling
 * more consistent formating and i think i might be indenting weird or explaining things wrong
 * updated store info
 * my currency formating is off
 * overall better flexibility
 * at the moment the outcome is great so who cares!
 */

int main() {
    printHorizontalLine();

    /*
     * I thought about adding a dynamic store array where you could just access a store information and call a store number
     * but i realized that was to much for what I had going on
     * will update later
     */
    std::cout  << "\t     Fresh Fish Forever" << std::endl;
    std::cout  << "884 Sailing Tilapia Ln, Spam, New Hampshire" << std::endl;
    std::cout  << "\t     >>(207) 725-6667<<" << std::endl;

    printMotd();
    printHorizontalLine();

    //thank you mrcrabs very nice
    std::cout << "\nServer: MrCrabs" <<std::endl;
    std::cout << "Table: 012\n" << std::endl;

    printHorizontalLine();

    //didnt feel like making up anything else on the menu
    //add full menu and easier acess later
    const int sizeOfMenu = 5;
    //florida salestaxrate
    const double salesTaxRate = 0.07;


    //accessing menu array from menuitem struct
    //i thought about making 2 arrays that work along side each other but the struct makes more sense especially for later
    MenuItem menu[sizeOfMenu] = {
            {"\t[1]Original Fish and chips", 9.99},
            {"\t[2]Brazen Dozen Oysters", 14.99},
            {"\t[3]Slopped Tuna Sandwich", 5.99},
            {"\t[4]Honey Baked Salmon", 15.99},
            {"\t[5]Holy Clam Chowder", 8.99}
    };

    //displaying a menu on a reciept?
    //sure why not, will use that
    std::cout << "\n[Menu:]\n";
    for (int i = 0; i < sizeOfMenu; ++i) {
        std::cout << std::setw(10) << menu[i].name << ": $" << menu[i].price << '\n';
    }

    //this guy sure does love horizontal lines i mean line breaks
    std::cout << "\n" << std::endl;
    printHorizontalLine();

    //prob a better way of doing this but made
    //each index in array an int and accessed that way
    int fishAndChips = 1;
    int dozenOysters = 2;
    int tunaSandwich = 3;
    int bakedSalmon = 4;
    int clamChowder = 5;

    //access array through struct very nice
    //decided not to use typedef for struct
    std::cout << "Table: 012 | Order: 0694 | Items: 02\n" << std::endl;
    std::cout << std::setw(10) << menu[fishAndChips - 1].name << " - $" << menu[fishAndChips - 1].price << '\n';
    std::cout << std::setw(10) << menu[dozenOysters - 1].name << " - $" << menu[dozenOysters - 1].price << '\n';

    double subtotal = menu[fishAndChips - 1].price + menu[dozenOysters - 1].price;
    std::cout << std::setw(20) << "\nSubtotal: $" << subtotal << std::endl;

    double salesTax = subtotal * salesTaxRate;
    std::cout << "Sales Tax: $" << std::fixed << std::setprecision(2) << salesTax << std::endl;

    double total = subtotal + salesTax;
    std::cout << "Total: $" << std::fixed << std::setprecision(2) << total << std::endl;


    std::cout << "\nWould you like to tip?:  [1]0%  [2]0%  [3]0%  [4]Other  [5]No Tip\n";

    int tipOption;
    std::cout << "\n\tSelect [1-5]: ";
    std::cin >> tipOption;

    double tipPercentage;
    switch (tipOption) {
        case 1:
            tipPercentage = 0.10;
            break;
        case 2:
            tipPercentage = 0.20;
            break;
        case 3:
            tipPercentage = 0.30;
            break;
        case 4:
            std::cout << "Custom:\t";
            std::cin >> tipPercentage;
            tipPercentage /= 100.0;
            break;
        case 5:
            tipPercentage = 0.0;
            break;
        default:
            std::cerr << "Invalid choice. Exiting.\n"; //unbuffered standard error steam in case there is a need to display an error message immediately.
            return 1; //from what ive read bc there's no error message it cannot store the message to display it later
    }

    //the only thing that was actually asked for in this
    double tip = total * tipPercentage;

    //got all confused with the different types of totals
    //realized that i needed to set percision of double
    //using library features for that
    std::cout << "\nTotal: $" << std::fixed << std::setprecision(2) << total << '\n';
    std::cout << "Tip: $" << std::fixed << std::setprecision(2) << tip << '\n';
    double grandTotal = total + tip;
    std::cout << "Grand Total: $" << std::fixed << std::setprecision(2) << grandTotal << '\n';

    printHorizontalLine();

    std::cout << "   Thank you for dining at Fresh Fish Forever!" << std::endl;

    printHorizontalLine();

    return 0;
}

//<iomanip> library for setw and set fill
void printHorizontalLine() {
    // i wanted to have alternating stuff but wasnt sure how
    std::cout << std::setw(50) << std::setfill('=') << "" << std::setfill(' ') << std::endl;
}

//creates an array of 7 messages for each day of the week
void printMotd() {
    const char *messages[] = {
            "The only thing fishy here are picky eaters. Sunday apps are BOGO ALL day.",
            "Enjoy Fresh Fish everyday of the week and half off oysters on Mondays!",
            "Tuesday's are for the kids. BOGO Fish and Chips ALL day!",
            "The Lords day is also Wednesday. Sangria Pitchers in his name are just $12.99 after church!",
            "Thursday's are basically the weekend anyway right? BOGO Drinks from 3-9.",
            "Friday is here and so is our freshest catch. Lobster tails HALF off ALL day.",
            "Every hour on the hour we top off your pint. Happy Saturday!",

    };

    //takes a pointer variable and sets it to the current time
    std::time_t currentTime = std::time(0);
    //tm* struct apart of ctime library returns the calendar time
    //points to the tm struct and converts the current time to something the struct has defined
    std::tm* currentDate = std::localtime(&currentTime);
    //defines dayOfWeek for accessing the array and retrieving current date
    int dayOfWeek = currentDate->tm_wday;

    // loop that accesses the messages in the array and displays the motd based on the currentDate
    if (dayOfWeek >= 0 && dayOfWeek < 7) {
        std::cout <<"                " << (currentDate->tm_mon + 1) << '/' << currentDate->tm_mday << '/' << (currentDate->tm_year + 1900) << std::endl;
        std::cout << messages[dayOfWeek] << std::endl;
    } else {
        std::cout << "ERROR" << std::endl;
    }
}