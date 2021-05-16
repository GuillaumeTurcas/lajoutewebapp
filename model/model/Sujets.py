from model.config.config import mydb as mysql

class Sujets:

    def registSujets(sujet):
        cursor = mysql.cursor()
        cursor.execute(""" INSERT INTO sujets 
            (sujet, type)
            VALUES (%s,%s)""",
            (sujet[0], sujet[1],))
        
        mysql.commit()

        return True
            

    def getSujet(_id):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM sujets 
            WHERE id = %s""", (_id,))

        sujet = cursor.fetchall()

        return sujet[0]


    def getSujets(sujet):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM sujets 
            WHERE type = %s 
            ORDER BY sujet""", (sujet,))

        sujets = cursor.fetchall()
        
        return sujets


    def updateSujet(_id, sujet):
        cur = mysql.cursor()
        cur.execute("""UPDATE sujets SET 
            sujet = %s, type = %s
            WHERE id = %s""", 
            (sujet[0], sujet[1], _id,))
        
        mysql.commit()

        return True


    def delSujet(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM sujets 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
