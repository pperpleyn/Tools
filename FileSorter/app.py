from flask import Flask, request, render_template, jsonify
from utils.pathValidator import isValidPath, createDict, sortItemByExtension

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    default = render_template('base.html', items=[{"name": "No Item Found!"}], other_btn_disabled=True)
    if request.method == 'POST':
        path = request.form["folderPath"]
        if isValidPath(path):
            print(path, "is a valid path!")
            sample_list = [1, 2, 3]
            sample_list = createDict(path)
            return render_template('base.html', items=sample_list, other_btn_disabled=False)
        else:
            print(path, "is not a valid path!")
            return default
    return default

# For Future Feature
@app.route('/process-file', methods=['POST'])
def process_file():
    data = request.get_json()
    selected_item = data.get('item')
    
    print("Received path:", selected_item) # Check your terminal output!

    # Return a JSON object back to fetch()
    return jsonify({
        "status": "success",
        "received_path": selected_item
    })

@app.route('/sort-files', methods=['POST'])
def sort_files():
    path = sortItemByExtension()

    sample_list = createDict(path)
    return render_template('base.html', items=sample_list, other_btn_disabled=False)

if __name__ == '__main__':
    app.run(debug=True)