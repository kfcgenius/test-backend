import os
import random
import string

import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db_connection():
    return mysql.connector.connect(
        host=os.environ["BACKEND_DB_HOST"],
        user=os.environ["BACKEND_DB_USER"],
        password=os.environ["BACKEND_DB_PASSWORD"],
        database=os.environ["BACKEND_DB_NAME"],
    )


@app.get("/strings/random")
def generate_random_string():
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS strings (id INT AUTO_INCREMENT PRIMARY KEY, value VARCHAR(255))"
    )
    cursor.execute("INSERT INTO strings (value) VALUES (%s)", (random_string,))
    db.commit()
    cursor.close()
    db.close()

    return {"random_string": random_string}
