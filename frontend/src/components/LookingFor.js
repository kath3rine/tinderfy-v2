import Logo from '../assets/lookingfor-logo.png';
import Logo1 from '../assets/logo1.png'
import Logo2 from '../assets/logo2.png'
import Logo3 from '../assets/logo3.png'
import Logo4 from '../assets/logo4.png'

function LookingFor(props) {
    var icon = Logo1;
    if (props.x > 75) {
        icon = Logo4;
    } else if (props.x > 50) {
        icon = Logo3;
    } else if (props.x > 25) {
        icon = Logo2;
    } 

    return(
        <div className="component" id="looking-for">
            <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
            </div>
            
            <div className='title-container'>
                <img className="icon2" src={icon}></img>
                <h2>{props.x} / 100</h2>
            </div>
            
        </div>
    );
}
export default LookingFor;