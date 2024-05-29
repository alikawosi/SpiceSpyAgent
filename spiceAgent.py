from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class Message(Model):
    message:str

recipent_address = "agent1qv2gauxf44cpcmaxmxm8jj0dqaa4djg9d5gdnfetwck2t4n9ghsgjswgx9m"

spice = Agent(name="spice",port=8000, seed="spice recovery phrase", endpoint=["http://127.0.0.1:8000/submit"])
fund_agent_if_low(spice.wallet.address())

print(spice.address)

@spice.on_interval(period=2.0)
async def send_message(ctx: Context):
    await ctx.send(recipent_address,Message(message=f'hello, my name is {ctx.agent.name}'))

@spice.on_message(model=Message)
async def spice_message_handler(ctx:Context, sender:str, incomingMessage:Message ):
    ctx.logger.info(f"Received message from {sender}: {incomingMessage.message}")

if __name__ == "__main__":
    spice.run()
