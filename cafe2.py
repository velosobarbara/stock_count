import math

menu = ['Steak Frites', 'Avocado Toast', 'Curry and Rice', 'BLT Sandwich']

stock = { 'Steak Frites' : 4,
         'Avocado Toast' : 3,
         'Curry and Rice' : 5,
         'BLT Sandwich' : 6}

price = { 'Steak Frites' : 10.99,
         'Avocado Toast' : 8.60,
         'Curry and Rice' : 12.00,
         'BLT Sandwich' : 9.00}

#take stock keys and price keys
#multiply both values via range[] funct
#loop through the dictionary
#display total stock worth

#THIS NEEDS TO BE A NEW LIST
item_value_sf = round((stock['Steak Frites'] * price['Steak Frites']), 2)
item_value_at = round((stock['Avocado Toast'] * price['Avocado Toast']), 2)
item_value_cr = round((stock['Curry and Rice'] * price['Curry and Rice']), 2)
item_value_blt = round((stock['BLT Sandwich'] * price['BLT Sandwich']), 2)
#LIST CAN BE SUMMED AS TOTAL STOCK WORTH

print(f"Each item's stock worth is as displayed below:\nSteak Frites: £{item_value_sf}\nAvocado Toast: £{item_value_at}\nCurry and Rice: £{item_value_cr}\nBLT Sandwich: £{item_value_blt}\n")

total_stock_worth = item_value_sf, item_value_at, item_value_cr, item_value_blt
final_stock_calcu = sum(total_stock_worth)
print(f"The total worth of all your current stock is as displayed below: \n£{final_stock_calcu}")