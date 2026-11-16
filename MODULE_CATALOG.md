# Module catalog — Discord and DayZ automation

This catalog organizes **12 feature-level showcases** into three domains. Most describe private-source modules; **Config Manager additionally includes a separate runnable SQLite backend demo**. These are not 12 independent commercial products.

**Read this first:** The private-system interface sketches in these repositories deliberately raise `NotImplementedError`; they are **not production code**. The new [Config Manager demo](https://github.com/Scumbagsss/discord-config-manager) is independent of its private interface sketch. Architecture documents are not proof of deployment. The portfolio's **four** runnable examples are in the [reviewer guide](REVIEWERS.md).

## Operations and server management

| Module | Responsibility | Most relevant engineering questions |
|---|---|---|
| [Admin Control Panel](https://github.com/Scumbagsss/discord-admin-control-panel) | Role-gated Discord entry point for operational tools | Server-side permission checks, stale controls, routing to subsystem adapters |
| [Config Manager](https://github.com/Scumbagsss/discord-config-manager) | Private JSON/JSONC case + runnable synthetic SQLite settings backend | Expected versions, atomic batches, audit and rollback (36 tests) |
| [Role Prefix Manager](https://github.com/Scumbagsss/discord-role-prefix-bot) | Role-based nickname normalization | Idempotency, role precedence, event loops, permissions |
| [Temporary Radio Channels](https://github.com/Scumbagsss/temporary-radio-bot) | Create-on-join voice rooms | Voice-event races, owner recovery, safe cleanup |

## Player support and review

| Module | Responsibility | Most relevant engineering questions |
|---|---|---|
| [Support Workflow](https://github.com/Scumbagsss/discord-support-workflow-bot) | Tickets and administrative request routing | Privacy boundaries, state, transcripts, restart recovery |
| [Feedback Triage](https://github.com/Scumbagsss/discord-feedback-manager) | Collect and review community feedback | Persistent queue, duplicate intake, reviewer concurrency |
| [Nickname Requests](https://github.com/Scumbagsss/discord-nickname-request-bot) | Moderated nickname-change requests | Permissions, pending requests, prefix synchronization |
| [Character Applications](https://github.com/Scumbagsss/rp-character-application-bot) | RP character/quenta approval | Dynamic forms, versioned submissions, staff review |
| [Faction Reservations](https://github.com/Scumbagsss/faction-reservation-bot) | Faction application/reservation review | Single active allocation, concurrency, expiry |

## Moderation and activity review

| Module | Responsibility | Most relevant engineering questions |
|---|---|---|
| [Discord Audit Log](https://github.com/Scumbagsss/discord-audit-log-bot) | Normalized member and moderation event summaries | Actor attribution, privacy, event volume, audit delivery |
| [Forbidden Item Spawn Monitoring](https://github.com/Scumbagsss/forbidden-item-spawn-detector) | Configured item-policy alerts | Log parsing, policy versioning, false positives, deduplication |
| [Admin Activity Monitoring](https://github.com/Scumbagsss/deadcity-admin-abuse-detector) | Context for suspicious admin item/teleport events | Time windows, exceptions, correlation and human review |

## Why are some features in separate repositories?

These pages were originally published as *module-level portfolio entries*. In a single product they may belong to the same codebase:

- **Support Workflow** overlaps the larger [Ticket Workflow Backend](https://github.com/Scumbagsss/advanced-discord-ticket-bot), which has runnable, independently testable Python.
- **Nickname Requests** is closely related to **Role Prefix Manager**; publishing both as independent products would be misleading without a separate deployable implementation.
- **Forbidden Item Spawn Monitoring** is a narrower feature of **Admin Activity Monitoring**.
- **Admin Control Panel** describes a front-end to settings that are also addressed in **Config Manager**.

For an employer, the recommended entry points remain the [four runnable backends](REVIEWERS.md), [DeadCity platform case study](https://github.com/Scumbagsss/BOT), [SpawnSet investigation](https://github.com/Scumbagsss/spawnset-dupe-detector) and [Vehicle Marketplace](https://github.com/Scumbagsss/dayz-transport-market-bot).

## Publication / archival policy

**No repository was deleted or archived automatically.** Preserve published URLs, licenses, production integrations and historical references until you've checked whether any users or external services depend on them. Archiving is usually a safer first step than deletion.

See [portfolio curation and repository settings](PORTFOLIO.md) for recommended pins and candidates for manual archive.

**Contact:** Discord `scumbagsss` · Telegram [@dilarion](https://t.me/dilarion)
