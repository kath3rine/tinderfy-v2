    // App.js
    import React from 'react';
    import { BrowserRouter, Route, Routes } from 'react-router-dom';
    import UserPage from './components/UserPage';
    
    function App() {
        return (
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<UserPage />} />
            </Routes>
          </BrowserRouter>
        );
    }
    
    export default App;