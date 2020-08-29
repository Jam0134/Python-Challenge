
import os
import csv

# Specify the file to write to
output_path = os.path.join(  "budget_data.csv")
total_months = 0
net_profit_loss = 0.0
curr_month_pl = 0.0
monthly_change_list=[]
prev_month_pl = 0.0
curr_monthly_change_val = 0.0
prev_month_change_val = 0.0
g_monthly_profit = 0.0
g_profit_date=""
g_monthly_loss = 0.0
g_loss_date=""

# Open the file using mode. Specify the variable to hold the contents
with open("budget_data.csv") as financial_data:

    # Initialize csv.reader 
    csvreader = csv.reader(financial_data, delimiter=',')

    print(csvreader)

    # Write the first row (column headers)
    header = next(csvreader)


      
#Find total number of months in budget data file
#Find the average of the changes in the pfrt/losses
#Find the greatest increase in profits (date and amount) over entire period
#Find the greatest decrease in losses (date and amount) over the entire period
   
    for row in csvreader:
        total_months=total_months+1
        curr_month_pl = int(row[1])
        if (total_months >1):
            curr_monthly_change_val = curr_month_pl - prev_month_pl
            monthly_change_list.append(curr_monthly_change_val)
            if (curr_monthly_change_val > g_monthly_profit):
                g_monthly_profit = curr_monthly_change_val
                g_profit_date=row[0]
            if (curr_monthly_change_val < g_monthly_loss):
                g_monthly_loss = curr_monthly_change_val
                g_loss_date = row[0]
        else:
            curr_monthly_change_val = curr_month_pl
        


#Find the net total amount of Prft/losses over the period
        net_profit_loss = net_profit_loss + curr_month_pl
        prev_month_pl = curr_month_pl
        prev_month_change_val =curr_monthly_change_val


    print ('total_months ',total_months)
    print("Total profit loss",net_profit_loss)
    avg_change = round(sum(monthly_change_list) / len(monthly_change_list),2)
    print(avg_change)
    print(g_monthly_profit)
    print(g_profit_date)
    print(g_monthly_loss)
    print(g_loss_date)



# writing to csv file  
financial_output = "my_financial_output.txt"

with open(financial_output, 'w') as csvfile:  

    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    writer = csv.writer(my_financial_output) 
        
    # writing the data rows  
    writer.writerows(myData)





