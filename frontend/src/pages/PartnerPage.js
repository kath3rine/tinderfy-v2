import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import Header from '../components/Header.tsx'
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

    return (
        <div>
            {message && 

                <div className="profile-base">
                    <Header 
                    name={message.name} 
                    pfp={message.pfp}/>
 
                    <AboutMe 
                    title={`${message.name}'s favorite songs`}
                    names={message.track_names} 
                    artists={message.track_artists}
                    urls={message.track_urls}/> 

                    <Essentials 
                    title={`${message.name}'s favorite artists`}
                    list={message.top_artists}
                    artist_urls={message.artist_urls}/>

                    {message.shared_artists.length > 0 && 
                        <div>
                            <Essentials 
                            title={`Artists you and ${message.name} both like`}
                            list={message.shared_artists}/>
                        </div>
                    }

                    <Interests 
                    title="Genres"
                    list={message.all_genres
                        .filter(element => !message.shared_genres.includes(element))
                        .slice(0, 5 - message.shared_genres.length)}
                    red_list={message.shared_genres}/>
            
                    <LookingFor 
                    title="Uniqueness score"
                    x={100 - message.popularity}/>

                    { (message.rec_artist != "None" || message.rec_track != "None") && 
                        <Basics title="Recommendations"
                        artist={message.rec_artist} 
                        artist_url={message.rec_artist_url}
                        track={message.rec_track}
                        track_url={message.rec_track_url}/>
                    }
                   
            
                    <MyAnthem 
                    title={`${message.name}'s album`}
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