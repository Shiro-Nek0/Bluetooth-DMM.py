from bleak import BleakClient
import DMMdecoder
import asyncio

ADDRESS = ("") #MAC address of the multimeter
CHARACTERISTIC_UUID = "0000fff4-0000-1000-8000-00805f9b34fb"

def notification_handler(sender, data):
    # Simple notification handler which prints the data received
    hex_data = data.hex(' ')
    print(hex_data)
    print(DMMdecoder.decode(hex_data))

async def run(address):
    client = BleakClient(address)
    async with BleakClient(address) as client:
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        await asyncio.sleep(60.0) #show data for a minute
        await client.stop_notify(CHARACTERISTIC_UUID)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(False)
    loop.run_until_complete(run(ADDRESS))