import mysql.connector
class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="https://web.tecnica4berazategui.edu.ar/phpmyadmin/index.php?route=/sql&pos=0&db=lperconti_g1&table=estudiantes",
            user="lperconti_g1",
            password="Syssen23",
            database="lperconti_g1"
            #host="localhost",
            #user="root",
            #password="",
            #database="colegio"
        )
        self.cursor=self.connection.cursor()