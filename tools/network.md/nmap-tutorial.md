# Nmap – Scanner de Portas e Hosts

O Nmap permite descobrir **hosts ativos, portas abertas e serviços**.

## Exemplos de Uso

```bash
# Scan básico
nmap 192.168.1.1

# SYN scan
nmap -sS 192.168.1.1

# Scan de múltiplas portas
nmap -p 1-1000 192.168.1.1

# Detectar sistema operacional
nmap -O 192.168.1.1
