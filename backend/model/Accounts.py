from backend.init.config import mydb as mysql

class Accounts: 

    def registAccount(account):
        cursor = mysql.cursor()
        cursor.execute(""" INSERT INTO accounts 
            (username, password, 
            email, admin, present, 
            nom, prenom, ecole, annee, 
            phone, specialite, theme, token) 
            VALUES (%s,%s, %s, %s, 0, %s, 
            %s, %s, %s, %s, %s, 'light', %s)""",
            (account[0], account[1], 
            account[2], account[3], 
            account[4], account[5], 
            account[6], account[7], 
            account[8], account[9],
            account[10]))

        mysql.commit()

        return True


    def logAccount(username, password):
        try: 
            cursor = mysql.cursor()
            cursor.execute("""SELECT * FROM accounts 
                WHERE username = %s AND password = %s""", 
                (username, password,))
            
            logAccount = cursor.fetchall()

            return logAccount[0]

        except:
            return False


    def getAccount(_id):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM accounts 
            WHERE id = %s""", (_id,))
        
        account = cursor.fetchall()

        return account[0]


    def getAccounts():
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM accounts
            ORDER BY nom""")

        account = cursor.fetchall()

        return account

    
    def getAccountToken(token):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM accounts
            WHERE token = %s""",
            (token))
        
        account = cursor.fetchall()

        return account


    def getToken(username):
        cursor = mysql.cursor()
        cursor.execute("""SELECT * FROM accounts
            WHERE username = %s""", (username,))
        
        account = cursor.fetchall()

        return account[0][13]


    def verifAccount(username):
        try:
            cursor = mysql.cursor()
            cursor.execute("""SELECT * FROM accounts 
                WHERE username = %s""", (username,))

            account = cursor.fetchall()

            return account[0]

        except:
            return False


    def updateAccount(account):
        cur = mysql.cursor()
        cur.execute("""UPDATE accounts SET 
            username = %s, password = %s, 
            email = %s, admin = %s, 
            present = %s, nom = %s, 
            prenom = %s, ecole = %s, 
            annee = %s, phone = %s, 
            specialite = %s, theme = %s 
            WHERE id = %s""", 
            (account[1], account[2], 
            account[3], account[4], 
            account[5], account[6],
            account[7], account[8], 
            account[9], account[10], 
            account[11], account[12],
            account[0],))

        mysql.commit()

        return True


    def updatePassword(password, username):
        cur = mysql.cursor()
        cur.execute("""UPDATE accounts SET 
            password = %s WHERE username = %s""", 
            (password, username,))

        mysql.commit()

        return True


    def presentAccount(_id):
        cursor = mysql.cursor()
        cursor.execute("""UPDATE accounts 
            SET present = %s 
            WHERE id =%s""", 
            (True, _id))

        mysql.commit()

        return True


    def presentAccounts():
        cursor = mysql.cursor()
        cursor.execute("""UPDATE accounts 
            SET present = %s""", 
            (False,))

        mysql.commit()

        return True


    def delAccount(_id):
        cur = mysql.cursor()
        cur.execute("""DELETE FROM accounts 
            WHERE id = %s""", (_id,))

        mysql.commit()

        return True
