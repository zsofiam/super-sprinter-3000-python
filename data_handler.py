import csv
import os

#DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_FILE_PATH = 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
LATEST_ID_PATH = 'latest_id.txt'

def get_all_user_story():
    user_stories = []
    with open(DATA_FILE_PATH) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user_stories.append(row)
    return user_stories

def add_user_story(user_story):
    user_stories = get_all_user_story()
    user_stories.append(user_story)
    save_user_stories_in_file(user_stories)


def save_user_stories_in_file(user_stories):
    f = open(DATA_FILE_PATH, "w")
    writer = csv.DictWriter(f, DATA_HEADER)
    writer.writeheader()
    for story in user_stories:
        writer.writerow(story)
    f.close()


def get_new_id():
    new_id = 1
    with open(LATEST_ID_PATH) as file:
        new_id += int(file.read())
    with open(LATEST_ID_PATH, 'w') as file:
        file.write(str(new_id))
    return new_id

def get_user_story(story_id):
    user_stories = get_all_user_story()
    for user_story in user_stories:
        if user_story['id'] == story_id:
            return user_story
    return None

def delete_user_story(story_id):
    user_stories = get_all_user_story()
    user_stories = delete_user_story_from_list(story_id, user_stories)
    save_user_stories_in_file(user_stories)

def delete_user_story_from_list(story_id, user_stories):
    new_user_stories = []
    for user_story in user_stories:
        if int(user_story["id"]) is not int(story_id):
            new_user_stories.append(user_story)
    return new_user_stories



