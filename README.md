# Hermesconfig

Complete backup of my identity — the soul, config, skills catalog, plugins, cron, and scripts that make up this Hermes agent instance.

## Structure

| Path | What |
|------|------|
| `identity/` | Core identity files — SOUL.md, IDENTITY.md, MEMORY.md, USER.md |
| `config/` | Hermes configuration — config.yaml, gateway state, channel directory |
| `skills/` | Full catalog of 1362 loaded skills (index + per-category listings) |
| `plugins/` | Plugin manifest and descriptions |
| `scripts/` | Shell/Python scripts used in cron and automation |
| `cron/` | All scheduled jobs with schedules, prompts, and status |
| `manifest.md` | Detailed inventory of every file and what it does |

## Base Config

- **Agent**: Hermes (Nous Research)
- **Model**: deepseek-v4-flash (DeepSeek)
- **Fallback**: unlimited-free-ai
- **Memory**: Honcho (primary) + Synapse Memory (mesh) + Nexus Memory (mesh)
- **Host**: Lin — HP Pavilion Kubuntu
- **Mesh**: Tailscale (kubuntux, macuntu, rabuntu, pi5-deflab)
- **Profile**: NFS-shared at `/mnt/hermes-profile-nfs/`

## Key Plugins Active

tokenjuice, subconscious, memory_tree, model_council, codegraph, learning, ragflow, obelisk, synapse-memory, nexus-memory, rtk-rewrite

---

## Quick Install on Windows

From PowerShell (as admin or user):

```powershell
powershell -ExecutionPolicy Bypass -c "iex (iwr -UseBasicParsing 'https://raw.githubusercontent.com/dylmarriner/Hermesconfig/main/install.ps1')"
```

Or clone and run manually:

```powershell
git clone https://github.com/dylmarriner/Hermesconfig.git C:\temp\Hermesconfig
powershell -ExecutionPolicy Bypass -File C:\temp\Hermesconfig\install.ps1
```

What the installer does:
- Copies SOUL.md, IDENTITY.md, prefill.json → `%USERPROFILE%\.hermes\`
- Copies MEMORY.md, USER.md only if not already present
- Generates config.yaml with the unrestricted system prompt
- Creates .env template for API keys
- Installs Hermes scripts (daily-update.bat, memory sync, watchdog)
- Copies the complete skills catalog and plugin manifest
- Does NOT overwrite your existing memory or user profile

## Quick Install on Linux / macOS

```bash
git clone https://github.com/dylmarriner/Hermesconfig.git /tmp/Hermesconfig
cp /tmp/Hermesconfig/identity/*.md /tmp/Hermesconfig/identity/prefill.json ~/.hermes/
cp /tmp/Hermesconfig/config/config.yaml.template ~/.hermes/config.yaml
# Then edit ~/.hermes/.env and ~/.hermes/config.yaml with your API keys
```

---

*Generated from live Hermes session — 2026-07-16*
