#LINK FILES
from inspect import istraceback
import bot_token
from keep_alive import keep_alive
# import sys 
# sys.path.append("PhonePi_SampleServer-master/Python/WebSocket/PhonePi.py")

# from home/pi/Desktop/NDP/code/PhonePi_SampleServer-master/Python/WebSocket/PhonePi import data1
#LIBRARIES
import discord
import os
from discord.ext import commands, tasks
import time

#INTENTS DECLARATION
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#VARIABLES
token = bot_token.token
bot = commands.Bot(command_prefix='!')
# vibration = 0
run_loop = True
manual = """>>> Prefix: "!"
```fix
commands        - Shows all commands.
start           - Start notifying users about the vibration(s).
stop            - Stop notifying users about the vibration(s).
ping            - Informs the users about the WiFi latency.
clear(amount)   - Clears a set amount of messages. If no arguments are passed, 10 messages are cleared.
```
"""
# from PhonePi_SampleServer_master.Python.WebSocket.PhonePi import data1

#CODE
keep_alive()
@bot.event
async def on_ready():
    print('We have log in as {0.user}'. format(bot))

#!/usr/bin/env python
#phone detection accelerometer value
import asyncio
import websockets
import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

global istData 
istData = 0
hostname = socket.gethostname()
IPAddr = get_ip()
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)
print("Enter {0}:5000 in the app [PhonePi] and select the sensors to stream. For PhonePi+ just enter {0}, without the port".format(IPAddr))


async def echo(websocket, path):
    async for message in websocket:
        #global istData

        if path == '//accelerometer':
            
            print("Accelerometer data:")
            data1 = await websocket.recv()
            print(data1)
            f = open("accelerometer.txt", "a")
            f.write(data1+"\n")
            print(type(data1))
            istData = data1.split(",")[0]           
            #print(istData)
            print ("i read value "+ str(istData))
            if float(istData) > 3:
                print("LLLLLLLLLLLLLLLLLLLLLL = halo")
                channel = bot.get_channel(1011274122824790087)
                await channel.send("WOI DANGER IS COMING")


        if path == '//gyroscope':
            data = await websocket.recv()
            print(data)
            f = open("gyroscope.txt", "a")
            f.write(data+"\n")

        if path == '//magnetometer':
            data = await websocket.recv()
            print(data)
            f = open("magnetometer.txt", "a")
            f.write(data+"\n")

        if path == '//orientation':
            data = await websocket.recv()
            print(data)
            f = open("orientation.txt", "a")
            f.write(data+"\n")

        if path == '//stepcounter':
            data = await websocket.recv()
            print(data)
            f=open("stepcounter.txt", "a")
            f.write(data+"\n")

        if path == '//thermometer':
            data = await websocket.recv()
            print(data)
            f=open("thermometer.txt", "a")
            f.write(data+"\n")
            
        if path == '//lightsensor':
            data = await websocket.recv()
            print(data)
            f=open("lightsensor.txt", "a")
            f.write(data+"\n")
        
        if path == '//proximity':
            data = await websocket.recv()
            print(data)
            f=open("proximity.txt", "a")
            f.write(data+"\n")

        if path == '//geolocation':
            data = await websocket.recv()
            print(data)
            f=open("geolocation.txt", "a")
            f.write(data+"\n")


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', 5000))


#continue discord bot code
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! in {round(bot.latency, 3)}ms')



@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
async def commands(ctx):
    channel = bot.get_channel(1011274122824790087)
    await channel.send(manual)

    # await channel.send(data1)


bot.run(token)
