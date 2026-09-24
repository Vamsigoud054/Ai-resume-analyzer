import os
import mysql.connector


def get_database_connection():

    connection = mysql.connector.connect(
        host=os.getenv(
            "DB_HOST",
            "localhost"
        ),
        user=os.getenv(
            "DB_USER",
            "root"
        ),
        password=os.getenv(
            "DB_PASSWORD",
            ""
        ),
        database=os.getenv(
            "DB_NAME",
            "resume_analyzer"
        )
    )

    return connection