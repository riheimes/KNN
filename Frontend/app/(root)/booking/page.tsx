"use client";

import { useState } from "react";

export default function BookingPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    service: "",
    date: "",
    message: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Booking submitted:", formData);
  };

  return (
    <main className="container">
      <h1>Book a Consultation</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name
          <input name="name" value={formData.name} onChange={handleChange} required />
        </label>

        <label>
          Email
          <input name="email" type="email" value={formData.email} onChange={handleChange} required />
        </label>

        <label>
          Service
          <select name="service" value={formData.service} onChange={handleChange} required>
            <option value="">Select a service</option>
            <option value="coaching">1-on-1 Coaching</option>
            <option value="wellness">Wellness Consulting</option>
            <option value="strategy">Strategy Session</option>
          </select>
        </label>

        <label>
          Preferred Date
          <input name="date" type="date" value={formData.date} onChange={handleChange} required />
        </label>

        <label>
          Additional Notes
          <textarea name="message" value={formData.message} onChange={handleChange} />
        </label>

        <button type="submit">Book Appointment</button>
      </form>
    </main>
  );
}