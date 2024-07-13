# Weather Forecast Application Script
from forecast import forecast

def main():
    default_weather = {
        "New York": {"temperature": 70, "condition": "sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "rainy", "humidity": 70, "city": "Tokyo"}
    }
    forecasts = {}
    while True:
        # add default forecasts
        for weather_forecast in default_weather.items():
            forecast_city = weather_forecast[1].get("city")
            forecast_temperature = weather_forecast[1].get("temperature")
            forecast_humidity = weather_forecast[1].get("humidity")
            forecast_condition = weather_forecast[1].get("condition")
            new_forecast = forecast(forecast_city, forecast_temperature, forecast_condition, forecast_humidity)
            forecasts.update({forecast_city: new_forecast})
        # base weather conditions to choose from later, people probably won't be inventing new ones like apocalypse but that functionality could be added
        weather_conditions = ["sunny", "rainy", "partly cloudy", "cloudy", "inclement weather", "snowing"]
        # main menu options
        options = [f"{index+1} {option}" for index, option in enumerate(["Create forecast", "Get forecast"])]
        string = "\n".join(options)
        try:
            # provide main menu to user to get operation
            chosen_operation = int(input(f"Operations:\n{string}\nPlease choose an operation: "))
            chosen_operation = int(chosen_operation)
            if chosen_operation == 1:#Create forecast
                # prepare forecast arguments
                forecast_city = str(input("Please enter a city: "))
                forecast_temperature = int(input("Please enter a temperature: "))
                forecast_humidity = int(input("Please enter a humidity: "))
                # prepare condition options, present to user and get the name via index
                options = [f"{index+1} {option}" for index, option in enumerate(weather_conditions)]
                string = "\n".join(options)
                chosen_condition_index = int(input(f"Operations:\n{string}\nPlease choose a condition: "))
                forecast_condition = str(options[chosen_condition_index-1])[2:]
                # create forecast
                new_forecast = forecast(forecast_city, forecast_temperature, forecast_condition, forecast_humidity)
                # add forecast to forecasts
                forecasts.update({forecast_city: new_forecast})
            elif chosen_operation == 2:#Get forecast
                # get list of forecasts
                options = [f"{index+1} {option[0]}" for index, option in enumerate(forecasts.items())]
                if len(options) > 0:
                    # get forecast name via options and index
                    string = "\n".join(options)
                    chosen_forecast_index = int(input(f"Operations:\n{string}\nPlease choose a forecast: "))
                    # get forecast from forecast dict using index
                    list(forecasts.items())[chosen_forecast_index-1][1].print_forecast()
                else:
                    print("Please create a forecast first!")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        else:
            print("-----------------")
        

main()
