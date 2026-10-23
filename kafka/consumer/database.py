import pyodbc
import dotenv
import os

dotenv.load_dotenv()

SERVER = os.getenv("SQL_SERVER")
DATABASE = os.getenv("SQL_DATABASE")
USERNAME = os.getenv("SQL_USERNAME")
PASSWORD = os.getenv("SQL_PASSWORD")


connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER=tcp:{SERVER},1433;"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Authentication=SqlPassword;"
    "Connection Timeout=30;"
)

conn = None
cursor = None


def get_connection():
    global conn, cursor

    try:
        if conn is None:
            print("Connecting to Azure SQL...")
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            print("Connected to Azure SQL!")

        return conn, cursor

    except Exception as e:
        print("Connection Error:", e)
        conn = None
        cursor = None
        raise


def insert_prediction(transaction, prediction, probability):
    global conn, cursor

    try:
        conn, cursor = get_connection()

        cursor.execute(
            """
            INSERT INTO fraud_predictions
            (
                trans_num,
                merchant,
                category,
                amt,
                prediction,
                fraud_probability
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                transaction["trans_num"],
                transaction["merchant"],
                transaction["category"],
                float(transaction["amt"]),
                int(prediction),
                float(probability),
            ),
        )

        conn.commit()

        print("Inserted into Azure SQL")

    except pyodbc.OperationalError:
        print("Connection lost. Reconnecting...")

        try:
            if cursor:
                cursor.close()
        except:
            pass

        try:
            if conn:
                conn.close()
        except:
            pass

        conn = None
        cursor = None

        conn, cursor = get_connection()

        cursor.execute(
            """
            INSERT INTO fraud_predictions
            (
                trans_num,
                merchant,
                category,
                amt,
                prediction,
                fraud_probability
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                transaction["trans_num"],
                transaction["merchant"],
                transaction["category"],
                float(transaction["amt"]),
                int(prediction),
                float(probability),
            ),
        )

        conn.commit()

        print("Inserted after reconnect")


def close_connection():
    global conn, cursor

    try:
        if cursor:
            cursor.close()

        if conn:
            conn.close()

        print("Azure SQL connection closed.")

    except:
        pass