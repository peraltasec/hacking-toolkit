

# Shodan – Pesquisa de Dispositivos Conectados à Internet

Shodan permite **descobrir dispositivos expostos à internet**.

## Exemplos de Uso

```bash
# Buscar servidores Apache
shodan search apache

# Filtrar por país
shodan search apache country:BR

# Obter detalhes de um host
shodan host <IP>
