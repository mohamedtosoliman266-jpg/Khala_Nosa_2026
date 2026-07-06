import re


class FactsExtractor:

    PATTERNS = [

        (r"انا بحب (.+)", "likes"),

        (r"أنا بحب (.+)", "likes"),

        (r"انا بكره (.+)", "dislikes"),

        (r"أنا بكره (.+)", "dislikes"),

        (r"لوني المفضل (.+)", "favorite_color"),

        (r"عربيتي (.+)", "car"),

        (r"مراتي اسمها (.+)", "wife"),

        (r"زوجتي اسمها (.+)", "wife"),

        (r"ابني اسمه (.+)", "son"),

        (r"بنتي اسمها (.+)", "daughter"),
    ]

    def extract(self, message):

        text = (
            message.strip()
            .replace("؟", "")
            .replace("?", "")
            .replace("ى", "ي")
        )

        for pattern, key in self.PATTERNS:

            m = re.fullmatch(pattern, text)

            if m:

                return {
                    "intent": "save_fact",
                    "key": key,
                    "value": m.group(1).strip(),
                }

        return None
