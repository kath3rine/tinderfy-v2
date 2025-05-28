function Essentials(props) {
    return(
        <div className="component" id="essentials">
              <h3>{props.title} </h3>
              {[0, 1, 2].map((i) => (
                <li className={`${i == 4 ? 'last-essential' : 'essential'}`}>
                  {props.list[i]}
                </li>
              ))}
        </div>
    );
}
export default Essentials;