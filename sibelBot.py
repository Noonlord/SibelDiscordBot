import random
import discord
import os
from datetime import *
from pytz import timezone
import pytz
from tinydb import TinyDB, Query
db = TinyDB("database.json")
client = discord.Client()

@client.event
async def on_message(message):

	if message.content.startswith("-kick") and (message.author.permissions_in(message.channel).administrator):
		try:
			userToKick = message.mentions[0]
		except:
			await message.channel.send("Kicklenecek kullanıcıyı etiketleyin")
		if userToKick:
			try:
				await userToKick.kick()
			except:
				await message.channel.send("Bunu yapmak için yeterli iznim yok")

	if message.content.startswith("-ban") and (message.author.permissions_in(message.channel).administrator):
		try:
			userToBan = message.mentions[0]
		except:
			await message.channel.send("Banlanacak kullanıcıyı etiketleyin")
		if userToBan:
			try:
				await userToBan.ban()
			except:
				await message.channel.send("Bunu yapmak için yeterli iznim yok")
	if message.content.startswith("-tekrar"):
		msg = message.content[7:]
		try:
			await message.delete()
		except:
			pass
		await message.channel.send(msg)

	if message.content.startswith("-kisi") or message.content.startswith("-kişi"):
		for i in message.guild.members:
			try:
				embedKisi = discord.Embed(description=i.activity.name,  title = i.name + " oynuyor:"  ,color=0x00e600)
				embedKisi.set_thumbnail(url = i.avatar_url)
				if i.bot == False:
					await message.channel.send(embed=embedKisi)
			except:
				pass
	if message.content.startswith("-spotify"):
		for i in message.guild.members:
			try:
				if "Spotify" in i.activity.name:
					embedd = discord.Embed(title=i.activity.title, url = "https://open.spotify.com/track/" + i.activity.track_id, description = i.activity.artist ,color=0x00e600)
					embedd.set_thumbnail(url = i.activity.album_cover_url)
					embedd.add_field(name= i.name, value="Dinliyor", inline=True)
					embedd.add_field(name= "Uzunluk", value = str(i.activity.duration)[:-7], inline=True)
					await message.channel.send(embed=embedd)
			except:
				pass

	if message.content.startswith("-avatar"):
		if message.content == "-avatar server":
			embedd = discord.Embed(title = message.guild.name, url = "https://cdn.discordapp.com/icons/" + str(message.guild.id) + "/" + message.guild.icon + ".png?size=1024", color=0x00e600)
			embedd.set_image(url = "https://cdn.discordapp.com/icons/" + str(message.guild.id) + "/" + message.guild.icon + ".png?size=1024")
			await message.channel.send(embed=embedd)
		else:
				try:
					embedd = discord.Embed(title = message.mentions[0].name, url = str(message.mentions[0].avatar_url), color=0x00e600)
					embedd.set_image(url = message.mentions[0].avatar_url)
					await message.channel.send(embed=embedd)
				except:
					embedd = discord.Embed(title = message.author.name, color=0x00e600)
					embedd.set_image(url = message.author.avatar_url)
					await message.channel.send(embed=embedd)

	if message.content.startswith("-bot"):
		await message.channel.send("https://discordapp.com/api/oauth2/authorize?client_id=535037957128585236&permissions=8&scope=bot")
	
	if message.content.startswith("-server"):
		serName = message.guild.name
		serReg = message.guild.region
		serAfkTime = message.guild.afk_timeout
		serOwner = message.guild.owner
		serMembers = message.guild.members
		serIcon = message.guild.icon_url
		serChannelCount = message.guild.channels
		serCreated = str(message.guild.created_at)

		now = datetime.now()
		old = message.guild.created_at
		diff = now - old
		creationTime = serCreated[:-15] + "(" + str(diff).split(",")[0].replace("days", "gün") + ")"

		embedd = discord.Embed(color=0x00e600)
		embedd.set_author(name = "Server Bilgileri", icon_url = serIcon)
		embedd.set_thumbnail(url = serIcon)
		embedd.add_field(name= "Adı:",value=serName , inline=True)
		embedd.add_field(name= "Server Bölgesi:", value = serReg, inline=True)
		embedd.add_field(name= "Afk Zamanı:", value = str(serAfkTime) + " Saniye", inline=True)
		embedd.add_field(name= "Sahibi:", value = serOwner , inline=True)
		embedd.add_field(name= "Üye Sayısı", value = len(serMembers), inline=True)
		embedd.add_field(name= "Kanal Sayısı", value = len(serChannelCount), inline=True)
		embedd.add_field(name= "Server Oluşturma Tarihi", value = creationTime, inline=True)
		await message.channel.send(embed = embedd)
	
	if message.content.startswith("-profil"):
		try:
			lookupUser = message.mentions[0]
		except:
			lookupUser = message.author
		username = lookupUser.name
		IDofUser = str(lookupUser.id)
		isBot = lookupUser.bot
		MemRoles = ""
		for i in lookupUser.roles:
			MemRoles = MemRoles + ", " + i.name
		isBot = lookupUser.bot
		if isBot:
			isBotstr = "Evet"
		else:
			isBotstr = "Hayır"
		if lookupUser.id == 337673625547046923:
			isBotstr = "Evet"
		simdi = datetime.now()
		eski = lookupUser.created_at
		fark = simdi - eski
		creationTime = str(lookupUser.created_at)[:-15] + "(" + str(fark).split(",")[0].replace("days", "gün") + ")"
		displayName = str(lookupUser.display_name)
		embedd = discord.Embed(color=0x00ff33)
		embedd.set_author(name=lookupUser.name,icon_url=lookupUser.avatar_url)
		embedd.add_field(name = "İsim: ", value = username, inline = True)
		embedd.add_field(name = "Sunucudaki İsim: ", value = displayName, inline = True)
		embedd.add_field(name = "ID: ", value = IDofUser, inline = True)
		embedd.add_field(name = "Bot: ", value = isBotstr, inline = True)
		embedd.add_field(name = "Roller: ", value = MemRoles[12:], inline = True)
		embedd.set_thumbnail(url = lookupUser.avatar_url)
		embedd.add_field(name = "Oluşturma zamanı: ", value = creationTime, inline = False)
		await message.channel.send(embed=embedd)
	if message.content.startswith("-yazitura"):
		sayi = random.randint(1, 100)
		if sayi < 50:
			metin = "Tura."
		if sayi > 50:
			metin = "Yazı."
		if sayi == 50:
			metin = "Dik geldi."
		await message.channel.send(metin)

	if message.content.startswith("-yardım") or message.content.startswith("-yardim"):
		embedd = discord.Embed(title = "Yardım Paneli", color=0x00e600)
		embedd.add_field(name = "-tekrar", value = "Yazdıklarınızı Tekrar Eder", inline = True)
		embedd.add_field(name = "-kisi", value = "Sunucudaki Aktiviteleri Gösterir", inline = False)
		embedd.add_field(name = "-spotify", value = "Spotify Dinleyenleri Gösterir", inline = True)
		embedd.add_field(name = "-avatar", value = "Avatar'ınızı Gösterir", inline = False)
		embedd.add_field(name = "-bot", value = "Botun Davet Linkini Atar", inline = False)
		embedd.add_field(name = "-yazitura", value = "Yazı - Tura Atar", inline = True)
		embedd.add_field(name = "-tas / kagit / makas", value = "Botla Tas Kağıt Makas Oynarsınız", inline = False)
		embedd.add_field(name = "-profil", value = "Profil Detaylarını Gösterir", inline = False)
		embedd.add_field(name = "-log", value = "-log \#(log tutulması istediğiniz kanal)", inline = False)
		embedd.add_field(name = "-server", value = "Server Bilgilerini Verir", inline = False)
		await message.channel.send(embed=embedd)

	if message.content.startswith("-tas") or message.content.startswith("-taş"):
		oyunList = ["tas", "kagit", "makas"]
		secilen = random.choice(oyunList)
		if secilen == "tas":
			await message.channel.send("Taş seçtim. Berabere.")
		elif secilen == "makas":
			await message.channel.send("Makas seçtim. Kazandın.")
		elif secilen == "kagit":
			await message.channel.send("Kağıt seçtim. Kaybettin")

	if message.content.startswith("-kagit") or message.content.startswith("-kağıt"):
		oyunList = ["tas", "kagit", "makas"]
		secilen = random.choice(oyunList)
		if secilen == "tas":
			await message.channel.send("Taş seçtim. Kazandın.")
		elif secilen == "makas":
			await message.channel.send("Makas seçtim. Kaybettin.")
		elif secilen == "kagit":
			await message.channel.send("Kağıt seçtim. Berabere")

	if message.content.startswith("-makas"):
		oyunList = ["tas", "kagit", "makas"]
		secilen = random.choice(oyunList)
		if secilen == "tas":
			await message.channel.send("Taş seçtim. Kaybettin.")
		elif secilen == "makas":
			await message.channel.send("Makas seçtim. Berabere.")
		elif secilen == "kagit":
			await message.channel.send("Kağıt seçtim. Kazandın")
	if message.content.startswith("-log"):
		if message.author.permissions_in(message.channel).administrator or message.author.id == 368452825069387786 or message.author.id == 262192783702360074:
			try:
				logGuild = str(message.guild.id)
				logChannel = str(message.channel_mentions[0].id)
				dbQuery = Query()
				if db.search(dbQuery.server_id == logGuild):
					db.remove(dbQuery.server_id == logGuild)
				db.insert({"server_id": logGuild, "channel_id" : logChannel})
				await message.channel.send("**\#" + message.channel_mentions[0].name + "** log kanalı olarak ayarlandı.")
			except:
				embedd = discord.Embed(title = "Kullanım", color=0xff0000)
				embedd.add_field(name = "-log", value = "-log #kanal", inline = True)
				embedd.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Red_information_icon_with_gradient_background.svg/1024px-Red_information_icon_with_gradient_background.svg.png")
				await message.channel.send(embed = embedd)
	if message.content.startswith("-sil"):
		if message.author.permissions_in(message.channel).administrator:
			limit = message.content[4:]
			await message.channel.purge(limit = int(limit) + 1)
