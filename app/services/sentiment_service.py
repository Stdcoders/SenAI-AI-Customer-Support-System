from statistics import mean


class SentimentTrendService:
    """
    Computes sentiment trend across an email thread.

    Responsibilities

    - compute moving average
    - detect deterioration
    - recommend escalation
    """

    WINDOW_SIZE = 5

    def analyze(self, classifications):

        if not classifications:

            return {

                "trend": "Unknown",

                "average_sentiment": 0.0,

                "latest_sentiment": 0.0,

                "requires_attention": False,

                "recommendation": None,

            }

        scores = [

            item.get(

                "sentiment_score",

                0.0,

            )

            for item in classifications

        ]

        window = scores[-self.WINDOW_SIZE:]

        average = mean(window)

        latest = window[-1]

        consecutive_negative = 0

        for score in reversed(window):
            if score < 0:

                consecutive_negative += 1

            else:

                break

        deteriorating = (

            consecutive_negative >= 3
        )

        improving = (

            len(window) >= 2

            and latest > average

            and latest > 0

        )

        if deteriorating:

            trend = "Deteriorating"

            recommendation = (

                "Escalate to Customer Success"

            )

        elif improving:

            trend = "Improving"

            recommendation = None

        else:

            trend = "Stable"

            recommendation = None

        return {

            "trend": trend,

            "average_sentiment": round(

                average,

                2,

            ),

            "latest_sentiment": latest,

            "requires_attention": deteriorating,

            "recommendation": recommendation,

        }


sentiment_trend_service = SentimentTrendService()