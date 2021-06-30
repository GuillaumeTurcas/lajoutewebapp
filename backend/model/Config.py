from backend.init.config import mydb as mysql

class Config: 

    def registConfig(config):
        cursor = mysql.cursor()
        cursor.execute(""" INSERT INTO config 
            (type, name, value, description) 
            VALUES (%s,%s, %s, %s)""",
            (config[0], config[1], 
            config[2], config[3],))
        
        mysql.commit()

        return True


    def getConfig(_id):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM config 
            WHERE id = %s""", (_id,))
        
        config = cursor.fetchall()

        return config[0]


    def getConfigs(name, typeconf):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM config
            WHERE name = %s AND type = %s
            ORDER BY value""",
            (name, typeconf,))

        configs = cursor.fetchall()

        return configs


    def updateConfig(_id, config):
        cur = mysql.cursor()
        cur.execute("""UPDATE config SET 
            type = %s, name = %s, 
            value = %s, description = %s 
            WHERE id = %s""",
            (config[0], config[1], 
            config[2], config[3], _id,))

        mysql.commit()

        return True


    def delConfig(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM config 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
