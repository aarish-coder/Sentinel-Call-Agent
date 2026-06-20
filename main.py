import sqlite3
import pyttsx3

def start_audio_alert(caller_name):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)
    
    alert_text = f"Warning! Priority call from {caller_name}. I repeat, priority call from {caller_name}."
    
    for _ in range(3): # 3 times repeat pannum
        engine.say(alert_text)
        engine.runAndWait()

def check_and_override(incoming_number):
    # Data Cleaning: +91 or spaces irundha remove pannuvom
    incoming_number = incoming_number.replace("+91", "").replace(" ", "")
    
    conn = sqlite3.connect('sentinel_contacts.db')
    cursor = conn.cursor()
    
    # SQL query to find the match
    cursor.execute("SELECT name FROM priority_list WHERE phone=?", (incoming_number,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"!!! PRIORITY MATCH: {result[0]} is calling !!!")
        start_audio_alert(result[0])
    else:
        print(f"Call from {incoming_number} - Not a priority. Status: Silent.")

if __name__ == "__main__":
    # Testing with your specific number
    test_call = "8778720748" 
    check_and_override(test_call)