import { useNavigate } from 'react-router-dom';
import '../styles/Menu.css';

const Menu = () => {
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
                    My profile
                </button>
            </div>
            
            <div className='menu-button-container'>
                <button id="submit-button"
                    className="menu-button"
                    onClick={onClickSubmit}>
                    Find my match
                </button>
            </div>
            
        </div>
    );
}
export default Menu