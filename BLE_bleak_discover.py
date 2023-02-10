from bleak import BleakScanner
import asyncio

async def discover_devices():
    devices = await BleakScanner.discover(timeout=5.0)
    for device in devices:
        print(device)
        
asyncio.run(discover_devices())