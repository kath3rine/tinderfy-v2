import React, { useState, useEffect } from 'react';
import axios from "axios";
import '../styles/MePage.css';

const MePage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get('http://localhost:5000/me', { withCredentials: true })
      .then((res) => setData(res.data))
      .catch((err) => {
        setError(err);
      });
  }, []);

  if (error) return <div><p>oops</p>{error.toString()}</div>

  return (
    <div>
      <h1>Me</h1>
      <p>{data && JSON.stringify(data)}</p>
    </div>
  );
}
export default MePage;
