import requests, os, argparse
debug = False

zip_code_api_key = os.environ["ZIP_CODE_API_KEY"]
voicemonkey_api_key = os.environ["VOICEMONKEY_API_KEY"]


def main(zip_code, routine_trigger):
  lat_long = lat_long_by_zip(zip_code)
  temp = temp_by_lat_long(*lat_long)
  if temp <= 0:
    turn_on_device(routine_trigger)
  else:
    print("Temp above freezing, no change")

def turn_on_device(routine_trigger):
  vm_api_url = f"https://api-v2.voicemonkey.io/trigger?token={voicemonkey_api_key}&device={routine_trigger}"
  vm_response = requests.get(vm_api_url)
  status = vm_response.status_code
  if status == 200:
    print("Turned on device") 
  else:
    raise Exception(f"Voicemonkey: non-success status code: {status}")


def lat_long_by_zip(zip_code):
  zip_api_url = f"https://app.zipcodebase.com/api/v1/search?apikey={zip_code_api_key}&codes={zip_code}&country=US"
  if debug:
    print(zip_api_url)
  zip_response = requests.get(zip_api_url)
  if zip_response.status_code == 200:
    zip_response_json = zip_response.json()
    if debug:
      print("Retrieved lat/long")
      print(zip_response_json)
    zip_json = zip_response_json["results"][zip_code][0]
    latitude = zip_json["latitude"]
    longitude = zip_json["longitude"]
    if debug:
      print(f"Latitude: {latitude}, Longitude: {longitude}")
    return (latitude, longitude)
  else:
    raise Exception(f"Zip: non-success status code: {zip_response.status_code}")


def temp_by_lat_long(latitude, longitude):
  weather_api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&hourly=temperature_2m"
  weather_response = requests.get(weather_api_url.format(latitude,longitude))
  if weather_response.status_code == 200:
    weather_response_json = weather_response.json()
    if debug:
      print ("Retrieved weather")
      print(weather_response_json)
    temperature = weather_response_json["current"]["temperature_2m"]
    if debug:
      print(f"Temperature: {temperature}")
    return temperature
#  else:
#    raise Exception(f"Weather: non-success status code: {weather_response.status_code}"


if __name__ == '__main__':
  
  parser = argparse.ArgumentParser()
  parser.add_argument("zip_code")
  parser.add_argument("routine_trigger")
  args = parser.parse_args()
  main(args.zip_code, args.routine_trigger)

