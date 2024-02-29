import React from 'react';
import './App.css';
import RouteLink from './routes/Route';
import NavBar from "./components/organisms/NavBar";

import { PersistGate } from 'redux-persist/integration/react';
import { store, persistor } from './store/store';

function App() {
  return (
    <div className="App">
      <PersistGate loading={null} persistor={persistor}>
        <NavBar></NavBar>
        <RouteLink></RouteLink>
      </PersistGate>
    </div>
  );
}

export default App;
