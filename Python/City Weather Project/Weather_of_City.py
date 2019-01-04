import re
import urllib.request
#http://www.weather-forecast.com/locations/Paris/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('span class="phrase">', data1)
#print(m)

start = m.end()
end = start + 200
newString = data1[start:end]
#print(newString)

m = re.search("</span>", newString)
#m=m.split('<',1)
#print(m)

end = m.start()
final = newString[0:end]
final=str(final)
final=final.split("<")
print(final)

