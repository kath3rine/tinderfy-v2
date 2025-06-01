import Logo from '../assets/interests-logo.png'

function Interests(props) {
    return(
        <div className="component" id="interests">
            <div className="title-container">
                <img className="icon" src={Logo}></img> 
                <h3>{props.title}</h3>
            </div>
              
              <div id="bubbles">
                {props.list.map((item) => (
                    <div id="bubble">{item}</div>
                ))}
              </div>
        </div>
    );
}
export default Interests;