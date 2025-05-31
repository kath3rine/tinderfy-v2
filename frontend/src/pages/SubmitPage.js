import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SubmitPage = () => {
    const [pid, setPid] = useState('')
    const navigation = useNavigate();

    const goToPartner = async(e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                'http://localhost:5000/match', 
                { pid: pid },
                {withCredentials: true} 
            );
            const message = response.data.message;
            navigation('/partner', { state: { message }});
        } catch (err) {
            alert(err);
        }
    };

    return(
        <div>
        <input 
                type="text"
                value={pid}
                onChange={e => setPid(e.target.value)}
                placeholder="Enter partner's playlist URL"
            />
        <form onSubmit={goToPartner}>
            <button type="submit">See partner's profile</button>
        </form>
        </div>
    );
}
export default SubmitPage;