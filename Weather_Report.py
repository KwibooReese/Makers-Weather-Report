def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "not great"

def as_snow_lover(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "not great"

def report_weather(temperature, func):
    return func(temperature)