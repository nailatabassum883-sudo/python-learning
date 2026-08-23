retry_count=2
while True:
    password=input('Please Enter Your Password:')
    if password=="Sesame":
        print('Access granted -->')
        break
    else:
        print("Access denied.")
        print("Please Try Again.")
        if retry_count==0:
            print("You can't enter your password anymore.")
            break
        retry_count-=1

