from weather import Weather
weather = Weather()

# Lookup WOEID via http://weather.yahoo.com.

lookup = weather.lookup(23129)
condition = lookup.condition()
print condition['text']
print condition['temp']
