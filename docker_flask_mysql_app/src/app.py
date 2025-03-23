from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
        )
        return "Conexión a la base de datos exitosa. Hola Mundo!"
    except Exception as e:
        return f"Error conectando a la base de datos: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
