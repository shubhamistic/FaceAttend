import pandas as pd


def createExcel(date, data):
    # Convert the array to a DataFrame
    data = [('Registration Number', 'Student Name', 'Department', 'Email', 'Date', 'Status', 'Reporting Time')] + data
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    df.to_excel("Excel/" + date + ".xlsx", index=False, header=False)
