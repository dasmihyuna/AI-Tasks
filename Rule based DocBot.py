def appointment_chatbot():
    print("Hello! I'm DocBot, here to help you book a doctor's appointment.")

    last_prompt = ""

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("DocBot: Goodbye! Stay healthy.")
            break

        # Greetings
        elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
            print("DocBot: Hi there! Are you looking to book an appointment?")
            last_prompt = "booking"

        # Interpreting 'yes' in context
        elif user_input in ["yes", "yeah", "yup"]:
            if last_prompt == "booking":
                print("DocBot: Great! What type of doctor do you need? (e.g., dentist, cardiologist, general physician)")
                last_prompt = "doctor_type"
            elif last_prompt == "doctor_type":
                print("DocBot: Please tell me what kind of doctor you need. (e.g., dentist, cardiologist)")
            elif last_prompt == "day":
                print("DocBot: Awesome. What time would you prefer? (e.g., 10 AM, 2 PM)")
            elif last_prompt == "time":
                print("DocBot: Cool. Can I have your full name to confirm the appointment?")
                last_prompt = "name"
            elif last_prompt == "name":
                print("DocBot: Please type your full name so I can confirm the appointment.")
            else:
                print("DocBot: Could you clarify what you're saying 'yes' to?")

        # Intent to book
        elif "appointment" in user_input or "book" in user_input:
            print("DocBot: Great! What type of doctor do you need? (e.g., dentist, cardiologist, general physician)")
            last_prompt = "doctor_type"

        # Doctor type
        elif "dentist" in user_input:
            print("DocBot: Got it! Dentists are available Monday to Friday. What day works best for you?")
            last_prompt = "day"

        elif "cardiologist" in user_input:
            print("DocBot: Noted. Cardiologists are available on Wednesdays and Fridays. Which one do you prefer?")
            last_prompt = "day"

        elif "general" in user_input or "physician" in user_input:
            print("DocBot: General physicians are available every day. Would you like a morning or evening slot?")
            last_prompt = "time"

        # Day
        elif any(day in user_input for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]):
            print("DocBot: What time would you prefer? (e.g., 10 AM, 2 PM, 6 PM)")
            last_prompt = "time"

        # Time
        elif any(x in user_input for x in ["am", "pm", "morning", "evening", "10", "2", "6"]):
            print("DocBot: Thank you! Can I have your full name to confirm the appointment?")
            last_prompt = "name"

        # Name input (fuzzy matching)
        elif last_prompt == "name" and (
            user_input.startswith("my name is") or user_input.startswith("i am") or len(user_input.split()) >= 2
        ):
            name = user_input.replace("my name is", "").replace("i am", "").strip()
            name = name.title() if name else "Guest"
            print(f"DocBot: Thank you, {name}. Your appointment has been scheduled!")
            print("DocBot: You'll receive a confirmation message shortly. Take care!")
            break

        else:
            print("DocBot: I'm not sure how to respond to that. Could you please clarify?")

if __name__ == "__main__":
    appointment_chatbot()
