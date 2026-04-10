# PLAN-email-spam-check

Plan for documenting the **Email Spam Checker** tool in the `nudgen-docs` repository.

## 1. Context & Requirements
- **Goal**: Add a dedicated documentation page for the Email Spam Checker tool (`https://nudgen.net/email-spam-checker`).
- **Location**: A new "Spam Checker" section in the navigation.
- **Content**: How the tool works, explanation of the "Spam Score," and how it helps with deliverability.

## 2. Proposed Structure
- **Directory**: `en/spam-checker/`
- **File**: `en/spam-checker/overview.mdx`
- **Navigation**: Add a "Spam Checker" group to `docs.json` immediately after the "Signature Generator" section.

## 3. Implementation Tasks

### Phase 1: Structure & Configuration
- [ ] Create the `en/spam-checker` directory.
- [ ] Add the "Spam Checker" group to `en` navigation in `docs.json`.

### Phase 2: Content Development
- [ ] Create `en/spam-checker/overview.mdx`.
- [ ] Write introductory content explaining the purpose of the tool.
- [ ] Detail the "Analysis" features:
    - **Spam Score**: Explain the radial gauge and risk levels (Good, Caution, Risky).
    - **Spam Triggers**: How Nudgen identifies words that trigger spam filters.
    - **Best Practices**: Tips for improving deliverability based on the tool's output.
- [ ] Add a "Try it out" link pointing to `https://nudgen.net/email-spam-checker`.

### Phase 3: Verification
- [ ] Run `mint dev` to preview the new page and navigation.
- [ ] Check for broken links using `mint broken-links`.
- [ ] Verify MDX formatting (cards, accordions, etc.) matches the existing style.

## 4. Verification Checklist
- [ ] **Navigation**: Is "Spam Checker" visible in the sidebar?
- [ ] **Content**: Does the page clearly explain how to use the Spam Checker?
- [ ] **Links**: Does the link to the tool work?
- [ ] **Style**: Does it follow the Mintlify standards (Sentence case headings, active voice)?

## 5. Agent Assignments
- **Project Planner**: Create this plan and coordinate tasks.
- **Frontend/Content Specialist**: Writing the MDX content and updating `docs.json`.
- **QA/Reviewer**: Running the local preview and link checks.
