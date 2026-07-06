class DecisionEngine:

    def decide(self, text):

        text = text.lower()

        if any(x in text for x in ("اسمي", "عمري", "بشتغل", "ساكن", "احكيلي عني")):
            return "profile"

        if any(c in text for c in "+-*/"):
            return "calculator"

        if any(x in text for x in ("فكرني", "ذكرني", "ميعاد", "الساعة", "بكرة")):
            return "reminder"

        if any(x in text for x in ("طقس", "حر", "مطر")):
            return "weather"

        if any(x in text for x in ("جمعية", "قسط", "فلوس", "مصروف")):
            return "finance"

        return "ai"
