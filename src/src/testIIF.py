import os
from src.src import ImportIIF as p

filePath = os.getenv("filePath")
pob=p.PowerBI()
pob.get_data(filePath)
