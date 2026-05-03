# Nudgen Documentation

This repository contains the documentation for [Nudgen](https://nudgen.net), a retention email automation platform for shop owners and growing SMEs to boost customer lifetime value.

The documentation is built with [Mintlify](https://mintlify.com).

## Local Development

To preview your documentation changes locally, you need to install the [Mintlify CLI](https://www.npmjs.com/package/mint).

1. **Install the CLI:**
   ```bash
   npm i -g mint
   ```

2. **Run the development server:**
   At the root of the repository, run:
   ```bash
   mint dev
   ```

3. **View the preview:**
   Open [http://localhost:3000](http://localhost:3000) in your browser.

## Writing and Structure

- **Content:** Documentation is written in MDX files (Markdown with JSX components).
- **Structure:** The navigation and global settings are defined in `docs.json`.
- **Guidelines:** See [AGENTS.md](./AGENTS.md) for writing standards, terminology, and project-specific instructions.

### AI-Assisted Writing

If you are using an AI-enabled coding tool (like Claude Code, Cursor, or Windsurf), you can install the Mintlify skill to help with component usage and writing standards:

```bash
npx skills add https://mintlify.com/docs
```

## Publishing

Changes pushed to the main branch are automatically deployed via the Mintlify GitHub App. You can monitor the status and configuration in the [Mintlify Dashboard](https://dashboard.mintlify.com).

## Resources

- [Live Documentation](https://docs.nudgen.net)
- [Mintlify Documentation](https://mintlify.com/docs)
- [Nudgen Website](https://nudgen.net)

