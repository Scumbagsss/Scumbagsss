# Technical reviewer guide

**Goal:** evaluate public, runnable Python engineering samples in about 5–10 minutes. All inputs are synthetic and both demos work without Discord, private game servers, API keys or paid services.

## Start here

| Repository | What it proves | Run / inspect |
|---|---|---|
| [Ticket Workflow Backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | SQLite transactions, workflow state, permissions, audit history and escaped HTML exports | [Source](https://github.com/Scumbagsss/advanced-discord-ticket-bot/blob/main/ticket_demo.py) · [Tests](https://github.com/Scumbagsss/advanced-discord-ticket-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/advanced-discord-ticket-bot/actions/workflows/python-demo.yml) |
| [Server Monitoring Pipeline](https://github.com/Scumbagsss/dayz-server-monitor-bot) | Input validation, timezone normalization, repeatable ingestion, atomic batch persistence and aggregates | [Source](https://github.com/Scumbagsss/dayz-server-monitor-bot/blob/main/monitor_demo.py) · [Tests](https://github.com/Scumbagsss/dayz-server-monitor-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/dayz-server-monitor-bot/actions/workflows/monitor-demo.yml) |

**Both projects:** Python 3.11+, no third-party dependencies for their standalone demonstrations.

## Five-minute local review

```bash
git clone https://github.com/Scumbagsss/advanced-discord-ticket-bot.git
cd advanced-discord-ticket-bot
python -m unittest discover -s tests -v
python ticket_demo.py --db example.sqlite3
```

In another folder:

```bash
git clone https://github.com/Scumbagsss/dayz-server-monitor-bot.git
cd dayz-server-monitor-bot
python -m unittest discover -s tests -v
python monitor_demo.py --db example.sqlite3
```

Local `*.sqlite3` files are deliberately ignored by Git. The server monitor consumes a fabricated JSONL file in `fixtures/`.

## What to look for

- **Ticket demo:** authorization is explicit, workflow transitions are validated, audit events are stored in SQLite, closed tickets cannot be silently modified, and user content is escaped in HTML output. Its caller-supplied `Actor` is **not** real authentication.
- **Monitor demo:** invalid records are rejected, timestamps are stored in UTC, retries upsert the same sample rather than duplicating it, and JSONL imports validate the complete batch before committing. Daily availability is *sample-based*, not a time-weighted SLA.

## CI status and scope

As of the latest reviewed source update on **16 November 2026**, the public demos have **21** and **28** unit tests respectively. Both workflows passed their GitHub Actions checks on Python 3.11, 3.12 and 3.13.

A green test suite is evidence that *the included scenarios passed*, not a production reliability or security guarantee.

## Private-source case studies

The [DeadCity platform](https://github.com/Scumbagsss/BOT), [activity investigation subsystem](https://github.com/Scumbagsss/spawnset-dupe-detector), [priority access workflow](https://github.com/Scumbagsss/priority-access-bot) and [vehicle marketplace](https://github.com/Scumbagsss/dayz-transport-market-bot) are **not deployable from their public repositories**. They document architecture, workflows, engineering trade-offs and publication boundaries. Some source fragments are deliberately unimplemented.

## Contact

- Discord: `scumbagsss`
- Telegram: [@dilarion](https://t.me/dilarion)
