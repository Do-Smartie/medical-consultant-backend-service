import json

class MedicalModel:

    def __init__(self, message) -> None:
        self.message = message

    def get_health_tips(self):
        with open("health_tips.json", "r") as file:
            health_tips_data = json.load(file)
            for tip in health_tips_data["health_tips"]:
                print(str(tip["condition"]))
                if str(tip["condition"]).lower() == str(self.condition).lower():
                    return tip["tips"]
            return None

    def extract_condition(self) -> str:
        condition_keywords = [
        "sneeze", "sneezing", "shivering", "joint pain", "stomach pain",
        "acidity", "ulcer", "muscle pain", "vomiting", "weight gain",
        "anxiety", "mood swings", "weight loss", "irregular periods",
        "cough", "fever", "sweating", "indigestion", "headache",
        "back pain", "constipation", "diarrhea", "throat pain",
        "running nose", "neck pain", "dizziness", "cramps",
        "obesity", "dehydration", "knee pain", "depression",
        "lack of concentration", "cold", "acne", "insomnia",
        "hair care", "grey hair", "hair loss", "face care", "skin care",
        "body care", "foot care"]
        for keyword in condition_keywords:
            if keyword in self.message.lower():
                return keyword
        return None
    
    def give_tips(self):
        self.condition = self.extract_condition()
        if self.condition:
            tips = self.get_health_tips()
            print(f"Tips -> {tips}")
            l = []
            if tips:
                print(f"Health Tips for {self.condition}:")
                for i, tip in enumerate(tips, start=1):
                    l.append(f"{i}. {tip}")
                return l        
            else:
                return json.dumps({"error": f"No health tips found for {self.condition}"})
        else:
            return json.dumps({"error": "No health condition mentioned in the message"})
    
        


