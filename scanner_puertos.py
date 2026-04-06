import socket

objetivo = input("Ingresa la Ip o sitio web:")
print(f"Escanenado {objetivo}...\n")

for puerto in range(1,1025):
  cliente =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  cliente.settimeout(0.5)

  resultado = cliente.connect_ex((objetivo, puerto))
  
  if resultado == 0:
    print(f"puerto {puerto} está abierto")

  cliente.close()

