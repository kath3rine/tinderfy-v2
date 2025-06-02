import Logo from '../assets/essentials-logo.png';
import Icon from '../assets/person-logo.png';

function Essentials(props) {
    return(
        <div className="component" id="essentials">
              <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
              </div>

              {props.list.map((item, index) => (
                <p className={`${index === props.list.length - 1 ? 'last-essential' : 'essential'}`}>
                  <img className="icon" src={Icon}></img>
                  {item}
                </p>
              ))}
        </div>
    );
}
export default Essentials;