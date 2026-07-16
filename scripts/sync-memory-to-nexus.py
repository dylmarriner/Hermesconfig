#!/usr/bin/env python3
"""Watch Hermes local memory files and sync new entries to Synapse Memory.

Reads MEMORY.md and USER.md from ~/.hermes/memories/, checks what's already
in Nexus, and pushes any missing entries.

Usage: python3 sync-memory-to-nexus.py
Run as a cron job every 5 minutes for near-real-time sync.
"""
import json, logging, os, urllib.request, urllib.error
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger("memory-sync")
HERMES_HOME = os.path.expanduser("~/.hermes")
MEMORIES_DIR = os.path.join(HERMES_HOME, "memories")
AGENT_ID = os.environ.get("NEXUS_AGENT_ID", "hermes")
DEVICE = os.environ.get("NEXUS_DEVICE", "lin")
NEXUS_URL = os.environ.get("NEXUS_URL", "http://100.93.75.87:7777")
NEXUS_SECRET = os.environ.get("NEXUS_SECRET", "nexus-memory-shared-key-2026")
MEMORY_FILE = os.path.join(MEMORIES_DIR, "MEMORY.md")
USER_FILE = os.path.join(MEMORIES_DIR, "USER.md")
STATE_FILE = os.path.join(HERMES_HOME, ".memory-sync-state.json")

def parse_entries(filepath):
    if not os.path.exists(filepath): return []
    with open(filepath, "r") as f: content = f.read().strip()
    return [e.strip() for e in content.split("\u00a7") if e.strip()] if content else []

def load_state():
    if os.path.exists(STATE_FILE):
        try: return json.load(open(STATE_FILE, "r"))
        except: return {}
    return {}

def save_state(state):
    json.dump(state, open(STATE_FILE, "w"), indent=2)

def load_existing_hashes():
    existing = set()
    url = f"{NEXUS_URL}/v1/memory/profile/{AGENT_ID}"
    req = urllib.request.Request(url)
    req.add_header("X-Nexus-Secret", NEXUS_SECRET)
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read().decode())
        for m in data.get("memories", []): existing.add(m.get("content", ""))
    except: pass
    return existing

def sync_entry(content, memory_type, importance=0.7):
    url = f"{NEXUS_URL}/v1/memory/save"
    payload = json.dumps({"agent_id": AGENT_ID, "content": content, "memory_type": memory_type, "importance": importance, "metadata": {"device": DEVICE, "source": "hermes-local-sync"}}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Nexus-Secret", NEXUS_SECRET)
    try:
        urllib.request.urlopen(req, timeout=10)
        logger.info("Synced: [%s] %s...", memory_type, content[:60])
        return True
    except: return False

def main():
    logger.info("Starting memory sync for agent '%s' \u2192 %s", AGENT_ID, NEXUS_URL)
    memory_entries = parse_entries(MEMORY_FILE)
    user_entries = parse_entries(USER_FILE)
    if not memory_entries and not user_entries:
        logger.info("No local entries found, nothing to sync"); return
    existing = load_existing_hashes()
    logger.info("Found %d existing memories in Nexus for agent '%s'", len(existing), AGENT_ID)
    synced = 0
    for entry in memory_entries:
        if entry not in existing and sync_entry(entry, "observation", 0.7): synced += 1; existing.add(entry)
    for entry in user_entries:
        if entry not in existing and sync_entry(entry, "preference", 0.8): synced += 1; existing.add(entry)
    logger.info("Sync complete: %d new entries synced", synced)

if __name__ == "__main__": main()
