from udpy import UrbanClient

client = UrbanClient()

defs = client.get_definition('netflix and chill')

for i in defs:
    print(i)