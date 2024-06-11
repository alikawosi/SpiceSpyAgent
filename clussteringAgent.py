import json
from uagents import Agent,Model, Context, Protocol
from sklearn.cluster import KMeans
from geopy.distance import geodesic
from uagents.setup import fund_agent_if_low
from flask import jsonify

# Define a simple protocol for receiving data

class Message(Model):
    locationsList: str

class Responses(Model):
    responseMessage: str

class Clustering:
    def __init__(self):
        self.points = []

    async def add_points(self, points):
        for point in points:
            self.points.append(point)
        self.cluster_points()

    def cluster_points(self):
        """Cluster the points based on their distance from a specific point."""
        # Define the specific point (latitude, longitude)
        specific_point = (40.748817, -73.985428)  

        # Calculate distances from the specific point
        distances = [geodesic(specific_point, (lat, lon)).km for lat, lon in self.points]

        # Clustering using KMeans (you can choose the number of clusters)
        kmeans = KMeans(n_clusters=3)
        clusters = kmeans.fit_predict([[d] for d in distances])
        print("Clusters:", clusters)

# Create the agent
agent = Agent(name='clustering_agent',port=8000, seed="clustering_agent recovery phrase", endpoint=["http://localhost:8000/get_clustered_List"])

# Register the protocol and skill with the agent
skill = Clustering()

print(agent.address)
fund_agent_if_low(agent.wallet.address())


@agent.on_query(model=Message,replies=Responses)
async def qurey_handler(ctx:Context,sender:str, msg:Message):
    try:
        data = await Clustering.add_points(jsonify(msg.locationsList))
        ctx.logger.info(sender)
        ctx.logger.info(data)
    except Exception as e:
        error_message = f"Error! {str(e)}"
        ctx.logger.info(error_message)


if __name__ == '__main__':
    # Run the agent and Flask app
    agent.run()
