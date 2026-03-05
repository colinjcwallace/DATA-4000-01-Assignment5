import sys

def get_seed():
    """Prompts for student key and computes the integer seed."""
    while True:
        student_key = input("Student key: ").strip()
        if student_key:
            return sum(ord(ch) for ch in student_key)
        print("Error: Student key cannot be empty.")

def get_valid_input(prompt, type_func, condition_func, error_msg):
    """Generic helper to handle try/except validation loops."""
    while True:
        try:
            value = type_func(input(prompt).strip())
            if condition_func(value):
                return value
            else:
                print(error_msg)
        except ValueError:
            print(f"Invalid input. Please enter a valid {type_func.__name__}.")

def main():
    seed = get_seed()

    subtotal = 0.0
    total_units = 0

    print("\n--- POS System Started (Type 'DONE' for item name to exit) ---")

    while True:
        item_name = input("\nItem name: ").strip()
        
        if item_name.upper() == "DONE":
            break
        
        if not item_name:
            print("Error: Item name cannot be empty.")
            continue

        price = get_valid_input(
            "Unit price: ", 
            float, 
            lambda x: x > 0, 
            "Price must be greater than 0."
        )

        quantity = get_valid_input(
            "Quantity: ", 
            int, 
            lambda x: x >= 1, 
            "Quantity must be at least 1."
        )

        subtotal += (price * quantity)
        total_units += quantity

    discount_percent = 0
    if total_units >= 10 or subtotal >= 100:
        discount_percent = 10
    
    discounted_amount = subtotal * (1 - (discount_percent / 100))

    perk_applied = "NO"
    final_total = discounted_amount

    if seed % 2 != 0: 
        final_total -= 3.00
        perk_applied = "YES"
    
    if final_total < 0:
        final_total = 0.0

    print("\n" + "="*20)
    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Perk applied: {perk_applied}")
    print(f"Total: ${final_total:.2f}")
    print("="*20)

main()