import pandas as pd
import random
from pymongo import MongoClient 
df=pd.read_csv("feed.csv")

print(df)
column_names = df.columns

print(column_names)
try: 
    conn = MongoClient("mongodb://root:3215903287aA%40@142.93.198.98:27017/?authMechanism=DEFAULT") 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 




# database 
db = conn.database 
  
# Created or Switched to collection names: my_gfg_collection 
collection = db.my_gfg_collection 
"""
#data dummy
emp_rec1 = { 
        "name":"Mr.Geek", 
        "eid":24, 
        "location":"delhi"
        } 
 
# Insert Data 
rec_id1 = collection.insert_one(emp_rec1) 
"""
schema_extra = {
            "example": {
                "project_name": "Advanced AI Exploration",
                "project_url_on_catalog": "http://catalog.airoboticsexploration.com",
                "project_url_external": "http://airoboticsexploration.com",
                "project_description": "An advanced project exploring AI and robotics",
                "keywords": ["AI", "robotics", "advanced"],
                "fields_of_science": ["Robotics", "Advanced AI"],
                "project_status": "Active",
                "agency_sponsor": "RoboticExplorers",
                "agency_sponsor_other": "N/A",
                "gov_contact": "Jane Doe",
                "gov_contact_email": "janedoe@gov.com",
                "geographic_scope": "International",
                "participant_age": "18+",
                "participation_tasks": ["Robot training", "model development"],
                "scistarter": "Yes",
                "email": "new_owner@example.com",
                "start_date": "2023-05-01",
                "project_goals": "Explore advanced techniques in AI and robotics.",
                "stars": 5,
                "collaborators": ["user3_id", "user4_id"],
                "owner_id": "new_owner_id",
                "discussions": ["thread3_id", "thread4_id"]

            }
        }

#print("Data inserted with record ids",rec_id1) 
  
# Printing the data inserted 
cursor = collection.find() 
for record in cursor: 
    print(record)  

def funcmigrate():
    for index, row in df.iterrows():
        #print(index,row)
        #for col in df.columns:
        #print(row["project_name"],row["project_url_on_catalog"])
        #break
        print(".")
        random.randint(0,5)
        schema_extra = {
                    str(index): {
                        "project_name": row["project_name"],
                        "project_url_on_catalog": row["project_url_on_catalog"],
                        "project_url_external": row["project_url_external"],
                        "project_description": row["project_description"],
                        "keywords":row["keywords"],
                        "fields_of_science": row["fields_of_science"],
                        "project_status": row["project_status"],
                        "agency_sponsor": row["agency_sponsor"],
                        "agency_sponsor_other": row["agency_sponsor_other"],
                        "gov_contact": "",
                        "gov_contact_email": "",
                        "geographic_scope": row["geographic_scope"],
                        "participant_age": row["participant_age"],
                        "participation_tasks": row["participation_tasks"],
                        "scistarter":row["scistarter"],
                        "email": row["email"],
                        "start_date": row["start_date"],
                        "project_goals": row["project_goals"],
                        "stars": random.randint(0,5),
                        "collaborators":[],
                        "owner_id": "",
                        "discussions": []

                    }
                }

        rec_id1 = collection.insert_one(schema_extra) 
funcmigrate()