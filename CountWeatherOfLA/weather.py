#Count the Weather Appeared in Los Angeles Most Frequently

weather_list = ['Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Sunny','Fog','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Fog-Rain','Rain','Fog-Rain','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Fog','Fog','Sunny','Sunny','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Fog','Sunny','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Fog','Fog','Sunny','Rain','Rain','Sunny','Sunny','Sunny','Fog','Fog','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Fog','Sunny','Fog','Fog','Fog','Fog','Rain','Sunny','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog','Sunny','Rain','Sunny','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Fog','Sunny','Sunny','Rain','Rain','Rain','Sunny','Thunderstorm','Fog','Sunny','Fog','Sunny','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog','Sunny','Sunny','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog','Fog','Fog','Sunny','Fog','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Fog-Rain','Fog','Fog','Sunny','Fog','Sunny','Fog','Fog','Fog','Sunny','Rain','Fog','Fog','Fog','Fog','Fog-Rain','Sunny','Sunny','Fog','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog','Fog','Fog','Fog','Fog','Fog','Fog','Fog','Sunny','Fog','Fog','Fog','Fog','Sunny','Fog','Fog','Fog','Sunny','Sunny','Fog','Sunny','Fog','Fog','Sunny','Sunny','Fog','Fog','Fog','Sunny','Sunny','Fog','Fog','Sunny','Fog','Fog','Fog','Fog','Fog','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Fog','Sunny','Sunny','Sunny','Sunny','Fog','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog','Fog','Sunny','Sunny','Fog','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Fog','Fog','Sunny','Fog','Fog','Sunny','Sunny','Fog','Sunny','Sunny','Fog','Sunny','Rain','Rain','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny','Sunny','Sunny','Fog','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Fog','Fog']

weather_counts = {}

for weather in weather_list:
    if weather in weather_counts:
        weather_counts[weather] = weather_counts[weather]+1
    else:
        weather_counts[weather] = 1

print(weather_counts)