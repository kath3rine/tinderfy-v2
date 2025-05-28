import React from 'react';
import { useLocation } from 'react-router-dom';

const PartnerPage = () => {
    const location = useLocation();
    const { message } = location.state || {};

    return (
        <div>
            <h1>partner page</h1>
            {message && <p>
                {message.toString()}
            </p>}
        </div>
    );
};
export default PartnerPage;