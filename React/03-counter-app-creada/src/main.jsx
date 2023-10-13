import React from "react";
import ReactDOM from "react-dom/client";

import {App} from "./FirstApp";
//tambien se puede importar asi
//import App from "./FirstApp";

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);
