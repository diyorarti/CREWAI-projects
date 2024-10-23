#!/usr/bin/env python
import sys
from a_martketing_team.crew import AMartketingTeamCrew
import datetime

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'instagram_description': input('Enter the page description here: '),
        'topic_of_the_week': input('Enter the topic of the week here: '),
    }
    AMartketingTeamCrew().crew().kickoff(inputs=inputs)


