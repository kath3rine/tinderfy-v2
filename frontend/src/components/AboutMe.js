import Logo from '../assets/about-logo.png';

function AboutMe(props) {
    return(
        <div className="component" id="about-me">
              <div className='title-container'>
                <img className="icon" src={Logo}></img>
                <h3>{props.title}</h3>
              </div>

                <div>
                  {props.urls ? (
                  <div>
                    {Array.from({ length: 5 }, (_, i) => i).map((i) => (
                      <div><a href={props.urls[i]}>
                        {i+1}. {props.names[i]} by {props.artists[i]}
                      </a></div>
                    ))}
                  </div>
                  ) : (
                    <div>
                      {Array.from({ length: 5 }, (_, i) => i).map((i) => (
                        <p>{i+1}. {props.names[i]} by {props.artists[i]}</p>
                      ))}
                    </div>
                  )}
                  
                </div>
              
              
        </div>
    );
}
export default AboutMe;