def weather_condtions(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Enter temperature: "))
print(weather_condtions(user_input))
