import streamlit as st

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    # Convert user input to lowercase for easier matching
    user_input_lower = user_input.lower()
    
    # Simple rule-based keywords to respond
    if "symptom" in user_input_lower:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input_lower:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input_lower:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    elif "emergency" in user_input_lower:
        return "If this is an emergency, please call your local emergency number immediately."
    elif "pain" in user_input_lower:
        return "Pain can be a sign of various conditions. It's best to consult a healthcare professional for an accurate diagnosis."
    else:
        # For other inputs, use a general response (DeepSeek-V3)
        return "I'm here to help! Can you provide more details about your concern?"

# Streamlit web app interface
def main():
    # Set up the web app title and input area
    st.title("Healthcare Assistant Chatbot")
    
    # Display a simple text input for user queries
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()