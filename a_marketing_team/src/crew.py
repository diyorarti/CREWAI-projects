from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from a_martketing_team.tools.search import Searchtools
# Uncomment the following line to use an example of a custom tool
# from a_martketing_team.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class AMartketingTeamCrew():
	"""AMartketingTeam crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def content_strategist(self) -> Agent:

		return Agent(
			config=self.agents_config['content_strategist'],
			tools=[
				SearchTools.search_internet,
                SearchTools.search_instagram,
                SearchTools.open_page
			],
			Verbose=True
		)
	
	@agent
	def seo_researcher(self) -> Agent:

		return Agent(
			config=self.agents_config['seo_researcher'],
			tools=[],
			Verbose=True
		)

	@agent
	def social_media_manager(self) -> Agent:

		return Agent(
			config=self.agents_config['social_media_manager'],
			tools=[],
			Verbose=True
		)



	
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)


    @task
	def generate_content_ideas(self) -> Task:
		return Task(
			config=self.tasks_config["generate_content_ideas"],
			agent=self.content_strategist,	
		)
	
	@task
	def seo_hashtag_research(self) -> Task:
		return Task(
			config=self.tasks_config["seo_hashtag_research"],
			agent=self.seo_researcher,
			
		)
	
	@task
	def content_scheduling(self) -> Task:
		return Task(
			config=self.tasks_config["content_scheduling"],
			agent=self.social_mdeia_manager,
			output_file="content_scheduling.md"
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the AMartketingTeam crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)