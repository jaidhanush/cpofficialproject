import logo from './logo.svg';
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import BookingPage from './pages/BookingPage';
import CancellationPage from './pages/cancellationpage';
// import AvailabilityPage from './pages/AvailabilityPage';
// import ReservationPage from './pages/ReservationPage';

function App() {
  return (
    <Router>
            <Routes>
                <Route path="/booking" element={<BookingPage />} />
                <Route path="/cancellation" element={<CancellationPage />} />
                {/* <Route path="/availability" element={<AvailabilityPage />} />
                <Route path="/reservation" element={<ReservationPage />} /> */}
            </Routes>
        </Router>
  );
}

export default App;
