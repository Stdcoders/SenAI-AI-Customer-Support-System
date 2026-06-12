import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import ThreadWorkspace from "./pages/ThreadWorkspace";
import Analytics from "./pages/Analytics";

import Sidebar from "./components/Sidebar";

function App() {

    return (

        <div className="flex h-screen bg-slate-100">

            <Sidebar />

            <div className="flex-1 overflow-auto p-6">

                <Routes>

                    <Route

                        path="/"

                        element={<Dashboard />}

                    />

                    <Route

                        path="/thread"

                        element={<ThreadWorkspace />}

                    />

                    <Route

                        path="/analytics"

                        element={<Analytics />}

                    />

                </Routes>

            </div>

        </div>

    );

}

export default App;