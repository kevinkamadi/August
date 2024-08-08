def temp():
    print("Mama")
temp()

is_hot=''
is_cold=''
name= input('Enter Your Name: ')
hot= input("Is it a hot day?(Reply with True or False): ")
cold= input("Is it a cold day?(Reply with True or False): ")
x = is_hot = hot
y = is_cold = cold

def weather(is_hot, is_cold):
    if is_hot:
        return(f"What a warm day it is{name}\n Keep it cool")
    elif is_cold:
        return(f"What a cold day it is{name}\n Keep it warm")
    else:
        return(f"Have a great Day {name}")
weather(x, y)

