import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import TimetablePage from './pages/TimetablePage';
import SettingsPage from './pages/SettingsPage';

const App: React.FC = () => {
  return (
    <Router>
      <div className="container mx-auto p-4">
        <Switch>
          <Route path="/" exact component={TimetablePage} />
          <Route path="/settings" component={SettingsPage} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