@client.event
async def on_message_delete(message):
	#os.chdir("C:\\Users\\varda")
	os.chdir("/home/metin/metin")
	fileOp = open("logs.txt", "a")
	try:
		fileOp.write("SİLİNDİ Kullanıcı " + message.author.name + " @ " + message.guild.name + " / " + message.channel.name +  "  //  " +  message.content + " \n")
	except:
		fileOp.write("SİLİNDİ Kullanıcı " + message.author.name + "  //  " +  message.content + " \n")
	fileOp.close()
	dbQuery = Query()
	if db.search(dbQuery.server_id == str(message.guild.id)) and message.author.bot is False:
		channelID = int(db.search(dbQuery.server_id == str(message.guild.id))[0].get("channel_id"))
		messageChannel = client.get_channel(channelID)
		embedd = discord.Embed(title= "#" + message.channel.name + " kanalındaki mesaj silindi", description=message.content, color=0xff0000, timestamp = datetime.utcnow())
		embedd.set_author(name=message.author.name,icon_url=message.author.avatar_url)
		await messageChannel.send(embed = embedd)
	
@client.event
async def on_message_edit(before, after):
	if before.content is not after.content and after.author.bot is False:
		fileOp = open("logs.txt", "a")
		try:
			fileOp.write("DÜZENLENDİ Kullanıcı " + after.author.name + " @ " + after.guild.name + " / " + after.channel.name +  "  //  " + before.content + " ==> " + after.content + "\n")
		except:
			fileOp.write("DÜZENLENDİ Kullanıcı " + after.author.name +  "  //  " + before.content + " ==> " + after.content + "\n")
		fileOp.close()
		dbQuery = Query()
		if db.search(dbQuery.server_id == str(after.guild.id)):
			channelID = int(db.search(dbQuery.server_id == str(after.guild.id))[0].get("channel_id"))
			messageChannel = client.get_channel(channelID)
			embedd = discord.Embed(title= "#" + after.channel.name + " kanalındaki mesaj düzenlendi", description=before.content + " ==> " + after.content, color=0xff8888, timestamp = datetime.utcnow())
			embedd.set_author(name=after.author.name,icon_url=after.author.avatar_url)
			await messageChannel.send(embed = embedd)
	
