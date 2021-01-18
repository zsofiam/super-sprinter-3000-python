from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    all_user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=all_user_stories)


@app.route('/story', methods=['GET', 'POST'])
def new_story():
    user_story = {}
    if request.method == 'POST':
        user_story["title"] = request.form["story-title"]
        user_story["user_story"] = request.form["user-story"]
        user_story["acceptance_criteria"] = request.form["acceptance-criteria"]
        user_story["business_value"] = request.form["business-value"]
        user_story["estimation"] = request.form["estimation"]
        user_story["id"] = data_handler.get_new_id()
        user_story["status"] = 'planning'
        data_handler.add_user_story(user_story)
        return redirect('/')

    return render_template('story.html')


@app.route("/story/<story_id>", methods=['GET', 'POST', 'PUT'])
def edit_story(story_id):
    user_story = data_handler.get_user_story(story_id)
    if request.method == 'POST':
        data_handler.delete_user_story(story_id)
        user_story["title"] = request.form["story-title"]
        user_story["user_story"] = request.form["user-story"]
        user_story["acceptance_criteria"] = request.form["acceptance-criteria"]
        user_story["business_value"] = request.form["business-value"]
        user_story["estimation"] = request.form["estimation"]
        user_story["id"] = data_handler.get_new_id()
        user_story["status"] = request.form["status"]
        data_handler.add_user_story(user_story)
        return redirect('/')
    story_statuses = data_handler.STATUSES
    return render_template('story.html', story=user_story, statuses=story_statuses)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
