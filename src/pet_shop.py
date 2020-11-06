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