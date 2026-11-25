# thesis-assistant

[![CI](https://github.com/belajarcarabelajar/thesis-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/belajarcarabelajar/thesis-assistant/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A Claude Code plugin marketplace for writing a master's thesis. It currently holds one plugin, `asisten-tesis`, with six skills: Chapter 4 analysis, verified APA 7 sources, supervisor revision tracking, academic editing in English and Indonesian, an "AI slop" check, and editable defense slides. Deliverables are in English by default.

## Install

In Claude Code:

```
/plugin marketplace add belajarcarabelajar/thesis-assistant
/plugin install asisten-tesis@belajarcarabelajar-tesis
```

Update later with `/plugin marketplace update belajarcarabelajar-tesis`. Prerequisites (Git, uv, TinyFish MCP, optional DeckCraft) and the skill list: [plugins/asisten-tesis/README.md](plugins/asisten-tesis/README.md).

## Repository layout

| Path | Contents |
|---|---|
| `.claude-plugin/marketplace.json` | Marketplace `belajarcarabelajar-tesis`, lists the plugins below |
| `plugins/asisten-tesis/` | The thesis plugin: skills, templates, references, bundled scripts |
| `examples/defense-deck-sample/` | Sample deck built by the `defense-deck` skill from fictional data, with previews |
| `scripts/validate.py` | Repository checks run by CI |

## Responsible use

The skills help the author analyse their own data, find and verify sources, track revisions, and prepare a defense. The author stays responsible for the thesis and must follow their university's rules on AI use. The skills mark gaps (`[NEEDS DATA]`, `[NEEDS SOURCE]`, `[UNVERIFIED]`) instead of inventing numbers or references, and `ai-slop-check` refuses requests to evade AI detectors.

## Status

Behaviour-tested on Linux with fictional data (November 2026). Not yet tested on Windows or macOS. Slide previews from DeckCraft can differ from PowerPoint; check final files in Microsoft Word and PowerPoint.

## License

Apache License 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). `plugins/asisten-tesis/skills/lugas/` is vendored from [rezaprama/Lugas](https://github.com/rezaprama/Lugas) under its own terms (Apache-2.0 code, CC BY 4.0 data); details in NOTICE.

Not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic.
