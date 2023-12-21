"""
Creating my variables for reading the file, instructions: 
* The total number of months included in the dataset.
* The net total amount of Profit/Losses over the entire period.
* The average of the changes in Profit/Losses over the entire period.
* The greatest increase in profits (date and amount) over the entire period.
* The greatest decrease in losses (date and amount) over the entire period.
"""


data = {}

with open("budget_data.csv", "r") as file: # We have now opened the file. 
                                        #print(file) #checked that everything runs smoothly. Which it does! 
    for line in file:
                                        # print(line) #tested this, it works. now we can comment it out 
        line = line.strip()             #stripped my "white space" - SOURCE: https://www.w3schools.com/python/ref_string_strip.asp 
                                        #print(line) #Checked this out already. The lines are stripped
        if line[0:4] == "Date":          #also alternative: if "Date" in line: continue
            continue                    #Skip this cycle (skips this section)
                                        # print(line[0:4])
        line = line.split(",")          #Should help me split my columns <= 
                                        # print(line)
        date = line[0]
        pnl = line[1]
        #Setting the value in the dictionary 
        data[date] = int(pnl) #Sets my code #okay like lists, in lists it is: e.g. in this hyptohetical list: List = [0,1,5,6] = list[0] = 5 , switch 0 => 5
#print(data) 

#Read through my data! 
#Step 2: Calculate the total number of months in the dataset 
# print(data["Jan-2012"]) #this gives me my value. how do I get my keys? 
#To get my keys... 
# print(data.keys())
months = 0
dates = data.keys() #source: https://www.w3schools.com/python/python_ref_dictionary.asp 
"""
Question: 1 
"""
for date in dates: #I already assigned 'date' as a key and 'dates' are my dictionary
    # print(date) Works! 
    months += 1 #
# print(months) - printed! 

"""
Question 2: 
"""
sales = 0
pnl = data.values() 

for p in pnl:
    sales += p 
# print(sales)


"""
Setup for question 3,4,5: 
- get keys 
1) dates. Loop through them skipping 0. Subtract current value by previous value.
Set key into dictionary: Differences with the value being the diff between: current - prior values 

"""
differences = {}

dates = data.keys()  #Data.keys is a 'set of keys' 
dates = list(dates) #Turn keys into a list. <- these ones I can [] 
length_dates = len(dates) 
for i in range(1,length_dates):
    previous_month = dates[i-1]
    current_month = dates[i]
    #print(i, current_month,previous_month)
    current_value = data[current_month]
    previous_value = data[previous_month]
    difference = current_value-previous_value
    # print(current_month, difference)
    differences[current_month] = difference #<- set key & number 


"""
Question 3: Get the average change between months
0) Initialize my variables: avg, length_dict, sumnumbers 
1) Create a loop that loops through into my differences dictionary 
2) Then I take the sum of the differences in dictionary. 
3) Then I take that sum. And I divide it by the length of the dictionary 
"""

avg = 0
length = 0
sum = 0 
list_differences = list(differences.values()) #Get all the values in my differences dictionary & cast it into a list
# print(list_differences)

for diff in list_differences:
    sum += diff
    length += 1
# print(length)

avg = (sum/length)
# print(avg)



"""
Question 4 & 5: 
1. 
"""
# for (date,difference) in differences.items():
#     print(date,difference)
maximum = 0 
minimum = 0 
maximum_date = "" 
minimum_date = ""


### https://www.tutorialspoint.com/python/dictionary_items.htm Source<- 
for item_date_value in differences.items():
    # print(item_date_value[1])
    if item_date_value[1] > maximum: 
        maximum = item_date_value[1]
        maximum_date = item_date_value[0]
    elif item_date_value[1] < minimum:
        minimum = item_date_value[1]
        minimum_date = item_date_value[0]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${sales}")
print(f"Average Change: ${avg:.2f}")
print(f"Greatest Increase in Profits: {maximum_date} (${maximum}) ")
print(f"Greatest Decrease in Profits: {minimum_date} (${minimum}) ")

# Sources: https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

# for (date,difference) in differences.items():
#     if difference > maximum: 
#         maximum = difference
#         maximum_date = date
#     elif difference < minimum: 
#         minimum = difference
#         minimum_date = date

# print(maximum_date,maximum,minimum_date,minimum)

    


#### Void 
# profits = 0
# losses = 0 

# # Ask questions about Q3 
# for p in pnl:
#     if p>0:
#         profits+=p 
#     else: 
#         losses += p 
# # print((profits*86) /(losses * 86))
