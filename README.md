# CREWAI Projects
This repository showcases various projects built using the CREWAI framework. The projects are designed to demonstrate the power of multi-agent systems and task orchestration for use cases like marketing strategy generation, meeting preparation, and more. Each project employs tools such as Exa Search and agents from the CREWAI framework.

## Projects Overview
1. **Meeting Preparation System** (CREWAI-tutorial)
- Description: This project automates the preparation process for business meetings by creating a multi-agent system that performs research, industry analysis, meeting strategy development, and summarizes everything in a concise briefing document.
## Key Features:
- Agents: Research Specialist, Industry Analyst, Strategy Advisor, Briefing Coordinator.
- Tasks: Research on meeting participants, industry analysis, development of strategy points, and briefing preparation.
Integration with Exa Search Toolset for web-based research.
## Technologies Used:
- CREWAI
- Exa_py
- Langchain
**Files**:
- Agents: CREWAI-tutorial/agents.py
- Tasks: CREWAI-tutorial/tasks.py
- Execution: CREWAI-tutorial/main.py, CREWAI-tutorial/app.py
2. **A Marketing Team** (a_marketing_team)
- Description: This project creates a virtual marketing team that generates content strategies, researches SEO trends, and schedules social media posts. The system orchestrates a content strategist, SEO researcher, and social media manager to automate key marketing tasks.
## Key Features:
- Agents: Content Strategist, SEO Researcher, Social Media Manager.
- Tasks: Generate creative content ideas, SEO hashtag research, and content scheduling.
- Uses Exa Search Toolset and other web search tools for researching trends and keywords.
## Technologies Used:
- CREWAI
- Langchain
- Exa_py
- Files:
- Agents & Tasks: a_marketing_team/src/config/agents.yaml, a_marketing_team/src/config/tasks.yaml
- Main logic: a_marketing_team/src/main.py

## Features
- Multi-Agent Systems: Each project leverages CREWAI agents to perform specific roles, from researching to strategizing and creating output.
- Automated Task Orchestration: Tasks such as research, strategy development, and social media content scheduling are automated and can be customized to fit various workflows.
- Custom Tools: Integrated with tools like Exa Search for querying the web and Serper API for Google search results to enhance research capabilities.