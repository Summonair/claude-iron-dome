# Claude Iron Dome

A security layer for Claude Code.
This plugin hooks into your tool usage to prevent accidental execution of destructive commands.

## Features
- **Iron Dome Hook**: Intercepts `rm -rf`, `sudo`, and `terraform destroy` commands.
- **Safety First**: Warns and requires confirmation before proceeding.

## Installation
To install this plugin locally:

```bash
claude --plugin-dir .
```

## Adding to Marketplace
Add this repository to your Claude Code marketplace:

```bash
/plugin marketplace add summonair/claude-iron-dome
/plugin install iron-dome
```
