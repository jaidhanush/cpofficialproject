import { useState } from 'react';
import axios from 'axios';

const CancellationPage = () => {
    const [bookingId, setBookingId] = useState('');

    const handleCancellation = async () => {
        const response = await axios.post('http://127.0.0.1:8000/api/cancel_booking/', {
            booking_id: bookingId,
        });
        alert(response.data.message);
    };

    return (
        <div>
            <h2>Cancel Booking</h2>
            <input type="text" placeholder="Booking ID" onChange={(e) => setBookingId(e.target.value)} />
            <button onClick={handleCancellation}>Cancel</button>
        </div>
    );
};

export default CancellationPage;
