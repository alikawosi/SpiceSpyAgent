from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

class Message(Model):
    message:str

recipent_address = "agent1qw8cmux3sjpvxn9jevc7d0mwrg3gx8ssktlsj9udssq2fte8sfl0jtg23zd"

user = Agent(name="Mo",port=8001, seed="user recovery phrase", endpoint=["http://127.0.0.1:8001/submit"])
fund_agent_if_low(user.wallet.address())

print(user.address)

@user.on_message(model=Message)
async def user_message_handler(ctx:Context, sender:str, incomingMessage:Message ):
    ctx.logger.info(f"Received message from {sender}: {incomingMessage.message}")
    await ctx.send(recipent_address,Message(message=f'hello, my name is {ctx.agent.name}'))

if __name__ == "__main__":
    user.run()
 