import requests
import json
import sys

def get_seed():
    """Prompts for student key and computes the integer seed."""
    while True:
        student_key = input("Student key: ").strip()
        if student_key:
            return sum(ord(ch) for ch in student_key)
        print("Error: Student key cannot be empty.")

def main():
    # Part A: Inventory Entry
    # Step 1: Student Key
    seed = get_seed()

    # Step 4: Threshold Logic
    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9

    total_skus = 0
    reorder_count = 0

    # Step 2 & 3: SKU Entry Loop
    while True:
        sku = input("\nSKU (or 'DONE'): ").strip()
        if sku.upper() == "DONE":
            break
        if not sku:
            print("Error: SKU cannot be blank.")
            continue

        # On-hand validation
        while True:
            try:
                on_hand = int(input(f"On hand for {sku}: "))
                if on_hand >= 0:
                    break
                print("Error: Quantity must be 0 or greater.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        # Step 5: Reorder Decision
        total_skus += 1
        if on_hand < threshold:
            reorder_count += 1
            print(f"Status for {sku}: REORDER")
        else:
            print(f"Status for {sku}: OK")

    # Part B: API Spot Check
    # Step 6: Select Term
    search_term = "weezer" if seed % 2 == 0 else "drake"
    
    api_status = "OK"
    songs_returned = "N/A"
    
    # Step 7 & 8: API Request and Exception Handling
    try:
        params = {
            "entity": "song",
            "limit": 5,
            "term": search_term
        }
        response = requests.get("https://itunes.apple.com/search", params=params, timeout=10)
        response.raise_for_status() # Raises exception for 4xx/5xx errors
        
        # Step 9: JSON Processing
        try:
            data = response.json()
            if "results" in data:
                song_list = [item for item in data["results"] if item.get("kind") == "song"]
                songs_returned = len(song_list)
            else:
                api_status = "INVALID_RESPONSE"
        except (ValueError, KeyError):
            api_status = "INVALID_RESPONSE"

    except (requests.RequestException):
        api_status = "FAILED"

    # Step 10: Output Format
    print("\n" + "-"*30)
    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {search_term}")
    print(f"Songs returned: {songs_returned}")
    print(f"API status: {api_status}")
    print("-"*30)

main()