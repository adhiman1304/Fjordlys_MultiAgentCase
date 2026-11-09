# Fjordlys Energi – Multi-Agent Case Workshop

Case material and Copilot Studio agent setup for a team workshop. Groups of consultants advise the fictitious company **Fjordlys Energi ASA** by interviewing six AI agents, then deliver a recommendation to a board.

The content is in Norwegian. The company is fictitious and not tied to any real organisation.

## How the workshop works

1. Each group reads the case description.
2. Groups interview agents 1–5 to gather facts, check rumours and find the real problem.
3. Groups use the delivery assistant to turn their findings into a recommendation in the fixed delivery format.
4. The board agent (facilitator only) assesses and ranks the deliveries.

## Agents

| Agent | Role |
|---|---|
| Anne | CEO, owns the goals but not the whole truth |
| Per | Spreads rumours |
| Jan | Holds the experience and process knowledge |
| Maria | Technology and digitalisation |
| Kari | Union representative |
| Leveranse-assistent | Available to groups. Asks pointed questions and produces the delivery in the required format |
| Styret | Board and judge (**facilitator only**) |

## Repository structure

| Path | Content |
|---|---|
| `01_case_description.md` | Case handed out to the groups |
| `02_leveransemal.md` | Delivery template groups must follow |
| `03_slide_case_og_utfordring.md` | Slide with case context and challenge (Marp) |
| `04_slide_leveranseformat.md` | Slide with the delivery format (Marp) |
| `COPILOT_OPPSETT/` | Ready-to-paste instructions and knowledge files per agent. Start with `LES_MEG_FORST.md` |
| `COPILOT_OPPSETT/7_Leveranse/` | Delivery assistant: instructions, knowledge and `SKILL.md` |
| `kunnskap/` | Knowledge files per agent, split by topic |
| `agenter/`, `agenter_src/` | Agent definitions and build scripts |
| `materiale/` | Source material (M01–M10) behind the agents |
| `leveranse.md`, `leveranse-format/` | Delivery assistant for VS Code Copilot Chat |
| `00_README_access_matrix.md` | Which agent may see which material |

## Setup

1. Create one agent per folder in `COPILOT_OPPSETT/` in Copilot Studio.
2. Paste `1_INSTRUKSJONER.txt` into the instructions field and upload the `KUNNSKAP` file(s) as knowledge.
3. Share agents 1–5 and the delivery assistant with participants. Keep the board agent private.

See `COPILOT_OPPSETT/LES_MEG_FORST.md` for details.

## Confidential material

The following files contain the answer key or board criteria and must not be shared with participants:

- `materiale/M00_answer_key_fact_sheet.md`
- `kunnskap/A6_Styret_dommer/`
- `COPILOT_OPPSETT/6_Styret_KUN_FASILITATOR/`

Keep this repository private.
