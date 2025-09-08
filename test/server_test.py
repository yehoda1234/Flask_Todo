import requests
import time
import sys
import re

def test_flask_app():
    time.sleep(20)
    created_task_ids = []

    try:
        # בדיקה 1: דף הבית
        home_response = requests.get("http://flask_app:5001/")
        if home_response.status_code != 200:
            print("❌ דף הבית לא החזיר 200")
            return False

        # בדיקה 2: הוספת משימה ראשונה
        url = "http://flask_app:5001/add"
        data = {"title": "new task"}
        requests.post(url, data=data)

        home_response = requests.get("http://flask_app:5001/")
        task_matches = re.findall(r'(\d+) \| new task', home_response.text)
        if task_matches:
            created_task_ids.append(int(task_matches[0]))

        # בדיקה 3: הוספת משימה שנייה
        data2 = {"title": "second task"}
        requests.post(url, data=data2)

        home_response = requests.get("http://flask_app:5001/")
        task_matches = re.findall(r'(\d+) \| second task', home_response.text)
        if task_matches:
            created_task_ids.append(int(task_matches[0]))

        # בדיקה 4: מחיקת כל המשימות
        for task_id in created_task_ids:
            delete_url = f"http://flask_app:5001/delete/{task_id}"
            delete_response = requests.get(delete_url)
            if delete_response.status_code != 200:
                print(f"❌ מחיקה נכשלה עבור משימה {task_id}")
                return False

        # בדיקה סופית: לוודא שנמחק
        final_response = requests.get("http://flask_app:5001/")
        for task_id in created_task_ids:
            if f"{task_id} |" in final_response.text:
                print(f"❌ המשימה {task_id} עדיין קיימת")
                return False

        print("✅ כל הטסטים עברו בהצלחה!")
        return True

    except Exception as e:
        print(f"❌ חריגה בטסט: {e}")
        return False


if __name__ == "__main__":
    success = test_flask_app()
    sys.exit(0 if success else 1)
