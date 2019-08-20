import os
import psycopg2
import psycopg2 as error
from database import Postgres

DATABASE_URL = os.environ.get('DATABASE_URL')

def create_tables(Postgres):
    """ create tables in the nbox database"""
    tables = (
        """
        CREATE TABLE user (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE work (
                work_id SERIAL PRIMARY KEY,
                work_name VARCHAR(255) NOT NULL
                ),
        """)

    try:
        connection = psycopg2.connect('DATABASE_URL')
        cursor = connection.cursor()

        for table in tables:
            cursor .execute(table)
        cursor.close()

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


