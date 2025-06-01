import Logo from '../assets/music-logo.png'

function MyAnthem(props) {
    return(
        <div className="component" id="my-anthem">
            <div className="title-container">
                <img src={Logo} className='icon'></img> 
                <h3>{props.title}</h3>
            </div>

            <div id="my-anthem-container">
                <img src={props.pfp} />
                <div id="my-anthem-text">
                    <h3>{props.name}</h3>
                    <p>{props.artist}</p>
                </div>
            </div>
        </div>
        
    );
}
export default MyAnthem