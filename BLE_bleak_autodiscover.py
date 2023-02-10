from bleak import BleakScanner, BleakClient, BleakError
import DMMdecoder
import asyncio

#based of the script from https://justanotherelectronicsblog.com/?p=930

device_name = "Bluetooth DMM"
DMM_UUID = "0000fff4-0000-1000-8000-00805f9b34fb" 

def on_disconnect(client, *args, **kwargs):
    print("Disconnected from device.")
    exit()

async def run():
    print("Scanning for devices...")
    address = await BleakScanner.find_device_by_filter(filterfunc =(lambda d, ad: d.name == device_name), timeout=20.0)
    if not address:
        print("Device with name " + device_name + " not found!")
        exit()
    
    print("Found "+ address.name + ", Address: " + address.address + "!")
    
    async with BleakClient(address, disconnected_callback=on_disconnect) as client:
        while True:
            await client.start_notify(DMM_UUID, notification_handler)
            await asyncio.sleep(5.0)
            await client.stop_notify(DMM_UUID)

def notification_handler(sender, data):
    DMM_data = DMMdecoder.decode(data.hex(" "))
    #do something with the data

    print("DMM ID: ", DMM_data["typeID"])
    print("Display: ", DMM_data["display"])
    print("Value type: ", DMM_data["value_type"])
    print("Icons: ",DMM_data["icons"])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(False)
    loop.run_until_complete(run())