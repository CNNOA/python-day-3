def weather_check(temp):
    if temp >= 25:
        print("It is hot outside!")
    elif temp >= 15:
        print("It is nice outside!")
    else:
        print("It is cold outside!")
                 
        
def main():
    weather_check(35) # Expecting hot outside
    weather_check(-10) # Expecting cold outside
    weather_check(20) # Expecting nice outside
main()