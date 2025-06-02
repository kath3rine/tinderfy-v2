import Logo from '../assets/essentials-logo.png';
import Icon from '../assets/person-logo.png';

function Essentials(props) {
    return(
        <div className="component" id="essentials">
              <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
              </div>

                <div id="item">
                  {props.list.map((item, index) => (
                    <div className={`${index === props.list.length - 1 ? 'last-essential' : 'essential'}`}>
                      <img className="icon" src={Icon}></img>
                      {props.artist_urls ? (
                        <span><a href={props.artist_urls[index]}>{item}</a></span>
                      ) : (
                        <span>{item}</span>
                      )}
                    </div>
                ))}
                </div>

              
        </div>
    );
}
export default Essentials;