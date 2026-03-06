#!/bin/bash
# Monitor de logs em tempo real

echo "Monitorando /var/log/syslog... (Ctrl+C para sair)"
tail -f /var/log/syslog
