import discord
from discord.ext import commands

intens = discord.Intents.default()
intens.message_content = True

bot=commands.Bot(command_prefix = "!", intents = intens)

@bot.event
async def on_ready():
    print(f"se inicio el bot{bot.user}")


descomposicion_residuos = {
    "botella de plastico":500,
    "lata de aluminio":40,
    "bolsa de plastico":150,
    "vidrio":4000
}

@bot.command()
async def impacto(ctx,*,objeto:str):
    objeto = objeto.lower()
    if objeto in descomposicion_residuos:
        tiempo = descomposicion_residuos[objeto]
        await ctx.send(f"El objeto {objeto} tarda aproximadamente {tiempo} años")

        if tiempo >= 100:
            await ctx.send("Porfavor reutilizar el producto o utilizar otro producto.")
    else:
        await ctx.send(f"No tenemos información de {objeto}")

@bot.command()
async def IA(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            await archivo.save(f"img/{nombre_archivo}")
        await ctx.send("Se guardo correctamente la información")
    else:
        await ctx.send("El mensaje no tiene una imagen, por favor, adjunte una")


bot.run("TOKEN")