from flask import Flask
import mysql.connector
import redis

app = Flask(__name__)

# إعداد الاتصال بـ MySQL
def get_mysql_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="password",
        database="flask_db"
    )

# إعداد الاتصال بـ Redis
def get_redis_connection():
    return redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/mysql')
def mysql_test():
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0]

@app.route('/redis')
def redis_test():
    redis_client = get_redis_connection()
    redis_client.set('hello', 'Hello from Redis!')
    return redis_client.get('hello').decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
