from serpapi import GoogleSearch
import csv
import pandas as pd
params = {
  "engine": "google_maps",
  "q": "pizza",
  "ll": "@40.7455096,-74.0083012,15.1z",
  "type": "search",
  "api_key": "2c8412f6dcffad48eefb445b95239a3d5aa60bbe811de7ee3eca083f4d8de283"
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]

for  res in local_results:
  print(res)
  print("\n")

# new=pd.DataFrame.from_dict(res)
# new.to_csv("test.csv")
# print(new)
  
# fields=['position','title','place_id','data_id','data_cid','reviews_link','photos_link','gps_coordinates','place_id_search','rating','reviews','price','type','address','open_state','hours','operating_hours','phone','website','description','service_options','thumbnail']

# filename="scrap.csv"

# with open(filename,'w') as csvfile:
#     writer=csv.DictWriter(csvfile,fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(local_results)


