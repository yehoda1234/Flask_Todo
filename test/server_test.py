import requests
import time

def test_flask_app():
    print("ממתין לשרת Flask...")
    time.sleep(20)  # זמן סביר יותר
    
    try:
        # בדיקה 1: דף הבית
        print("בודק דף הבית...")
        home_response = requests.get("http://flask_app:5000/")
        print(f"דף הבית: {home_response.status_code}")
        
        # בדיקה 2: הוספת משימה
        print("מוסיף משימה...")
        url = "http://flask_app:5000/add"
        data = {"title": "משימה חדשה"}
        response = requests.post(url, data=data)
        print(f"הוספת משימה: {response.status_code}")
        
        # בדיקה 3: משימה שנייה
        data2 = {"title": "משימה חדשה מהלקוח"}
        response2 = requests.post(url, data=data2)
        print(f"משימה שנייה: {response2.status_code}")
        
        print("✅ הטסטים הושלמו!")
        
    except Exception as e:
        print(f"❌ שגיאה בטסט: {e}")

if __name__ == "__main__":
    test_flask_app()