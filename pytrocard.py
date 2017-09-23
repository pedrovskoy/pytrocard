initial_balance = float(input("Initial balance: "))
recharge_value = 5.5
fare = 2.75


while True:
	if (round(1.05 * recharge_value, 2) + initial_balance) % fare == 0:
		while True:
			if len(str(recharge_value)) < 4:
				recharge_value = str(recharge_value) + '0'
			else:
				break
		message = "Minimum recharge value: "
		message += str(recharge_value)
		print(message)
		break
	else:
		recharge_value = round(recharge_value + 0.05, 2)
