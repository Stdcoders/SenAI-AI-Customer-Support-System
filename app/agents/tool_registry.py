from app.services.rag_service import rag_service
from app.services.classification_service import classification_service
from app.services.heuristic_service import heuristic_service
from app.services.sentiment_service import sentiment_trend_service
from app.services.contact_service import contact_service
from app.services.reply_service import draft_reply_service
from app.services.escalation_service import escalation_service
from app.services.thread_service import thread_service
TOOLS = {

    "rag_search": rag_service.search,

    "classify": classification_service.classify,

    "heuristic": heuristic_service.analyze,

    "sentiment_trend": sentiment_trend_service.analyze,

    "thread_history": thread_service.get_history,

    "contact_profile": contact_service.get_profile,

    "draft_reply": draft_reply_service.generate,

    "escalate": escalation_service.escalate,

}