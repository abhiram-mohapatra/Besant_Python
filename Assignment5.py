'''The electricity deptartment has the following billing criteria:
basic charge 100 rupees
1-50 unit 1 rs per unit
51-100 unit 2 rs per unit
101-200 unit 3 rs per unit
201-300 unit 4 rs per unit
301-400 unit 5 rs per unit 
401-500 unit 6 rs per unit
> 500 unit 8 rs per unit
The monthly rent of the house is 15000 and water charge for 100 unit is rs 150 for 100-200 unit is rs 250 and for more than 200 unit is rs 400 and monthly meter chargre is rs 50
Calculate the total rent paid by the tenant in a month including the electric bill and water charges.'''

rent=15000
print("Monthly rent of the house: ",rent)

electric_unit=int(input("Enter the electric_units consumed from electric meter: "))

if(electric_unit<=50):
    amount = electric_unit*1
    electric_bill=amount+100
elif(electric_unit>50 and electric_unit<=100):
    amount = (electric_unit-50)*2
    electric_bill=amount+150
elif(electric_unit>100 and electric_unit<=200):
    amount = (electric_unit-100)*3
    electric_bill=amount+250
elif(electric_unit>200 and electric_unit<=300):
    amount = (electric_unit-200)*4
    electric_bill=amount+550
elif(electric_unit>300 and electric_unit<=400):
    amount = (electric_unit-300)*5
    electric_bill=amount+950
elif(electric_unit>400 and electric_unit<=500):
    amount = (electric_unit-400)*6
    electric_bill=amount+1450
else:
    amount = (electric_unit-500)*8
    electric_bill=amount+2050

print("Electric Bill: ",electric_bill)

water_unit=int(input("Enter the units consumed from water meter: "))
if(water_unit<=100):
    water_bill=150
if(water_unit>100 and water_unit<=200):
    water_bill=250
if(water_unit>200):
    water_bill=400

meter_charge=50
water_bill=water_bill+meter_charge
print("Water Bill: ",water_bill)

total_bill=rent+electric_bill+water_bill
print("Amount paid by the tenant: ",total_bill)