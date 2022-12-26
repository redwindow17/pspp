def main():
    try:
        age=int(input("Enter your age"))
        if age>18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote") #display exception's default error message
    except ValueError as err:
        print(err)
    except:
        print("An Error occured")
        print("rest of the code...")
main()
