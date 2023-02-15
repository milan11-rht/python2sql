import mysql.connector

def connectdatabase(user,password,databasename):
    conn = mysql.connector.connect(
        host="localhost",
        user="{}".format(user),
        password="{}".format(password)

    )

    print("Connection Established!!!!")
    conn.close()
    conn = mysql.connector.connect(
        host="localhost",
        user="{}".format(user),
        password="{}".format(password),
        database='{}'.format(databasename)

    )
    curs = conn.cursor()

    return curs,conn

def create_tables(cur):
    cur.execute("CREATE TABLE abc(name VARCHAR(255),user_name VARCHAR(255))")
    cur.execute("CREATE TABLE AccountsCountry (Code VARCHAR(255),Long_Name VARCHAR(255),Currency_Unit VARCHAR(255),Short_Name VARCHAR(255),Table_Name VARCHAR(255))")


def drop_tables(cur):
    cur.execute("DROP TABLE abc")
    cur.execute("CREATE TABLE AccountsCountry")


def list_all_tables(cur):

    cur.execute("SHOW TABLES")
    for i in cur:
        print(i[0])

def user_interaction():
    print("*****************WELCOME TO DB USER INTERFACE*********************")
    user=str(input("ENTER USER NAME :"))
    password=str(input("ENTER PASSWORD :"))
    databasename=str(input("ENTER DATABASE NAME TO CONNECT :"))
    cur, con = connectdatabase(user, password, databasename)
    #list_all_tables(cur,"SHOW TABLES")
    print("*****************ENTER CHOICE OF ACTION*********************")
    choice=int(input("LIST ALL TABLES -> press 1: "))
    if choice==1:
        list_all_tables(cur)

user_interaction()


