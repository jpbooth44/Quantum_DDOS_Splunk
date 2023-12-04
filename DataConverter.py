#JP Booth
#Last Edited 11/28/23 10:52PM EST

import csv
import random

#file_path = r'C:\Users\clone\Desktop\Honeypot_Data.csv'

#############################################################################################
# This program should not be ran directly, instead being run by the Max Cut Quantum program #
#############################################################################################

last_attack = 274248 #last "Attack" Entry
first_safe = 274249 #first "Not Attack" Entry
last_entry = 289345 #last entry


#function to check if a value is in a list of values, and return the index of said value if so
def checkInList(list, value, index):
    i = 0
    for row in list:
        if (i == index):
            True
        elif (list[i] == value):
            return i
        i+=1
    return 0;

#function to take x random attack entries from csv data and x random not attack data, and create a functional elist from it
def extract_random_entries(file_path, num_attack, num_safe):
    total = []
    ipList = []
    indexList = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        #CSV file is read iteratively and put into "data" variable
        data = list(csv.reader(csvfile))[1:]

        #samples attack data randomly
        r = random.sample(range(0, last_attack), num_attack)

        #appends selected data to list and prints for reference
        i = 0
        while (i < num_attack):
            print(data[r[i]])
            total.append(data[r[i]])
            i+=1

        #samples not attack data randomly
        r = random.sample(range(first_safe, last_entry), num_safe)

        #appends selected data to list and prints for reference
        i = 0
        while(i < num_safe):
            print(data[r[i]])
            total.append(data[r[i]])
            i+=1
        
        #creates a list of all the selected IP addresses
        for row in total:
            ipList.append(row[4].split())

        #creates the index list for the first elist data point, using a new index for new ips, and using the same index for repeated ips
        i = 0
        x = 1
        while (i < len(total)):
            inList = checkInList(ipList, ipList[i], i)
            if (inList and (inList < i)):
                indexList.append(indexList[inList])
            else:
                indexList.append(x)
                x+=1
            i+=1
            
            

        #generates the elist using the index list, destination of 0, and weight of 5 or 1 depending on attack status
        counter = 0 
        final = []
        for row in total:
            final.append((indexList[counter],0,5 if row[0] == "Attack" else 1))
            counter+=1

        #prints results for refence and returns elist
        print(ipList)
        print(indexList)
        print("elist:\n")
        for x in range(len(final)):
            print (final[x],)
        return final
        
#default entries, don't run quantum program with total entries/nodes that would surpass 20
num_attack_entries = 10
num_safe_entries = 5

#random_data = extract_random_entries(file_path, num_attack_entries, num_safe_entries)

#print(random_data)

