import requests
from src.db import connect_database

def insert_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()

    conn = connect_database()
    cursor = conn.cursor()

    for user in users:
        company = user["company"]
        cursor.execute("INSERT INTO companies (name, catch_phrase, bs) VALUES (%s, %s, %s)",
                       (company["name"], company["catchPhrase"], company["bs"]))
        company_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO users (name, username, email, phone, website, company_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user["name"], user["username"], user["email"], user["phone"], user["website"], company_id))

    conn.commit()
    cursor.close()
    conn.close()
    print("Usuários inseridos com sucesso!")

if __name__ == "__main__":
    insert_data()
