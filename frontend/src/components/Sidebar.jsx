import { NavLink } from "react-router-dom";

function Sidebar() {

    const linkStyle = ({ isActive }) =>

        `block rounded-lg px-4 py-3 mb-3 transition-all ${
            isActive
                ? "bg-blue-600 text-white"
                : "bg-white text-gray-700 hover:bg-blue-50"
        }`;

    return (

        <div className="w-64 min-h-screen bg-slate-900 text-white p-6 shadow-lg">

            <h1 className="text-3xl font-bold mb-2">

                SenAI

            </h1>

            <p className="text-slate-400 text-sm mb-10">

                AI Customer Support

            </p>

            <nav>

                <NavLink
                    to="/"
                    className={linkStyle}
                >
                    Dashboard
                </NavLink>

                <NavLink
                    to="/thread"
                    className={linkStyle}
                >
                    Thread Workspace
                </NavLink>

                <NavLink
                    to="/analytics"
                    className={linkStyle}
                >
                    Analytics
                </NavLink>

            </nav>

        </div>

    );

}

export default Sidebar;