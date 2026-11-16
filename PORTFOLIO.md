# Portfolio index & repository guide

This page distinguishes **runnable code**, **private-source case studies** and **smaller legacy module showcases**.

## Recommended six pinned repositories

| Priority | Repository | Positioning |
|---|---|---|
| 1 | [advanced-discord-ticket-bot](https://github.com/Scumbagsss/advanced-discord-ticket-bot) | Runnable Python/SQLite ticket-workflow demo with automated tests |
| 2 | [dayz-server-monitor-bot](https://github.com/Scumbagsss/dayz-server-monitor-bot) | Runnable ingestion, persistence and reporting demo with CI |
| 3 | [BOT](https://github.com/Scumbagsss/BOT) | DeadCity private-source platform case study |
| 4 | [spawnset-dupe-detector](https://github.com/Scumbagsss/spawnset-dupe-detector) | Log-analysis and case-management architecture |
| 5 | [priority-access-bot](https://github.com/Scumbagsss/priority-access-bot) | External entitlement API and authorization workflow |
| 6 | [dayz-transport-market-bot](https://github.com/Scumbagsss/dayz-transport-market-bot) | Moderated marketplace and multi-step state |

## Other public case studies (optional depth)

These are legitimate **feature-level documentation showcases**, not independent runnable services.

| Area | Repositories |
|---|---|
| Moderation | [deadcity-admin-abuse-detector](https://github.com/Scumbagsss/deadcity-admin-abuse-detector), [forbidden-item-spawn-detector](https://github.com/Scumbagsss/forbidden-item-spawn-detector), [discord-audit-log-bot](https://github.com/Scumbagsss/discord-audit-log-bot) |
| Support & review | [discord-support-workflow-bot](https://github.com/Scumbagsss/discord-support-workflow-bot), [rp-character-application-bot](https://github.com/Scumbagsss/rp-character-application-bot), [discord-nickname-request-bot](https://github.com/Scumbagsss/discord-nickname-request-bot), [discord-feedback-manager](https://github.com/Scumbagsss/discord-feedback-manager) |
| Operations | [discord-admin-control-panel](https://github.com/Scumbagsss/discord-admin-control-panel), [discord-config-manager](https://github.com/Scumbagsss/discord-config-manager), [discord-role-prefix-bot](https://github.com/Scumbagsss/discord-role-prefix-bot) |
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
