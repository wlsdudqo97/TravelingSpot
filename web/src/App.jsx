import React from 'react';
import { Route, Switch } from 'react-router';
import { BrowserRouter } from 'react-router-dom';

import Main from './pages/Main'
import Result from './pages/Result'

const App = () => {
  //
  return(
    <BrowserRouter>
      <Switch>
        <Route path="/result" component={Result} />
        <Route component={Main} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;