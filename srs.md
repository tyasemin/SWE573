<ol>
<li>Introduction</li>
<ul>
<li>1.1 Document Purpose</li>
The purpose of this document is to define in detail the functional and non-functional requirements of the web-based information connection platform to be developed. The document clearly states what the system should do, how it will interact with users, and what technical and structural limitations it is subject to.

The document creates a common reference source for project managers, software developers, designers, testers, and other stakeholders of the system. In addition, this document helps determine the path to be followed in the project development process and forms the basis for future version updates or system expansions.

The document aims to prevent misunderstanding of the requirements by clarifying the elements that are outside the scope of the system. In this way, all stakeholders are ensured to progress towards the same goal throughout the project.
  
<li>1.2 Document Scope</li>
This document defines the scope of the link-based information network platform to be developed. The system will be designed as a web-based application that allows users to establish meaningful connections between different entities (persons, concepts, events, places, etc.), visually analyze these connections, and produce content.

The following topics are covered in the scope of the document:

Basic functions to be provided by the system (search, content creation, editing, linking, voting, etc.)

User interactions and roles within the system

Technical limitations (language support, web access, anonymous login restriction, etc.)

Features such as graphical interface, tagging structure, change history, discussion area

Data suggestion integration with Wikidata

Boards, media integration, and contribution tracking system

The scope of this document covers only the features that will be offered in the first version of the system (MVP - Minimum Viable Product). Features such as the user scoring system planned to be added in the future are excluded from this document.

The document only includes the functional and non-functional requirements of the system, and detailed technical design and test scenarios are outside this scope.


<li>1.3 Definitions, Acronyms, and Abbreviations</li>
### Definitions, Acronyms, and Abbreviations

| **Term / Acronym**       | **Description** |
|--------------------------|-----------------|
| **Wikidata**             | A structured, open knowledge base that contains information about entities and their relationships. The system uses it to suggest relevant content. |
| **Tag**                  | Keywords used to classify and make content searchable. The system uses only tags for content organization, not categories. |
| **Connection / Link**    | A relationship or interaction created by users between different pieces of content (entities). |
| **Board**                | A collection of connections grouped under a specific topic or theme. Each board has an owner. |
| **MVP (Minimum Viable Product)** | The first functional version of the product that includes only core features. |
| **Voting System**        | A mechanism allowing users to upvote or downvote content based on its usefulness. |
| **Change History**       | A log that records all user modifications and additions with timestamps. |
| **Discussion Area**      | A forum-like section under each topic where users can post comments and exchange ideas. |
| **Web-Based Application**| Software that runs in a web browser, accessible across different platforms. |
| **Media Integration**    | The ability to attach media files such as images, videos, and documents to the content. |


<li>1.4 References</li>

