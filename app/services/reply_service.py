class DraftReplyService:
    """
    Generates a structured draft reply for the AI Agent.

    Agent Tool

    Responsibilities
    ----------------
    - prepare response template
    - include customer context
    - include policy context
    - return editable draft
    """

    def generate(

        self,

        customer_email: str,

        classification: dict,

        rag_context: str = "",

    ):

        category = classification.get(

            "category",

            "General",

        )

        reply = (

            f"Hello,\n\n"

            f"Thank you for contacting SenAI Support.\n\n"

            f"We have received your {category.lower()} request.\n\n"

        )

        if rag_context:

            reply += (

                "Based on our policies:\n\n"

                f"{rag_context}\n\n"

            )

        reply += (

            "If you need any additional assistance, "

            "please let us know.\n\n"

            "Best regards,\n"

            "SenAI Support"

        )

        return {

            "tool": "draft_reply",

            "category": category,

            "draft": reply,

        }


draft_reply_service = DraftReplyService()