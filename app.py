import discord
from discord.ext import commands
from discord import app_commands
import random
import time
import os
from server import keep_alive

bot = os.environ.get('token')
client = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@client.event
async def on_ready():
    print("Bot is ready.")
    await client.tree.sync()
    time.sleep(5)
    print(f"\x1Bc")

@client.tree.command(name='ด่า', description='Replies with bad word')
@app_commands.describe(ชื่อ="ชื่อคนที่ต้องการจะด่า")
async def bad(interaction: discord.Interaction, ชื่อ:str):
    random_number = random.randint(0, 3)
    badword = ["นิสัยไม่ดี", "ทำตัวแย่", "พูดมาก", "ไอ่เด็กเชี่ยยยย"]
    await interaction.response.send_message(f"{ชื่อ} {badword[random_number]}")
    print(f"{interaction.user.name} ใช้คำสั่ง ด่ากับชื่อ {ชื่อ}")

@client.tree.command(name='ask', description='สุ่มคำถามชวนคุย')
async def bad(interaction: discord.Interaction):
    rn = random.randint(0, 22)
    askthink = ["ชอบท่องเที่ยวมั้ย? สถานที่ที่คุณอยากไปท่องเที่ยวมากที่สุดคืออะไร?",
                "มีเรื่องราวตลกหรือเรื่องขำให้บอกมั้ย?",
                "ถ้ามีเวลาว่างในวันหยุด คุณชอบทำอะไร?",
                "มีความสนใจในกิจกรรมกลุ่มหรือกิจกรรมที่เกี่ยวกับความเป็นอยู่ร่วมกันมั้ย?",
                "มีฝันในการทำอะไรบ้างที่คุณยังไม่ได้ทำแต่อยากจะทำ?",
                "คุณชอบอ่านหนังสือมั้ย? มีเนื้อหาหรือเรื่องราวใดที่คุณชื่นชอบมากที่สุด?",
                "มีเพลงใดที่ทำให้คุณรู้สึกถึงความสุขหรือความรู้สึกอบอุ่นบ้าง?",
                "ถ้ามีโอกาสได้ทำงานในสถานที่ใดก็ได้ทั่วโลก คุณจะเลือกทำงานที่ไหนและทำอะไร?",
                "มีความฝันหรือเป้าหมายในชีวิตที่คุณอยากบังเอิญไปบอกคนที่คุณรักมั้ย?",
                "ถ้าคุณมีเวลา 24 ชั่วโมงเพื่อทำอะไรก็ได้ แต่ไม่ใช่การทำงานหรือการนอน คุณจะใช้เวลาไปทำอะไร?",
                "คุณมีเรื่องราวหรือประสบการณ์ใดที่เปลี่ยนแปลงวิธีคิดหรือมีอิทธิพลต่อชีวิตคุณอย่างมาก?",
                "ถ้าคุณได้มีโอกาสเรียนรู้สิ่งใดก็ได้ในโลก คุณจะเลือกเรียนรู้เรื่องใดและทำไม?",
                "สิ่งที่คุณคาดหวังจากความสัมพันธ์เพื่อนกับคนรักคืออะไร?",
                "ถ้าคุณมีโอกาสที่จะกลับไปย้อนเวลาและแนะนำตัวเองในอดีต คุณจะบอกอะไรกับตัวเองในวัยรุ่นหรือยุคเรียน?",
                "สิ่งที่คุณชอบทำในวันหยุดเพื่อผ่อนคลายและให้ความสุขแก่ตัวเองคืออะไร?",
                "ถ้าคุณได้เรียนรู้ภาษาหนึ่งภาษาใหม่ได้โดยไม่มีค่าใช้จ่าย คุณจะเลือกเรียนภาษาใดและทำไม?",
                "มีวันหยุดสุดท้ายในชีวิตของคุณ คุณคิดว่าคุณจะใช้เวลาอย่างไร?",
                "ถ้าคุณมีโอกาสที่จะเปลี่ยนสภาพอากาศในสถานที่ใดก็ได้ในโลก คุณจะเลือกสภาพอากาศไหนและทำไม?",
                "มีเหตุการณ์หรือประสบการณ์ใดในชีวิตที่ทำให้คุณรู้สึกอย่างเฉพาะเจาะจงหรือสำคัญมากที่สุด?",
                "ถ้าคุณได้มีโอกาสในการเดินทางไปย้อนเวลาและเลือกที่จะเปลี่ยนแปลงเหตุการณ์ใดในอดีต คุณจะทำอย่างไรและทำไม?",
                "มีเหตุการณ์หรือประสบการณ์ใดในชีวิตที่ทำให้คุณเรียนรู้เรื่องใหม่หรือพัฒนาตนเองมากที่สุด?",
                "ถ้าคุณได้มีโอกาสที่จะเลือกอาชีพใหม่ คุณจะเลือกทำอะไรและทำไม?",
                "สิ่งที่คุณคาดหวังจากชีวิตคืออะไรที่ทำให้คุณรู้สึกมั่นคงและมีความสุข?",
                "คุณมักจะเตรียมตัวในช่วงเช้าอย่างไรเพื่อให้วันของคุณเริ่มต้นอย่างดี?"]
    askrned = askthink[rn]
    askwho = discord.Embed(title="เอะจะเอาไปถามใครนะ?", description=askrned, colour=discord.Colour.random())
    askwho.set_image(url="https://www.animatedimages.org/data/media/562/animated-line-image-0289.gif")
    await interaction.response.send_message(embed=askwho, ephemeral=True)
    print(f"{interaction.user.name} ใช้คำสั่ง ask ได้คำว่า",askrned)

    
@client.tree.command(name='letter', description='ส่งข้อความหาใครสักคนและบอกคำใบ้ว่าคนส่งคือใคร')
@app_commands.describe(ส่งให้กับ="ส่งให้กับใคร", คำที่จะบอก="ชื่อคนที่ต้องการจะบอก", คำใบ้="ใบ้ว่าคนส่งคือใคร")
async def bai(interaction: discord.Interaction, คำที่จะบอก: str, คำใบ้: str, ส่งให้กับ: discord.User):
    channel = client.get_channel(1221354536824995961)
    embe = discord.Embed(title="ข้อความ", description=คำที่จะบอก, colour=discord.Colour.random())
    embe.add_field(name="คำใบ้จากผู้ส่ง", value=คำใบ้)
    embe.set_image(url="https://www.animatedimages.org/data/media/562/animated-line-image-0015.gif")
    tec = discord.Embed(title="ส่งข้อความเรียบร้อยแล้วค่ะ")
    await channel.send(f"ฝากถึง {ส่งให้กับ.mention}", embed=embe)
    print(f"{interaction.user.name} ใช้คำสั่ง letter ให้กับ",ส่งให้กับ,"ว่า",คำที่จะบอก,"ใบ้ว่า",คำใบ้)
    await interaction.response.send_message(embed=tec, ephemeral=True)
    

client.run(bot)
keep_alive()