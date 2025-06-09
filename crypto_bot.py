class rulebasedchatbot:
    def __init__(self):
        self.crypto_db = {# Predefined crypto database
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}
    def greet(self):
        print("Hi! I'm CryptoBuddy – your AI-powered financial sidekick!")
        print("Ask me things like:\n- Which crypto is trending?\n- What's the most sustainable coin?\n- What should I buy for long-term growth?\n")

    def respond_to_query(self, user_query):
        query = user_query.lower()

        if "sustainable" in query or "eco" in query:
            # Recommend most sustainable coin
            best = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            print(f"Try {best}! It’s eco-friendly and built for the future.")

        elif "trending" in query or "rising" in query:
            trending = [coin for coin, data in self.crypto_db.items() if data["price_trend"] == "rising"]
            print(" These coins are trending up: " + ", ".join(trending))

        elif "long-term" in query or "growth" in query or "invest" in query:
            for coin, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                    print(f"🚀 {coin} is a great choice for long-term growth and sustainability!")
                    return
            print("No perfect picks right now. Check back later!")
            #Example of user query
chatbot= rulebasedchatbot()
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("👋 Bye! Happy investing!")
        break
    chatbot.respond_to_query(user_input)
    





