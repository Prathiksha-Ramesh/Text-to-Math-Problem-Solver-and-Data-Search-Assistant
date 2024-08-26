# Text to Math Problem Solver and Data Search Assistant

This project is a Streamlit-based web application that serves as a math problem solver and data search assistant using the Google Gemma 2 model. The app leverages the power of Large Language Models (LLMs) via the `ChatGroq` model and various tools to help users solve mathematical problems and search for information on the internet.

## Features

- **Math Problem Solver**: The app can solve complex mathematical problems by interpreting and calculating user inputs. It provides detailed, step-by-step explanations of how it arrived at the solution.
  
- **Data Search Assistant**: The app includes a Wikipedia search tool that fetches relevant information on various topics, making it a powerful assistant for research and learning.

- **Interactive Chat Interface**: The app offers a chat-based interface where users can interact with the assistant to solve problems or search for information.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Langchain**: Provides the underlying chain of operations for LLMs and tools integration.
- **ChatGroq**: An advanced LLM model from Groq for processing and generating responses.
- **WikipediaAPIWrapper**: For searching information on Wikipedia.
- **dotenv**: To manage environment variables securely.

## How to Run the Application

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/text-to-math-problem-solver.git
   cd text-to-math-problem-solver
   ```

2. **Install Dependencies:**

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

3. **Set Up Environment Variables:**

Create a `.env` file in the project root and add your Groq API key:

``` bash 
GROQ_API_KEY=your_api_key_here
```
4. **Run the App:**
Start the Streamlit server:

``` bash 
streamlit run app.py
```

5. **Access the Web App:**
Open your browser and go to `http://localhost:8501` to interact with the app.

## Usage
-`Input your Groq API key`: Enter your Groq API key in the sidebar to start using the app.
-`Ask a Math Question`: Type a mathematical problem or question in the text area and click "Find my answer" to get a detailed solution.
-`Search for Information`: You can also search for general information on a topic by using the integrated Wikipedia tool.

![Web App Screenshot](Screenshot%202024-08-26%20222321.png)



## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

