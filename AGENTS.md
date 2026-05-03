> **First-time setup**: This file has been customized for Nudgen. Please review and refine the terminology and content boundaries as needed.
> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is the documentation site for [Nudgen](https://nudgen.net), built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Run `mint dev` to preview locally
- Run `mint broken-links` to check links

## Terminology

- Use **campaign** for automated email sequences.
- Use **contact** instead of "user" or "subscriber" when referring to people in the audience.
- Use **workspace** for the organizational unit (not "project" or "account").
- Use **nudge** when referring to individual emails sent within a sequence.
- Use **brand voice** for the AI-driven tone settings.

## Style preferences

- Use active voice and second person ("you").
- Keep sentences concise — one idea per sentence.
- Use sentence case for headings.
- Bold for UI elements: Click **Settings**.
- Code formatting for file names, commands, paths, and code references.
- Use standard Mintlify components (Cards, Accordions, Steps) for better readability.

## Content boundaries

- Focus on the Nudgen web app and the Agents (CLI/API) functionality.
- Do not document internal admin-only features.
- Ensure all technical guides include a "Why this matters" context for business owners.
