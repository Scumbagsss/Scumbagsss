# Technical reviewer guide — runnable Python backends

The public portfolio has **four independently runnable synthetic projects** using fictional inputs and no production Discord/DayZ credentials. The commercial code remains private.

## Where to begin

| Project | What to inspect | Evidence |
|---|---|---|
| [Priority Access REST API](https://github.com/Scumbagsss/priority-access-bot) | FastAPI, locally provisioned user identities, salted passwords, expiring/revocable sessions, roles, SQLite workflow state | [Source](https://github.com/Scumbagsss/priority-access-bot/tree/main/api_demo) · [44 tests](https://github.com/Scumbagsss/priority-access-bot/blob/main/tests/test_api_demo.py) · [CI](https://github.com/Scumbagsss/priority-access-bot/actions/workflows/api-demo.yml) |
| [Versioned Config Backend](https://github.com/Scumbagsss/discord-config-manager) | SQLite, input validation, optimistic version checks, atomic batch writes, audit history, undo | [Source](https://github.com/Scumbagsss/discord-config-manager/blob/main/config_demo.py) · [36 tests](https://github.com/Scumbagsss/discord-config-manager/blob/main/tests/test_config_demo.py) · [CI](https://github.com/Scumbagsss/discord-config-manager/actions/workflows/config-demo.yml) |
| [Ticket Workflow Backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | Ticket state, staff permissions, SQLite transactions, history and escaped HTML exports | [Source](https://github.com/Scumbagsss/advanced-discord-ticket-bot/blob/main/ticket_demo.py) · [21 tests](https://github.com/Scumbagsss/advanced-discord-ticket-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/advanced-discord-ticket-bot/actions/workflows/python-demo.yml) |
| [Server Monitoring Pipeline](https://github.com/Scumbagsss/dayz-server-monitor-bot) | UTC normalization, JSONL ingestion, SQLite upserts, batch integrity and aggregates | [Source](https://github.com/Scumbagsss/dayz-server-monitor-bot/blob/main/monitor_demo.py) · [28 tests](https://github.com/Scumbagsss/dayz-server-monitor-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/dayz-server-monitor-bot/actions/workflows/monitor-demo.yml) |

All four support Python **3.11+**. The three SQLite CLI demos use only the standard library. The FastAPI demo declares its dependencies in `requirements-demo.txt`.

## Run each example

### Priority REST API

```bash
git clone https://github.com/Scumbagsss/priority-access-bot.git
cd priority-access-bot
python -m pip install -r requirements-demo.txt
python -m pytest -q tests/test_api_demo.py
```

For a local API server, provision fictional accounts interactively with `python -m api_demo.manage`, then run Uvicorn; complete commands are in [the API walkthrough](https://github.com/Scumbagsss/priority-access-bot/blob/main/docs/API_DEMO.md). It uses local **bearer sessions**, not static API keys.

### Config backend

```bash
git clone https://github.com/Scumbagsss/discord-config-manager.git
cd discord-config-manager
python -m unittest discover -s tests -v
python config_demo.py --db demo.sqlite3 list
```

Read the [configuration walkthrough](https://github.com/Scumbagsss/discord-config-manager/blob/main/docs/CONFIG_DEMO.md) for stale-version conflicts and rollback.

### Ticket workflow

```bash
git clone https://github.com/Scumbagsss/advanced-discord-ticket-bot.git
cd advanced-discord-ticket-bot
python -m unittest discover -s tests -v
python ticket_demo.py --db example.sqlite3
```

### Monitoring pipeline

```bash
git clone https://github.com/Scumbagsss/dayz-server-monitor-bot.git
cd dayz-server-monitor-bot
python -m unittest discover -s tests -v
python monitor_demo.py --db example.sqlite3
```

## Testing scope

At the verified public review point on **16 November 2026**, the suites contain **44 + 36 + 21 + 28 = 129 tests**. GitHub Actions checks passed on **Python 3.11, 3.12 and 3.13**. This is evidence of the included synthetic scenarios, **not** of deployment uptime, comprehensive security or complete production coverage.

## Trust boundaries

- **Priority API:** has locally provisioned users and short-lived revocable sessions, but does not implement production login rate limits, MFA, SSO, TLS termination, monitoring or Steam ownership validation. Never deploy publicly without those safeguards.
- **Config demo:** is a local backend with an `Actor` supplied by its caller; it does not authenticate network users or edit actual Discord JSONC.
- **Ticket demo:** the caller supplies an `Actor`; authorization is a demonstration rather than a full authentication stack.
- **Monitor demo:** measurements are made from fabricated samples. Sample-based availability is not real server uptime.

## Commercial architecture studies

[DeadCity](https://github.com/Scumbagsss/BOT), [SpawnSet investigation](https://github.com/Scumbagsss/spawnset-dupe-detector), [priority workflow architecture](https://github.com/Scumbagsss/priority-access-bot/blob/main/docs/ARCHITECTURE.md) and [Transport Marketplace](https://github.com/Scumbagsss/dayz-transport-market-bot) contain design context and deliberately unimplemented public interface sketches—not runnable copies of the proprietary systems.

**Contact:** Discord `scumbagsss` · Telegram [@dilarion](https://t.me/dilarion)
