from uagents import Agent, Context
spice = Agent(name="spice", seed="spice recovery phrase")

print("Address: " , spice.address)
print("Wallet Address: " , spice.wallet.address())


