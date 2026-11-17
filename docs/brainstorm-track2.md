# AGENTHON 2026: Track 2 team brainstorm

<!-- (2026-11-16) -->

Snapshot of the team brainstorm taken on 16 November 2026.
This file is now the shared reference; edit it here.

## What we know

We have one day to build a working AI prototype and pitch it to a jury.
The detailed brief is handed out only at kick-off, so the exact task is unknown until Saturday morning.

| Item       | Detail                                                                                                           |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| Event      | AGENTHON, a GDG Torino hackathon in Google's Build with AI series ([event page](https://agenthon.gdgtorino.it/)) |
| When       | Saturday 21 November 2026, 9:00 to 21:00                                                                         |
| Where      | Feat. House, Via Giuseppe Giacosa 15, 10125 Torino                                                               |
| Format     | Kick-off and briefs, build time, final pitches, awards. Times per phase are not published yet                    |
| Team       | Solo or up to 3 people, 18 or older, one track per person                                                        |
| Bring      | Own laptop and charger                                                                                           |
| Cost       | Free                                                                                                             |
| Our status | Applied as a team to track 2. Acceptance emails go out by 17 November                                            |
| Rules      | Not published yet. The event page says they are coming soon                                                      |

## Our track: GenAI for marketing

Track 2 asks for AI systems that produce text, images and other content to support marketing, at scale.
That one sentence is all the event page gives; the full brief arrives after kick-off.

- The track has 50 seats, its own sponsor, its own jury and its own ranking.
- "At scale" is in the theme itself, so a single nice output is probably not enough.
  Expect to show many variants, many channels or many audiences.
- Open question: does the brief come with the sponsor's data, a client brand or a product to work on?

## Track 2 sponsor: Demetra

