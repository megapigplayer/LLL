import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import os


Client = commands.Bot(command_prefix = "+")
Client.remove_command("help")
owner = ["Insert-Owner-ID"]

@Client.event
async def on_ready():
    print("Bot Is ready!")


@Client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.mute_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant mute this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.kick_members or ctx.message.author.id == '194151340090327041':
       await Client.kick(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Kicked!", description="**{0}** was kick by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant kick this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def warn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.move_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Warn')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User Warned!", description="**{0}** was warned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant warn this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
       await Client.ban(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Baned!", description="**{0}** was ban by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant ban this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def clear(ctx, amount=100):
    if ctx.message.author.server_permissions.manage_messages or ctx.message.author.id == '194151340090327041':
       channel = ctx.message.channel
       messages = []
       async for message in Client.logs_from(channel, (amount)):
            messages.append(message)
       await Client.delete_messages(messages)
       await Client.say("**The Messages delete!**")
    else:
        embed=discord.Embed(title="You cant Do This Command!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await Client.change_presence(game=discord.Game(name=game))
        except:
            await Client.say("Failed to change game")
        else:
            await Client.say("Successfuly changed game to {}".format(game))
    else:
        await Client.send_cmd_help(ctx)

@Client.command()
async def servers():
  	"""Bot Guild Count"""
  	await Client.say("**I'm in {} servers!**".format(len(Client.servers)))

@Client.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await Client.reply("{}".format(ctx.message.server.icon_url))

@Client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await Client.reply("{}".format(member.avatar_url))

@Client.command(pass_context=True)
async def question(ctx):

	possible_responses = ["לא", "כן", "אני לא בטוח, תשאל שוב אולי אני יחליט"]

	current_response = random.choice(possible_responses)

	await Client.say(current_response)

@Client.command(pass_context = True)
async def instantwarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.move_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='instantwarn')
        await Client.add_roles(member, role)
        embed=discord.Embed(title="User instantWarned!", description="**{0}** was instantwarned by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await Client.say(embed=embed)
     else:
        embed=discord.Embed(title="You cant instantwarn this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)


@Client.command(pass_context = True)
async def removewarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.send_messages or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='instantwarn')
        await Client.remove_roles(member, role)
	
@Client.command()
async def say(output):
    await Client.say(output)


@Client.command()
async def info():
        await Client.say("""Hello! My name is MegaBot!
I have 3 types of commands:
**Information Commands**
**General Commands**
**Staff Commands**
For see all the commands type: __+help__""")

@Client.command()
async def creator():
        await Client.say("""**My Creator Is MegaPig#1576!**
__If you see bug in the bot say to him!__
__And you can ask him for support!__""")
        await Client.add_reaction('\U0001F44D')

@Client.command()
async def invite():
        await Client.say("""https://discordapp.com/api/oauth2/authorize?client_id=459490391146627073&permissions=8&scope=bot
__You Can Invite Me When Ever You Want!__
You Can Help If You Say Bugs To My Creator- **MegaPig#1576**""")

@Client.command()
async def help():
        embed = discord.Embed(title="Command List", description="""
__**Information Commands**__
**+info** - Small Information Of The Bot.
**+invite** - The Bot Invite Link.
**+creator** - The Bot Creator.
__**General Commands**__
**+avatar @tag** - The avatar of the member.
**+servericon** - the picture of the server.
**+servers** - how many servers the bot in.
**+question (שאלת כן ולא)** - The Bot answear to you.
__**Staff Commands**__
**+warn** @TAG- warn member (move members permission)
**+mute** @TAG- mute member (mute members permission)
**+clear (2-100)** - clear messages (manage_messages permission)
**+kick** @TAG - kick member (kick members permission)
**+ban** @TAG - ban member (ban members permission)
""", color=0xe88af4)
        await Client.say(embed=embed)

@Client.command()
async def תצעק():
        await Client.say("האהאהאההאהאהאהאהאהאהאהאאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאאהאההאהההאהאהאהאהאהאאהאהאהאהאהאהאאהאאאהאאאהאהאהאאהאההאהאאההאהאאהאהאהאהאאהאהאהאהאהאהאהאאהאהאהאהאהאאהאהאהאהאהאהאאהאהאהאהאאהאהאהאהאאהאהאהאהאהאהאהאהאההאההאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאהאההאהאהאאהאהאהאהאההאאהאהאהאהאהאהאהאהאהאהאאהאהאהאהאאההאאהאהאהאהאהאהאהאהאהאאאהאהאהאהאהאהאהאהאהאהה")

@Client.command(pass_context=True)
async def story(ctx):

	possible_responses = ["""כוחן של מילים - עידוד `סיפור מספר 1` 

להקה של צפרדעים טיילו להם ביער, לפתע נפלו שני צפרדעים לתוך בור עמוק מאוד. כל שאר הצפרדעים התגודדו יחד סביב הבור. כשהם ראו עד כמה הבור עמוק הם צעקו לצפרדעים שנפלו: 

"חבר'ה, אין לכם שום סיכוי שתצאו מכאן בחיים... אתם נחשבים כבר למתים... 
חבל לכם בכלל להתאמץ!" 
לצפרדעים שנפלו לא היה שום חשק לוותר על חייהם בכזאת קלות. שני הצפרדעים התעלמו מהצעקות והסימנים של חבריהם מלמעלה וניסו לקפוץ החוצה בכל כוחם, בשעה שהצפרדעים שמחוץ לבור ממשיכים לצעוק להם ולסמן להם בכל מיני דרכים עם הידים שאין להם סיכוי... "בחיים לא תצאו מכאן..." 

אחד הצפרדעים שמע בעצתם של הצפרדעים, אפסו כוחותיו, הוא פשוט נכנע ומת בקרקעית הבור. הצפרדע השני, לא ויתר, הוא ניסה והמשיך בכל כוחו בשעה שהצפרדעים מסמנים לו בתנועות וצועקים מפתח הבור "חבל על המאמץ... אין לך שום סיכוי בעולם...". 
"הפסק את המאמץ והסבל שלך, ופשוט תמות". 
בכל זאת הצפרדע המשיך לנסות, הוא קפץ אפילו חזק יותר... ובסופו של דבר, הוא נתן ניתור כזה חזק שהצליח לצאת החוצה מהבור כשהוא יצא החוצה, שאלו אותו חבריו הצפרדעים: 
"איך עשית את זה? הבור היה ממש עמוק..." 
בשפת הסימנים הסביר להם הצפרדע הזה כי הוא חירש... הוא לא שמע מה אומרים לו, ובטעות פירש את קריאותיהם הנרגשות כמילות עידוד... 

מוסר השכל 
1. בלשוננו יש את הכוח לחיים ויש את הכוח להרוג 

2. מילים הרסניות למי שנמצא למטה לא יעלו אותו למעלה 

3. עידוד זה כוח - לחצו כאן כדי ללמוד איך מעודדים 

""", """סיפור מארץ נכר נושא עמו מסר מסתובב לאחרונה במחוזותינו : 
לפני זמן מה, העניש אב את בתו הקטנה על שבזבזה גליל נייר שלם 
מוזהב מיוחד ויקר ערך . 
המשפחה חיה בדוחק וכעס האב התגבר כשגילה שבתו השתמשה 
בנייר גם כדי לעטוף קופסת קרטון כמתנה לחג המולד. 

ביום שלאחר מכן, הביאה הילדה את הקופסה במתנה לאביה."זה בשבילך, אבא". 
האב בוש בהתנהגותו הזועמת, אבל זעמו גאה שוב כאשר ראה 
שהקופסה ריקה מתוכן. הוא פנה אל בתו בטון כועס ואמר לה: "את 
לא יודעת, גבירתי הצעירה, שכאשר נותנים למישהו מתנה לחג 
המולד אמורים לשים משהו בתוך הקופסה?" 

הילדה, עם דמעות בעיניים, ענתה לאביה: "אבל אבא, כן שמתי משהו 
בקופסה. הכנסתי לתוכה המון המון נשיקות בשבילך עד שהיא התמלאה". 
האבא כרע על ברכיו וביקש מהילדה שתסלח לו על כעסו הלא מוצדק. 
לא עבר זמן רב, אסון נפל על המשפחה - הילדה נהרגה בתאונה. 

מספרים כי אביה שמר את קופסת הזהב ליד מיטתו עד סוף חייו. 
ובכל פעם שהרגיש מדוכא או עצוב או חסר כוחות הוא פתח את 
הקופסה והוציא ממנה נשיקה דמיונית אותה שמה עבורו בתו, 
הילדה שאהבה אותו כל כך. 


כל אחד מאיתנו קיבל במתנה קופסת זהב, 
מלאה באהבה מהסובבים אותנו וללא תנאים : 

- מההורים, מהאחים ומהילדים שלנו, מכל המשפחה. 
-	מחברים ומידידים . 
-	מפרחים , מבעלי חיים , מיופי הטבע והבריאה . 
-	מאלוהים 

לא קיים נכס יקר יותר. 

עתה, יש בידיכם שתי אפשרויות: 
1. להתייחס למסר ולספר את הסיפור לכמה שיותר אנשים. 
2. לשכוח שאי פעם שמעתם אותו ולהתעלם מהעובדה שהוא נגע ללבכם. 

רק זכרו אהבה, 
אהבת המשפחה החברים והסובבים אותנו 
היא כמו מלאכים שמעמידים אותנו על רגלינו 
בכל פעם שהכנפיים שלנו לא זוכרות כיצד לעוף. 
""", """יש דברים מרובים חשובים בעולם אך החשוב מכולם הוא... ביתו של האדם 
וכמו שאדם מאדם הוא שונה, כך שונים הבתים שאותם הוא בונה... 

יש בית שהוא מבצר על ההר, יש בית והוא כ-ארמון מפואר. 
אך לא העיקר הוא ארמון או בקתה, החשוב הוא ה- בית שבנית אתה. 

כי בית אינו רק אבנים וקירות, כי בית אינו רק צריף של דירות 
כי בית אינו סתם מבנה של בטון, כי בית מעניק הרגשת ביטחון 
כי בית הוא שולחן או מפה, כי בית הוא ילד , רעיה מצפה. 
כי בית הוא גג ופינה חמימה, וברית כרותה בין איש לאישה. 
יש בתי עשירים העולים כסף רב, ארמונות נוצצים מצופים בזהב 
ארמונות נוצצים הנראים כ- מעשה אומנות, אך הבא לתוכם מרגיש ריקנות. 
יש בית והוא צריף או צריפון, יש בית והוא רק אוהל קטון. 
ויש בית והוא רק מצע על הקש, אבל מה שחשוב הוא "איך המרגש?". 

על כן חשוב להיזכר ולזכור, כי על הבית צריך להגן ולשמור. 
כי רבים דברים יקרים בעולם, אך אין כה יקר כ-ביתו של אדם. 
"""]

	current_response = random.choice(possible_responses)

	await Client.say(current_response)

                    

Client.run(os.getenv('TOKEN'))
