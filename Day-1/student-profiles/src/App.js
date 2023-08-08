import logo from './logo.svg';
import './App.css';
import taskList from './components/TaskList/tasklist';
function App() {
  return (
   <div className="App">
    <h1>Task List</h1>
    <div>
      <input type="text" placeholder ="Add a task" />
      <button>Add</button>
      <taskList></taskList>
    </div>
   </div>
  );
}

export default App;
