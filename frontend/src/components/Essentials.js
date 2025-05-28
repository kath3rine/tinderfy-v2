function Essentials({list}) {
    return(
        <div className="component" id="essentials">
              <h3>My top artists </h3>
              {[0, 1, 2, 3, 4].map((i) => (
                <li className={`${i == 4 ? 'last-essential' : 'essential'}`}>
                  {list[i]}
                </li>
              ))}
        </div>
    );
}
export default Essentials;