import sqlite3

def init_db():
    conn = sqlite3.connect('sentinel_contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS priority_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
    print("Database Initialized!")

def add_vip(name, phone):
    try:
        conn = sqlite3.connect('sentinel_contacts.db')
        cursor = conn.cursor()
        # Cleaning the number before saving
        clean_phone = phone.replace(" ", "").replace("+91", "")
        cursor.execute("INSERT INTO priority_list (name, phone) VALUES (?, ?)", (name, clean_phone))
        conn.commit()
        conn.close()
        print(f"Success: {name} ({clean_phone}) added to Sentinel Vault.")
    except sqlite3.IntegrityError:
        print(f"Info: Number {phone} is already in the VIP list.")

if __name__ == "__main__":
    init_db()
    # Adding your specific number here
    add_vip("Primary Priority Contact", "8778720748")