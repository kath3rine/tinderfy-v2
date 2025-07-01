import React, { useState, useEffect } from 'react';
import Header from '../components/Header.tsx'
import AboutMe from '../components/AboutMe'
import Essentials from '../components/Essentials'
import Interests from '../components/Interests'
import LookingFor from '../components/LookingFor'
import Basics from '../components/Basics'
import MyAnthem from '../components/MyAnthem';
import Menu from '../components/Menu';
import axios from "axios";
import '../styles/Profile.css'

const MePage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get('http://localhost:5000/user', { withCredentials: true })
      .then((res) => setData(res.data))
      .catch((err) => {
        setError(err);
      });
  }, []);

  if (error) return <div>{error.toString()}</div>

  return(
    <div>
      
    
    <div>{data &&
      
      <div className="profile-base">
        <Header name={data.name} 
          pfp={data.pfp}/>

        <AboutMe title="My top songs"
          names={data.track_names} 
          artists={data.track_artists}/>

        <Essentials title="My top artists"
          list={data.top_artists}/>

        <Interests title="Genres"
          list={data.top_genres}/>

        <LookingFor title="Uniqueness score"
          x={100 - data.popularity}/>

        { (data.rec_artist != "None" || data.rec_track != "None") && 
          <Basics title="Recommendations"
          artist={data.rec_artist} 
          artist_url={data.rec_artist_url}
          track={data.rec_track}
          track_url={data.rec_track_url}/>
        }

        <MyAnthem title="My album"
          name={data.album} 
          pfp={data.album_pfp} 
          artist={data.album_artist}/>
        
        <Menu/>
      </div>  
    }
    </div>
    </div>
  );
  
}
export default MePage;
