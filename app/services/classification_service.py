from app.services.heuristic_service import heuristic_service


class ClassificationService:

    CATEGORY_RULES = {
        "refund": "Billing",
        "invoice": "Billing",
        "payment": "Billing",
        "pricing": "Inquiry",
        "discount": "Inquiry",
        "feature": "Feature Request",
        "bug": "Bug Report",
        "error": "Bug Report",
        "crash": "Bug Report",
        "compliance": "Compliance",
        "hipaa": "Compliance",
        "gdpr": "Legal",
        "lawyer": "Legal",
        "legal": "Legal",
    }

    POSITIVE_WORDS = [
        "love",
        "great",
        "excellent",
        "happy",
        "thanks",
        "awesome",
    ]

    NEGATIVE_WORDS = [
        "refund",
        "angry",
        "hate",
        "terrible",
        "bad",
        "broken",
        "issue",
        "problem",
        "complaint",
    ]

    def classify(
        self,
        payload,
        thread_history=None,
        rag_context=None,
    ):

        heuristics = heuristic_service.analyze(payload)

        subject = (payload.subject or "").lower()
        body = (payload.body or "").lower()

        text = f"{subject} {body}"

        category = "Other"

        for keyword, value in self.CATEGORY_RULES.items():

            if keyword in text:
                category = value
                break

        positive = sum(
            word in text
            for word in self.POSITIVE_WORDS
        )

        negative = sum(
            word in text
            for word in self.NEGATIVE_WORDS
        )

        if positive > negative:

            sentiment = "Positive"
            sentiment_score = 0.7

        elif negative > positive:

            sentiment = "Negative"
            sentiment_score = -0.7

        else:

            sentiment = "Neutral"
            sentiment_score = 0.0

        confidence = 0.92

        requires_human = heuristics["requires_human"]

        escalation_reason = None
        suggested_reply = None

        if heuristics["is_security"]:

            category = "Security"
            requires_human = True
            escalation_reason = "Potential security incident"
            confidence = 0.99

        elif heuristics["is_gdpr"]:

            category = "Legal"
            requires_human = True
            escalation_reason = "GDPR compliance request"
            confidence = 0.99

        elif heuristics["is_spam"]:

            category = "Spam"
            requires_human = False
            confidence = 0.99

        else:

            suggested_reply = (
                "Thank you for contacting us. "
                "Your request has been received and "
                "our team will get back to you shortly."
            )

        detected_entities = {

            "order_ids": [],
            "ticket_ids": [],
            "monetary_amounts": [],
            "deadlines": [],
            "products_mentioned": [],
        }

        #
        # Agent-friendly output
        #

        needs_rag = category in [
            "Inquiry",
            "Billing",
            "Feature Request",
            "Compliance",
            "Legal",
        ]

        needs_heuristic = (
            heuristics["is_security"]
            or heuristics["is_gdpr"]
            or heuristics["is_spam"]
        )

        return {

            "tool": "classification",

            "intent": category.lower().replace(" ", "_"),

            "category": category,

            "sentiment": sentiment,

            "sentiment_score": sentiment_score,

            "urgency": heuristics["priority"],

            "requires_human": requires_human,

            "needs_rag": needs_rag,

            "needs_heuristic": needs_heuristic,

            "escalation_reason": escalation_reason,

            "suggested_reply": suggested_reply,

            "confidence": confidence,

            "detected_entities": detected_entities,

        }


classification_service = ClassificationService()