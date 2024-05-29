from uagents import Agent, Context
spice = Agent(name="spice", seed="spice recovery phrase")

@spice.on_event("startup")
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.agent.name}')

if __name__ == "__main__":
    spice.run()