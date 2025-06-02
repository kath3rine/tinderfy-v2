import Logo from '../assets/basics-logo.png';
import ArtistLogo from '../assets/person-logo.png';
import SongLogo from '../assets/music-logo.png';

function Component({subtitle, rec, style, logo, url}) {
    return(
        <div id={`${style == "border" ? "basic-border" : "basic"}`}>
            <p id="basic-subtitle">{subtitle}</p>
            <img className="icon" src={logo}></img>
            <span id="basic-rec">
                <a href={url}>
                    {rec}
                </a>
            </span>
        </div>
    );
}

function Basics(props) {
    return(
        <div className="component" id="basics">
                <div className='title-container'>
                    <img className="icon" src={Logo}></img>
                    <h3>{props.title}</h3>
                </div>
                
                { (props.track != "None" && props.artist != "None") ? (
                    <div>
                        <Component 
                            subtitle="Artist" 
                            rec={props.artist}
                            style="border"
                            logo={ArtistLogo}
                            url={props.artist_url} />

                        <Component 
                            subtitle="Song" 
                            rec={props.track}
                            style="no-border"
                            logo={SongLogo}
                            url={props.track_url} />
                    </div>
                ) : (
                    <div>
                        {(props.track === "None" && props.artist != "None") ? (
                            <Component 
                            subtitle="Artist" 
                            rec={props.artist}
                            style="no-border"
                            logo={ArtistLogo}
                            url={props.artist_url} />
                        ) : (
                            <Component 
                            subtitle="Song" 
                            rec={props.track}
                            style="no-border"
                            logo={SongLogo}
                            url={props.track_url} />
                        )}
                    </div>
                )}
                
            </div>
    );
}
export default Basics;