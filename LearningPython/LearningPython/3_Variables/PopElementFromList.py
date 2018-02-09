#Defined list containing 4 elements
todays_temperature = [23, 32, 33, 31]

#Added one element to the end
todays_temperature.append(29)
   
#print list
print(todays_temperature)
#Pop() : Removed first element from list
morning = todays_temperature.pop(0)
print("This morning tempreture was {}".format(morning))

#Pop(): Removed first element from list
late_morning = todays_temperature.pop(0)
print("Late morning tempreture was {}".format(late_morning))

#Pop(): Removed first element from list
noon = todays_temperature.pop(0)
print("Afternoon tempreture was {}".format(noon))

#Remaining list
print(todays_temperature)