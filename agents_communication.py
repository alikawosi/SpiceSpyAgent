from uagents import Agent,Context,Model,Bureau

class Message(Model):
    message: str

spice = Agent(name="spice",seed="spice recovery phrase")
user = Agent(name="Mo",seed="Mo recovery phrase")

@user.on_interval(period=3.0)
async def send_message(ctx:Context):
    await ctx.send(spice.address,Message(message="I'm Hungry!!!!"))

@user.on_message(model=Message)
async def spice_message_handler(ctx:Context, sender:str, incomingMessage:Message ):
    ctx.logger.info(f"Received message from {sender}: {incomingMessage.message}")

@spice.on_message(model=Message)
async def slaanesh_message_handler(ctx: Context, sender: str, incomingMessage: Message):
    ctx.logger.info(f"Received message from {sender}: {incomingMessage.message}")
    await ctx.send(user.address, Message(message="Go buy something!"))

bureau = Bureau()
bureau.add(user)
bureau.add(spice)
 
if __name__ == "__main__":
    bureau.run()