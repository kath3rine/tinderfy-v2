import Logo from '../assets/basics-logo.png';
import ArtistIcon from '../assets/person-logo.png';
import SongIcon from '../assets/music-logo.png';

function Basics(props) {
    return(
        <div className="component" id="basics">
                <div className='title-container'>
                    <img className="icon" src={Logo}></img>
                    <h3>{props.title}</h3>
                </div>
                
                
                <div className="basic-item" id={`${props.track == "None" ? "artist-no-track-rec" : "artist-track-rec"}`}>
                    <p className="basic-title">Artist</p>
                    <div className='title-container'>
                        <img className="icon" src={ArtistIcon}></img>
                        <p className="basic-text">{props.artist}</p>
                    </div>
                </div>
                <div className="basic-item" id={`${props.track == "None" ? "no-track-rec" : "track-rec"}`}>
                    <p className="basic-title">Song</p>
                    <div className='title-container'>
                        <img className="icon" src={SongIcon}></img>
                        <p className="basic-text">{props.track}</p>
                    </div>
                    
                </div>
            </div>
    );
}
export default Basics;