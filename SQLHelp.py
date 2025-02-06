import sqlite3

class sqH:
    file = 'dbase.db'
    conn = None
    c = None

    def getVersion(self):
        query = "select sqlite_version();"
        self.c.execute(query)
        result = self.c.fetchall()
        return result
    
    def getDatabases(self):
        query = "select * from ;"
        self.c.execute(query)
        result = self.c.fetchall()
        #print(type(result))
        #print(result)
        return None        
    
    def createTable(self,name,data):
        if type(data) != dict or type(name) != str:
            return None
        query = 'Create table ' + name +'( id integer primary key autoincrement '
        for k in data:
            query += f", {k} {data[k]}"
        query += ");"
        print(query)
        try:
            self.c.execute(query)
            print('table created successfully')
        except Exception as e:
            print(e)
    
    def dropTable(self,name):
        query = f"drop table {name};"
        print(query)
        try:
            self.c.execute(query)
            self.conn.commit()
            print("table successfully deleted")
        except Exception as e:
            print(e)

    def listTables(self):
        # Retrieves a list of tables from your current database
        # returns data as a list
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        result = self.c.fetchall()
        tables = []
        for i in result:
            tables.append(i[0])
        #print("Tables\n======")
        #for i in result:
        #    print(i[1])
        return tables

    def getTableStructure(self,table):
        self.c.execute(f'PRAGMA table_info({table});')
        result = self.c.fetchall()
        #for i in result:
        #    print(i)
        return result

    def insert(self,table,vals):
        keys = ""
        values = ""
        fields = self.getTableStructure(table)
        for i in range(1,len(fields)):
            keys += f"{fields[i][1]},"
            #print(fields[i][1])
        for k in vals:
            if type(k) == str:
                values += f"'{k}',"
            else:
                values += f"{k},"
        keys = keys[0:-1]
        values = values[0:-1]
        query = f"insert into {table} ({keys}) values ({values});"
        #print(query)
        self.c.execute(query)
        self.conn.commit()

    def __init__(self,file):
        self.file = file
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()
        print( self.getVersion() )
        


x = sqH('dbase.db')

"""
Example: Create table with structure defined in dbase
tableStruct is the structure of the table
tableName is the name of the table
tableName = 't3'
tableStruct = {"name":"text","age":"int","stnumber" : "int", "email":"text","grade":"int"}
x.createTable(tableName,tableStruct)
"""

tables = x.listTables()
print(tables)
#x.insert('t3',["Benjamin",8,1234,'benjamin@gmail.com',12])

#self.dropTable('t3')
#self.listTables()

