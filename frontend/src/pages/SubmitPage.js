import React, { useState } from 'react';
import axios from 'axios';
import '../styles/Submit.css';
import { useNavigate } from 'react-router-dom';
import Menu from '../components/Menu';
import Tinder from '../assets/tinder.png'

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
        <div id="submit-base"
        className="profile-base">
            <div id="title-container">
                <h1>Find My Match</h1>
                <img src={Tinder}></img>
            </div>
            

            <input className='submit-component'
            type="text"
            value={pid}
            onChange={e => setPid(e.target.value)}
            placeholder="Enter a playlist URL"
            />

            <form onSubmit={goToPartner}>
                <button className='submit-component'
                type="submit">
                    See profile
                </button>
            </form>
            <Menu/>
        </div>
    );
}
export default SubmitPage;