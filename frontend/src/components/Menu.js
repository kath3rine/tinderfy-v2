import { useNavigate } from 'react-router-dom';
import '../styles/Menu.css';

function Menu() {
    const navigate = useNavigate();
    const onClickUser = () => {
        navigate('/');
      }
    
      const onClickSubmit = () => {
        navigate('/submit');
      }

    return(
        <div id="menu">
            <div className='menu-button-container'>
                <button id="user-button"
                    className="menu-button"
                    onClick={onClickUser}>
                    Profile
                </button>
            </div>
            
            <div className='menu-button-container'>
                <button id="submit-button"
                    className="menu-button"
                    onClick={onClickSubmit}>
                    Match
                </button>
            </div>
            
        </div>
    );
}
export default Menu