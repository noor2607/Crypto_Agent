from agents import Agent, Runner, function_tool
import requests
from connection import config

#
@function_tool
def get_crypto_price(crypto: str):
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={crypto.upper()}USDT')
    data = response.json()

    if 'price' in data:
        return f'price of {crypto.upper()} is {data["price"]} USDT'
    else:
        return f'Could not retrieve price for {crypto.upper()}. Please input correct symbol.'


agent = Agent(
    name='crypto_agent',
    instructions="You are a cryptocurrency price agent. You help users get real-time crypto prices using Binance API.",
    tools=[get_crypto_price]
)


if __name__ == "__main__":
    user_input = input("plz enter here..... ")
    response = Runner.run_sync(
        agent,  
        input=user_input,
        run_config=config
    )
    print(response.final_output)
