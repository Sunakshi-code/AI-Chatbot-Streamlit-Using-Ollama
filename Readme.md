# 🤖 AI Chatbot using Streamlit & Ollama

An interactive AI-powered chatbot developed using **Python, Streamlit, and Ollama**. This application provides a conversational AI experience through a clean, responsive, and user-friendly web interface.

It uses the **Qwen 2.5 (1.5B)** language model through Ollama to generate AI responses locally without requiring an external cloud-based AI API.

## 🚀 Project Overview

The AI Chatbot is designed to provide an intelligent conversational experience. Users can ask questions, explore ideas, learn new skills, and receive helpful AI-generated responses.

The application also allows users to customize the AI's response personality, manage conversations, and download chat history.

## ✨ Key Features

### 1. AI-Powered Conversations
- Interactive chatbot powered by Ollama.
- Uses Qwen 2.5 (1.5B) language model.
- Generates responses based on user queries.
- Maintains conversation context during the current session.

### 2. Multiple AI Response Personalities

Users can customize how the AI responds by selecting one of four response styles:

| Response Style | Description |
|---|---|
| Friendly | Friendly and conversational responses |
| Professional | Clear, structured, and professional responses |
| Teacher | Step-by-step explanations with simple examples |
| Technical | Detailed technical explanations and terminology |

### 3. Chat Management
- **New Chat:** Start a fresh conversation.
- **Clear Chat:** Clear the current conversation.
- **Chat History:** Display messages from the current conversation.
- **Message Counter:** Track the number of messages.

### 4. Download Chat History
- Download the current conversation as a `.txt` file.
- Includes both user messages and AI responses.
- Useful for saving conversations for future reference.

### 5. User Interface & Design
- Clean and interactive Streamlit interface.
- Theme-aware styling for light and dark themes.
- Custom CSS styling.
- Sidebar navigation.
- Chat message containers.
- Loading spinner while AI generates responses.
- Responsive and user-friendly layout.

### 6. Error Handling
- Handles Ollama connection errors.
- Displays helpful error messages.
- Checks for empty AI responses.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Ollama | Local LLM integration |
| Qwen 2.5 (1.5B) | AI language model |
| HTML & CSS | Custom interface styling |

## 🧠 AI Model

**Model:** Qwen 2.5 (1.5B)

**Model identifier:** `qwen2.5:1.5b`

The chatbot uses Ollama to run the Qwen language model locally and generate conversational responses.

## 📂 Project Structure

```text
AI-Chatbot/
│
├── app.py
├── test_ollama.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd AI-Chatbot
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Install Ollama

Download and install Ollama:

https://ollama.com/

### Step 6: Download the AI Model

Open the terminal and execute:

```bash
ollama pull qwen2.5:1.5b
```

### Step 7: Run the Application

Execute the following command:

```bash
 python -m streamlit run app.py
```

The chatbot will open in your default web browser.

## 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
ollama
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building interactive web applications using Streamlit.
- Integrating locally hosted Large Language Models.
- Connecting Python applications with Ollama.
- Managing conversational context using Streamlit Session State.
- Implementing customizable AI response personalities.
- Designing user interfaces using custom CSS.
- Handling exceptions and application errors.
- Managing Python dependencies and virtual environments.

## 🔮 Future Enhancements

- Support for multiple AI language models.
- Persistent conversation history.
- Chat search functionality.
- Export conversations in PDF format.
- Document-based question answering.
- Improved response streaming.

## 👩‍💻 Author

**Sunakshi Chauhan**

MCA Student | Aspiring Data Analyst

GitHub: https://github.com/Sunakshi-code

---

⭐ If you find this project interesting, feel free to explore the repository!