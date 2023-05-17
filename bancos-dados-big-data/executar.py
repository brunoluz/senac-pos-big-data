import mysql.connector
import pandas as pd



mysql_host = 'localhost'
mysql_user = 'root'
mysql_pass = 'xpto'
mysql_database = 'senac'

def exist(database, table):
    mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass)
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        if x[0] == database:
            if table != "":
                mydb1 = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass)
                mycursor1 = mydb1.cursor()
                mycursor1.execute("USE " + database)
                mycursor1 = mydb1.cursor()
                mycursor1.execute("SHOW TABLES")
                for y in mycursor1:
                    if y[0] == table:
                        return True
            else:
                return True
    return False


mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass)
if not exist(mysql_database, ""):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE senac")

mydb = mysql.connector.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass, database=mysql_database) 
if not exist(mysql_database, "disciplina"):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE disciplina (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), ch INT, cp INT, cr INT)")

if not exist(mysql_database, "docente"):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE docente (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(50) NOT NULL, celular VARCHAR(20) NOT NULL)")


data_disciplina = pd.read_csv('disciplina.csv', sep=';',  encoding='latin-1')
mysql_insert_query_disciplina = 'INSERT INTO disciplina (nome, ch, cp, cr) VALUES (%s, %s, %s, %s)'
disciplina = data_disciplina[['NOME','CH','CP','CR']]
disciplina = disciplina.values.tolist()
mycursor = mydb.cursor()
mycursor.executemany(mysql_insert_query_disciplina, disciplina)
mydb.commit()



data_disciplina_docente = pd.read_csv('disciplina_docente.csv', sep=',',  encoding='latin-1')
docentes_duplicados = data_disciplina_docente[['DOCENTE', 'E-MAIL', 'TELEFONE']]
docentes_unicos = docentes_duplicados.drop_duplicates()

mysql_insert_query_doscente = 'INSERT INTO docente (nome, email, celular) VALUES (%s, %s, %s)'
doscentes = docentes_unicos[['DOCENTE', 'E-MAIL', 'TELEFONE']]
doscentes = doscentes.values.tolist()
mycursor = mydb.cursor()
mycursor.executemany(mysql_insert_query_doscente, doscentes)
mydb.commit()