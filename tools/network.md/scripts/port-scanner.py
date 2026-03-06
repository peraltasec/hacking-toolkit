
# Scanner de portas simples
import socket

target = input("Digite o IP alvo: ")
print(f"\nEscaneando portas de {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((target, port)) == 0:
        print(f"[ABERTA] Porta {port}")
    s.close()

print("\nEscaneamento concluído. Use sempre em ambientes autorizados!")
