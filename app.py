from flask import Flask, render_template, request, jsonify
from image_search import search_images
from openai import OpenAI
from keys import openai_keys
app = Flask(__name__)

@app.route('/generate-mnemonic', methods=['POST'])
def generate_mnemonic():
    data = request.get_json()
    print (data)
    query = data['query']
    # Call OpenAI API to generate mnemonic
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"Create a memorable mnemonic or short rhyming song for remembering the following concept: {query} in under 50 words"}
        ],
    )
    print (query)
    print (response)
    mnemonic = response.choices[0].message.content
    return jsonify({'mnemonic': mnemonic})

@app.route('/save-image', methods=['POST'])
def save_image():
    query = request.form['query']
    image_url = request.form['image_url']

    # Save the image URL and query to a file
    with open('saved_images.txt', 'a') as file:
        file.write(f"{query}: {image_url}\n")

    return render_template('save_confirmation.html', query=query, image_url=image_url)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        image_urls = search_images(query)  # Use your search function here
        return render_template('images.html', image_urls=image_urls, query=query)
    return render_template('search.html')


@app.route('/flashcards')
def flashcards():
    with open('saved_images.txt', 'r') as file:
        lines = file.readlines()

    flashcards = [{'query': line.split(': ')[0], 'image_url': line.split(': ')[1].strip()} for line in lines]
    return render_template('flashcards.html', flashcards=flashcards)

if __name__ == '__main__':
    client = OpenAI(api_key=openai_keys['OPENAI_API_KEY'])
    app.run(debug=True)
