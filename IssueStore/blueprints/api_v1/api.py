from flask import render_template, request, flash, redirect, url_for,  jsonify, Blueprint

from github import Github

git_bot = Github("99kies", "thf1290017556")

api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/issueStore', methods=["POST", "GET"])
def issueStore():
    title = request.values.get('title')
    body = request.values.get('body')
    labels = request.values.get('labels')

    if title and body:
        if labels:
            repo = git_bot.get_repo("99Kies/a_pri")

            # repo.create_issue("This is a test issue")
            repo.create_issue(title=title, body=body, labels=[labels, ])
            return jsonify({
                "result": "hello",
                "title": title,
                "body": body,
                "labels": labels,
                "code": "200"
            })
        else:
            repo = git_bot.get_repo("99Kies/a_pri")

            # repo.create_issue("This is a test issue")
            repo.create_issue(title=title, body=body, labels=["development", ])
            return jsonify({
                "result": "hello",
                "title": title,
                "body": body,
                "labels": labels,
                "code": "200"
            })
    return jsonify({
        "result": "Please post title and body.",
        "code": "201"
    })

    # for repo in g.get