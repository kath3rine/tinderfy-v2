import React, { useState, useEffect } from 'react';
import ProfileTemplate from './ProfileTemplate.js';
import axios from "axios";

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
    <ProfileTemplate data={data}/>
  );
  
}
export default MePage;
