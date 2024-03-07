import React, { useRef } from 'react';

import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Boxes from './components/Boxes';
import Headings from './components/Headings';
import NavScrollExample from './components/Navbar';
import Animationtime from './components/animationtime';
import Index1vedu from './components/index1vedu';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <NavScrollExample/>
    <div className="mainheadin"><Headings /></div>
    <Animationtime/>
    <div className="gap">
    {/* <OtterClone/> */}
    <Index1vedu/>

    </div>
    
    
    {/* <Boxes/> */}
    {/* <App/> */}
    

  </React.StrictMode>
);

reportWebVitals();
