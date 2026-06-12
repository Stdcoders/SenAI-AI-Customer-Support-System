import { useEffect, useState } from "react";

import {
    LineChart,
    Line,
    CartesianGrid,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
} from "recharts";

import api from "../services/api";

function Analytics() {

    const [sender, setSender] = useState("");

    const [days, setDays] = useState(30);

    const [trend, setTrend] = useState(null);

    const [categories, setCategories] = useState([]);

    useEffect(() => {

        loadCategories();

    }, []);

    async function loadCategories() {

        try {

            const response = await api.get(

                "/analytics/category-breakdown"

            );

            setCategories(

                response.data.data

            );

        }

        catch (error) {

            console.log(error);

        }

    }

    async function loadTrend() {

        try {

            const response = await api.get(

                "/analytics/sentiment-trend",

                {

                    params: {

                        sender,

                        days,

                    },

                }

            );

            setTrend(

                response.data.data

            );

        }

        catch (error) {

            console.log(error);

        }

    }

    const trendData = trend
        ? [

              {

                  name: "Average",

                  score: trend.average_sentiment,

              },

              {

                  name: "Latest",

                  score: trend.latest_sentiment,

              },

          ]
        : [];

    return (

        <div>

            <h1 className="text-4xl font-bold mb-8">

                Analytics

            </h1>

            <div className="bg-white rounded-xl shadow p-5 mb-8">

                <h2 className="text-xl font-semibold mb-4">

                    Sentiment Trend

                </h2>

                <div className="flex gap-4 mb-5">

                    <input

                        className="border rounded-lg p-3 flex-1"

                        placeholder="Customer Email"

                        value={sender}

                        onChange={(e) =>

                            setSender(e.target.value)

                        }

                    />

                    <input

                        type="number"

                        className="border rounded-lg p-3 w-32"

                        value={days}

                        onChange={(e) =>

                            setDays(e.target.value)

                        }

                    />

                    <button

                        className="bg-blue-600 text-white px-5 rounded-lg"

                        onClick={loadTrend}

                    >

                        Analyze

                    </button>

                </div>

                <ResponsiveContainer

                    width="100%"

                    height={300}

                >

                    <LineChart

                        data={trendData}

                    >

                        <CartesianGrid strokeDasharray="3 3" />

                        <XAxis dataKey="name" />

                        <YAxis />

                        <Tooltip />

                        <Line

                            type="monotone"

                            dataKey="score"

                            stroke="#2563eb"

                            strokeWidth={3}

                        />

                    </LineChart>

                </ResponsiveContainer>

                {

                    trend &&

                    <div className="mt-6 space-y-2">

                        <p>

                            <strong>

                                Trend:

                            </strong>

                            {" "}

                            {trend.trend}

                        </p>

                        <p>

                            <strong>

                                Requires Attention:

                            </strong>

                            {" "}

                            {

                                trend.requires_attention

                                    ? "Yes"

                                    : "No"

                            }

                        </p>

                        <p>

                            <strong>

                                Recommendation:

                            </strong>

                            {" "}

                            {

                                trend.recommendation ||

                                "-"

                            }

                        </p>

                    </div>

                }

            </div>

            <div className="bg-white rounded-xl shadow p-5">

                <h2 className="text-xl font-semibold mb-4">

                    Category Breakdown

                </h2>

                <ResponsiveContainer

                    width="100%"

                    height={350}

                >

                    <BarChart

                        data={categories}

                    >

                        <CartesianGrid strokeDasharray="3 3" />

                        <XAxis dataKey="category" />

                        <YAxis />

                        <Tooltip />

                        <Bar

                            dataKey="count"

                            fill="#2563eb"

                        />

                    </BarChart>

                </ResponsiveContainer>

            </div>

        </div>

    );

}

export default Analytics;