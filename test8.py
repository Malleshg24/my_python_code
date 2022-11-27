import csv
#stored procedure gives output 20 Columns andd 16 rows of records.
def Stored_Procedure(tbl,database,conn):
    cursor = conn.cursor()
    sql = "[DB_Main].[Stored_Procedure] ?,?"
    params = (tbl,database)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    header = next(zip(*cursor.description))
    return header,result


def main():
    tbl = "Table1"
    database = "database1"
    conn = "conn_obj"
    header,result = Stored_Procedure(tbl, database, conn)

    for idx,row in result:
        info = dict(zip(header,result))

    with open("abc.csv","w",newline="") as output:
        writer = csv.writer(outfile,delimeter="|")
        writer.rows(col[0],for col in cursor.description)
        while True:
            rows = cursor.fetchmany(10000)
            if len(rows) ==0:
                break
            else:
                for row in rows:
                    writer.writerow(row)

if __name__ == '__main__':
    main()

