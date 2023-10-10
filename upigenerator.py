import random
import string

def generate_random_upi_id(username_length=6):
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
    upi_domain = "@upi"  # You can replace this with the specific UPI service provider's domain
    return username + upi_domain

# Generate a random UPI ID
random_upi_id = generate_random_upi_id()
print("Random UPI ID:", random_upi_id)
