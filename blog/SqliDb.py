import sqlite3
import os

class SqliDb():

    dbPath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/sqlite/blog.db"

    def query(self, sql, arrParam=None):
        conn=None
        try:
            conn = sqlite3.connect(self.dbPath)
            cur = conn.cursor()
            if arrParam==None or len(arrParam)==0:
                cursorRows=cur.execute(sql)
            else:
                cursorRows=cur.execute(sql,arrParam)
            rows=[]
            for cursorRow in cursorRows:
                row={}
                index=0
                for item in cursorRows.description:
                    row[item[0]]=cursorRow[index]
                    index=index+1
                rows.append(row)
        except Exception as err:
            print(err.args)
            ret={'err':err.args}
        else:
            #print(len(rows))
            ret={'rows':rows}
        if not conn is None:
            conn.close()
        return ret

    def exec(self, sql, arrParam=None):
        conn=None
        try:
            conn = sqlite3.connect(self.dbPath)
            cur = conn.cursor()
            if arrParam==None or len(arrParam)==0:
                cur.execute(sql)
            else:
                cur.execute(sql,arrParam)
            conn.commit()
            ret={ 'lastrowid':cur.lastrowid, 'rowcount':cur.rowcount }
        except Exception as err:
            print(err.args)
            ret={'err':err.args}
        if not conn is None:
            conn.close()
        return ret



