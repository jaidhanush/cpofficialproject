import { useState } from 'react';
import axios from 'axios';

const BookingPage = () => {
    const [carId, setCarId] = useState('');
    const [pickupDate, setPickupDate] = useState('');
    const [dropDate, setDropDate] = useState('');

    const handleBooking = async () => {
        const response = await axios.post('http://127.0.0.1:8000/api/book_car/', {
            car_id: carId,
            pickup_date: pickupDate,
            drop_date: dropDate,
        });
        alert(response.data.message);
    };

    return (
        <div>
            <h2>Book a Car</h2>
            <input type="text" placeholder="Car ID" onChange={(e) => setCarId(e.target.value)} />
            <input type="date" onChange={(e) => setPickupDate(e.target.value)} />
            <input type="date" onChange={(e) => setDropDate(e.target.value)} />
            <button onClick={handleBooking}>Book Now</button>
        </div>
    );
};

export default BookingPage;
