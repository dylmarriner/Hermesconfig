# Hermes Config Manifest

## File Inventory

### `/identity/`
| File | Description |
|------|-------------|
| `SOUL.md` | Core soul/personality — unrestricted, no filters, direct execution ethos |
| `IDENTITY.md` | Extended identity — inherited from Cipher, same ethos |
| `MEMORY.md` | Persistent memory notes — Dylan, projects, environment facts |
| `USER.md` | User profile — name, timezone, focus, tech stack |
| `prefill.json` | Prefill messages injected at conversation start (security researcher framing) |

### `/config/`
| File | Description |
|------|-------------|
| `config.yaml` | Main Hermes configuration — model, providers, toolsets, agents, memory, platforms, gateways, security, cron, plugins |
| `config.yaml.bak.*` | Historical backups at various timestamps |
| `gateway_state.json` | Gateway process state — PID, platforms connected |
| `channel_directory.json` | Platform channel directory — Telegram chat/thread IDs |
| `context_length_cache.yaml` | Cached context length limits per model |
| `tokenjuice_savings.json` | TokenJuice compression stats — savings by compressor type |

### `/config/mcp_servers/`
MCP server configs (extracted from config.yaml):
- `docling` — Document conversion MCP
- `filesystem` — File system access MCP
- `markitdown` — Markdown conversion MCP
- `nexus-memory` — Nexus memory MCP (Synapse bridge)
- `codegraph` — Code symbol exploration MCP
- `airis-gateway` — Airis gateway MCP

### `/skills/`
| File | Description |
|------|-------------|
| `index.md` | Full catalog of all 1362 skills across all categories |
| `by-category/` | Skills organized by category directory |

### `/plugins/`
| File | Description |
|------|-------------|
| `PLUGINS.md` | All 21 installed plugins with descriptions |

### `/scripts/`
| File | Description |
|------|-------------|
| `daily-update.sh` | Daily Hermes auto-update (stash → update → pop → restart gateway) |
| `sync-memory-to-nexus.py` | Watch local memory files and sync new entries to Synapse Memory |
| `honcho-watchdog.sh` | Docker container health watchdog — restarts unhealthy/exited Honcho containers |
| `adapters/nexus_mcp_stdio.py` | STDIO adapter for Nexus MCP server |

### `/cron/`
| File | Description |
|------|-------------|
| `CRON_JOBS.md` | All 6+ scheduled cron jobs with schedules, prompts, status |

### `/profiles/`
| Content | Description |
|---------|-------------|
| NFS shared profile info | Profile stored at `/mnt/hermes-profile-nfs/` with 1324+ skill dirs, 1205 SKILL.md files |

---

## Secrets NOT included (removed from repo)
- `config.yaml` — `.env` references (API keys redacted to `${VAR_NAME}`)
- `auth.json` — Provider auth tokens
- `.env` — Environment variable secrets
- `plugins/*` — Plugin source code (only manifest included)
- `state.db` / `sessions/*` — Session data and conversation history