@client.event
async def on_voice_state_update(member, before, after):
	fileOp = open("logs.txt", "a")
	timeZone = pytz.timezone('Europe/Istanbul')
	activityTime = datetime.now(timeZone).strftime("%c")
	if before.channel is not after.channel and before.channel is not None and after.channel is not None:
		fileString = "AYRILDI Kullanıcı " + member.name + " " + before.channel.guild.name + " / " + before.channel.name + " @ " + activityTime
	if before.channel is not after.channel and after.channel is not None:
		fileString = "BAĞLANDI Kullanıcı " +  member.name + " " + after.channel.guild.name + " / " + after.channel.name + " @ " + activityTime
		dbQuery = Query()
		if db.search(dbQuery.server_id == str(after.channel.guild.id)):
			channelID = int(db.search(dbQuery.server_id == str(after.channel.guild.id))[0].get("channel_id"))
			messageChannel = client.get_channel(channelID)
			embedd = discord.Embed(title= after.channel.name + " kanalına bağlandı", color=0x00ff44, timestamp = datetime.utcnow())
			embedd.set_author(name=member.name,icon_url=member.avatar_url)
			await messageChannel.send(embed = embedd)
	if after.channel is None:
		fileString = "AYRILDI Kullanıcı  " + member.name +" " +  before.channel.guild.name + " / " + before.channel.name + " @ " + activityTime
		dbQuery = Query()
		if db.search(dbQuery.server_id == str(before.channel.guild.id)):
			channelID = int(db.search(dbQuery.server_id == str(before.channel.guild.id))[0].get("channel_id"))
			messageChannel = client.get_channel(channelID)
			embedd = discord.Embed(title= before.channel.name + " kanalından ayrıldı", color=0xff4400, timestamp = datetime.utcnow())
			embedd.set_author(name=member.name,icon_url=member.avatar_url)
			await messageChannel.send(embed = embedd)
	try:
		fileOp.write(fileString + "\n")
	except:
		pass
	fileOp.close()
client.run("YourOwnPreciousToken")
