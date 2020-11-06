# WRITE YOUR FUNCTIONS HERE

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
    pet_shop["admin"]["total_cash"] +=  cash

# The purpose of the function:
#   - To return how many pets were sold in a given pet shop
def get_pets_sold (pet_shop):
    return pet_shop["admin"]["pets_sold"]

# The purpose of the function:
#   - To increase number of pets sold for a given pet shop
def increase_pets_sold (pet_shop, pets):
    pet_shop["admin"]["pets_sold"] += pets 

# The purpose of the function:
#   - To return number of pets in given pet shop
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])