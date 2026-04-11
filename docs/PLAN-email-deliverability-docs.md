# Plan: Email Deliverability Audit Documentation

This plan outlines the steps to add comprehensive documentation for the `/email-deliverability-audit` tool in the `nudgen-docs` repository.

## Phase 1: Analysis & Content Selection
- [ ] Review `EmailDeliverabilityAuditClient.tsx` in the core repository to extract all technical checks (SPF, DKIM, DMARC).
- [ ] Identify key value propositions: instant lookup, record recommendation, and technical status explanations.
- [ ] Gather FAQs from the component to include in the documentation.

## Phase 2: File Structure & Creation
- [ ] Create a new directory: `en/email-deliverability-audit/`.
- [ ] Create `en/email-deliverability-audit/overview.mdx` with the following sections:
    - Introduction (What is the tool?).
    - Core Checks (SPF, DKIM, DMARC explained).
    - Understanding Results (Pass, Fail, Warning).
    - Technical Recommendations (How to fix records).
    - FAQ (Technical deep dive).
- [ ] Replicate directory structure and files for other locales (`ar`, `de`, `es`, `fr`, `id`, `jp`, `ko`, `ru`, `tr`, `ur`, `vi`).

## Phase 3: Navigation Integration
- [ ] Modify `docs.json` to register the new "Email Deliverability Audit" group.
- [ ] **Placement**: Ensure the group is positioned immediately after the "Spam Checker" group in the `navigation` array for all languages.
- [ ] Add the overview page to the "Guides" tab for English.
- [ ] Add corresponding entries for all other languages to maintain consistency.

## Phase 4: Verification
- [ ] Run `mint dev` (locally if applicable) to preview the new documentation.
- [ ] Check for broken links using `mint broken-links`.
- [ ] Verify that the "Open App" links point correctly to `https://nudgen.net/email-deliverability-audit`.

## Agent Assignments
| Agent | Task |
|-------|------|
| @frontend-specialist | MDX content creation and formatting |
| @orchestrator | `docs.json` navigation updates |
| @i18n-specialist | Translation of documentation (if requested) |
