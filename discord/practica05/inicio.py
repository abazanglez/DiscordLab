
import discord

import os

import re

import ssl

import aiohttp

import asyncio

from dotenv import load_dotenv



# --- CONFIGURACIÓN DE DISCORD Y VARIABLES DE ENTORNO ---

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')



# Definir los "intents" (permisos) necesarios

intents = discord.Intents.default()

intents.message_content = True  # Necesario para leer el contenido de los mensajes



client = discord.Client(intents=intents)



# --- LÓGICA DE TU AGENTE ---



def mostrar_bienvenida():

    """Retorna la lista de comandos disponibles."""

    return (

        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"

        "📜 Primeros pasos Agente Discord UX:\n"

        "📜 Escriba !Exit para salir del Agente:"

    )



def main_procesador(entrada):

    PREFIJO = "!"

    if not entrada.startswith(PREFIJO):

        if entrada: 

            print("Recuerda usar '!' para comandos.")

        return None

        

    # Procesamiento de la entrada

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)

    comando = cuerpo[0].lower()

    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    

    # Selección de acción (Estructura de control)

    if comando == "exit":

        print("Saliendo del gestor...")

        return "Saliendo del gestor..."

    elif comando == "inicio":

        print(mostrar_bienvenida())

        return mostrar_bienvenida()

    else:

        print(f" Error: Comando '!{comando}' no reconocido.")

        return f" Error: Comando '!{comando}' no reconocido."



# --- EVENTOS DE DISCORD ---



@client.event

async def on_ready():

    print(f'Sincronizado como {client.user} (ID: {client.user.id})')

    print('------')



@client.event

async def on_message(message):

    # Evitar que el bot se responda a sí mismo

    if message.author == client.user:

        return

        

    # Procesamiento: Pasamos el contenido del mensaje a nuestra lógica

    print(f"Mensaje recibido de {message.author}: {message.content}")



    # Solo procesamos si el mensaje empieza con un prefijo

    if message.content.startswith('!'):

        resultado = main_procesador(message.content)

        

        if resultado:

            print(f"Resultado del procesamiento: {resultado}")

            # Respuesta: El bot escribe el resultado en el mismo canal

            await message.channel.send(f" **Bot Procesador:** {resultado}")



# --- ARRANQUE ASÍNCRONO CON CORRECCIÓN SSL ---



async def iniciar_agente():

    # 1. Crear el contexto SSL que salta la verificación de macOS

    ssl_context = ssl.create_default_context()

    ssl_context.check_hostname = False

    ssl_context.verify_mode = ssl.CERT_NONE

    

    # 2. Inyectar el conector SSL en el cliente de Discord

    connector = aiohttp.TCPConnector(ssl=ssl_context)

    client.http.connector = connector

    

    # 3. Arrancar el cliente de forma segura

    async with client:

        await client.start(TOKEN)



# Ejecutar el programa principal

if __name__ == "__main__":

    if TOKEN:

        try:

            asyncio.run(iniciar_agente())

        except KeyboardInterrupt:

            print("\nAgente apagado de forma segura.")

    else:

        print("ERROR: No se encontró el TOKEN en el archivo .env")
