import reflex as rx
import requests
import googlemaps
from dotenv import load_dotenv
from lahacks2024.cluster import Kmeans
import os
import pandas as pd

# Keep track of entered users
class State(rx.State):
    driver_dict: dict = {}
    passenger_dict: dict = {}
    # users = [driver_dict, passenger_dict] # 0 driver, 1 passenger

    # Add user to dictionary
    def add_user(self, form_data):
        name = form_data["Name"]
        location = form_data["Location"]
        if (form_data["User Type"] == "Driver"):
            self.driver_dict[name] = location
        else:
            self.passenger_dict[name] = location
    
    def calculate(self):
        coords = self.get_geocoding_all()

        x = []
        y = []
        centroids = []
        for coord in coords[0]:
            x.append(coord[0])
            y.append(coord[1])
            centroids.append(coord)
        for coord in coords[1]:
            x.append(coord[0])
            y.append(coord[1])
        
        dataset = pd.DataFrame({'x': x, 'y': y})
        print(centroids)
        clusters = Kmeans.cluster(dataset, centroids)
        print(clusters)
    
    def user_list_type(self, type):
    #     users_l = []
    #     for each in self.users[type]:
    #         users_l.append(each)
    #     return users_l
        if type == 0:
            return list(self.driver_dict.keys())
        else:
            return list(self.passenger_dict.keys())
        

    
    # Return names of users added
    def user_list(self):
        # users_l = []
        # for type in self.users:
        #     for each in type:
        #         print(each)
        #         users_l.append(each)
        # return users_l
        return self.user_list_type(0).extend(self.user_list_type(1))
    
    # Return locations of drivers added
    def loc_list_drivers(self):
        # loc_l = []
        # for each in self.users[0]:
        #     loc_l.append(self.users[0][each])
        # return loc_l
        return list(self.driver_dict.values())
    
    # Return locations of passengers added
    def loc_list_passengers(self):
        # loc_l = []
        # for each in self.users[1]:
        #     loc_l.append(self.users[1][each])
        # return loc_l
        return list(self.passenger_dict.values())

    # Return latitude, longitude coordinates of each address
    def get_geocoding_all(self):
        driver_locations = self.loc_list_drivers()
        passenger_locations = self.loc_list_passengers()
        driver_geocodes = []
        passenger_geocodes = []

        for location in driver_locations:
            geocode = get_geocoding(location)
            driver_geocodes.append([geocode["longitude"], geocode["latitude"]])
        
        for location in passenger_locations:
            geocode = get_geocoding(location)
            passenger_geocodes.append([geocode["longitude"], geocode["latitude"]])

        for code in driver_geocodes:
            print(code)
        
        for code in passenger_geocodes:
            print(code)

        return [driver_geocodes, passenger_geocodes]

def get_geocoding(address):
    """
    Fetches longitude and latitude for a given address using Google Geocoding API.

    Args:
        address: The address to geocode.

    Returns:
        A dictionary containing latitude, longitude and formatted address if successful, 
        None otherwise.
    """

    load_dotenv('lahacks2024/.env')
    
    api_key = os.getenv('GOOGLE_API')  # Replace with your actual API Key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    print(response)
    print(response.json())

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
        rx.heading(
            'Drivers:',
            size="3"
        ),
        rx.foreach(
            State.driver_dict,
            lambda name: rx.text(name)
        ),
        rx.heading(
            'Passengers:',
            size="3"
        ),
        rx.foreach(
            State.passenger_dict,
            lambda name: rx.text(name),
        )
    )


def create_lobby():
    return rx.vstack(
        rx.form.root(
            rx.text("Name: "),
            rx.input(name="Name"),
            rx.text("Location: "),
            rx.input(name="Location"),
            rx.radio(
                ['Driver', 'Passenger'],
                direction="row",
                spacing="3",
                size="3",
                name="User Type",
                required=True,
            ),
            rx.button(
                "Add attendee",
                type="submit",
            ),
            on_submit=State.add_user,
        ),
        rx.button(
            "Calculate",
            on_click=State.calculate(),
        ),
        display_user_list(),
    )

def transform_data(df):
    def number_to_color(n):
        colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'navy', 'beige', 'brown']
        return colors[n]
    
    coords = State.get_geocoding_all()
    coords = coords[0] + coords[1]
    l = len(State.driver_dict)
    return df.assign(
        x = [coord[0] for coord in coords],
        y = [coord[1] for coord in coords],
        type = [('driver' if i < l else 'passenger') for i in range(df.shape[0])],
        color = df['group'].apply(number_to_color),
    ).drop(columns=['id', 'group'])

def map_url(df): # columns: x, y, type, color
    df = transform_data(df)
    size = '500x400'
    format = 'png'
    language = 'english'
    key = "AIzaSyBk6mPEMyEkSzlwE11KmcCcS_DWBmMfg-0"

    passenger_df = df[df['type'] == 'passenger']
    driver_df = df[df['type'] == 'driver']

    marker_p_list = [marker_str(x, y, c, 'passenger') for x, y, c in 
                     zip(passenger_df['x'].to_list(), 
                         passenger_df['y'].to_list(), passenger_df['color'].to_list())]
    marker_d_list = [marker_str(x, y, c, 'driver') for x, y, c in 
                     zip(driver_df['x'].to_list(),
                         driver_df['y'].to_list(), driver_df['color'].to_list())]

    base = "https://maps.googleapis.com/maps/api/staticmap?"
    format_list = ['size=' + size, 'format=' + format, 'language=' + language]
    format_list.extend(marker_p_list)
    format_list.extend(marker_d_list)
    format_list.append('key=' + key)
    return base + '&'.join(format_list)

def marker_str(x, y, color, type):
    if type == 'driver':
        marker_style = ['anchor:top', f'color:{color}', f'label:D', f'{x},{y}']
    else:
        marker_style = ['anchor:top', f'color:{color}', f'label:P', f'{x},{y}']
    return 'markers=' + '|'.join(marker_style)