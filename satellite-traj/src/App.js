import logo from './solar-system.png';
import './App.css';

function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Orbital mechanics simulator
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <Button text="Mercury" onClick={() => alert("Hello!")} />
        <Button text="Wenus" onClick={() => alert("Hello!")} />
        <Button text="Earth" onClick={() => alert("Hello!")} />
        <Button text="Mars" onClick={() => alert("Hello!")} />
        <Button text="Jupiter" onClick={() => alert("Hello!")} />
        <Button text="Saturn" onClick={() => alert("Hello!")} />
        <Button text="Uranus" onClick={() => alert("Hello!")} />
        <Button text="Neptune" onClick={() => alert("Hello!")} />
        <Button text="Pluto" onClick={() => alert("Hello!")} />
    </div>
  );
}

export default App;
