import React, { useState } from 'react';
import './Auth.css';
import SignUp from '../../organisms/SignUp';
import SignIn from '../../organisms/SignIn';
import Overlay from '../../organisms/Overlay';

function SignPage() {
  const [rightPanelActive, setRightPanelActive] = useState(true);

  const handleClickSignUpButton = () => setRightPanelActive(true);
  const handleClickSignInButton = () => setRightPanelActive(false);

  return (
    <div className="Auth">
      <div className={`container ${rightPanelActive ? 'right-panel-active' : ''}`} id="container">
        <SignUp />
        <SignIn />
        <Overlay
          handleClickSignInButton={handleClickSignInButton}
          handleClickSignUpButton={handleClickSignUpButton}
        />
      </div>
    </div>
  );
}

export default SignPage;