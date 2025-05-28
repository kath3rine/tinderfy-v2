    // App.js
    import React from 'react';
    import { BrowserRouter, Route, Routes } from 'react-router-dom';
    import MePage from './components/MePage';
    import MatchPage from './components/MatchPage';
    
    function App() {
        return (
          <BrowserRouter>
            <Routes>
              <Route path="/match" element={<MatchPage />} />
              <Route path="/" element={<MePage />} />
            </Routes>
          </BrowserRouter>
        );
    }
    
    export default App;