[Demetra](https://demetradesign.it/) is a Torino integrated communication agency, and one of its people sits on our jury.
The event page lists it as the track 2 sponsor; track 1 belongs to Ariete Tech Solutions.

| Area                    | What Demetra does                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| Consulting and strategy | Brand positioning, tone of voice, marketing plans, buyer personas, competitor analysis                  |
| Digital marketing       | Social media management, editorial plans, Meta, Google, LinkedIn and TikTok ads, lead generation        |
| Branding and image      | Visual identity, brochures, catalogues, packaging, product and corporate photo and video                |
| Web design              | Sites and e-commerce on WordPress and Shopify, SEO                                                      |
| AI automation           | Lead to AI to CRM to conversion flows with Zapier and n8n, email automation, AI consulting and training |

Three things worth knowing before we pick an idea:

- **They already sell an AI product.**
  [AI4Lead](https://ai4lead.com/) is their agent for B2B lead generation:
  it finds prospects, writes personalised outreach in the client's tone of voice, and qualifies leads.
  A plain outreach-email generator would look like a copy of it.
- **Their stated philosophy is direction before volume.**
  Their [approach page](https://demetradesign.it/approccio/) says working with them does not mean
  "making more content" or "chasing trends", but communicating with a direction and evolving with consistency.
  Content at scale that ignores brand strategy would go against the sponsor's own pitch.
- **Their clients are varied.**
  The [portfolio](https://demetradesign.it/portfolio/) names Shiseido, Stosa Cucine, Dorelan and BMW Motorrad dealer Biauto,
  and they run an automotive division, Demetra GT.
  An agency serving many brands needs tools that switch brand voice cleanly.

Our reading: the strongest fit is probably a tool an agency like Demetra could use across clients,
where brand strategy (positioning, tone of voice, personas) goes in and consistent multi-channel content comes out.
This is a guess until the brief is out.

## How we are judged

A jury of five scores each project on five criteria:
one juror from the track sponsor, one from GDG Torino and three external.
Names are not announced yet, and the page gives no weighting.

| Criterion                          | What it likely means for us                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| Innovation                         | Not another "write me a post" chatbot                       |
| Fit with the track theme           | Marketing content, produced at scale                        |
| Feasibility beyond the prototype   | A believable path to real use: cost, data, who would run it |
| Quality of the technical execution | The demo works live, not a slideshow                        |
| Quality of the pitch               | A clear story in a few minutes                              |

The second column is our reading, not the organisers' wording.

Prizes: up to €2,500 in total, going to the top two teams of each track and split equally within a team.
Each jury also gives books to projects that stand out.

## Proposed preparation before Saturday

Prepare generic plumbing only, and build the actual product on the day.
The rules are not published, and hackathons often require the project to be built during the event.

Our repository, [b-arol-o/agenthon-2026](https://github.com/b-arol-o/agenthon-2026),
has the event facts in `README.md` but no issues and no project code yet.

| Piece               | What it is                                                                        | Why before Saturday                   |
| ------------------- | --------------------------------------------------------------------------------- | ------------------------------------- |
| Repository identity | `README.md` with event facts, track theme, judging criteria, team                 | Everyone lands on the same page       |
| Python skeleton     | uv project, `src/` package, Ruff, pytest, `.env.example` for API keys             | No setup time lost at 9:00            |
| Generation plumbing | Thin provider-agnostic wrapper for text and image generation, with one smoke test | Swap models once the brief is known   |
| Demo shell          | Minimal web UI: prompt in, generated output shown                                 | Starting point for the live demo      |
| Pitch scaffold      | Short outline mapped to the five judging criteria                                 | The pitch is one of the five criteria |

None of this is built yet. It waits on the decisions below.

## Decisions for the team

These are the choices to settle in the brainstorming session.

- [ ] **Model provider.** Which API keys do we actually have?
      The natural guess is Gemini for text and images, since this is a Google Build with AI event,
      plus ElevenLabs for voice, since it is listed as tech partner.
      Neither is confirmed as required.
- [ ] **Scope of preparation.** All five pieces above, or only `README.md` and the Python skeleton for now?
- [ ] **Roles on the day.** Who builds the backend, who builds the demo UI, who owns the pitch?
- [ ] **Stack for the demo.** A quick Python UI, or a separate web frontend?
- [ ] **Budget.** Who pays for API usage, and is there a cap?
- [ ] **Rules check.** Someone rereads the event page before Saturday for the published rules and the per-phase schedule.

## Idea prompts

These questions are starting points for the session, not proposals.
The brief may narrow the field on Saturday, so aim for directions we can adapt.

- Which marketing job do we know first-hand, for example B2B industrial marketing, where generic tools do poorly?
- What does "at scale" mean for our idea: many languages, many channels, many customer segments, or many products?
- What keeps generated content on brand and factually correct? A review or checking step could be the innovation.
- Can one input, such as a product sheet or a catalogue, become a full campaign kit of posts, emails, images and voice-over?
- What would make the demo memorable in three minutes of live use?
- What would a marketing team need before trusting this in production? That is the feasibility criterion.

Add ideas below, one line each, with the name of who proposed it.

| Idea | Proposed by | Notes |
| ---- | ----------- | ----- |
|      |             |       |
|      |             |       |
|      |             |       |

## Session context for picking this up later

This section records where the working session stopped on 16 November,
so a new session or another assistant can continue without redoing the research.

### Done so far

- Read the [event page](https://agenthon.gdgtorino.it/) and the Demetra pages
  ([home](https://demetradesign.it/), [approach](https://demetradesign.it/approccio/),
  [projects](https://demetradesign.it/realta-e-progetti/), [AI4Lead](https://ai4lead.com/)).
  Everything learned is in the sections above.
- Inspected the repository: still the bare `python-project-template`, no issues.
- Wrote this document. No code was written; this file is the only change to the repository.

### State of the repository

- Repository: [b-arol-o/agenthon-2026](https://github.com/b-arol-o/agenthon-2026).
- Working branch of the session: `claude/sweet-mccarthy-ciyxfz`. It holds this file, merged with the latest `main`.
- Contents: devcontainer, a linter workflow, a docsify `docs/` folder, a `README.md` with the event facts
  and the original template text in `README_template.md`.
  No `pyproject.toml`, no source package.

### Waiting on the team

- The items under "Decisions for the team", above all the model provider and the scope of preparation.
- Acceptance email, due by 17 November.
- Published rules and per-phase schedule, both still missing from the event page.

### Next steps once decided

1. Extend `README.md` with the track theme, judging criteria and team roles.
2. Add the Python skeleton: uv project, `src/` package, Ruff, pytest, `.env.example`.
3. Add the generation wrapper and the demo shell, if the team wants them before Saturday.
4. Reread the event page for the rules before building anything product-specific.

### Practical notes

- In the cloud session, a site can only be read after its domain is added to the environment's allowed domains.
  `agenthon.gdgtorino.it` was added on 16 November;
  the page fetch tool still failed on it, while a plain download with `curl` worked.
- Not yet researched: the jury members (not announced), Ariete Tech Solutions (track 1 sponsor, not our track),
  and the other partners listed on the page (ElevenLabs, DevPunks, Apogeo, Feat. House),
  whose exact roles were not checked.

<!-- EOF -->
