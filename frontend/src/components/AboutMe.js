function AboutMe(props) {
    return(
        <div>
              favorite songs: 
              {[0, 1, 2, 3, 4].map((i) => (
                <li>{i + 1}. {props.names[i]} by {props.artists[i]}</li>
              ))}
        </div>
    );
}
export default AboutMe;