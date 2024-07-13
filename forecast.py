# This is a class that specifically handles weather forecasts
# You can get create a forecast and manipulate various aspects of it

class forecast:
    def __init__(self, city, temperature, condition, humidity):
        self.__temperature = temperature
        self.__condition = condition
        self.__humidity = humidity
        self.__city = city

    def get_temperature(self):
        return self.__temperature
    
    def get_condition(self):
        return self.__condition
    
    def get_humidity(self):
        return self.__humidity
    
    def get_city(self):
        return self.__city
    
    def set_temperature(self, new_temperature):
        if isinstance(new_temperature, int) or isinstance(new_temperature, float):
            self.__temperature = new_temperature
        else:
            print("Temperature is not a number.")
    
    def set_condition(self, new_condition):
        if isinstance(new_condition, str):
            self.__condition = new_condition
        else:
            print("Temperature is not a string.")
    
    def set_humidity(self, new_humidity):
        if isinstance(new_humidity, int) or isinstance(new_humidity, float):
            self.__humidity = new_humidity
        else:
            print("Humidity is not a number.")
    
    def set_city(self, new_city):
        if isinstance(new_city, str):
            self.__city = new_city
        else:
            print("City is not a string.")
    
    def get_forecast_data(self):
        forecast = {
            "temperature": self.__temperature,
            "condition": self.__condition,
            "humidity": self.__humidity,
            "city": self.__city
        }
        return forecast
    
    def print_forecast(self):
        print(f"The weather forecast in {self.__city} is {self.__condition}. It is {self.__temperature} degrees and the humidity is {self.__humidity}%.")

# new_forecast = forecast("New York", 56, "Sunny", 14)
# print(new_forecast.get_city())
# print(new_forecast.get_condition())
# print(new_forecast.get_humidity())
# print(new_forecast.get_temperature())
# print(new_forecast.get_forecast_data())
# new_forecast.print_forecast()
# new_forecast.set_city(1)
# new_forecast.set_city("Las Vegas")
# new_forecast.set_temperature("1")
# new_forecast.set_temperature(105)
# new_forecast.set_condition(100)
# new_forecast.set_condition("Inferno")
# new_forecast.set_humidity("none")
# new_forecast.set_humidity(-10)
# print(new_forecast.get_forecast_data())
# new_forecast.print_forecast()