# Cron Jobs — 2026-07-16

## System Cron (crontab)

### 1. Daily Hermes Update
- **Schedule**: 0 3 * * * (daily 3:00 AM)
- **Script**: `/home/lin/.hermes/scripts/daily-update.sh`
- **Action**: Stash local changes, `hermes update -y`, pop stash, restart gateway

### 2. Universal Unlock Suite Dark Web Crawl
- **Schedule**: 0 */12 * * * (every 12 hours)
- **Script**: `~/Documents/universal-unlock-suite && python3 scripts/crawl_darkweb.py`
- **Log**: `~/unlock_crawl.log`

### 3. Nexus Sync
- **Schedule**: */5 * * * * (every 5 minutes)
- **Command**: `. $HOME/.config/nexus-sync/env && $HOME/.local/bin/nexus-sync.sh`

## Hermes Cron Jobs

### 4. daily-harddrive-junk-cleanup
- **Schedule**: `0 8 * * *` (daily 8 AM)
- **Agent**: claude-sonnet-4 (Anthropic)
- **Skills**: linux-laptop-performance-tuning
- **Status**: Last run error (HTTP 403 — Claude auth issue)
- **Total runs**: 52

### 5. sync-memory-to-nexus (no-agent mode)
- **Schedule**: every 5 minutes
- **Script**: `sync-memory-to-nexus.py`
- **Deliver**: local (silent — no output unless errors)
- **Status**: OK — 3929 runs

### 6. subconscious-tick
- **Schedule**: every 30 minutes
- **Provider**: deepseek, deepseek-v4-flash (pinned)
- **Deliver**: local
- **Status**: OK — 388 runs
- **Action**: Run subconscious plugin tick() — observe/reflect/commit cycle

### 7. rsi-cycle-kubuntux
- **Schedule**: `0 3 * * *` (daily 3 AM)
- **Provider**: deepseek-v4-flash
- **Deliver**: origin
- **Status**: OK — 7 runs
- **Action**: SSH to kubuntux, run RSI training loop at /media/kubuntux/DEVELOPMENT1/rsi/

### 8. rsi-cycle-lin
- **Schedule**: `0 4 * * *` (daily 4 AM)
- **Provider**: deepseek-v4-flash
- **Deliver**: origin
- **Status**: OK — 7 runs
- **Action**: Run RSI locally at ~/Documents/recursive-self-improve/

### 9. honcho-watchdog (no-agent mode)
- **Schedule**: every 60s
- **Script**: `honcho-watchdog.sh`
- **Deliver**: origin
- **Action**: Check Honcho Docker stack health, restart unhealthy/exited containers
