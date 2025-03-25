
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
- [x] Collect and document all functional and non-functional requirements  
- [x] Define user roles and interaction flows  
- [x] Create user stories and use cases  
- [x] Design low-fidelity wireframes and flow diagrams  
- [x] Prepare design mockups  
- [x] Plan technical architecture (frontend, backend, data model, APIs)  
- [x] Draft initial project plan and timeline  
- [x] Decide on tech stack and CI/CD tools (e.g., GitHub Actions, GitLab CI)
- [ ] Configure CI pipeline (lint, test, build)
- [ ] Backend setup: authentication, database models, REST APIs  
- [ ] Frontend setup: layout, routing, forms
- [ ] Implement user registration & login


#### 🟡 March 25 – April 15: Core Development Phase
- [ ] Deploy first staging version via CI/CD
- [ ] Implement Boards, Tags, Connections logic  
- [ ] Integrate tag-based classification system  
- [ ] Set up Git repository and branching strategy  
- [ ] Configure CI pipeline (lint, test, build)  
- [ ] Prepare `Dockerfile` and basic `docker-compose` setup  
- [ ] Add automated tests to pipeline  
- [ ] Configure deployment pipeline (staging environment)
- [ ] Implement unit tests 

#### 🌐 April 15 – April 22: Hosting Environment Setup
- [ ] Choose hosting platform (e.g., Vercel, Netlify, Heroku, AWS)  
- [ ] Configure environment variables and secrets  
- [ ] Set up PostgreSQL hosting (e.g., Supabase or Railway)  
- [ ] Connect frontend/backend to the hosted DB  
- [ ] Enable HTTPS and domain setup (optional)

      
#### 🟠 April 22 – April 29: Interactive & Visual Features
- [ ] Implement connection editing with history tracking  
- [ ] Build graph-based visualization (D3.js or Cytoscape.js)  
- [ ] Create filterable UI for nodes and relationships  
- [ ] Begin Wikidata integration (SPARQL suggestions)  
- [ ] Display user contribution history  
- [ ] Predefined tag logic and UI  

#### 🔵 April 30 – May 9: Final Features, Testing & Fixes
- [ ] Add discussion section per node  
- [ ] Implement trending topics algorithm  
- [ ] Add contributors view per topic  
- [ ] Finalize media upload and quick access links  
- [ ] Complete system testing: functionality, UX, performance  
- [ ] Fix critical bugs and polish design  
- [ ] Add final test coverage to CI/CD pipeline  

#### 🟣 May 10 – May 13: Final Packaging & Delivery
- [ ] Run final testing on production or staging  
- [ ] Record product demo video (if needed)  
- [ ] Write handover guide or user documentation  
- [ ] Package and deliver the final product  
- [ ] Present or deploy project publicly  

# DB ER Diagram

<p align="center">
  <img src="assets/db_ER_diagram.png" width="900">
</p>
