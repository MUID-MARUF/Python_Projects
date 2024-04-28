print("--Welcome to the revolutionary Brand Name Generator programme--")
city = input("What is your city name? \n")
fruit = input("What is your favourite fruit? \n")

brand_name = city + fruit+"s"
brand_name_len = len(brand_name)
print("The brand name is :: " + brand_name)
print("Your brand name contains " + str(brand_name_len) + " characters.")

print("--End of programme--")