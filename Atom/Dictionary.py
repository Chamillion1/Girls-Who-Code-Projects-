names_ages = {
"Kamila": 16,
"Isabella": 12,
"Anabel": 48,
"Omar": 49,}
total=0
#print(names_ages)
for keys,values in names_ages.items():

    total= values+total
print(total/len(names_ages))
