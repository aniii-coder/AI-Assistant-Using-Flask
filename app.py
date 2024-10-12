from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Set your API key (replace <YOUR_API_KEY> with your actual key)
os.environ["API_KEY"] = "<YOUR_API_KEY>"

# Configure the Google Generative AI API with the API key
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    # Call the AI response function to get a response from the model
    ai_response = get_ai_response(user_input)
    return jsonify({"response": ai_response})

def get_ai_response(question):
    # Generate AI content based on user input
    try:
        response = model.generate_content(question)
        return response.text.replace("**", "")  # Remove any markdown or bold characters
    except Exception as e:
        return f"Error generating response: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
