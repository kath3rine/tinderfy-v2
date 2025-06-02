import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import Header from '../components/Header'
import AboutMe from '../components/AboutMe'
import Essentials from '../components/Essentials'
import Interests from '../components/Interests'
import LookingFor from '../components/LookingFor'
import Basics from '../components/Basics'
import MyAnthem from '../components/MyAnthem';
import Menu from '../components/Menu';
import '../styles/Profile.css'

const PartnerPage = () => {
    const location = useLocation();
    const { message } = location.state || {};
    const navigate = useNavigate();
    
    const goToUser = () => {
        navigate('/');
    }

    return (
        <div>
            
            {message && 
                
                <div className="profile-base">
                    <Header name={message.name} 
                    pfp={message.pfp}/>
 
                    <AboutMe title={`${message.name}'s favorite songs`}
                    names={message.track_names} 
                    artists={message.track_artists}/>
            
                    <Essentials title={`${message.name}'s top artists`}
                    list={message.top_artists}/>
            
                    <Interests title="Genres"
                    list={message.top_genres}/>
            
                    <LookingFor title="Uniqueness score"
                    x={100 - message.popularity}/>
            
                    <Basics title="Recommendations"
                    artist={message.rec_artist} 
                    track={message.rec_track}/>
            
                    <MyAnthem title={`${message.name}'s album`}
                    name={message.album} 
                    pfp={message.album_pfp} 
                    artist={message.album_artist}/>

                    <Menu/>
                </div>  
            }
        </div>
    );
};
export default PartnerPage;