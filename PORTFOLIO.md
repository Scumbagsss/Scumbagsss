# Portfolio index & repository guide

This page distinguishes **runnable code**, **private-source case studies** and **smaller legacy module showcases**.

## Recommended six pinned repositories

| Priority | Repository | Positioning |
|---|---|---|
| 1 | [priority-access-bot](https://github.com/Scumbagsss/priority-access-bot) | **Runnable FastAPI + SQLite**; sessions, permissions, 44 HTTP/database tests |
| 2 | [discord-config-manager](https://github.com/Scumbagsss/discord-config-manager) | **Runnable versioned settings backend**, SQLite, atomic writes, rollback, 36 tests |
| 3 | [advanced-discord-ticket-bot](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | Runnable ticket workflow, audit and transcript, 21 tests |
| 4 | [dayz-server-monitor-bot](https://github.com/Scumbagsss/dayz-server-monitor-bot) | Runnable ingestion and reporting demo, 28 tests |
| 5 | [BOT](https://github.com/Scumbagsss/BOT) | DeadCity private-source platform case study |
| 6 | [spawnset-dupe-detector](https://github.com/Scumbagsss/spawnset-dupe-detector) | Event analysis and case-management architecture |

## Other public case studies (optional depth)

These are **feature-level documentation showcases**, rather than independent runnable services. The separate [Config Manager](https://github.com/Scumbagsss/discord-config-manager) synthetic backend now appears in the six recommended pins.

| Area | Repositories |
|---|---|
| Moderation | [deadcity-admin-abuse-detector](https://github.com/Scumbagsss/deadcity-admin-abuse-detector), [forbidden-item-spawn-detector](https://github.com/Scumbagsss/forbidden-item-spawn-detector), [discord-audit-log-bot](https://github.com/Scumbagsss/discord-audit-log-bot) |
| Support & review | [discord-support-workflow-bot](https://github.com/Scumbagsss/discord-support-workflow-bot), [rp-character-application-bot](https://github.com/Scumbagsss/rp-character-application-bot), [discord-nickname-request-bot](https://github.com/Scumbagsss/discord-nickname-request-bot), [discord-feedback-manager](https://github.com/Scumbagsss/discord-feedback-manager) |
| Operations | [discord-admin-control-panel](https://github.com/Scumbagsss/discord-admin-control-panel), [discord-role-prefix-bot](https://github.com/Scumbagsss/discord-role-prefix-bot) |
| Community | [faction-reservation-bot](https://github.com/Scumbagsss/faction-reservation-bot), [temporary-radio-bot](https://github.com/Scumbagsss/temporary-radio-bot) |

## Cleanup recommendations (review before archive)

**These have not been deleted or archived.** GitHub account-level archive/delete controls are not available through the connected repository write actions.

- **Scumbags:** empty public repository; archive or delete if not reserved for a future purpose.
- **Bot-Soc:** private and nearly empty; keep if it is intended as a future workspace, otherwise archive.
- **discord-support-workflow-bot:** substantially overlaps the richer ticket-demo and nickname workflow showcases; archive if it adds no distinct implementation.
- **discord-admin-control-panel:** overlaps `discord-config-manager`; consolidate documentation and archive if redundant.
- **forbidden-item-spawn-detector:** overlaps broader admin abuse detection; keep as a separate project only if its implementation is materially different.
- **-Privacy-Policy-for-Dead-City-Discord-Applications:** **do not delete** merely for portfolio aesthetics; it may serve a live application compliance purpose. Its README contains an unfilled operator legal-name placeholder that needs owner review and appropriate correction.

## Safe archive workflow

1. Open the repository, confirm there are no dependencies, external app links or pending issues relying on it.
2. Prefer **Settings → General → Danger Zone → Archive this repository**. Archiving preserves the code and history while making it read-only.
3. Remove it from pinned repositories if applicable.
4. Use deletion only after a deliberate backup and dependency check.

## Publishing standards

A good showcase states whether it is runnable; names its problem and technical stack; provides evidence without inventing production metrics; avoids publishing private logs/identifiers; and uses an explicit authorization boundary for commercial assets.

## GitHub profile settings — manual finishing steps

The current GitHub connection can change repository files but **cannot edit profile Bio, repository About/Topics, pinned repositories or archive status**. These suggestions are copy-ready; none have been applied automatically.

**Profile Bio:** `Python Backend Developer | Automation Engineer | REST APIs, SQLite, Discord`

**Website / social link:** `https://t.me/dilarion`  
**Discord handle (text):** `scumbagsss`

### Repository About and Topics

Set each under **Repository → About (gear icon)**. Keep descriptions concise and distinguish runnable examples from private case studies.

| Repository | Suggested About description | Suggested Topics |
|---|---|---|
| [priority-access-bot](https://github.com/Scumbagsss/priority-access-bot) | Runnable FastAPI demo with expiring bearer sessions, SQLite approvals and 44 tests. | `python`, `fastapi`, `rest-api`, `sqlite`, `authentication`, `backend` |
| [discord-config-manager](https://github.com/Scumbagsss/discord-config-manager) | Runnable Python/SQLite settings service: optimistic versions, audit, batch transactions and 36 tests. | `python`, `sqlite`, `configuration`, `backend`, `automation`, `testing` |
| [advanced-discord-ticket-bot](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | Runnable Python/SQLite ticket workflow demo with audit history, staff rules and tests. | `python`, `sqlite`, `ticket-system`, `discord`, `automation` |
| [dayz-server-monitor-bot](https://github.com/Scumbagsss/dayz-server-monitor-bot) | Runnable synthetic monitoring pipeline: JSONL, UTC timestamps, SQLite, metrics and tests. | `python`, `sqlite`, `data-processing`, `monitoring`, `dayz` |
| [BOT](https://github.com/Scumbagsss/BOT) | Private-source DeadCity operations platform case study: support, moderation and monitoring. | `python`, `discord`, `dayz`, `automation`, `case-study` |
| [spawnset-dupe-detector](https://github.com/Scumbagsss/spawnset-dupe-detector) | Private-source DayZ activity investigation case study: logs, timelines and review workflows. | `python`, `log-analysis`, `dayz`, `case-study` |
| [dayz-transport-market-bot](https://github.com/Scumbagsss/dayz-transport-market-bot) | Private-source Discord vehicle marketplace case study: listings, reservations and staff review. | `python`, `discord`, `marketplace`, `dayz`, `case-study` |

### Recommended pinned repositories

Click **Customize your pins** on your profile and select the six listed at the beginning of this document, in order if the interface permits. The profile repository `Scumbagsss` does not need its own pin because its README is already featured on your profile.

### Archive candidates — verify before changing anything

- [ ] `Scumbags`: currently empty public repository. Confirm there are no external links or future plans; archive if unused.
- [ ] `Bot-Soc`: empty private repository. Keep if reserved for development; otherwise consider archiving.
- [ ] `discord-support-workflow-bot`: overlaps the runnable ticket backend. Keep only if it documents a distinct feature beyond the parent case.
- [ ] `discord-admin-control-panel`: overlaps `discord-config-manager`; archive only after preserving useful context and checking cross-links.
- [ ] `forbidden-item-spawn-detector`: narrower than `deadcity-admin-abuse-detector`. Preserve if it needs a distinct case page; otherwise archive after review.

**Do not archive/delete the privacy-policy repository just to reduce the public count.** It may be linked by a running application and includes a legal-name placeholder that should be resolved by the actual operator, not guessed.

Use **Settings → General → Danger Zone → Archive this repository** after checking GitHub Pages, integrations, deployment links, issues and documentation references. Archiving is reversible and preserves history; deletion is not a routine cosmetic cleanup.
