import React from 'react';
import ReactDOM from 'react-dom/client';
import { CounterApp } from './CounterApp';

import { FirstApp } from './FirstApp';
// import { HelloWorldApp } from './HelloWorldApp';
import './styles.css';



ReactDOM.createRoot( document.getElementById('root') ).render(
    <React.StrictMode>
        <CounterApp value={ 20 } />
        {/* <FirstApp title="Hola, Soy Vegeta" /> */}
    </React.StrictMode>
);


//se instala jest
//https://jestjs.io/docs/getting-started

//se instala babel
//yarn add --dev babel-jest @babel/core @babel/preset-env

//React Testing Library para DOM 
//https://testing-library.com/docs/react-testing-library/intro
