from flask import Blueprint, render_template, request, redirect, url_for
from notion_client import Client
import os

view= Blueprint('view', __name__)
page_id = os.environ.get('PAGE_ID')
db_id = os.environ.get('DB_ID')
token =os.environ.get('TOKEN')
client = Client(auth=token)


@view.route('/')
def top():
    return redirect(url_for("view.HxS_request"))


@view.route('/HxS_request', methods=['GET','POST'])
def HxS_request():
    if request.method == 'POST':
        content = request.form['content']
        title = request.form['title']
        add_suggestion(content, title)
        return render_template("succ_post.html")
    else:
        return render_template('form.html')



def add_suggestion(content, title):
    client.pages.create(
        **{
            "parent": {"database_id": db_id},
            "properties": {
                "Title": {"title": [{"text": {"content": title}}]},
            },
            "children": [{
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": content}}]
                }
            }
            ]
            }
    )