- [Wikidata](https://www.wikidata.org/) - A free and open knowledge base that can be read and edited by both humans and machines. Used in the system to support content suggestion and connection building.

<li>1.5 Document Overview</li>
</ul>

<li>Product Overview</li>
<ul>
<li>2.1 Product Perspective</li>
  This system has been developed as a standalone web-based application and will not be directly integrated into any existing system. It aims to provide an interactive platform that allows users to establish connections between various entities (people, concepts, places, etc.), visually analyze these connections, and produce content.

The system will be designed to work integrated with Wikidata. Thanks to this integration, users will be able to get suggestions or pull data from Wikidata while producing content. However, artificial intelligence support is not mandatory, it can be added optionally.

The system will not have any category structure; instead, content will be classified only through tags. There will also be multiple boards within the system, and each board will have an owner. With this structure, users will be able to create customized boards based on their own focus areas.

This product offers a unique solution that combines features such as user-contributed link creation, voting, tagging, and visual analysis, unlike social media, content management, or infographic tools currently on the market. Some advanced features (such as a user rating system) will not be included in the first version, but are planned for later versions.


<li>2.2 Product Functions</li>

This system provides a platform that allows users to establish, organize, and analyze connections between various entities. The basic functions are:

Link Creation and Discovery:
Users can create new connections between different contents (people, places, concepts, etc.) and visually examine existing connections.

Search and Browse:
Users can explore content in the system by searching or browsing through tags.

Add and Edit Content:
Users can add new content, add descriptions/tags to existing links, and edit them. All changes are recorded in the change history.

Voting System:
Users can vote on the usefulness of the content; these votes are effective in highlighting the content.

Tagging System:
Content is classified only with tags. Categories are not used. The system offers predefined tags to the user.

Graphical Display:
Links are displayed in a graphical interface. Users can filter the links.

Contribution Tracking:
Every user can view the topics they have contributed to. Contributors for each topic are listed in a separate section.

Discussion Area:
Although there is no real-time messaging, there is a discussion section where users can share their opinions on every topic.

Popular and Trending Topics:
The system lists the trending and trending topics according to user activity.

Content Merge Suggestion:
If two contents are very similar, the system suggests merging them.

User Registration and Profile Information:
Anonymous login is not allowed. Users must add their work and location information when registering.

Board Management:
There are multiple boards in the system. Each board has an owner. These boards allow the links to be organized.

Media and Quick Link Integration:
Users can add media files to the content and use quick access links.

Content Suggestion with Wikidata:
The system works in conjunction with Wikidata to assist the user during content production.


<li>2.3 Product Constraints</li>

Language Support:
The application will only offer English language support. Other languages ​​will not be supported.

Anonymous Login is Prohibited:
Users are required to register to access the system. Anonymous (guest) logins are not allowed.

Category System Will Not Be Used:
Content will be classified only through tags instead of being divided into categories.

Artificial Intelligence Integration is Not Mandatory:
The system does not have to work with artificial intelligence support. However, the system must be compatible with Wikidata.

No Real-Time Chat:
There will be no real-time messaging feature in the application. Instead, a discussion area will be provided for each topic.

User Verification is Not Mandatory:
Registered users do not need to verify their identities. However, users are required to provide their work and location information.

No Point System in the First Version:
A point system is planned according to user contributions, but this feature will not be included in the first version.

Must be a Web-Based Application: The product will be developed to be accessible only via the web. Mobile or desktop application versions are not planned.


<li>2.4 User Characteristics</li>

The target user group of this system consists of individuals who are willing to produce and share information, have analytical thinking skills, are researcher and accustomed to using interactive platforms. Users are expected to have the following characteristics:

Registered Users:
Access to the system is only possible for registered users. Anonymous or guest logins are not allowed.

Professional and Individual Participants:
Users are responsible for entering their own work (profession) and location information when producing content in the system. Therefore, the system targets both individual users and people with professional backgrounds.

Ability to Produce and Interpret Content:
Users are expected to be competent in establishing connections between entities, adding explanations to these connections and creating meaningful content.

Familiarity with Technology:
Since a web-based interface is used, it is sufficient for users to have basic computer and internet knowledge. The user-friendly interface minimizes the need for technical knowledge.

Ability to Provide Interactive Contributions:
Users can contribute to content, vote, comment on others' contributions, and share ideas in discussion areas.

Contribution-Focused Profile Development:
Users can track the topics they contribute to and create a profile over time by evaluating their contribution history in the system.


<li>2.5 Assumptions and Dependencies</li>
<li>2.6 Apportioning of Requirements</li>
</ul>

<li>Requirements</li>
<ul>
<li>3.1 External Interfaces</li>
<li>3.2 Functional Requirements</li>
<ul>
<li>The system must allow users to create, explore and analyze connections between different entities.</li>
<li>Users must be able to interact with the system by searching, browsing, adding content, and analyzing data.</li>
<li>Users must be able to edit, annotate, and expand existing links. A change history should be maintained for changes made.</li>
<li>The system must support both user-based and content-based connections.</li>
<li>Users must be able to determine whether content is useful or not through a voting system.</li>
<li>Predefined labels must be provided for users.</li>
<li>Graphical representation must be used and connections should be filterable.</li>
<li>Users must be able to see the topics they have contributed to.</li>
<li>There must be a user scoring system based on user contributions and votes, but this will not be included in the first version.</li>
<li>Users must register and anonymous logins are not allowed.</li>
<li>Users must add their own business and location information.</li>

</ul>
  
<li>3.3 Non-Functional Requirements</li>
<ul>
<li>The product must only provide English support.</li>
<li>The user interface must be clear and easy to use.</li>
<li>The product must be web application.</li>
<li>Categories must not be used, content classification must be done only through tags.</li>
<li>Adding AI is not mandatory, but the system must work with Wikidata.</li>
<li>There will be no real-time chat feature added, but there must be a discussion section.</li>
<li>Popular and trending topics must be displayed based on user activity.</li>
<li>If the contents are too similar, it is suggested to merge them.</li>
<li>There must be a contributors section for each topic.</li>
<li>Media integration must be provided and fast links must be offered to users.</li>
<li>There must be more than one board in the system and each board must have an owner.</li>
<li>The system must provide guidance to users on generating content from Wikidata.</li>
<li>User verification will not be required as part of security requirements, but anonymous logins will not be allowed.</li>

</ul>


  
<li>3.4 Compliance</li>
<li>3.5 Design and Implementation</li>
</ul>

<li>Verification</li>
<li>Appendixes</li>
</ol>
