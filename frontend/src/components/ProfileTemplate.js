function ProfileTemplate({data}) {
    return (
        <div>
          <h1>Me</h1>
          {data &&
          <div>
            <p>{data.name}</p>
            <img src={data.pfp} />
    
            <div>
              favorite songs: 
              {[0, 1, 2, 3, 4].map((i) => (
                <li>{i + 1}. {data.track_names[i]} by {data.track_artists[i]}</li>
              ))}
            </div>
    
            <div>
              favorite artists: 
              {[0, 1, 2, 3, 4].map((i) => (
                <li>{i + 1}. {data.artist_names[i]}</li>
              ))}
            </div>
    
            <div>
                recommendations
                artist:
                <p>{data.rec_artist}</p>
                <p>{data.rec_track == "None" ? "": `song: ${data.rec_track}`}</p>
            </div>
    
            <div>
              genres: {data.genres.map((genre) => (
                <li>{genre}</li>
              ))}
            </div>
    
            <div>
              popularity: {data.popularity}
            </div>
    
            <div>
              my album: {data.album}
            </div>
    
          </div>
          }
        </div>
      );
}
export default ProfileTemplate;