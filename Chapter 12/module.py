def myFunc():
    print("This Function is present in module.py file.")

if __name__ == "__main__":
    # agar code directly usi file se run horha hai jaha likha gaya hai tu....

    print("We are directly running the code.")
    myFunc()
    print(__name__)