import psycopg2

connection =psycopg2.connect(
    host ="localhost",
    database="gear5_tasks",
    user="postgres",
    password = "buru@god"
)

cursor = connection.cursor()