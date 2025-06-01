import Logo from '../assets/about-logo.png';

function AboutMe(props) {
    return(
        <div className="component" id="about-me">
              <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
              </div>
              
              {[0, 1, 2, 3, 4].map((i) => (
                <p>{i + 1}. {props.names[i]} by {props.artists[i]}</p>
              ))}
        </div>
    );
}
export default AboutMe;