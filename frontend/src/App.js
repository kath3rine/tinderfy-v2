    // App.js
    import React from 'react';
    import { BrowserRouter, Route, Routes } from 'react-router-dom';
    import UserPage from './pages/UserPage';
    import SubmitPage from './pages/SubmitPage';
    import PartnerPage from './pages/PartnerPage';
    
    function App() {
        return (
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<UserPage />} />
              <Route path="/submit" element={<SubmitPage />} />
              <Route path="/partner" element={<PartnerPage />} />
            </Routes>
          </BrowserRouter>
        );
    }
    
    export default App;