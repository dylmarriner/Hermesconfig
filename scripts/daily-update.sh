#!/usr/bin/env bash
# Daily Hermes Update - Lin (git-based venv)
LOGFILE="$HOME/.hermes/daily-update.log"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === HERMES DAILY UPDATE START ===" >> "$LOGFILE"
export PATH="$HOME/.local/bin:$HOME/.hermes/hermes-agent/venv/bin:$PATH"
BEFORE=$(hermes version 2>/dev/null | head -1)
cd "$HOME/.hermes/hermes-agent" || { echo "FAIL: cant cd to repo" >> "$LOGFILE"; exit 1; }
git stash push -m "pre-update-$(date +%Y%m%d-%H%M%S)" -- ':!plugins/memory/nexus/' 2>/dev/null || true
hermes update -y 2>&1 >> "$LOGFILE"
UPDATE_EXIT=$?
STASH_COUNT=$(git stash list | wc -l)
if [ "$STASH_COUNT" -gt 0 ]; then
    git stash pop 2>&1 >> "$LOGFILE" || true
fi
AFTER=$(hermes version 2>/dev/null | head -1)
echo "BEFORE: $BEFORE" >> "$LOGFILE"
echo "AFTER:  $AFTER" >> "$LOGFILE"
echo "Restarting gateway..." >> "$LOGFILE"
hermes gateway restart 2>&1 >> "$LOGFILE"
GATEWAY_EXIT=$?
echo "[$(date '+%Y-%m-%d %H:%M:%S')] === END (update=$UPDATE_EXIT, gateway=$GATEWAY_EXIT) ===" >> "$LOGFILE"
exit $((UPDATE_EXIT + GATEWAY_EXIT))
