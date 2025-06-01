import Logo from '../assets/essentials-logo.png';
import Icon from '../assets/person-logo.png';

function Essentials(props) {
    return(
        <div className="component" id="essentials">
              <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
              </div>

              {[0, 1, 2].map((i) => (
                <p className={`${i == 4 ? 'last-essential' : 'essential'}`}>
                  <img className="icon" src={Icon}></img>
                  {props.list[i]}
                </p>
              ))}
        </div>
    );
}
export default Essentials;