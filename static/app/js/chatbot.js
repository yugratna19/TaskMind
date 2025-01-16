// Toggle the chatbot visibility
function toggleChatbot() {
    const chatbotWindow = document.getElementById('chatbot-window');
    chatbotWindow.style.display = chatbotWindow.style.display === 'none' ? 'block' : 'none';
}

// Send a message to the chatbot
function sendMessage() {
    const inputField = document.getElementById('chatbot-input');
    const userMessage = inputField.value.trim();

    if (userMessage === '') return;

    displayMessage(userMessage, 'user');
    inputField.value = '';

    // Simulate bot response (this will later be connected to Rasa)
    setTimeout(() => {
        displayMessage("Coming soon...", 'bot');
    }, 500);
}

// Display messages in the chat window
function displayMessage(message, sender) {
    const chatbox = document.getElementById('chatbot-messages');
    const messageElement = document.createElement('div');
    messageElement.className = sender === 'user' ? 'user-message' : 'bot-message';
    messageElement.innerText = message;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Handle 'Enter' key press for sending messages
function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
