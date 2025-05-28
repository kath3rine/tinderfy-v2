
function AboutMe(props) {
    return(
        <div className="component" id="about-me">
              <h3>" {props.title}</h3>
              {[0, 1, 2, 3, 4].map((i) => (
                <p>{i + 1}. {props.names[i]} by {props.artists[i]}</p>
              ))}
        </div>
    );
}
export default AboutMe;