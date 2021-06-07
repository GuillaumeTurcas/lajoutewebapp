from backend.init.config import mydb as mysql

def name(typeconf):

    unique = []

    cur = mysql.cursor()
    cur.execute("""SELECT * FROM config 
        WHERE type = %s ORDER BY value""", (typeconf,))
    config = cur.fetchall()

    for conf in config:
        name = str(conf[2]) 
        unique.append(name) if name not in unique else 0

    return unique
