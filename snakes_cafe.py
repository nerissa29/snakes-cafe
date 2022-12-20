from textwrap import dedent


print(dedent("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""))

print(dedent("""
Appetizers
----------
Wings
Cookies
Spring Rolls
   
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
    
Desserts
--------
Ice Cream
Cake
Pie
    
Drinks
------
Coffee
Tea
Unicorn Tears 
"""))

food_dict = {
    "Wings": 0,
    "Cookies": 0,
    "Spring": 0,
    "Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn ": 0
}

def order_options():
    print(dedent("""
    ***********************************
    **  What would you like to order? **
    *********************************** 
    """))
    food_selected = input("> ")
    if food_selected.lower() == "quit":
        return

    # for i in food_dict:
    #     if food_selected == food_dict[i]:
    #         food_dict[selected] += 1
    #         print(f"** {food_dict[selected]} order of {food_selected} have been added to your meal **")

    if food_selected in food_dict:
        food_dict[food_selected] += 1
        print(f"** {food_dict[food_selected]} order of {food_selected} have been added to your meal **")

    prompt_again = True
    while prompt_again:
        print(dedent("""
        ***********************************
        **  Would you like to add another order, y/n? **
        *********************************** 
        """))
        user_input = input("> ")
        if user_input.lower() == "quit":
            return
        elif user_input.lower() == "y":
            print(dedent("""
            ***********************************
            **  What would you like to order? **
            *********************************** 
            """))
            next_order = input("> ")
            # if next_order == food_dict[i]:
            #     food_dict[next_order] += 1
            #     print(f"** {food_dict[next_order]} order of {next_order} have been added to your meal **")

            if next_order in food_dict:
                food_dict[next_order] += 1
                print(f"** {food_dict[next_order]} order of {next_order} have been added to your meal **")
        elif user_input.lower() == "n":
            return
        else:
            print("Please try again!")


if __name__ == "__main__":
    order_options()
