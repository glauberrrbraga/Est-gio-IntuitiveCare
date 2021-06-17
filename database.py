import psycopg2
from psycopg2 import Error
import pandas as pd


try:
    connection = psycopg2.connect(user="postgres",
                                  password="846222",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="estagio")
    cursor = connection.cursor()

    df = pd.read_csv('aquivo.csv', error_bad_lines=False)       
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO HumanResources.DepartmentTest (DepartmentID,Name,GroupName) values(?,?,?)", row.DepartmentID, row.Name, row.GroupName)
        connection.commit()
        cursor.close()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")