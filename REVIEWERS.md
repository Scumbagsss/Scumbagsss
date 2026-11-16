# Technical reviewer guide

**Goal:** evaluate the public Python engineering samples quickly. All examples use synthetic data and do not connect to private Discord/game-server systems. The FastAPI demo needs **locally generated demo-only API keys**, not commercial secrets.

## Start here

| Project | Backend focus | What to inspect |
|---|---|---|
| [Priority Access REST API](https://github.com/Scumbagsss/priority-access-bot) | FastAPI, HTTP auth, permissions, SQLite approval transactions, concurrency, audit and expiry projection | [Source](https://github.com/Scumbagsss/priority-access-bot/blob/main/api_demo/main.py) · [31 tests](https://github.com/Scumbagsss/priority-access-bot/blob/main/tests/test_api_demo.py) · [CI](https://github.com/Scumbagsss/priority-access-bot/actions/workflows/api-demo.yml) |
| [Ticket Workflow Backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | SQLite state transitions, permissions, audit history and escaped HTML export | [Source](https://github.com/Scumbagsss/advanced-discord-ticket-bot/blob/main/ticket_demo.py) · [Tests](https://github.com/Scumbagsss/advanced-discord-ticket-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/advanced-discord-ticket-bot/actions/workflows/python-demo.yml) |
| [Server Monitoring Pipeline](https://github.com/Scumbagsss/dayz-server-monitor-bot) | Validation, UTC timestamp normalization, batch ingestion, atomic SQLite writes and summaries | [Source](https://github.com/Scumbagsss/dayz-server-monitor-bot/blob/main/monitor_demo.py) · [Tests](https://github.com/Scumbagsss/dayz-server-monitor-bot/tree/main/tests) · [CI](https://github.com/Scumbagsss/dayz-server-monitor-bot/actions/workflows/monitor-demo.yml) |

**Versions:** Python 3.11+. Ticket and monitoring examples need only the Python standard library. The FastAPI example has a `requirements-demo.txt` file for external dependencies.

## Quick local review

Run the two standard-library demos separately:

```bash
git clone https://github.com/Scumbagsss/advanced-discord-ticket-bot.git
cd advanced-discord-ticket-bot
python -m unittest discover -s tests -v
python ticket_demo.py --db example.sqlite3
```

```bash
git clone https://github.com/Scumbagsss/dayz-server-monitor-bot.git
cd dayz-server-monitor-bot
python -m unittest discover -s tests -v
python monitor_demo.py --db example.sqlite3
```

To run the API tests (in its own folder):

```bash
git clone https://github.com/Scumbagsss/priority-access-bot.git
cd priority-access-bot
python -m pip install -r requirements-demo.txt
python -m pytest -q tests/test_api_demo.py
```

To start the HTTP service locally, follow the [FastAPI walkthrough](https://github.com/Scumbagsss/priority-access-bot/blob/main/docs/API_DEMO.md). It requires two distinct demo keys in environment variables and binds to `127.0.0.1` in the documented example.

## What the demos prove

- **Priority REST API:** test-only server-side identities, request validation, ownership checks, staff-only review, idempotent decisions and atomic creation of *local* entitlements. It does not contact Steam or grant real game-server privileges.
- **Ticket:** workflow and transaction logic, audit events, owner/staff actions, HTML encoding; a caller-provided `Actor` is **not** production authentication.
- **Monitoring:** input constraints, UTC timestamps, upsert-based retry behavior, whole-batch validation before commit and sample-based daily metrics.

## CI and coverage scope

On 16 November 2026, the three synthetic test suites covered **31**, **21** and **28** test cases, respectively; their GitHub Actions checks succeeded across Python 3.11, 3.12 and 3.13. This is not a measure of production uptime, end-to-end coverage or security certification.

## Private-source engineering case studies

[DeadCity](https://github.com/Scumbagsss/BOT), [SpawnSet investigation](https://github.com/Scumbagsss/spawnset-dupe-detector), the [private priority workflow](https://github.com/Scumbagsss/priority-access-bot/blob/main/docs/ARCHITECTURE.md) and [Transport Marketplace](https://github.com/Scumbagsss/dayz-transport-market-bot) document commercial designs without releasing sensitive source. Some public interfaces are intentionally unimplemented.

## Contact

**Discord:** `scumbagsss` · **Telegram:** [@dilarion](https://t.me/dilarion)
