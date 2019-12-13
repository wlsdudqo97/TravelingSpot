import React from 'react';

const Main = ({ history }) => {
  const onButtonClick = () => {
    history.push('/result');
  }

  return (
    <div className="main">
      <div>
        <h1>Title</h1>
        <h7>설명 어쩌구 저쩌구</h7>
      </div>
      <div>
        <button type="button" onClick={onButtonClick}>result</button>
      </div>
    </div>
  )
}

export default Main;