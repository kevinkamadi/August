#a simple program asking for user info and making sure it's correct
def get_user_information():
    name = input("What's your name? ")
    phone_number = input("What's your phone number? ")
    account_number = input("What's your account number? ")

    # Ensure phone_number is numeric
    while not phone_number.isdigit():
        print("Phone number should be numeric.")
        phone_number = input("Please enter your phone number again: ")
    
    correct = False

    while not correct:
        print(f"\nConfirm your Information below:\nName: {name}\nPhone Number: {phone_number}\nAccount Number: {account_number}")
        confirmation = input("Is this information correct? (yes/no): ").lower()

        if confirmation == "yes":
            print(f"Thank you, {name}. Your information has been recorded.")
            correct = True
        elif confirmation == "no":
            print("Let's try again.")
            name = input("What's your name? ")
            phone_number = input("What's your phone number? ")
            account_number = input("What's your account number? ")
            
            while not phone_number.isdigit():
                print("Phone number should be numeric.")
                phone_number = input("Please enter your phone number again: ")
        else:
            print("Invalid input. Please reply with 'yes' or 'no'.")

get_user_information()
