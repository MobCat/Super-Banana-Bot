#!/env/Python3.8.10
#!/MobCat (2022)
# Please note, this was programed as a meme, but then the meme became useful.

#!pip install discord

import discord  # discord bot api
import re # sorting and stripping strings


#!REPLACE THIS! DO NOT UPLOAD THIS!#
BotToken = "Your ID Goes Here"
# You can make a new bot here
# https://discord.com/developers/applications
# Bot invite link
# https://discord.com/api/oauth2/authorize?client_id=Your ID goes here&permissions=2147798080&scope=bot
# You can copy your ID from the bots page in the discords app devs portal.
# https://discord.com/developers/applications/{Your ID is here}/information

# Clinet instatance
client = discord.Client()

# Regeseter event
@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	print('Waiting for commands.')
	
	
# Get massage from discord
@client.event
async def on_message(message):
	# this is dumb, should be != then do the rest of the code
	if message.author == client.user:
		return

	if message.content.startswith('/sbb'):
		print("Processing ", end="", flush=True)
		#print(message.content)
		splitcmd = message.content.split() # ['/sbb', '12cm'] # Split the bot command from what we want to convert
		print(splitcmd[1], end="", flush=True)
		try:
			#num = re.sub('\F', '', splitcmd[1]) # Ripp the numbers out of our command and stor them for lator. Bad, only rips hole numbers.
			num = re.sub('[^0-9.]', '', splitcmd[1]) # Ripp the number and decimal from our string
			num = float(num) # convert string to float to be used lator
			#print(num) #Debug
			
			# This shit ton of if statements is wrong.
			# It should be some sort of case look up list but idk how to do that
			# and kinda don't wanna for a meme....
			if "cm" in splitcmd[1]: # 1cm = 0.39"
				inc = round(num/2.54, 2)
				banana = round(num/17.78, 2) # 17cm bannanas
				await message.channel.send(f'{num} Centimeters is {inc} Inches\nOr {banana} bananas.')
				print(f' = {inc}"')
				
			elif '"' in splitcmd[1]: # 1" = 2.54cm
				inc = round(num*2.54, 2)
				banana = round(int(inc)/17.78, 2)
				await message.channel.send(f'{num} Inches is {inc} Centimeters\nOr {banana} bananas.')
				print(f" = {inc}cm")

			elif "km" in splitcmd[1]: # 1km = 0.62mi
				inc = round(num/1.609, 2)
				tower = round(num/0.527, 2) # sears tower, 527m
				await message.channel.send(f'{num} Kilometres is {inc} Miles\nOr {tower} Sears towers.')
				print(f" = {inc}mi")
				
			elif "mi" in splitcmd[1]: # 1mi = 1.61km
				inc = round(num*1.609, 2)
				tower = round(inc/0.527, 2) # sears tower, 527m
				await message.channel.send(f'{num} Miles is {inc} Kilometres\nOr {tower} Sears towers.')
				print(f" = {inc}km")

			elif "ml" in splitcmd[1]: # 1ml = 0.03Fl Oz
				inc = round(num/29.574, 2)
				AriZona = round(inc/23, 2) # 23-ounce can of AriZona Iced Tea
				await message.channel.send(f'{num} Milliliters is {inc} Fluid Ounces.\nOr {AriZona} cans of AriZona Iced Tea.')
				print(f" = {inc}Fl Oz")

			elif "fl" in splitcmd[1]: # 1fl Oz = 29.57ml
				inc = round(num*29.574, 2)
				AriZona = round(num/23, 2) # 23-ounce can of AriZona Iced Tea
				await message.channel.send(f'{num} Fluid Ounces is {inc} Milliliters.\nOr {AriZona} cans of AriZona Iced Tea.')
				print(f" = {inc}ml")
				
			elif "ft" in splitcmd[1]: # 1ft = 0.3m
				inc = round(num/3.281, 2)
				Cows = round(inc/2.6, 2) # average length of a cow is 2.6m 
				await message.channel.send(f'{num} Foot is {inc} Meters\nOr {Cows} Cows.')
				print(f" = {inc}m")
				
			elif "kg" in splitcmd[1]: # 1kg = 2.21lb
				inc = round(num*2.205, 2)
				washer = round(inc/77.11, 2)
				await message.channel.send(f'{num} Kilograms is {inc} Pounds\nOr {washer} Washing machines.')
				print(f" = {inc}lb")
				
			elif "lb" in splitcmd[1]: # 1lb = 0.45kg
				inc = round(num/2.205, 2)
				washer = round(num/77.11, 2)
				await message.channel.send(f'{num} Pounds is {inc} Kilograms\nOr {washer} Washing machines.')
				print(f" = {inc}kg")
				
			elif "oz" in splitcmd[1]: # 1oz = 28.35g
				inc = round(num*28.35, 2)
				bullet = round(inc/7, 2) # 7 Grams
				await message.channel.send(f'{num} Ounces is {inc} Grams\nOr {bullet} 9×19mm Parabellum bullets')
				print(f" = {inc}g")
				
			elif "gal" in splitcmd[1]: # 1gal = 4.55l
				inc = round(num*4.546, 2)
				barrol = round(num/42 ,2) # 42 gallons
				await message.channel.send(f'{num} US liquid gallons is {inc} Liters\nOr {barrol} barrels of crude oil.')
				print(f" = {inc}l")
			
			elif "l" in splitcmd[1]: # 1l = 0.26gal # Discord wont let me have an upper case in a command?
				inc = round(num/3.785, 2)
				barrol = round(inc/42 ,2) # 42 gallons
				await message.channel.send(f'{num} Liters is {inc} US liquid gallons\nOr {barrol} barrels of crude oil.')
				if num == 2:
					await message.channel.send("Unless it's a 2 Liter soda bottle. Then it's just a 2L soda. Cans are fluid ounces (Fl Oz) though.")
				print(f" = {inc}gal")

			elif "m" in splitcmd[1]: # 1m = 3.28ft
				inc = round(num*3.281, 2)
				Cows = round(num/2.6, 2) #2.6m 
				await message.channel.send(f'{num} Meters is {inc} Foot\nOr {Cows} Cows.')
				print(f" = {inc}ft")


			elif "g" in splitcmd[1]: # 1g = 0.04oz
				inc = round(num/28.35, 2)
				bullet = round(num/7, 2) # 7 Grams
				await message.channel.send(f'{num} Grams is {inc} Ounces\nOr {bullet} 9×19mm Parabellum bullets')
				print(f" = {inc}oz")
				
			elif "c" in splitcmd[1]: # 1c = 33.8f
				inc = (num*1.8)+32
				hotdog = round(num/160, 2) # 160c
				await message.channel.send(f'{num} Celsius is {inc} Fahrenheit\nOr {hotdog} of the cooking temperature for hot dogs.')
				print(f" = {inc}f")
				
			elif "f" in splitcmd[1]: # 1f = -17.22c
				inc = round((num-32)*0.5556, 2)
				hotdog = round(inc/160, 2)
				await message.channel.send(f'{num} Fahrenheit is {inc} Celsius\nOr {hotdog} of the cooking temperature for hot dogs.')
				print(f" = {inc}c")
				
		# Unable to process command error messages.		
			else:
				await message.channel.send("Invalid command\nTry something like /sbb 12ft")
			
		except IndexError:
			await message.channel.send("Invalid command\nTry something like /sbb 12cm")
		
		# Bot is done, back to sleep.
		print("Done.")

		
#################################################################################################################################################		
# run the bot
#TODO: need a try and while true loop.... try except wasn't working for me, its not catching the RuntimeError: soo yeah I'll just leave it for now
print("Launching the bot..")
client.run(BotToken)
