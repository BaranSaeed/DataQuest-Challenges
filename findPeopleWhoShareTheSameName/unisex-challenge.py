#Open The File
f = open("unisex_names_table.csv", "r")

#Read the file
read = f.read()

#Convert the String to List
names_list = read.split("\n")

numerical_list = []
nested_list = []
thousand_or_greater_list = []

#Convert List into List of List
for names in names_list:
    comma_list = names.split(",")
    nested_list.append(comma_list)

#Convert Numerical value into string to float
for num in nested_list:
    name = num[1]
    decim = float(num[2])
    new_list = [name,decim]
    numerical_list.append(new_list)

#find which name people shares is greater than 1000 and append it to final list.
for uniqueNum in numerical_list:
    if uniqueNum[1] >= 1000:
        thousand_or_greater_list.append(uniqueNum)

#prints the list
print(thousand_or_greater_list)
