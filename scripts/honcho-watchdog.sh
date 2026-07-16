#!/bin/bash
# Honcho stack watchdog -- runs every 60s via cron (no-agent mode).
# Restarts unhealthy containers and reports issues.
COMPOSE_DIR="/home/lin/honcho"
COMPOSE="docker compose"
LOG_TAG="[honcho-watchdog]"
cd "$COMPOSE_DIR" || { echo "$LOG_TAG ERROR: cannot cd to $COMPOSE_DIR"; exit 1; }
UNHEALTHY=$($COMPOSE ps --format '{{.Name}} {{.Status}}' 2>/dev/null | grep -i 'unhealthy' | awk '{print $1}')
EXITED=$($COMPOSE ps --format '{{.Name}} {{.Status}}' 2>/dev/null | grep -i 'exited' | awk '{print $1}')
MESSAGES=""
for c in $UNHEALTHY; do echo "$LOG_TAG Restarting unhealthy container: $c"; $COMPOSE up -d --no-deps "${c%%-1}" 2>&1 | tail -1; MESSAGES="$MESSAGES restarted-unhealthy:$c"; done
for c in $EXITED; do echo "$LOG_TAG Restarting exited container: $c"; $COMPOSE up -d --no-deps "${c%%-1}" 2>&1 | tail -1; MESSAGES="$MESSAGES restarted-exited:$c"; done
EXPECTED="api database deriver redis"
for svc in $EXPECTED; do
    STATUS=$($COMPOSE ps --format '{{.Name}} {{.Status}}' 2>/dev/null | grep "honcho-${svc}-1" | head -1)
    if echo "$STATUS" | grep -qiE '(exited|unhealthy)'; then MESSAGES="$MESSAGES still-broken:$svc"
    elif [ -z "$STATUS" ]; then MESSAGES="$MESSAGES missing:$svc"; fi
done
HONCHO_CPU=$($COMPOSE top 2>/dev/null | grep -v 'UID\|PID' | awk '{sum+=$3} END {print int(sum)}')
if [ -n "$HONCHO_CPU" ] && [ "$HONCHO_CPU" -gt 50 ] 2>/dev/null; then MESSAGES="$MESSAGES high-cpu:${HONCHO_CPU}%"; fi
if [ -n "$MESSAGES" ]; then echo "$LOG_TAG $(date '+%Y-%m-%d %H:%M:%S') $MESSAGES"
    if echo "$MESSAGES" | grep -q 'still-broken\|missing'; then echo "$LOG_TAG Some services still broken -- attempting full stack restart"; $COMPOSE down && $COMPOSE up -d 2>&1 | tail -5; fi
    exit 1
fi
exit 0
