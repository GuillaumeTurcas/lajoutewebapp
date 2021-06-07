from backend.init.config import mydb as mysql

class Infos: 

    def registInfos(info):
        cursor = mysql.cursor()
        cursor.execute(""" INSERT INTO infos 
            (datedb, description) 
            VALUES (%s, %s)""",
            (info[0], info[1],))

        mysql.commit()

        return True


    def getInfos():
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM infos
            ORDER BY datedb""")

        infos = cursor.fetchall()

        return infos


    def delInfos(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM infos 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
