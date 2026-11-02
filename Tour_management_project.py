import connection as c 
from datetime import datetime

def view_tour():
    sql = """SELECT id, title, detail, start_date, days, adult_rate, child_rate FROM tour WHERE is_deleted = 0 ORDER BY id DESC"""

    table = c.fetchData(sql)

    if len(table) == 0:
        print("There are no tours")
    else:
        print(f"{'ID':<6}{'Title':<30}{'Start Date':<15}{'Days':<8}{'Adult Rate':<12}{'Child Rate':<12}")
        print("-" * 83)

        for row in table:
            print(f"{row['id']:<6}" ,f"{row['title']:<30}",f"{str(row['start_date']):<15}", f"{row['days']:<8}",f"{row['adult_rate']:<12}",f"{row['child_rate']:<12}")

        print("-" * 83)

    key = input("Press any key to continue")
def display_transaction():
    sql = "SELECT Id, tourid, amount, flag, description, challanno, trandate FROM `transaction` WHERE is_deleted=0 ORDER BY trandate"
    transactions = c.fetchData(sql)

    print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Challan No.':<15} {'Date':<12}")
    print("-"*100)

    TotalIncome = 0
    TotalExpense = 0

    for index, row in enumerate(transactions):
        if row['flag'] == 1:
            transaction_type = "Income"
            TotalIncome = TotalIncome + row['amount']
        else:
            transaction_type = "Expense"
            TotalExpense = TotalExpense + row['amount']

        print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {row['challanno']:<15} {str(row['trandate']):<12}")

        if True:
            key = input("Press any key to continue")

    print("-"*100)
    print(f"Total Income  = {TotalIncome}")
    print(f"Total Expense = {TotalExpense}")
    print(f"Balance       = {TotalIncome - TotalExpense}")

    key = input("Press any key to continue")
