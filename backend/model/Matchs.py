from backend.init.config import mydb as mysql

class Matchs: 

    def registMatchs(match):
        cursor = mysql.cursor()
        cursor.execute(""" INSERT INTO matchs 
            (datedb, type, sujet, equipe, 
            gouvernement, opposition, 
            meilorateur, meilequipe, jury) 
            VALUES 
            (%s,%s, %s, %s, %s, %s, %s, %s, %s)""",
            (match[0], match[1], 
            match[2], match[3], 
            match[4], match[5], 
            match[6], match[7], 
            match[8]))

        mysql.commit()

        return True


    def getMatch(_id):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM matchs 
            WHERE id = %s""", (_id,))
        
        match = cursor.fetchall()

        return match[0]


    def getMatchs(_type):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM matchs
            WHERE type = %s
            ORDER BY datedb""", (_type,))

        matchs = cursor.fetchall()

        return matchs


    def updateMatchs(_id, match):
        cur = mysql.cursor()
        cur.execute("""UPDATE matchs SET 
            datedb = %s, type = %s, sujet = %s, 
            equipe = %s, gouvernement = %s, 
            opposition = %s, meilorateur = %s, 
            meilequipe = %s, jury = %s 
            WHERE id = %s""", 
            (match[0], match[1], 
            match[2], match[3],
            match[4], match[5],
            match[6], match[7],
            match[8], _id))

        mysql.commit()

        return True


    def delMatchs(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM matchs 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
