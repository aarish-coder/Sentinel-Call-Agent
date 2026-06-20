# Sentinel Call Agent 🛡️📞

An automated backend-driven emergency call router that bypasses Android's silent mode for critical (VIP) contacts.

## How It Works
1. **Trigger:** MacroDroid captures an incoming call on the device.
2. **Gateway Check:** Sends a fast HTTP GET request to the local FastAPI server.
3. **Regex & DB Lookup:** The Python backend filters the number using robust Regex prefixes and queries an SQLite database.
4. **Action:** If matched as `VIP`, the server replies instantly, prompting the mobile client to override device volume to 100%.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Database:** SQLite3
* **Automation:** MacroDroid (Android)
* **Regex Optimization:** Handles country code prefixes (`+91`, `91`) seamlessly.
