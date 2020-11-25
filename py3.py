# email = input("Enter your email")

# # Check whether the email is valid or not !

# if "@" in email:
#     print("Email is Valid !")
# else:
#     print("Invalid")

# Check which email is valid and is not from the list of email ids

# Create a list named email_ids
email_ids = ["q@gmail.com", "2q@gmail.com", "wmail.com", "io@mail.com"]

print("Mail IDs :" + " ", email_ids)

print("----------------------------------------------------------------------------------------")

# Logic for validation (Validation Criteria - Check for @)

for email in email_ids:
    print(email)
    if "@" in email:
        print("Email ID is Valid :)", email)
    else:
        print("Email ID is not valid ! :(", email)
