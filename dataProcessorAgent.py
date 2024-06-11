from pyexpat import model
from uagents import Agent,Model,Context
from uagents.setup import fund_agent_if_low;


class WasteInfo(Model):
    type: str
    amount:float

class BinInfo(Model):
    latitude: float
    longtitude: float
    wastes: WasteInfo 

class Message(Model):
    data: BinInfo

class Responses(Model):
    responseMessage: str

BinDataProcessorAgent = Agent(name="BinProcessor",seed="Bin Processor Secret Phrase")

@BinDataProcessorAgent.on_message(model=Message , replies=Responses)
async def messageHandler(ctx:Context, sender:str, msg:Message):
    await ctx.send(sender,Responses(responseMessage=msg.data.wastes.type))