while True: 
    print("Press 1 for Tour Management")
    print("Press 2 for Transaction Management")
    print("Press 3 for Report management ")
    print("Press 0 for Exit ")

    choice = int(input("Enter your choice"))
    if choice == 1:
        while True :
            print("-"*100)
            print("Tour Management")
            print("-"*100)
            print("press 1 for insert ")
            print("press 2 for  update ")
            print("press 3 for delete ")
            print("press 4 for view ")
            print("press 0 to exit ")
            tour_choice = int(input("enter your choice of tour"))

            if tour_choice==1:
                print("let's add new tour")
                title = input('enter title of your tour')
                detail = input("enter details of the tour")
                start_date = input("enter start date in yy-mm-dd")
                days = int(input("enter number of days"))
                adult_price = int(input("enter price of adult"))
                child_rate = int(input("enter price of kids "))
                sql = "insert into tour( title, detail, start_date, days, adult_rate, child_rate ) VALUES (%s,%s,%s,%s,%s,%s)"
                values = [title,detail,start_date,days,adult_price,child_rate]
                success = c.runSQL(sql,values)
                if success==1:
                    print("Tour added successfully")
                key = input("Press any key to continue")

            elif tour_choice==2:
                print("let's update tour")
                tour_id = int(input("enter the tour id you want to update"))
                sql = "SELECT id, title FROM tour WHERE id = %s AND is_deleted = 0"
                values = [tour_id]
                data = c.fetchData(sql, values)
                if len(data)==0:
                    print("Id not found")

                else:
                    print("Enter new details")
                    title = input("enter new title")
                    detail = input("enter new details")
                    start_date = input("enter date in yy-mm-dd")
                    days = int(input("enter days"))
                    adult_rate = int(input("enter adult price"))
                    child_rate = int(input("enter child price"))
                    sql = "update tour set title = %s,detail =%s , start_date = %s,days = %s, adult_rate = %s, child_rate = %s where id = %s and is_deleted =0"
                    values =[title,detail,start_date,days,adult_rate,child_rate,tour_id]
                    success = c.runSQL(sql,values)
                    if success==1:
                        print("Tour updated successfully")
                key = input("Press any key to continue")

            elif tour_choice==3:
                print("let's delete tour")
                tour_id = int(input("Enter the tour ID you want to delete: "))
                sql = "SELECT id, title FROM tour WHERE id = %s AND is_deleted = 0"
                values = [tour_id]
                data = c.fetchData(sql, values)
                if len(data) == 0:
                    print("Tour ID not found")
                else:
                    sql = "UPDATE tour SET is_deleted = 1 WHERE id = %s"
                    values = [tour_id]
                    success = c.runSQL(sql, values)
                    if success == 1:
                        print("Tour deleted successfully")
                    else:
                        print("Delete cancelled")

                key = input("Press any key to continue")

            elif tour_choice==4:
                print("let's view tours")
                view_tour()
                
            elif tour_choice==0:
                print("let's exit to main menu")
                break
            else:
                print("Invalid choice")
    elif choice == 2:
        while True:
            print("-"*100)
            print("Transaction Management")
            print("-"*100)
            print("press 1 for insert ")
            print("press 2 for  view ")
            print("press 3 for delete ")
            print("press 4 for search ")
            print("press 0 to exit ")
            transaction_choice = int(input("enter your choice of editing"))
            if transaction_choice == 1:
                print("let's add new transaction")
                tourid = int(input("Enter tour ID: "))
                amount = int(input("Enter transaction amount: "))
                print("Press 1 for Income")
                print("Press 2 for Expense")
                flag = int(input("Enter transaction type: "))
                description = input("Enter transaction description: ")
                challanno = input("Enter receipt/challan number: ")
                trandate = input("Enter transaction date (YYYY-MM-DD): ")
                sql = " insert into transaction (tourid ,amount,flag,description,challanno,trandate) values (%s,%s,%s,%s,%s,%s)"
                values = [tourid, amount, flag, description, challanno, trandate]
                success = c.runSQL(sql, values)
                if success == 1:
                        print("Transaction added successfully")

                key = input("Press any key to continue")

            elif transaction_choice == 2:
                print("let's view transaction")
                display_transaction()

            elif transaction_choice == 3:
                print("let's delete transaction")
                id = int(input("enter transaction id to delete"))
                sql = "update transaction set is_deleted = 1 where id = %s"
                values =[id]
                success = c.runSQL(sql,values)
                if success ==1:
                    print("Transaction deleted successfully")



            elif transaction_choice == 4: 
                print("let's search transaction")
                search_value = int(input("enter tour id"))
                sql = "select * from transaction where tourid = %s and is_deleted = 0 order by tourid"
                values = [search_value]
                transaction = c.fetchData(sql,values)
                print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Challan No.':<15} {'Date':<12}")
                print("-"*100)
                if len(transaction) == 0:
                    print("No Transaction found for this Tour ID")
                else:
                    for row in transaction:
                        if row['flag'] == 1:
                            transaction_type = "Income"
                        else:
                            transaction_type = "Expense"

                        print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {row['challanno']:<15} {str(row['trandate']):<12}")

                key = input("Press any key to continue")


            elif transaction_choice == 0:
                print("let's exit to main menu")


                break
            else:
                print("Invalid choice")

    elif choice == 3:
        print("let's develop reports")
        while True:
            print("Press 1 for Month-wise Report")
            print("Press 2 for Quarter-wise Report")
            print("Press 3 for Year-wise Report")
            print("Press 4 for Tour ID-wise Report")
            print("Press 5 for All Tours Report")
            print("Press 0 for Back to Main Menu")
            report_choice = int(input("Enter your choice: "))
            if report_choice == 1:
                print("Here's Month-wise Report")
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year: "))

                sql = "SELECT Id, tourid, amount, flag, description, challanno, trandate FROM `transaction` WHERE MONTH(trandate) = %s AND YEAR(trandate) = %s AND is_deleted = 0 ORDER BY trandate"

                values = [month, year]
                transaction = c.fetchData(sql, values)

                if len(transaction) == 0:
                    print("No transaction found")
                else:
                    TotalIncome = 0
                    TotalExpense = 0

                    print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Date':<12}")
                    print("-"*85)

                    for row in transaction:
                        if row['flag'] == 1:
                            transaction_type = "Income"
                            TotalIncome += row['amount']
                        else:
                            transaction_type = "Expense"
                            TotalExpense += row['amount']

                        print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {str(row['trandate']):<12}")

                    print("-"*85)
                    print(f"Total Income = {TotalIncome}")
                    print(f"Total Expense = {TotalExpense}")
                    print(f"Balance = {TotalIncome - TotalExpense}")

                key = input("Press any key to continue")

            elif report_choice == 2:
                print("Here's Quarter-wise Report")
                year = int(input("Enter year: "))
                print("Press 1 for Q1 (Jan-Mar)")
                print("Press 2 for Q2 (Apr-Jun)")
                print("Press 3 for Q3 (Jul-Sep)")
                print("Press 4 for Q4 (Oct-Dec)")
                quarter = int(input("Enter quarter: "))

                if quarter == 1:
                    start_month = 1
                    end_month = 3
                elif quarter == 2:
                    start_month = 4
                    end_month = 6
                elif quarter == 3:
                    start_month = 7
                    end_month = 9
                elif quarter == 4:
                    start_month = 10
                    end_month = 12
                else:
                    print("Invalid quarter")
                    start_month = 0
                    end_month = 0

                if start_month != 0:
                    sql = "SELECT Id, tourid, amount, flag, description, challanno, trandate FROM `transaction` WHERE MONTH(trandate) BETWEEN %s AND %s AND YEAR(trandate) = %s AND is_deleted = 0 ORDER BY trandate"
                    values = [start_month, end_month, year]
                    transaction = c.fetchData(sql, values)

                    if len(transaction) == 0:
                        print("No transaction found")
                    else:
                        TotalIncome = 0
                        TotalExpense = 0

                        print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Date':<12}")
                        print("-"*85)

                        for row in transaction:
                            if row['flag'] == 1:
                                transaction_type = "Income"
                                TotalIncome += row['amount']
                            else:
                                transaction_type = "Expense"
                                TotalExpense += row['amount']

                            print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {str(row['trandate']):<12}")

                        print("-"*85)
                        print(f"Total Income = {TotalIncome}")
                        print(f"Total Expense = {TotalExpense}")
                        print(f"Balance = {TotalIncome - TotalExpense}")

                    key = input("Press any key to continue")

            elif report_choice == 3:
                print("Here's Year-wise Report")
                year = int(input("Enter year: "))

                sql = "SELECT Id, tourid, amount, flag, description, challanno, trandate FROM `transaction` WHERE YEAR(trandate) = %s AND is_deleted = 0 ORDER BY trandate"
                values = [year]
                transaction = c.fetchData(sql, values)

                if len(transaction) == 0:
                    print("No transaction found")
                else:
                    TotalIncome = 0
                    TotalExpense = 0
                    count = 0

                    print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Date':<12}")
                    print("-"*85)

                    for row in transaction:
                        if row['flag'] == 1:
                            transaction_type = "Income"
                            TotalIncome += row['amount']
                        else:
                            transaction_type = "Expense"
                            TotalExpense += row['amount']

                        print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {str(row['trandate']):<12}")
                        count += 1

                    print("-"*85)
                    print(f"Total Transactions = {count}")
                    print(f"Total Income = {TotalIncome}")
                    print(f"Total Expense = {TotalExpense}")
                    print(f"Balance = {TotalIncome - TotalExpense}")

                key = input("Press any key to continue")


            elif report_choice == 4:
                print("Here's Tour ID-wise Report")
                tourid = int(input("Enter Tour ID: "))

                sql = "SELECT Id, tourid, amount, flag, description, challanno, trandate FROM `transaction` WHERE tourid = %s AND is_deleted = 0 ORDER BY trandate"
                values = [tourid]
                transactions = c.fetchData(sql, values)

                if len(transactions) == 0:
                    print("No transaction found for this Tour ID")

                else:
                    TotalIncome = 0
                    TotalExpense = 0

                    print(f"{'ID':<5} {'Tour ID':<9} {'Type':<10} {'Description':<30} {'Amount':>10} {'Date':<12}")
                    print("-" * 85)

                    for row in transactions:
                        if row['flag'] == 1:
                            transaction_type = "Income"
                            TotalIncome += row['amount']
                        else:
                            transaction_type = "Expense"
                            TotalExpense += row['amount']

                        print(f"{row['Id']:<5} {row['tourid']:<9} {transaction_type:<10} {row['description'][:29]:<30} {row['amount']:>10} {str(row['trandate']):<12}")

                    print("-" * 85)
                    print(f"Total Income = {TotalIncome}")
                    print(f"Total Expense = {TotalExpense}")
                    print(f"Balance = {TotalIncome - TotalExpense}")

                key = input("Press any key to continue")

            elif report_choice == 5:
                print("Here's All Tours Report")
                sql = "SELECT id, title FROM tour WHERE is_deleted = 0 ORDER BY id"
                tours = c.fetchData(sql)

                if len(tours) == 0:
                    print("No tours found")

                else:
                    GrandIncome = 0
                    GrandExpense = 0

                    print(f"{'Tour ID':<10} {'Tour Name':<30} {'Income':>12} {'Expense':>12} {'Balance':>12}")
                    print("-" * 80)

                    for tour in tours:
                        tourid = tour['id']

                        sql = "SELECT flag, SUM(amount) AS total FROM `transaction` WHERE tourid = %s AND is_deleted = 0 GROUP BY flag"
                        values = [tourid]
                        totals = c.fetchData(sql, values)

                        TotalIncome = 0
                        TotalExpense = 0

                        for row in totals:
                            if row['flag'] == 1:
                                TotalIncome = row['total'] or 0
                            elif row['flag'] == 2:
                                TotalExpense = row['total'] or 0

                        balance = TotalIncome - TotalExpense

                        GrandIncome += TotalIncome
                        GrandExpense += TotalExpense

                        print(f"{tour['id']:<10} {tour['title'][:29]:<30} {TotalIncome:>12} {TotalExpense:>12} {balance:>12}")

                    print("-" * 80)
                    print(f"{'GRAND TOTAL':<40} {GrandIncome:>12} {GrandExpense:>12} {GrandIncome - GrandExpense:>12}")

                key = input("Press any key to continue")

            elif report_choice == 0:
                break
            else:
                print("Invalid choice")
    elif choice == 0:
        print("Thank you for using our software")
        break 
    else:
        print("Not a valid choice")



            