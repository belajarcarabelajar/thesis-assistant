# Security policy

## Reporting a vulnerability

Report privately through GitHub: open the **Security** tab of this repository and choose **Report a vulnerability**. Please do not open a public issue for security problems.

In scope:

- The bundled scripts (`plugins/*/skills/*/scripts/`), for example unsafe file handling or command execution.
- Skill instructions that could make Claude Code run harmful commands, leak files, or send data somewhere the user did not ask for.
- Personal data, credentials, or copyrighted third-party text committed to the repository.

Only the latest version on `main` is supported. You can expect a first reply within 7 days.

## Handling thesis data

The skills work on local files in the thesis folder. Do not attach real manuscripts, survey data, or supervisor comments to issues; use a minimal fictional example instead.
