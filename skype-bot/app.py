from markupsafe import escape
from flask import Flask, render_template, request, url_for, jsonify
from utilSkpy import buildStarted, buildSuccessful, buildFailed

app = Flask(__name__)
app.run(ssl_context='adhoc')


@app.route("/")
def hello_world():
    print("hello")
    return "<p>Index page</p>"


# @app.route('/hello')
# def hello():
#     return 'Hello, World'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


# @app.route('/api/e1', methods=['POST'])
# def my_test_endpoint():
#     input_json = request.get_json(force=True)
#     # force=True, above, is necessary if another developer
#     # forgot to set the MIME type to 'application/json'
#     print('data from client:'), input_json
#     dictToReturn = {'answer': 42}
#     return jsonify(dictToReturn)

@app.route('/api/e1', methods=['POST'])
def my_test_endpoint():
    print("got request /api/e1")
    input_json = request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'
    resource = input_json['resource']
    if resource == "build":
        status = input_json['data']['status']
        if status == "pending":
            print('BUILD STARTED..')
            buildStarted()
        if status == "succeeded":
            print('BUILD SUCCESSFUL..')
            buildSuccessful()
        if status == "failed":
            print('BUILD FAILED..')
            buildFailed()

    # Another way of accessing key's value in python: print (f"key: {key}, value: {mydictionary[key]}")
    # print(f"data from client:', {input_json['data']['status']}") # this works as well
    # if (input_json.data.status == "pending"):

    dataDictionary = {'answer': 42}
    return jsonify(dataDictionary)
