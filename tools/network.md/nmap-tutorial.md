# Nmap – Scanner de Portas e Hosts

O Nmap é uma das ferramentas mais usadas em **network pentesting e análise de rede**.  
Ele permite descobrir hosts ativos, portas abertas e serviços rodando.

## Exemplos de uso

1. **Scan básico**

```bash
nmap 192.168.1.1


SYN scan (mais rápido)

nmap -sS 192.168.1.1


Scan de múltiplas portas

nmap -p 1-1000 192.168.1.1


Detecção de sistema operacional

nmap -O 192.168.1.1
