import re


class HeuristicService:

    SPAM_KEYWORDS = [
        "seo",
        "backlink",
        "guest post",
        "buy now",
        "nigerian prince",
        "lottery",
        "free money",
        "crypto investment",
    ]

    URGENT_KEYWORDS = [
        "urgent",
        "asap",
        "immediately",
        "critical",
        "p0",
        "outage",
        "production down",
        "legal",
        "cease and desist",
    ]

    SECURITY_KEYWORDS = [
        "ransomware",
        "btc",
        "bitcoin",
        "breach",
        "hacked",
        "unauthorized login",
        "security incident",
        "publish data",
    ]

    INTERNAL_DOMAINS = [
        "@internal.com",
        "@mycompany.com",
    ]

    GDPR_KEYWORDS = [
        "gdpr",
        "article 20",
        "data portability",
        "delete my data",
        "privacy request",
    ]

    def analyze(self, payload):

        subject = (payload.subject or "").strip().lower()
        body = (payload.body or "").strip().lower()
        sender = (payload.sender or "").lower()

        text = f"{subject} {body}"

        result = {
            "tool": "heuristic",
            "is_spam": False,
            "is_security": False,
            "is_internal": False,
            "is_gdpr": False,
            "priority": "Low",
            "queue": "normal",
            "requires_human": False,
            "confidence": 0.90,
            "matched_rules": [],
        }

        # Empty email

        if not subject and not body:

            result["requires_human"] = True
            result["queue"] = "manual_review"
            result["matched_rules"].append("empty_email")

            return result

        # Spam detection

        spam_matches = [
            keyword
            for keyword in self.SPAM_KEYWORDS
            if keyword in text
        ]

        if spam_matches:

            result["is_spam"] = True
            result["queue"] = "spam"
            result["confidence"] = 0.99
            result["matched_rules"].extend(spam_matches)

            return result

        # Internal email

        if any(
            sender.endswith(domain)
            for domain in self.INTERNAL_DOMAINS
        ):

            result["is_internal"] = True
            result["queue"] = "internal"
            result["matched_rules"].append("internal_sender")

        # Security detection

        security_matches = [
            keyword
            for keyword in self.SECURITY_KEYWORDS
            if keyword in text
        ]

        if security_matches:

            result["is_security"] = True
            result["priority"] = "Critical"
            result["queue"] = "security"
            result["requires_human"] = True
            result["confidence"] = 0.99
            result["matched_rules"].extend(security_matches)

        # GDPR detection

        gdpr_matches = [
            keyword
            for keyword in self.GDPR_KEYWORDS
            if keyword in text
        ]

        if gdpr_matches:

            result["is_gdpr"] = True
            result["priority"] = "Critical"
            result["queue"] = "legal"
            result["requires_human"] = True
            result["confidence"] = 0.99
            result["matched_rules"].extend(gdpr_matches)

        # Urgency

        if any(
            keyword in text
            for keyword in self.URGENT_KEYWORDS
        ):

            result["priority"] = "High"

        # Long email

        if len(body) > 10000:

            result["requires_human"] = True
            result["matched_rules"].append("long_email")

        return result

    #
    # Agent compatibility
    #

    def process(self, payload):

        return self.analyze(payload)


heuristic_service = HeuristicService()