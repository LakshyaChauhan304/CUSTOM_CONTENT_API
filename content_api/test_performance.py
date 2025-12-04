import requests
import time
import random
import string

BASE_URL = "http://127.0.0.1:8000/content"

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_performance():
    print("Starting Performance Test...")
    print("-" * 30)

    username = f"perf_user_{generate_random_string(5)}"
    password = "password123"
    email = f"{username}@example.com"

    # 1. Register
    start_time = time.time()
    resp = requests.post(f"{BASE_URL}/register/", json={
        "username": username,
        "password": password,
        "email": email,
        "first_name": "Perf",
        "last_name": "Test"
    })
    duration = time.time() - start_time
    print(f"Register: {duration:.4f}s - Status: {resp.status_code}")

    # 2. Login
    start_time = time.time()
    resp = requests.post(f"{BASE_URL}/api/login/", json={
        "username": username,
        "password": password
    })
    duration = time.time() - start_time
    print(f"Login:    {duration:.4f}s - Status: {resp.status_code}")
    
    if resp.status_code != 200:
        print("Login failed, aborting.")
        return

    token = resp.json().get("token")
    headers = {"Authorization": f"Token {token}"}

    # 3. Create Item
    start_time = time.time()
    resp = requests.post(f"{BASE_URL}/api/items/", headers=headers, json={
        "title": "Performance Test Item",
        "body": "This is a test item for performance benchmarking."
    })
    duration = time.time() - start_time
    print(f"Create:   {duration:.4f}s - Status: {resp.status_code}")
    
    item_id = resp.json().get("id")

    # 4. Get Items
    start_time = time.time()
    resp = requests.get(f"{BASE_URL}/api/items/", headers=headers)
    duration = time.time() - start_time
    print(f"List:     {duration:.4f}s - Status: {resp.status_code}")

    # 5. Delete Item
    if item_id:
        start_time = time.time()
        resp = requests.delete(f"{BASE_URL}/api/items/{item_id}/", headers=headers)
        duration = time.time() - start_time
        print(f"Delete:   {duration:.4f}s - Status: {resp.status_code}")

    print("-" * 30)
    print("Test Complete.")

if __name__ == "__main__":
    test_performance()
