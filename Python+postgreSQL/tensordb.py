import psycopg2
from pprint import pprint

class dbConnection():
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
            "dbname='tensordb' user='postgres' host='localhost' port='5432' ")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to db")

    def create_table(self):
        create_table_command="CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)

    def insert_new_record(self):
        new_record = ("Koti", "13")
        insert_command = "INSERT INTO pet(name, age) VALUES('" + new_record[0] + "','" + new_record[1] + "')"
        #pprint(insert_command)
        self.cursor.execute(insert_command)

    def size_table(self):
        size_table_command = "SELECT pg_size_pretty(pg_total_relation_size('pet'));"
        #pprint(size_table_command)
        self.cursor.execute(size_table_command)
        for row in self.cursor:
            return row

    def size_table2(self):
        size_table_command = "SELECT pg_size_pretty(pg_total_relation_size('people'));"
        #pprint(size_table_command)
        self.cursor.execute(size_table_command)
        for row in self.cursor:
            return row

    def drop_table(self):
        drop_table_command = "DROP TABLE test"
        self.cursor.execute(drop_table_command)

def main():
    database_con = dbConnection()

if __name__ == "__main__":
    main()
