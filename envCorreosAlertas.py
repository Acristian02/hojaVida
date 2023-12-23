import smtplib
import psutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor de correo
#Desde este correo se deben dar permisos a python
email_add = 'correo envia'
email_pass = 'contraseña generada por gmail'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Envia un correo electrónico
def envio(Sj, body):
    De = email_add
    Para = 'correo que resive'  # Reemplaza con la dirección del destinatario

    # Configuración del mensaje
    msg = MIMEMultipart()
    msg['De'] = De
    msg['a'] = Para
    msg['Sj'] = Sj

    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Conexión SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_add, email_pass)

    # Envia correo
    server.sendmail(De, Para, msg.as_string())

    # Cierra conexión
    server.quit()

# Verificar el uso del disco
def Uso_Disco():
    threshold_percent = 40  # Puedes ajustar este umbral según tus necesidades

    # Obtener la información del disco
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > threshold_percent:
        Sj = 'Alerta: Espacio en disco lleno'
        body = f'El espacio en disco está al {disk_usage.percent}% de su capacidad.'
        envio(Sj, body)

# Verificar procesos
def Uso_Procesos():
    threshold_cpu_percent = 80  # Puedes ajustar este umbral según tus necesidades

    # Obtener la lista de procesos
    processes = psutil.process_iter()

    # Verificar el uso de CPU de cada proceso
    for process in processes:
        try:
            cpu_percent = process.cpu_percent()
            if cpu_percent > threshold_cpu_percent:
                Sj = 'Alerta: Alto uso de CPU'
                body = f'El proceso {process.name()} está utilizando el {cpu_percent}% de la CPU.'
                envio(Sj, body)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Llamar a las funciones de verificación
Uso_Disco()
Uso_Procesos()