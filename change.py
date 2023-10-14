print("Please enter an amount in cents less than a dollar.")
change = int(input())
one_quarter = 25
one_dime = 10
one_nickel = 5
one_penny = 1
print("Your change will be:")
quarter = change//one_quarter
print("Q:", quarter)
dime = (change - quarter*one_quarter)//one_dime
print("D:", dime)
nickel = (change - quarter*one_quarter - dime*one_dime)//one_nickel
print("N:", nickel)
penny = (change - quarter*one_quarter - dime*one_dime - nickel*one_nickel)
print("P:", penny)