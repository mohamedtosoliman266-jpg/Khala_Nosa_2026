import re


class ProfileExtractor:

    def extract(self, message):

        text = (
            message.strip()
            .replace("؟", "")
            .replace("?", "")
            .replace("ى", "ي")
        )

        # ===== الاسم =====

        if re.fullmatch(r"(هو )?اسمي (ايه|إيه)", text):
            return {"intent": "ask_name"}

        m = re.fullmatch(r"(انا|أنا)?\s*اسمي\s+(.+)", text)
        if m:
            return {"intent": "save_name", "value": m.group(2).strip()}

        # ===== العمر =====

        if re.fullmatch(r"(كام سنة عندي|عمري كام)", text):
            return {"intent": "ask_age"}

        m = re.fullmatch(r"عمري\s+(\d+)\s*(سنة)?", text)
        if m:
            return {"intent": "save_age", "value": int(m.group(1))}

        # ===== المهنة =====

        if re.fullmatch(r"(بشتغل ايه|بشتغل إيه|ايه شغلي|إيه شغلي)", text):
            return {"intent": "ask_job"}

        m = re.fullmatch(r"(انا|أنا)?\s*(بشتغل|شغال)\s+(.+)", text)
        if m:
            return {"intent": "save_job", "value": m.group(3).strip()}

        # ===== المدينة =====

        if re.fullmatch(r"(ساكن فين|عايش فين)", text):
            return {"intent": "ask_city"}

        m = re.fullmatch(r"(انا|أنا)?\s*(ساكن|عايش)\s+في\s+(.+)", text)
        if m:
            return {"intent": "save_city", "value": m.group(3).strip()}

        # ===== ملخص =====

        if text == "احكيلي عني":
            return {"intent": "about_me"}

        return  None

