import streamlit as st
from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MeetingPrepAgents

# Streamlit App
def main():
    # Load environment variables
    load_dotenv()
    
    st.title("Meeting Preparation Crew")
    st.write("Prepare for your meeting with detailed research, industry analysis, and strategy insights.")
    
    # Collect user inputs via Streamlit UI components
    meeting_participants = st.text_area("Enter participant emails (comma separated):", "")
    meeting_context = st.text_input("Enter meeting context:", "")
    meeting_objective = st.text_input("Enter your objective for the meeting:", "")
    
    # Proceed with the tasks if inputs are provided
    if st.button("Kick off Meeting Prep"):
        if meeting_participants and meeting_context and meeting_objective:
            # Initialize tasks and agents
            tasks = MeetingPrepTasks()
            agents = MeetingPrepAgents()
            
            research_agent = agents.research_agent()
            industry_analysis_agent = agents.industry_analysis_agent()
            meeting_strategy_agent = agents.meeting_strategy_agent()
            summary_and_briefing_agent = agents.summary_and_briefing_agent()
            
            # Create tasks for each agent
            research_task = tasks.research_task(research_agent, meeting_participants, meeting_context)
            industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent, meeting_participants, meeting_context)
            meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent, meeting_context, meeting_objective)
            summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent, meeting_context, meeting_objective)
            
            meeting_strategy_task.context = [research_task, industry_analysis_task]
            summary_and_briefing_task.context = [research_task, industry_analysis_task, meeting_strategy_task]
            
            # Initialize Crew with agents and tasks
            crew = Crew(
                agents=[
                    research_agent,
                    industry_analysis_agent,
                    meeting_strategy_agent,
                    summary_and_briefing_agent
                ],
                tasks=[
                    research_task,
                    industry_analysis_task,
                    meeting_strategy_task,
                    summary_and_briefing_task
                ]
            )
            
            # Kickoff the crew and display the results
            result = crew.kickoff()
            st.success("Meeting Prep Completed!")
            st.text_area("Result:", value=result, height=300)
        else:
            st.error("Please fill in all the fields before proceeding.")

if __name__ == "__main__":
    main()
