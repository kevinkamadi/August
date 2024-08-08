name = ''
name = input("Name: ").lower()
name == "kamadi" if print("welcome") else print("Wrong Username")

num1 =20
num2=2
def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")
divide(20,2)