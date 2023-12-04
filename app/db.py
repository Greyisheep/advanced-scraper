from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_cluster():
    cloud_config = {
        'secure_connect_bundle': 'ignored/secure-connect-fastapi-db.zip'
    }

    CLIENT_ID = os.getenv("ASTRA_DB_CLIENT_ID")
    CLIENT_SECRET = os.getenv("ASTRA_DB_CLIENT_SECRET")

    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

def get_session():
    cluster = get_cluster()
    session = cluster.connect()
    return session

session = get_session()
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")