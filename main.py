from api_key import *
import requests
from Functions import *

town_name = input("Where do you live? ")
timezone_data = get_timezone(town_name)
Timezone_info(timezone_data)


