def main():
    totEmp = 0
    totHours = 0
    totGross = 0
    response = input("Would you like to enter an employee's information? [y/n]: ")
    if response == 'N':
        response = 'n'
    while response != 'n':
        id, name, hours, pay = getEmployeeInfo()
        grossPay = calcGrossPay(hours, pay)
        displayPayStatement(id, name, hours, pay, grossPay)
        totEmp += 1
        totHours += hours
        totGross += grossPay
        response = input("Would you like to enter another employee's information? [y/n]: ")
    print('------------------------------------')
    print('Total number of Employees:', totEmp)
    print('Total number of hours worked:', totHours)
    print('Total Gross Pay: $', format(totGross, ',.2f'), sep='')
    print('------------------------------------')
    saveTotals(totEmp, totHours, totGross)
    backupFile()
    print('All info saved to Payroll.txt!')
    print('Goodbye!')

def getEmployeeInfo():
    id = input('Please enter the Employee ID: ')
    name = input('Please enter the Employee Name: ')
    hours = float(input('Please Enter the number of hours worked: '))
    pay = float(input('Please enter the hourly pay: '))
    return id, name, hours, pay

def calcGrossPay(hours, rate):
    if hours > 40:
        gross = ((hours - 40) * (rate * 1.5)) + (40 * rate)
    else:
        gross = hours * rate
    return gross

def displayPayStatement(empID, empName, hoursWorked, hourlyPayRate, grossPay):
    print('------------------------------------')
    print('Employee ID:', empID)
    print('Employee Name:', empName)
    print('Hours Worked:', hoursWorked)
    print('Hourly Pay Rate: $', format(hourlyPayRate, ',.2f'), sep='')
    print('Gross Pay: $', format(grossPay, ',.2f'), sep='')
    print('------------------------------------')
    saveStatement(empID, empName, hoursWorked, hourlyPayRate, grossPay)

def saveStatement(empID, empName, hoursWorked, hourlyPayRate, grossPay):
    empID = convertString('Employee ID: ', empID)
    empName = convertString('Employee Name: ', empName)
    hoursWorked = convertString('Hours Worked: ', hoursWorked)
    hourlyPayRate = convertString('Hourly Pay Rate: $', format(hourlyPayRate, ',.2f'))
    grossPay = convertString('Gross Pay: $', format(grossPay, ',.2f'))
    output_file = open('Payroll.txt', 'a')
    output_file.write('------------------------------------' + '\n')
    output_file.write(empID)
    output_file.write(empName)
    output_file.write(hoursWorked)
    output_file.write(hourlyPayRate)
    output_file.write(grossPay)
    output_file.write('------------------------------------' + '\n')
    output_file.close()

def saveTotals(totEmp, totHours, totGross):
    output_file = open('Payroll.txt', 'a')
    output_file.write('------------------------------------' + '\n')
    output_file.write(convertString('Total number of Employees: ', totEmp))
    output_file.write(convertString('Total number of hours worked: ', totHours))
    output_file.write(convertString('Total Gross Pay: $', format(totGross, ',.2f')))
    output_file.write('------------------------------------' + '\n')
    output_file.close()

def backupFile():
    input = open('Payroll.txt', 'r')
    contents = input.read()
    input.close()
    output = open('Payroll Backup.txt', 'w')
    output.write(contents)
    output.close()

def convertString(var1, var2):
    var = str(var1) + str(var2) + '\n'
    return var

main()
