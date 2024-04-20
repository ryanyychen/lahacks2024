import reflex as rx
import requests
import googlemaps

class State(rx.State):
    users: dict = {}

    def add_user(self, form_data):
        name = form_data["Name"]
        location = form_data["Location"]
        self.users[name] = location
        self.get_geocoding_all()
    
    def user_list(self):
        users_l = []
        for each in self.users:
            users_l.append(each)
        return users_l
    
    def loc_list(self):
        loc_l = []
        for each in self.users:
            loc_l.append(self.users[each])
        return loc_l

    def get_geocoding_all(self):
        locations = self.loc_list()
        geocodes = []

        for location in locations:
            geocode = get_geocoding(location)
            geocodes.append(geocode)
        
        for code in geocodes:
            print(code)

# async def get_geocoding(address):
#     base_url = "https://api.positionstack.com/v1/forward"
#     params = {
#         "query": address,
#         "access_key": "0df1ed6c498ab0a5b342bdfaf47400ea"
#     }
#     response = requests.get(base_url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         # Check for successful geocoding
#         if data["data"]:
#             return data["data"][0]  # Assuming first result
#     else:
#         print(f"Error: {response.status_code}")
#         return None

def get_geocoding(address):
    """
    Fetches longitude and latitude for a given address using Google Geocoding API.

    Args:
        address: The address to geocode.

    Returns:
        A dictionary containing latitude, longitude and formatted address if successful, 
        None otherwise.
    """
    api_key = "AIzaSyDnygqhrVgh6ZC9EiGpdruoF34s1qzs7dc"  # Replace with your actual API Key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Check for successful geocoding
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            formatted_address = data["results"][0]["formatted_address"]
            return {
                "latitude": location["lat"],
                "longitude": location["lng"],
                "formatted_address": formatted_address
            }
    else:
        print(f"Error: {response.status_code}")
    return None

def get_distance_matrix(api_key, origins, destinations, travel_mode="driving"):
  """
  Calculates distance and travel time between origins and destinations using Google Distance Matrix API.

  Args:
      api_key: Your Google Maps API Key.
      origins: List of origin addresses or coordinates (latitude, longitude).
      destinations: List of destination addresses or coordinates (latitude, longitude).
      travel_mode: Travel mode (driving, walking, bicycling, transit). Defaults to driving.

  Returns:
      A dictionary containing distance and duration matrices if successful, 
      None otherwise.
  """
  api_key = "AIzaSyDnygqhrVgh6ZC9EiGpdruoF34s1qzs7dc"
  client = googlemaps.Client(key=api_key)

  distance_matrix = client.distance_matrix(
      origins=origins,
      destinations=destinations,
      travel_mode=travel_mode
  )

  # Check for successful response
  if distance_matrix["status"] == "OK":
    return distance_matrix
  else:
    print("Distance Matrix API request failed:", distance_matrix["status"])
    return None

def display_user_list():
        return rx.vstack(
            rx.foreach(State.users, rx.text),
        )

def create_lobby():
    return rx.vstack(
        rx.form.root(
            rx.text("Name: "),
            rx.input(name="Name"),
            rx.text("Location: "),
            rx.input(name="Location"),
            rx.button(
                "Add attendee",
                type="submit",
            ),
            on_submit=State.add_user,
        ),
        display_user_list(),
    )