import random


# Assignment 8: Event Organizer and Analyzer
# Instructions:
# Write a program that simulates the organization and analysis of an event. The event has various activities,
# and participants will vote for their favorite activity at the end. Perform the following tasks:
# 1. Create a dictionary of activities with a unique ID (int) for each.
# 2. Generate a random list of votes (IDs) from participants.
# 3. Tally the votes and determine the most popular activity.
# 4. Return a summary: the total number of votes, the winning activity, and its vote count.
# Example input: activities = {'1': 'Music', '2': 'Sports', '3': 'Gaming'}, votes = ['2', '3', '2', '1', '3', '3', '2']
# Expected output: ('Total Votes: 7', 'Winning Activity: Sports', 'Votes for Winning Activity: 3')


def event_organizer(activities: dict, votes: list) -> tuple[str, str, str]:
    # TODO:Your code here
    #  Tally the votes and find the most popular activity
    ...


def test_event_organizer():
    random.seed(0)  # Setting a random seed for reproducibility
    activities = {'1': 'Music', '2': 'Sports', '3': 'Gaming'}

    # Test Case 1: Small number of votes
    votes = random.choices(list(activities.keys()), k=10)
    assert event_organizer(activities, votes) == (
        'Total Votes: 10', 'Winning Activity: Sports', 'Votes for Winning Activity: 5')

    # Test Case 2: Another scenario
    votes = random.choices(list(activities.keys()), k=50)
    assert event_organizer(activities, votes) == (
        'Total Votes: 50', 'Winning Activity: Gaming', 'Votes for Winning Activity: 22')

    votes = random.choices(list(activities.keys()), k=100)
    assert event_organizer(activities, votes) == (
        'Total Votes: 100', 'Winning Activity: Gaming', 'Votes for Winning Activity: 41')

    print("All tests passed!")

# Uncomment to run the test function
# test_event_organizer()
