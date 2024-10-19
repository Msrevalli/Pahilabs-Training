from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route('/timeline')
def timeline():
    items = [{"title": f"Item {i}", "content": f"This is the content for item {i}."} for i in range(1, 21)]
    
    # Streaming logic
    def generate():
        with app.app_context():  # Ensure the app context is active
            for item in items:
                yield render_template("timeline_item.html", item=item)
                if items.index(item) % 5 == 0:
                    yield "<div class='loading'>Loading more items...</div>"

    return Response(generate(), content_type='text/html')

if __name__ == "__main__":
    app.run(debug=True)
