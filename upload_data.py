from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
uri = "mongodb+srv://anu:171201@cluster0.wy20ogo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and cnnect to server 
client = MongoClient(uri)

# create a database name and collection name 
DataBase_NAME= "Pwskill_Mdb"
Collection_NAME= "waterfault"

df = pd.read_csv("C:\Users\HP\Desktop\Pwskill\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record=list(json.loads(df.T.to_json()).values())
type(json_record)

client[DataBase_NAME][Collection_NAME].insert_many(json_record)