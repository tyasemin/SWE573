
<p align="center">
  <img src="assets/project_icon.png" alt="Connect the Dots" width="250">
</p>


<p align="center">
  <img src="assets/CONNECTTHEDOTS.gif" width="900">
</p>


## Research
### wikidata
<ul>
  <li>Wikidata was launched in 2012 as a sister project of Wikipedia. It is an open-source platform that serves as central storage for structured data.</li>
  <li>Some of the Wikidata query examples can be found at: <a href="Wikidata_Examples_Page.md">Wikidata Examples</a></li>
</ul>

## Elicitation Questions

The aim of the elicitation questions is gathering information, clarifying the requirements of the project.

Elicitation questions can be found at : <a href="elicitation_questions.md">Click</a></li>

## Mockups

The aim to create mockup is to understand the project requirements better. <a href="mockups.md">Click</a></li>

## SRS Documentation

### 📅 Project Timeline (March 25 – May 13, 2025)

#### 🟢 - March 25: Requirements & Design Phase
- Collect and document all functional and non-functional requirements
- Define user roles and interaction flows
- Create user stories and use cases
- Design low-fidelity wireframes and flow diagrams
- Prepare design mockups 
- Plan technical architecture (frontend, backend, data model, APIs)
- Draft initial project plan and timeline
- Decide on tech stack and CI/CD tools (e.g., GitHub Actions, GitLab CI)
- User registration & login 

#### 🛠 March 25 – March 27 (parallel task): Initial CI/CD Setup
- Set up Git repository and branching strategy
- Configure CI pipeline (lint, test, build)
- Prepare Dockerfile and basic docker-compose setup
- Add automated tests to pipeline
- Configure deployment pipeline (staging environment)

#### 🟡 March 27 – April 18: Core Development Phase
- Backend setup: authentication, database models, REST APIs
- Frontend setup: layout, routing, forms
- Implement:
  - Boards, tags, connections
- Integrate tag-based classification
- Deploy first staging version (auto-deploy via CI/CD)

#### 🌐 April 15 – April 18: Hosting Environment Setup
- Choose hosting platform (e.g., Vercel, Netlify, Heroku, AWS)
- Configure environment variables and secrets
- Set up database hosting (e.g., PostgreSQL on Supabase or Railway)
- Connect frontend/backend with hosted DB
- Enable HTTPS and domain setup (optional)

#### 🟠 April 19 – April 29: Interactive & Visual Features
- Implement:
  - Voting system
  - Connection editing with history
  - Graph-based visualization (D3.js or Cytoscape.js)
  - Filtering UI
- Begin Wikidata integration (suggestions from SPARQL)
- Show user contribution history
- Predefined tag setup

#### 🔵 April 30 – May 9: Final Features, Testing & Fixes
- Add:
  - Discussion section
  - Trending topics logic
  - Contributors view per topic
  - Media upload and quick links
- Full system testing: functionality, UI/UX, performance
- Fix bugs and polish design
- Add final test coverage to CI pipeline

#### 🟣 May 10 – May 13: Final Packaging & Delivery
- Final testing on production/staging
- Prepare and record demo video (if needed)
- Write handover or user guide (optional)
- Deliver final product with documentation
- Present or deploy publicly

