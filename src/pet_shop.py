# The purpose of the function:
#   - To return name of a given pet shop
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# The purpose of the function:
#   - To return the total cash of a given pet shop
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# The purpose of the function:
#   - To add cash for a given pet shop
#   - To remove cash for a given pet shop
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# The purpose of the function:
#   - To return how many pets were sold in a given pet shop
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# The purpose of the function:
#   - To increase number of pets sold for a given pet shop
def increase_pets_sold(pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets

# The purpose of the function:
#   - To return number of pets in given pet shop
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# The purpose of the function:
#   - To return list with pets of a given breed from a pet shop
def get_pets_by_breed(pet_shop, breed_name):
    pets_number = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            pets_number.append(pet)
    return pets_number

# The purpose of the function:
#   - To return a pet of a given name from a pet shop
def find_pet_by_name(pet_shop, pet_name):
    pet_found = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_found = pet
            break
    return pet_found

# The purpose of the function:
#   - To remove a pet with a given name from a pet shop
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)
            break

# The purpose of the function:
#   - To add a pet to a pet shop stock
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

# The purpose of the function:
#   - To return customer cash
def get_customer_cash(customer):
    return customer["cash"]

# The purpose of the function:
#   - To remove cash from customer
def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

# The purpose of the function:
#   - To count pets of a given customer
def get_customer_pet_count (customer):
    return len(customer["pets"])