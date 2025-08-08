import random

# Pricing order
price_order = {"$": 1, "$$": 2, "$$$": 3}

# Restaurants on which side of O'ahu
restaurants_by_region = {
    "EAST": [
        {"name": "Nalu Health Bar & Cafe", "cuisine": "American", "price": "$$", "location": "Kailua"},
        {"name": "Uahi Island Grill", "cuisine": "Hawaiian", "price": "$$", "location": "Kailua"},
        {"name": "Sweet Home Waimanalo", "cuisine": "Hawaiian", "price": "$$", "location": "Waimānalo"},
        {"name": "Haleiwa Joe's", "cuisine": "Seafood", "price": "$$$", "location": "Kāneʻohe"},
        {"name": "Roy's Hawaii Kai", "cuisine": "Hawaiian", "price": "$$$", "location": "Hawaiʻi Kai"},
    ],
    "NORTH": [
        {"name": "Giovanni's Shrimp Truck", "cuisine": "Seafood", "price": "$", "location": "Haleʻiwa"},
        {"name": "Seven Brothers", "cuisine": "Burgers", "price": "$$", "location": "Laʻie"},
        {"name": "Waialua Bakery", "cuisine": "Bakery", "price": "$", "location": "Waialua"},
        {"name": "Haleʻiwa Beach House", "cuisine": "Seafood", "price": "$$$", "location": "Haleʻiwa"},
        {"name": "Ray's Kiawe Broiled Chicken", "cuisine": "Hawaiian", "price": "$", "location": "Haleʻiwa"},
    ],
    "WEST": [
        {"name": "My Café", "cuisine": "Brunch", "price": "$$", "location": "Kapolei"},
        {"name": "Tanioka’s Seafoods", "cuisine": "Seafood", "price": "$$", "location": "Waipahu"},
        {"name": "Thai Lao Restaurant", "cuisine": "Thai", "price": "$", "location": "ʻEwa Beach"},
        {"name": "Kalapawai Café & Deli", "cuisine": "American", "price": "$$", "location": "Kapolei"},
        {"name": "Laverne’s Hawaiian and Local Style Food", "cuisine": "Hawaiian", "price": "$", "location": "ʻEwa Beach"},
    ],
    "HONOLULU": [
        {"name": "Marukame Udon", "cuisine": "Japanese", "price": "$", "location": "Waikīkī"},
        {"name": "The Pig & the Lady", "cuisine": "Vietnamese", "price": "$$", "location": "Chinatown"},
        {"name": "TonTon Ramen", "cuisine": "Japanese", "price": "$$", "location": "Ala Moana"},
        {"name": "Liliha Bakery", "cuisine": "Bakery", "price": "$$", "location": "Kapiʻolani"},
        {"name": "Liliha Bakery", "cuisine": "Bakery", "price": "$$", "location": "Liliha Street"},
        {"name": "Cheeseburger Waikīkī", "cuisine": "American", "price": "$$", "location": "Waikīkī"},
    ]
}

# Sorting 
def sort_by_cuisine_and_price(restaurant):
    return (restaurant["cuisine"], price_order[restaurant["price"]])

# Main loop
while True:
    print("Can't decide where to eat?")

# Choosing which region
    print("Choose a region or type 'random' for a surprise:")
    for region in restaurants_by_region:
        print(f"  - {region.title()}")
    region_choice = input("Your region (or 'random'): ").strip().upper()

    if region_choice == "RANDOM":
        all_restaurants = []
        for region_data in restaurants_by_region.values():
            all_restaurants.extend(region_data)
        filtered_list = all_restaurants
    elif region_choice in restaurants_by_region:
        filtered_list = restaurants_by_region[region_choice]
    else:
        print("Invalid region. Try again.")
        continue

# Choosing the price
    print("\nChoose a price range:")
    print("  $   - Cheapass")
    print("  $$  - Mid")
    print("  $$$ - Pricey")
    price_choice = input("Your price ($ / $$ / $$$): ").strip()

    if price_choice not in price_order:
        print("Invalid price. Try again.")
        continue

    filtered_list = [r for r in filtered_list if r["price"] == price_choice]
    if not filtered_list:
        print("Sorry, there's no restaurant in that price range.")
        continue

# Choosing what cuisine
    available_cuisines = sorted(set(r["cuisine"] for r in filtered_list))
    print("\nAvailable cuisines in your selection:")
    for cuisine in available_cuisines:
        print(f"  - {cuisine}")
    cuisine_choice = input("Choose a cuisine (or 'any'): ").strip().title()

    if cuisine_choice != "Any":
        filtered_list = [r for r in filtered_list if r["cuisine"] == cuisine_choice]
        if not filtered_list:
            print("No restaurants found with that cuisine.")
            continue

# Picking random
    filtered_list = sorted(filtered_list, key=sort_by_cuisine_and_price)
    selected = random.choice(filtered_list)

# Display result
    print("\nLet's go to:")
    print(f"  Name    : {selected['name']}")
    print(f"  Location: {selected['location']}")
    print(f"  Cuisine : {selected['cuisine']}")
    print(f"  Price   : {selected['price']}")

    again = input("\n Another restaurant? (yes/no): ").strip().lower()
    if again != "yes":
        print("Eatwell")
        break
