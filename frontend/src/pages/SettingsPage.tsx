import React, { useState } from 'react';
import axios from 'axios';

const SettingsPage: React.FC = () => {
  const [teacherName, setTeacherName] = useState('');
  const [preferences, setPreferences] = useState<{ [key: number]: number }>({});

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/teachers/', {
        name: teacherName,
        preferences,
      });
      alert('Teacher added successfully!');
    } catch (error) {
      console.error('Error adding teacher:', error);
    }
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Settings</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block">Teacher Name</label>
          <input
            type="text"
            value={teacherName}
            onChange={(e) => setTeacherName(e.target.value)}
            className="border p-2 w-full"
          />
        </div>
        <div>
          <label className="block">Preferences (Slot: Weight)</label>
          {[1, 2, 3, 4, 5, 6].map((slot) => (
            <div key={slot} className="flex space-x-2">
              <label>Slot {slot}</label>
              <input
                type="number"
                value={preferences[slot] || ''}
                onChange={(e) => setPreferences({ ...preferences, [slot]: parseInt(e.target.value) })}
                className="border p-2 w-20"
              />
            </div>
          ))}
        </div>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Add Teacher
        </button>
      </form>
    </div>
  );
};

export default SettingsPage;
