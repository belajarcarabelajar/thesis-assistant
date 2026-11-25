# thesis-assistant

Repo for the `asisten-tesis` Claude Code plugin (v0.4.0): six skills for writing a master's thesis, deliverables in English by default.

| Path | Contents |
|---|---|
| `.claude-plugin/marketplace.json` | Marketplace `belajarcarabelajar-tesis` |
| `asisten-tesis/` | The plugin: skills, templates, references. Details and install steps: [`asisten-tesis/README.md`](asisten-tesis/README.md) |
| `examples/defense-deck-sample/` | Sample defense deck built by the `defense-deck` skill (fictional data) |

Install:

```
/plugin marketplace add belajarcarabelajar/thesis-assistant
/plugin install asisten-tesis@belajarcarabelajar-tesis
```

Try without installing: `claude --plugin-dir asisten-tesis`.
