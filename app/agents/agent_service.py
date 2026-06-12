import json
import re
from typing import Any, Dict

import google.generativeai as genai

from app.core.config import settings
from app.agents.tool_registry import TOOLS
from app.services.classification_service import classification_service
from app.services.sentiment_service import sentiment_trend_service

genai.configure(api_key=settings.GOOGLE_API_KEY)

class AgentService:

    MAX_STEPS = 6

    SYSTEM_PROMPT = """
You are SenAI.

Think in ReAct format.

Available actions:

rag_search
classify
heuristic
sentiment_trend
thread_history
contact_profile
draft_reply
escalate
finish

Always return valid JSON:

{
    "thought":"",
    "action":"",
    "action_input":{},
    "final_answer":""
}
"""
    def __init__(self):

        self.model = genai.GenerativeModel(

            model_name="gemini-2.5-flash",

            system_instruction=self.SYSTEM_PROMPT,

        )
    def _extract_json(self, text: str) -> Dict[str, Any]:

        if not text:
            return {}

        try:
            return json.loads(text)

        except Exception:

            pass

        match = re.search(

            r"\{.*\}",

            text,

            re.DOTALL,

        )

        if match:

            try:

                return json.loads(match.group())

            except Exception:

                return {}

        return {}

    def _run_tool(

        self,

        action,

        action_input,

    ):

        tool = TOOLS.get(

            (action or "").lower()

        )

        if tool is None:

            return {

                "error": f"Unknown tool: {action}"

            }

        try:

            if isinstance(

                action_input,

                dict,

            ):

                return tool(

                    **action_input

                )

            return tool(

                action_input

            )

        except Exception as e:

            return {

                "error": str(e)

            }
    def _build_prompt(

        self,

        query,

        classification,

        trend,

        scratchpad,

    ):

        return f"""

User Query

{query}

Classification

{json.dumps(classification,indent=2)}

Sentiment

{json.dumps(trend,indent=2)}

Scratchpad

{json.dumps(scratchpad,indent=2,default=str)}

Return ONLY valid JSON.

"""
    def invoke(

        self,

        query,

        dry_run=False,

    ):

        from types import SimpleNamespace

        payload = SimpleNamespace(

            subject="",

            body=query,

            sender="",

        )

        classification = classification_service.classify(

            payload

        )

        trend = sentiment_trend_service.analyze(

            [

                classification

            ]

        )

        scratchpad = []

        for step in range(

            self.MAX_STEPS

        ):

            prompt = self._build_prompt(

                query,

                classification,

                trend,

                scratchpad,

            )

            response = self.model.generate_content(

                prompt

            )

            result = self._extract_json(

                response.text

            )

            thought = result.get(

                "thought",

                "",

            )

            action = result.get(

                "action",

                "",

            )

            action_input = result.get(

                "action_input",

                {},

            )

            scratchpad.append(

                {

                    "step": step + 1,

                    "thought": thought,

                    "action": action,

                    "action_input": action_input,

                }

            )

            if action.lower() == "finish":

                return {

                    "success": True,

                    "answer": result.get(

                        "final_answer",

                        "",

                    ),

                    "reasoning": scratchpad,

                    "classification": classification,

                    "sentiment_trend": trend,

                    "dry_run": dry_run,

                }

            if dry_run:

                scratchpad[-1]["observation"] = {

                    "dry_run": True,

                    "planned_action": action,

                    "planned_input": action_input,

                }

                continue

            observation = self._run_tool(

                action,

                action_input,

            )

            scratchpad[-1]["observation"] = observation

        return {

            "success": True,

            "answer": "Maximum reasoning steps reached.",

            "reasoning": scratchpad,

            "classification": classification,

            "sentiment_trend": trend,

            "dry_run": dry_run,

        }
agent_service = AgentService()