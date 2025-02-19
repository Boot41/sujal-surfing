import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import StudentsList from './Pages/StudentsList';
import Assignment from './Pages/Assignment';


const App = () =>{
  return(
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/students/:orgName" element={<StudentsList />} />
        <Route path="/students/:orgName/:studentName" element={<Assignment />} />
      </Routes>
    </Router>
  )
}

export default App;