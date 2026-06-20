from fastapi import FastAPI
import sqlite3
import uvicorn
from typing import Optional
import re

app = FastAPI()

@app.get("/check")
def check_call(number: Optional[str] = None):
    if not number:
        print("[!] Warning: Received request with empty number.")
        return {"status": "NORMAL"}
    
    # Numbers (\d) mattum extract pannuvom - Enna space, special character irundhalum gaali!
    raw_clean = "".join(re.findall(r'\d+', number))
    
    # Prefix-la plain 91 irundha mattum strip pannuvom
    clean_num = re.sub(r'^91', '', raw_clean)
    
    print(f"[*] Incoming raw data: '{number}' -> Cleaned String: '{raw_clean}' -> Filtered Number: '{clean_num}'")
    
    try:
        conn = sqlite3.connect('sentinel_contacts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM priority_list WHERE phone=?", (clean_num,))
        result = cursor.fetchone()
        conn.close()
    except Exception as e:
        print(f"[!] Database Error: {e}")
        return {"status": "NORMAL"}

    if result:
        print(f"[+] Match Found! VIP: {result[0]}")
        return {"status": "VIP", "name": result[0]}
    
    print("[-] Status: NORMAL Contact")
    return {"status": "NORMAL"}

if __name__ == "__main__":
    print("[*] Launching Sentinel Gatekeeper Server...")
    uvicorn.run(app, host="0.0.0.0", port=8001)