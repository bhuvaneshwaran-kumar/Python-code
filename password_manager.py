import sqlite3
import os
from getpass import getpass

class App:
    def __init__(self):
        self.conn = sqlite3.connect('my_pass_db.db')
        self.cursor = self.conn.cursor()
        # run this code only once to create the table
        # self.cursor.execute("create table passwords(service text primary key,pass text not null)")
        # print("table created")

    def closeConnection(self):
        self.conn.commit()
        self.conn.close()

    def addPassword(self):
        service = input("Enter the service: ")
        password = input("Enter the password: ")
        if service!='' and password!='':
            try:
                self.cursor.execute('insert into passwords values(?,?)',(service,password))
            except Exception as ex :
                print(ex)
            else:
                print("succes!")
                self.conn.commit()
        else:
            print("service or password is invalid")

    def viewPassword(self):
        service = input("Enter the service you want to fetch :")
        if service!='':
            try:
                result = self.cursor.execute('select * from passwords where service = ?',(service,))
            except Exception as ex :
                print(ex)
            else:
                data = result.fetchone()
                print(f'{data[0]} ---> {data[1]}')
        else:
            print("service or password is invalid")

    def viewAllServices(self):
        try:
            result = self.cursor.execute('select service from passwords')
        except Exception as ex :
            print(ex)
        else:
            data = result.fetchall()
            for service in data:
                print(service[0])

    def updatePassword(self):
        service = input("Enter the service you want to change :")
        newPassword = input("Enter the new Password: ")
        try:
            result = self.cursor.execute('update passwords set pass=? where service=?',(newPassword,service))
        except Exception as ex :
            print(ex)
        else:
            # row count retuns the no of rows the query has affected
            print("updated password for ",result.rowcount," row")
            self.conn.commit()
            


if __name__ == "__main__":
    # for key,value in os.environ.items():
    #     print(key,"---->",value)
    # print("master: ",masterpass)

    masterpass = os.environ['MY_PASS']      # gets the value from our environment variables
    password_Master = getpass("Enter Master password: ")

    if(masterpass == password_Master):
        myApp = App()
        print("1. add  2.view  3.viewServices  4.updatePassword  5.Exit ")
        print("------------------------------------------------")
        while True:
            choice = input("Enter you choice: ")
            if choice=='1':
                myApp.addPassword()
            elif choice=='2':
                myApp.viewPassword()
            elif choice=='3':
                myApp.viewAllServices()
            elif choice=='4':
                myApp.updatePassword()
            else:
                myApp.closeConnection()
                break
            print("------------------------------------------------")
    else:
        print("Master password in wrong!")