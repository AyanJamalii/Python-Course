promo_codes = {"PROMO": 200, "AYAN": 10}

items = []

while True:

   item_name1 = input(f"Enter Item 1's name here: ")
   item_name2 = input("Enter Items 2's name here: ")
   item_name3 = input("Enter Items 3's name here: ")
   item_price1 = int(input(f"Enter {item_name1} Price here: "))
   item_price2 = int(input(f"Enter {item_name2} Price here: "))
   item_price3 = int(input(f"Enter {item_name3} Price here: "))

   items.append({"Item 1": item_name1, "| Item's Price": item_price1, 
                 "Item 2": item_name2, "| Item's Price": item_price2, 
                 "Item 3": item_name3, "| Item's Price": item_price3})

   print(f"these are your items: \n {items}")

   total_bill = item_price1 + item_price2 + item_price3
   print(f"Your total is {total_bill}")
   
   
   user_code = input("Enter Promo Code for Discound: ")

   if user_code == "PROMO":
        if total_bill >= 500:     
            new_bill = total_bill - 200
            print(f"Now your total is {new_bill} Rs")
        else: 
            print("Shop for more then 500 Rs to use promo code.")

   elif user_code == "AYAN":
      if total_bill >= 1000:
         bill = total_bill * 0.10
         final_bill = total_bill - bill
         print(f"Your new Total is {final_bill} Rs.")
      else:
        print("Shop more than 1000 to use this code.")

   else:
        total = total_bill
        print(f"No discount applied. Total is {total_bill} Rs.")

   exit_choice = input("Want to continue Shopping? type (yes/no): ")
   if exit_choice.lower() == "no":
    print("Thanks For Shopping")
    break
    


   


