while True:
	print("---Canteen Menu---")
	print("1. Tea → ₹10")
	print("2. Coffee → ₹15")
	print("3. Water → ₹5")
	print("4. Bunmuska → ₹20")

	choice = int(input("Enter your choice: "))

	match choice:
		case 1:
			item, rate = "Tea", 10
		case 2:
			item, rate = "Coffee", 15
		case 3:
			item, rate = "Water", 5
		case 4:
			item, rate = "Bunmuska", 20
		case _:
			print("Invalid choice. Please select a valid menu item.")
			continue

	qty = int(input("Enter quantity: "))
	print("----- Bill -----")
	print(f"Item: {item}")
	print(f"Quantity: {qty}")
	print(f"Rate: ₹{rate}")
	print(f"Total Amount: ₹{rate * qty}")
	print("Thank you! Visit again.")
	break
