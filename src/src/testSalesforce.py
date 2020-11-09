import os
from src.src import ImportSalesforce as s
username = os.getenv("username")
password=os.getenv("password")
security_token = os.getenv("security_token")
grant_type=os.getenv("grant_type")
client_secret=os.getenv("client_secret")
client_id=os.getenv("client_id")


params = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password
}
query = os.getenv("query")
instance=os.getenv("instance")

sob=s.SalesForce(params)
sob.query(instance, query)
