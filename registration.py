from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Protocol

spice = Agent(name="spice",port=8000,seed="spice secret phrase",
              endpoint=["http://127.0.0.1:8000/submit"])
fund_agent_if_low(spice.wallet.address())

@spice.on_interval(period=3)
async def hi(ctx:Context):
    ctx.logger.info("Hello")

spice.run()
