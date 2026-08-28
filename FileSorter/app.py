from flask import Flask, request, render_template, redirect, url_for
from utils.pathValidator import isValidPath, createDict, sortItemByExtension, sanitizePath, createDir

app = Flask(__name__)
g_path: str = ""

@app.route('/', methods=['GET', 'POST'])
def home():
    global g_path
    default = render_template('base.html', items=[{"name": "No Item Found!"}], other_btn_disabled=True)

    if request.method == 'POST':
        path = request.form["folderPath"]

        if isValidPath(path):
            path = sanitizePath(path)
            sample_list = createDict(path)
            g_path = path
            return render_template('base.html', items=sample_list, other_btn_disabled=False)
        else:
            print(path, "is not a valid path!")
            return default
    return default

# # For Future Feature
# @app.route('/process-file', methods=['POST'])
# def process_file():
#     data = request.get_json()
#     selected_item = data.get('item')
    
#     print("Received path:", selected_item) # Check your terminal output!

#     # Return a JSON object back to fetch()
#     return jsonify({
#         "status": "success",
#         "received_path": selected_item
#     })

@app.route('/sort-files', methods=['POST'])
def sort_files():
    createDir()
    sortItemByExtension(g_path)

    return redirect(url_for('refresh'))

@app.route('/refresh-1', methods=['GET', 'POST'])
def refresh():
    print("Refreshing path: " + g_path)
    sample_list = createDict(g_path)
    return render_template('base.html', items=sample_list, other_btn_disabled=False)

if __name__ == '__main__':
    app.run(debug=True)