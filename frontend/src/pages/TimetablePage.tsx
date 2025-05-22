import React, { useState, useEffect } from 'react';
import { getTimetable } from '../services/api';
import { Schedule } from '../types';

const TimetablePage: React.FC = () => {
  const [timetable, setTimetable] = useState<Schedule[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchTimetable = async () => {
    setLoading(true);
    try {
      const response = await getTimetable();
      setTimetable(response.schedules);
    } catch (error) {
      console.error('Error fetching timetable:', error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchTimetable();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Timetable</h1>
      <button
        onClick={fetchTimetable}
        className="bg-blue-500 text-white px-4 py-2 rounded mb-4"
      >
        Generate Timetable
      </button>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="w-full border-collapse border">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2">Course</th>
              <th className="border p-2">Teacher</th>
              <th className="border p-2">Group</th>
              <th className="border p-2">Day</th>
              <th className="border p-2">Slot</th>
              <th className="border p-2">Room</th>
            </tr>
          </thead>
          <tbody>
            {timetable.map((schedule) => (
              <tr key={schedule.id}>
                <td className="border p-2">{schedule.course.name}</td>
                <td className="border p-2">{schedule.course.teacher.name}</td>
                <td className="border p-2">{schedule.course.group.name}</td>
                <td className="border p-2">{schedule.day}</td>
                <td className="border p-2">{schedule.slot}</td>
                <td className="border p-2">{schedule.room.name}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default TimetablePage;
