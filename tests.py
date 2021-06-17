import pandas as pd


data = pd.read_csv(r'relatorio.csv', error_bad_lines=False)   
df = pd.DataFrame(data)
print(df)

 df = pd.read_csv('aquivo.csv', error_bad_lines=False)   
    # df = pd.DataFrame(data)
    
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
        connection.commit()
        cursor.close()
