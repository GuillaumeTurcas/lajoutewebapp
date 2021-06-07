from backend.init.config import mydb as mysql

class Cours: 

    def registCours(cours):
        cursor = mysql.cursor()
        cursor.execute("""INSERT INTO cours 
            (titre, datedb, start, end, lien, color) 
            VALUES (%s, %s,%s, %s, %s, %s)""",
            (cours[0], cours[1],
            cours[2], cours[3], 
            cours[4], cours[5],))

        mysql.commit()
        
        return True


    def getCours():
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM cours
            ORDER BY datedb""")

        cours = cursor.fetchall()

        return cours


    def delCours(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM cours 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
