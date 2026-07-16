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

*Generated from live Hermes session — 2026-07-16*
