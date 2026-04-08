# PLAN-docs-updates.md

## Objective
Update the Nudgen documentation to include new features: CC/BCC support in campaigns, a navigation link to the Blog, and comprehensive documentation for the "Lead Email Finder" browser extension.

## Phase 1: Navigation & Global Configuration
Update `docs.json` to incorporate the new external link and the extension sidebar group.

- [x] **Task 1.1**: Add "Blog" as a global anchor before "Affiliate" in `docs.json`.
- [x] **Task 1.2**: Register the "Lead Email Finder" group in the sidebar with pages: Overview, Installation, and Usage.

## Phase 2: Campaign Documentation Enhancement
Update the existing campaign creation guide to reflect new capabilities.

- [x] **Task 2.1**: Edit `en/campaigns/create.mdx`.
    - Add a new section **CC and BCC Recipients**.
    - Explain how to add CC/BCC addresses in the wizard.
    - **CRITICAL**: Document the limit of **50 total recipients** (Primary + CC + BCC) per email.

## Phase 3: Extension Documentation (Lead Email Finder)
Create a new top-level group for the browser extension.

- [x] **Task 3.1**: Create directory `en/extension/`.
- [x] **Task 3.2**: Create `en/extension/overview.mdx`.
    - Content: Introduction to the cross-browser extension, high-accuracy email finding (99%), and LinkedIn profile scanning.
- [x] **Task 3.3**: Create `en/extension/installation.mdx`.
    - Content: Step-by-step for Chrome, Edge, and Firefox. Reference store links.
- [x] **Task 3.4**: Create `en/extension/usage.mdx`.
    - Content: How to scan LinkedIn profiles, verify emails in real-time, and export results via CSV.

## Phase 4: Quality Assurance
- [ ] **Task 4.1**: Verify all internal links point to the correct MDX files.
- [ ] **Task 4.2**: Ensure the 50-recipient limit is prominent in the campaign guide.
- [ ] **Task 4.3**: Confirm the Blog link in the sidebar correctly redirects to `https://nudgen.net/blog`.

## Final Checklist
- [ ] All new files created in `en/` folder.
- [ ] `docs.json` updated with new navigation items.
- [ ] No broken links in English documentation.
