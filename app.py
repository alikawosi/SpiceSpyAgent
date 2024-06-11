import json
from flask import Flask, jsonify,request
from uagents.query import query
from uagents import Model

data = {
    "points": [
        (40.712776, -74.005974),  
        (34.052235, -118.243683),  
        (41.878113, -87.629799),  
    ]
}
clusteringAgentAddress="agent1qtnusyalz5umd07cljxjzfa4uf0n3da5yuywwx8mcf8f75aftc8nkmtn4el"

app = Flask(__name__)


class Message(Model):
    locationsList:str

@app.route('/get_clustered_List', methods=['GET'])
async def getClussteredList(data):
    response = await  query(destination=clusteringAgentAddress, message=Message(locationsList=data),timeout=180)
    responseData = json.loads(response.decode_payload()) 
    print(responseData)
    return jsonify(responseData) 


