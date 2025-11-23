from db import get_conn

def add_entry():
    site = input("Site: ")
    username = input("Username: ")
    password = input("Password: ")

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
                (site, username, password))
    conn.commit()
    conn.close()

    print("✔ Entry added!\n")


def list_entries():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords")
    rows = cur.fetchall()
    conn.close()

    print("\n--- Saved Passwords ---")
    for r in rows:
        print(f"[{r[0]}] {r[1]} | {r[2]} | {r[3]}")
    print()


def delete_entry():
    entry_id = input("Enter ID to delete: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM passwords WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

    print("✔ Entry deleted!\n")
