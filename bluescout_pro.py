import bluetooth
import asyncio
import csv
import json
import os
import time
from bleak import BleakScanner
from rich.console import Console
from rich.table import Table

console = Console()

known_devices = {}
scan_log = []


def guess_type(name):

    if not name:
        return "Unknown"

    name = name.lower()

    if "iphone" in name or "android" in name:
        return "Mobile"

    if "buds" in name or "headset" in name:
        return "Audio"

    if "watch" in name:
        return "SmartWatch"

    if "laptop" in name or "pc" in name:
        return "Computer"

    return "Unknown"


def termux_alert():

    if "TERMUX_VERSION" in os.environ:

        os.system("termux-vibrate -d 400")
        os.system(
            "termux-notification --title 'Bluetooth Alert' --content 'Suspicious Bluetooth Device Detected'"
        )


def classic_scan():

    devices = bluetooth.discover_devices(
        duration=8,
        lookup_names=True,
        lookup_class=True
    )

    return devices


async def ble_scan():

    devices = await BleakScanner.discover(timeout=5)
    return devices


def show_classic(devices):

    table = Table(title="Classic Bluetooth Devices")

    table.add_column("MAC")
    table.add_column("Name")
    table.add_column("Type")
    table.add_column("First Seen")

    for addr, name, device_class in devices:

        dtype = guess_type(name)

        if addr not in known_devices:

            known_devices[addr] = time.strftime("%H:%M:%S")
            termux_alert()

        table.add_row(
            addr,
            name if name else "Unknown",
            dtype,
            known_devices[addr]
        )

        scan_log.append({
            "mac": addr,
            "name": name,
            "type": dtype,
            "time": known_devices[addr]
        })

    console.print(table)


async def show_ble():

    devices = await ble_scan()

    table = Table(title="BLE Devices")

    table.add_column("MAC")
    table.add_column("Name")
    table.add_column("RSSI")

    for d in devices:

        table.add_row(
            str(d.address),
            str(d.name),
            str(d.rssi)
        )

        scan_log.append({
            "mac": d.address,
            "name": d.name,
            "type": "BLE",
            "time": time.strftime("%H:%M:%S"),
            "rssi": d.rssi
        })

    console.print(table)


def export_json():

    with open("bluetooth_report.json","w") as f:

        json.dump(scan_log,f,indent=4)

    console.print("[green]JSON report saved[/green]")


def export_csv():

    with open("bluetooth_report.csv","w",newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["mac","name","type","time"]
        )

        writer.writeheader()

        for row in scan_log:
            writer.writerow(row)

    console.print("[green]CSV report saved[/green]")


def live_monitor():

    console.print("[yellow]Live Bluetooth monitoring started[/yellow]")

    while True:

        try:

            devices = classic_scan()
            show_classic(devices)

            asyncio.run(show_ble())

            time.sleep(6)

        except KeyboardInterrupt:

            console.print("[red]Monitoring stopped[/red]")
            break


def menu():

    console.print("""

BlueScout Pro v3

1 Classic Scan
2 BLE Scan
3 Live Monitoring
4 Export JSON
5 Export CSV
6 Exit

""")

    choice = input("Select option: ")

    if choice == "1":

        devices = classic_scan()
        show_classic(devices)

    elif choice == "2":

        asyncio.run(show_ble())

    elif choice == "3":

        live_monitor()

    elif choice == "4":

        export_json()

    elif choice == "5":

        export_csv()

    elif choice == "6":

        exit()


if __name__ == "__main__":

    while True:
        menu()
