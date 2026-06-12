import { useEffect, useState } from "react";

import api from "../services/api";

import StatCard from "../components/StatCard";

function Dashboard() {

    const [stats, setStats] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchStats();

    }, []);

    async function fetchStats() {

        try {

            const response = await api.get(

                "/dashboard/stats"

            );

            setStats(response.data.data);

        }

        catch (error) {

            console.log(error);

        }

        finally {

            setLoading(false);

        }

    }

    if (loading) {

        return (

            <div className="text-xl">

                Loading...

            </div>

        );

    }

    return (

        <div>

            <h1 className="text-4xl font-bold mb-8">

                Mission Control Dashboard

            </h1>

            <div className="grid grid-cols-5 gap-5">

                <StatCard

                    title="Pending"

                    value={stats.pending}

                />

                <StatCard

                    title="Replied"

                    value={stats.replied}

                />

                <StatCard

                    title="Escalated"

                    value={stats.escalated}

                />

                <StatCard

                    title="Critical"

                    value={stats.critical}

                />

                <StatCard

                    title="Spam"

                    value={stats.spam}

                />

            </div>

        </div>

    );

}

export default Dashboard;