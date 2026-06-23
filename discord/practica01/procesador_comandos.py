import datetime

def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """
    return f"¡Hola! Soy {nombre_bot} y estoy listo para ayudarte."
    
def procesar_comando_recordar(comando):
    """
    Valida y procesa la accion de recirdar un dato
    """
    if not comando:
        return"Error: falta el nombre. Uso !recordar [nombre]"
    return f"¡He recordado el nombre '{comando}'"

def calcular_uptime(hora_inicio):
    """
    Calcula la diferencia de tiempo entre el inicio
    y el actual (mostrar actividad del bot)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {diferencia}"

def mostrar_ayuda():
    """
    Comandos disponibles para el usuario
    """
    return {
        "comandos disponibles:\n"
        "!recordar [nombre] - El bot recordará el nombre proporcionado.\n"
        "!uptime - Muestra el tiempo que el bot ha estado activo.\n"
        "!ayuda - Muestra esta lista de comandos.\n"
    }
    
def iniciar_agente():
    NOMBRE_BOT = "Enrique"
    PREFIJO = "!"
    hora_inicio = datetime.datetime.now()
    
    print(f"{obtener_saludo(NOMBRE_BOT)}")
    print("Escribe '!ayuda' para ver los comandos disponibles.")
    
    ejecutando = True
    while ejecutando:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()
        
        if not entrada.startswith(PREFIJO):
            print("Comando no reconocido.")
            continue
        
        partes = entrada[len(PREFIJO):].split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else ""
        
        if comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        elif comando == "finalizar":
            print("Finalizando el agente. ¡Hasta luego!")
            ejecutando = False
        elif comando == "recordar":
            print(procesar_comando_recordar(argumento))
        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
        else:
            print("Comando no reconocido.")
            

def main():
    iniciar_agente()
    

if __name__ == "__main__":
    main()