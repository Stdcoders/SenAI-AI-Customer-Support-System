import { useState } from "react";

import api from "../services/api";

function ThreadWorkspace() {

    const [email, setEmail] = useState("");

    const [thread, setThread] = useState(null);

    const [contact, setContact] = useState(null);

    const [reasoning, setReasoning] = useState(null);

    const [loading, setLoading] = useState(false);

    async function loadWorkspace() {

        setLoading(true);

        try {

            const threadResponse = await api.get(

                `/threads/${email}`

            );

            const contactResponse = await api.get(

                `/contacts/${email}`

            );

            setThread(

                threadResponse.data.data

            );

            setContact(

                contactResponse.data.data

            );

        }

        catch (error) {

            console.log(error);

        }

        finally {

            setLoading(false);

        }

    }

    async function runAgent() {

        if (!thread) return;

        try {

            const response = await api.post(

                `/agent/dry-run/${thread.thread_id}`

            );

            setReasoning(

                response.data.data

            );

        }

        catch (error) {

            console.log(error);

        }

    }

    async function respond() {

        if (!thread) return;

        try {

            await api.post(

                `/respond/${thread.thread_id}`

            );

            alert("Response marked as sent.");

        }

        catch (error) {

            console.log(error);

        }

    }

    return (

        <div>

            <h1 className="text-4xl font-bold mb-8">

                Thread Workspace

            </h1>

            <div className="flex gap-4 mb-6">

                <input

                    className="border rounded-lg p-3 flex-1"

                    placeholder="Customer Email"

                    value={email}

                    onChange={(e) =>

                        setEmail(e.target.value)

                    }

                />

                <button

                    onClick={loadWorkspace}

                    className="bg-blue-600 text-white px-5 rounded-lg"

                >

                    Load

                </button>

            </div>

            {

                loading &&

                <p>Loading...</p>

            }

            {

                thread &&

                <div className="grid grid-cols-2 gap-6">

                    <div className="bg-white rounded-xl shadow p-5">

                        <h2 className="font-bold text-xl mb-4">

                            Conversation

                        </h2>

                        {

                            thread.history?.map(

                                (item, index) => (

                                    <div

                                        key={index}

                                        className="border-b py-3"

                                    >

                                        <div className="font-semibold">

                                            {item.sender}

                                        </div>

                                        <div>

                                            {item.body}

                                        </div>

                                    </div>

                                )

                            )

                        }

                    </div>

                    <div className="bg-white rounded-xl shadow p-5">

                        <h2 className="font-bold text-xl mb-4">

                            Contact Profile

                        </h2>

                        <p>

                            Email : {contact?.email}

                        </p>

                        <p>

                            Status : {contact?.status}

                        </p>

                        <p>

                            Total Threads :

                            {" "}

                            {contact?.total_threads}

                        </p>

                        <p>

                            Total Emails :

                            {" "}

                            {contact?.total_emails}

                        </p>

                    </div>

                </div>

            }

            {

                thread &&

                <div className="mt-8 flex gap-4">

                    <button

                        onClick={runAgent}

                        className="bg-green-600 text-white px-5 py-3 rounded-lg"

                    >

                        Run Agent

                    </button>

                    <button

                        onClick={respond}

                        className="bg-blue-600 text-white px-5 py-3 rounded-lg"

                    >

                        Respond

                    </button>

                </div>

            }

            {

                reasoning &&

                <div className="bg-white rounded-xl shadow p-5 mt-8">

                    <h2 className="font-bold text-xl mb-4">

                        Agent Reasoning

                    </h2>

                    {

                        reasoning.reasoning?.map(

                            (step) => (

                                <div

                                    key={step.step}

                                    className="border-b py-4"

                                >

                                    <p>

                                        <strong>

                                            Thought:

                                        </strong>

                                        {" "}

                                        {step.thought}

                                    </p>

                                    <p>

                                        <strong>

                                            Action:

                                        </strong>

                                        {" "}

                                        {step.action}

                                    </p>

                                    <p>

                                        <strong>

                                            Observation:

                                        </strong>

                                    </p>

                                    <pre className="bg-slate-100 p-2 rounded mt-2 overflow-auto">

                                        {

                                            JSON.stringify(

                                                step.observation,

                                                null,

                                                2

                                            )

                                        }

                                    </pre>

                                </div>

                            )

                        )

                    }

                </div>

            }

        </div>

    );

}

export default ThreadWorkspace;