# Contributing

Issues and pull requests are welcome.

- Skill instructions, READMEs, and templates are written in English. Deliverables default to English; Indonesian stays supported through the thesis profile.
- Keep real thesis content out of issues and pull requests (see [SECURITY.md](SECURITY.md)).
- `plugins/asisten-tesis/skills/lugas/` is vendored from [rezaprama/Lugas](https://github.com/rezaprama/Lugas). Send changes to it upstream rather than editing the copy here.
- Bump `version` in the plugin's `.claude-plugin/plugin.json` and add a line to [CHANGELOG.md](CHANGELOG.md) when behaviour changes.

## Checks

Run before opening a pull request (needs [uv](https://docs.astral.sh/uv/)); CI runs the same:

```
uv run --with pyyaml python scripts/validate.py
python3 -m py_compile plugins/*/skills/*/scripts/*.py
uv run --with python-pptx python plugins/asisten-tesis/skills/defense-deck/scripts/build_pptx.py examples/defense-deck-sample/slides.json /tmp/deck.pptx
uv run --with python-pptx python plugins/asisten-tesis/skills/defense-deck/scripts/check_pptx.py /tmp/deck.pptx
```

Try a plugin without installing it: `claude --plugin-dir plugins/asisten-tesis`.

## License

By contributing, you agree that your contributions are licensed under the Apache License 2.0 (see [LICENSE](LICENSE)).
