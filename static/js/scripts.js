const bar = document.getElementById("bar");
const menu = document.getElementById("menu");

if(bar){
    bar.addEventListener("click", ()=>{
        menu.classList.toggle("active");
    });

}

// Function to toggle the chatbot window
function toggleChatbot() {
    var chatbotWindow = document.getElementById("chatbot-window");
    if (chatbotWindow.style.display === "none" || chatbotWindow.style.display === "") {
        chatbotWindow.style.display = "block";
    } else {
        chatbotWindow.style.display = "none";
    }
}

// Function to send message to the chatbot API and display the response
async function sendMessage() {
    var messageInput = document.getElementById("userMessage");
    var message = messageInput.value.trim();
    if (!message) return;

    var chatArea = document.getElementById("chatArea");

    // Display user's message
    chatArea.innerHTML += `<div style="text-align: right; margin-bottom: 10px;"><strong>You:</strong> ${message}</div>`;

    // Call the chatbot endpoint (adjust URL if necessary)
    // Example uses the default role "default"; if using user roles, pass a proper role parameter.
    const response = await fetch(`/chatbot/get-response/?message=${encodeURIComponent(message)}&role=default`);
    const data = await response.json();

    // Display the chatbot's response
    chatArea.innerHTML += `<div style="text-align: left; margin-bottom: 10px;"><strong>Bot:</strong> ${data.response}</div>`;

    // Clear the input field
    messageInput.value = "";

    // Auto-scroll chat area to the bottom
    chatArea.scrollTop = chatArea.scrollHeight;
}
