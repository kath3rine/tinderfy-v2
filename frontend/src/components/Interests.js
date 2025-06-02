import Logo from '../assets/interests-logo.png'

function Interests(props) {
    return(
        <div className="component" id="interests">
            <div className="title-container">
                <img className="icon" src={Logo}></img> 
                <h3>{props.title}</h3>
            </div>
              
              <div className="bubbles">
                {props.red_list && 
                    <div className="bubbles">
                        {props.red_list.map((item) => (
                            <div className="bubble" id="red-bubble">{item}</div>
                        ))}
                    </div>
                }
                {props.list.map((item) => (
                        <div className="bubble" id="grey-bubble">{item}</div>
                ))}
              </div>
        </div>
    );
}
export default Interests;